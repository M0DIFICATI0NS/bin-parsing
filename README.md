# About The Project 
**BIN Info Parser Script** is designed to automate the process of extracting company information from open-source API: data.egov.kz, based on a list of Business Identification Numbers (BIN) and retrieve an organization's [name], [registration_date], [legal_address], [activity_type], [director] and [liquidation_status], then report it to the Excel file correspondingly. All data saved in the local PostgreSQL Database with its logs.

# Built With
* [Python]
* [PostgreSQL]

# Getting Started
To obtain a local copy of the repository and set it up, please follow these steps:

### Software Dependencies
* Install Python 3.13.3
* Install PostgreSQL

### Clone the Repository
* Open your terminal or command prompt.
* Execute the following command, replacing URL with the repository’s URL:
  1. Clone the Repository:
     ```
     git clone https://github.com/M0DIFICATI0NS/bin-parsing.git
     ```
  2. Install dependencies:
     ```
     pip install psycopg2
     pip install beautifulsoup4

     ```
  4. Ensure the local path for both exporting and analyzing:
     
     https://github.com/M0DIFICATI0NS/log-analyzer/blob/b9de0dba754ab694f68c1ba592da235d10dd2249/ExportMessageLog.cs#L21
     https://github.com/M0DIFICATI0NS/log-analyzer/blob/b9de0dba754ab694f68c1ba592da235d10dd2249/AnalyzeMessageLog.cs#L14
     https://github.com/M0DIFICATI0NS/log-analyzer/blob/b9de0dba754ab694f68c1ba592da235d10dd2249/AnalyzeMessageLog.cs#L75
     
  3. Run the Project:
     ```
     python parse_bin_info.py run
     ```

# Overview
MessageLog.csv - user log-ins data retrieved from .\pigetmsg command-line utility with 100k+ records;
InactiveUsers.csv - script's report based on **MessageLog.csv**

<img width="100" alt="image" src="https://github.com/user-attachments/assets/75fb2a7b-0d4f-4638-a332-0bafa0a2f632">



# Contribute
Any contributions you make are **greatly appreciated**.

# Contact
Sultan Mecheyev - s.mecheyev@kmg.kz (deactivated)

[LinkedIn](www.linkedin.com/in/sultan-mecheyev-3b459a328)
