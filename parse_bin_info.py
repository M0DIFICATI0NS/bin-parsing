from bs4 import BeautifulSoup
import pandas as pd
import requests
import psycopg2
import time
import json
import logging

# # Configure logging
# logging.basicConfig(
#     level=logging.INFO, 
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     filename='bin_lookup.log'
# )

# API configuration
API_KEY = {yourApiKey}
API_URL = 'https://data.egov.kz/api/v4/gbd_ul/v1'


def lookup_bin(bin_number):

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # get query
    params = {
        'apiKey': API_KEY,
        'source': json.dumps({
            "size": 10,
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "bin": bin_number
                            }
                        }
                    ]
                }
            }
        })
    }
    
    try:
        response = requests.get(
            API_URL, 
            params=params, 
            headers=headers,
            timeout=10
        )
        
        logging.info(f"API Response Status Code: {response.status_code}")
        logging.info(f"API Response Headers: {response.headers}")
        logging.info(f"API Response Content: {response.text}")

        if response.status_code != 200:
            logging.error(f"API Request Failed: {response.status_code}")
            logging.error(f"Response Content: {response.text}")
            return None

        data = response.json()

        logging.info(f"Received data type: {type(data)}")
        logging.info(f"Received data: {json.dumps(data, indent=2)}")
        
        if isinstance(data, list) and len(data) > 0:
            org = data[0]
        elif isinstance(data, dict):
            hits = data.get('hits', {})
            if not hits:
                logging.info(f"No results found for BIN {bin_number}")
                return None
            
            total = hits.get('total', {})
            if isinstance(total, dict):
                total_value = total.get('value', 0)
            else:
                total_value = total
            
            if total_value == 0:
                logging.info(f"No results found for BIN {bin_number}")
                return None
            
            org = hits.get('hits', [{}])[0].get('_source', {})
        else:
            logging.error(f"Unexpected data structure for BIN {bin_number}")
            return None
        
        # extraction of org details
        return {
            'datereg': org.get('datereg', None),
            'nameru': org.get('nameru', 'Не найдено'),
            'director': org.get('director', 'Не найдено'),
            'addressru': org.get('addressru', 'Не найдено'),
            'bin': org.get('bin', bin_number),
            'liquidation_status': org.get('statusru', 'Не найдено'),
            'activity_type': org.get('okedru', 'Не указано')  
        }
    
    except requests.RequestException as e:
        logging.error(f"API request error for BIN {bin_number}: {e}")
        
        # exception to check code bugs
        if hasattr(e, 'response'):
            logging.error(f"Response Status Code: {e.response.status_code}")
            logging.error(f"Response Content: {e.response.text}")
        
        return None
    except Exception as e:
        logging.error(f"Unexpected error processing BIN {bin_number}: {e}", exc_info=True)
        return None

def main():
    try:
        # connection to psql db
        conn = psycopg2.connect(
            dbname="company_db",
            user={yourUserName},
            password={yourPassword},
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # BIN input Path
        df_bins = pd.read_excel(r"{yourPath}", dtype={'BIN': str})
        for bin in df_bins['BIN']:
            # 12-digit BIN establishment
            bin_str = bin.zfill(12)
            
            logging.info(f"Processing BIN: {bin_str}")

            org_details = lookup_bin(bin_str)
            
            if org_details:
                cur.execute("""
                    INSERT INTO organizations (
                        bin, 
                        name, 
                        liquidation_status, 
                        legal_address, 
                        registration_date, 
                        director,
                        activity_type
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (bin) DO UPDATE SET
                        name = EXCLUDED.name,
                        liquidation_status = EXCLUDED.liquidation_status,
                        legal_address = EXCLUDED.legal_address,
                        registration_date = EXCLUDED.registration_date,
                        director = EXCLUDED.director,
                        activity_type = EXCLUDED.activity_type
                """, (
                    org_details['bin'], 
                    org_details['nameru'], 
                    org_details['liquidation_status'], 
                    org_details['addressru'], 
                    org_details['datereg'], 
                    org_details['director'],
                    org_details['activity_type']
                ))
            else:
                # Not found
                cur.execute("""
                    INSERT INTO organizations (
                        bin, 
                        name, 
                        liquidation_status, 
                        legal_address, 
                        registration_date, 
                        director,
                        activity_type
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (bin) DO NOTHING
                """, (
                    bin_str, 
                    'Не найдено', 
                    'Не найдено', 
                    'Не найдено', 
                    None, 
                    'Не найдено',
                    'Не указано'
                ))
            
            # timeout
            time.sleep(1)

        conn.commit()

        cur.execute("INSERT INTO script_log (status, message) VALUES (%s, %s)", ('Успешно', 'Обработка завершена'))
        conn.commit()

        # BIN output Path
        df_out = pd.read_sql("SELECT * FROM organizations", conn)
        df_out.to_excel(r"{yourPath}", index=False)

    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)
        
        try:
            with psycopg2.connect(
                dbname="company_db",
                user={yourUserName},
                password={yourPassword},
                host="localhost",
                port="5432"
            ) as conn:
                with conn.cursor() as cur:
                    cur.execute("INSERT INTO script_log (status, message) VALUES (%s, %s)", ('Ошибка', str(e)))
                    conn.commit()
        except Exception as log_error:
            logging.error(f"Error logging to database: {log_error}")

    finally:
        if 'conn' in locals() and conn:
            conn.close()

if __name__ == '__main__':
    main()
