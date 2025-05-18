# About The Project 
**BIN Info Parser Script** is designed to automate the process of extracting company information from open-source API: data.egov.kz, based on a list of Business Identification Numbers (BIN) and retrieve an organization's [name], [registration_date], [legal_address], [activity_type], [director] and [liquidation_status], then report it to the Excel file correspondingly. All data saved in the local PostgreSQL Database with its logs.

# Built With
* [Python]
* [PostgreSQL]
* [OpenData from KZ Government](https://data.egov.kz/)

# Getting Started
To obtain a local copy of the repository and set it up, please follow these steps:

### Software Dependencies
* Install Python 3.8+
* Install PostgreSQL

### Prepare the PostgreSQL Database
* Open your PostgreSQL tool (e.g. pgAdmin 4 or psql CLI) to restore the included backup file (company_db.sql) from the project repository.
  1. In pgAdmin, right-click the Databases section and select **Create > Database**.
  2. Give 'company_db' name for a new database and click **Save**.
  3. Right-click your new database > **Restore..** and choose the .sql file from this repo.
 
* Using **psql** from the command-line is faster
  ```
  psql -U your_username -d your_database -f path/to/company_db.sql
  ```
### Generate your own API Key
* Open https://data.egov.kz/profile/apikeylist
  
  1. Click on generate API Key.
  2. Agree the conditions and sign it with your digital signature via NCALayer.
  3. Enter the reason why you're going to use it.
  4. Click on create an API Key.
  5. Save.

### Clone the Repository
* Open your terminal or command prompt.
* Execute the following command, replacing URL with the repository’s URL:
  1. Clone the Repository:
     ```
     git clone https://github.com/M0DIFICATI0NS/bin-parsing.git
     ```
  2. Install dependencies:
     ```
     pip install -r requirements.txt
     ```
  3. Ensure the local path for both exporting and analyzing, API Key field and update database credentials:
     
     https://github.com/M0DIFICATI0NS/bin-parsing/blob/6ff1ed943f5f69eeb47b0ad8f12d5350950d4f75/parse_bin_info.py#L17
     https://github.com/M0DIFICATI0NS/bin-parsing/blob/6ff1ed943f5f69eeb47b0ad8f12d5350950d4f75/parse_bin_info.py#L130
     https://github.com/M0DIFICATI0NS/bin-parsing/blob/6ff1ed943f5f69eeb47b0ad8f12d5350950d4f75/parse_bin_info.py#L199
     https://github.com/M0DIFICATI0NS/bin-parsing/blob/6ff1ed943f5f69eeb47b0ad8f12d5350950d4f75/parse_bin_info.py#L119

  5. Run the Project:
     ```
     python parse_bin_info.py
     ```

# Overview
bins.xlsx - organization's business idendification numbers entered by **you**;
organizations_report.xlsx - script's report based on **bins.xlsx**

<img width="200" alt="image" src="https://github.com/user-attachments/assets/fb524349-ba35-4b57-a628-bc2ca1911f6a">
<img width="350" alt="image" src="https://github.com/user-attachments/assets/841e7723-fac5-4e89-8993-6df407cfa481">

# Contribute
Any contributions you make are **greatly appreciated**.

# Contact
[LinkedIn](www.linkedin.com/in/sultan-mecheyev-3b459a328)
