import requests
import pprint
import zipfile
import io
import os

# Define API URL
api_url = "https://opendart.fss.or.kr/api/fnlttXbrl.xml"

# Define API Key 
api_key = "b590faa8f6fd1afca5b3491fa2017d2c32552bba"

#disclose.py 를 통해 확인하세요.
recpt_no = '20240318000459' 
report_code = "11011"
#1분기보고서 : 11013    반기보고서 : 11012  3분기보고서 : 11014  사업보고서 : 11011

# Define Parameters (Modify based on API documentation)

params = {
    "crtfc_key": api_key,  # 인증키 (Required)
    'rcept_no': recpt_no,
    "reprt_code": "11011"
    #1분기보고서 : 11013  반기보고서 : 11012 3분기보고서 : 11014 사업보고서 : 11011
}

# Make API request
response = requests.get(api_url, params=params, stream=True)

# Check if request was successful
if response.status_code == 200:
    print("✅ API request successful! Downloading ZIP file...")

    # Store ZIP file in memory
    zip_file = io.BytesIO(response.content)

    # Define extraction directory
    extract_path = "financial_statements"
    os.makedirs(extract_path, exist_ok=True)  # Ensure directory exists

    try:
        # Extract ZIP file contents
        with zipfile.ZipFile(zip_file, "r") as zip_ref:
            zip_ref.extractall(extract_path)
            extracted_files = zip_ref.namelist()
            print(f"✅ Files saved in: {extract_path}")

            # Show saved files (without printing content)
            for file_name in extracted_files:
                print(f"📂 {file_name} saved.")
                
    except zipfile.BadZipFile:
        print("❌ Error: The file is not a valid ZIP archive.")
else:
    print(f"❌ API request failed: {response.status_code}, {response.text}")