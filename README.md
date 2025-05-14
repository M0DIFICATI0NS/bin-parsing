# About The Project 
**BIN Info Parser Script** is designed to automate the process of extracting company information from open-source API: data.egov.kz, based on a list of Business Identification Numbers (BIN) and retrieve an organization's [name], [registration_date], [legal_address], [activity_type], [director] and [liquidation_status], then report it to the Excel file correspondingly. All data saved in the local PostgreSQL Database with its logs.

# Built With
* [Python]
* [PostgreSQL]
* [OpenData from KZ Government](https://data.egov.kz/)

# Getting Started
To obtain a local copy of the repository and set it up, please follow these steps:

### Software Dependencies
* Install Python 3.13.3
* Install PostgreSQL

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
     pip install psycopg2
     pip install beautifulsoup4
     pip install requests
     pip install pandas
     ```
  3. Ensure the local path for both exporting and analyzing, API Key field and database connection info:
     ```
     https://github.com/M0DIFICATI0NS/bin-parsing/blob/6ff1ed943f5f69eeb47b0ad8f12d5350950d4f75/parse_bin_info.py#L17
     https://github.com/M0DIFICATI0NS/bin-parsing/blob/6ff1ed943f5f69eeb47b0ad8f12d5350950d4f75/parse_bin_info.py#L130
     https://github.com/M0DIFICATI0NS/bin-parsing/blob/6ff1ed943f5f69eeb47b0ad8f12d5350950d4f75/parse_bin_info.py#L199
     https://github.com/M0DIFICATI0NS/bin-parsing/blob/6ff1ed943f5f69eeb47b0ad8f12d5350950d4f75/parse_bin_info.py#L119
     https://github.com/M0DIFICATI0NS/bin-parsing/blob/6ff1ed943f5f69eeb47b0ad8f12d5350950d4f75/parse_bin_info.py#L204
     ```
  5. Run the Project:
     ```
     python parse_bin_info.py run
     ```

# Overview
bins.xlsx - organization's business idendification numbers entered by **you**;
organizations_report.xlsx - script's report based on **bins.xlsx**


# Contribute
Any contributions you make are **greatly appreciated**.

# Contact
Sultan Mecheyev - s.mecheyev@kmg.kz (deactivated)

[LinkedIn](www.linkedin.com/in/sultan-mecheyev-3b459a328)
