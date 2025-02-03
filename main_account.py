import requests
import pprint

# Define API URL
api_url = "https://opendart.fss.or.kr/api/fnlttSinglAcnt.json"

# Define API Key 
api_key = "b590faa8f6fd1afca5b3491fa2017d2c32552bba"


# Define Parameters (Modify based on API documentation)

params = {
    "crtfc_key": api_key,  # 인증키 (Required)
    "corp_code": "01390344",
    "bsns_year": "2020",
    "reprt_code": "11011"
    #1분기보고서 : 11013  반기보고서 : 11012 3분기보고서 : 11014 사업보고서 : 11011
}

# Make API request
response = requests.get(api_url, params=params, stream=True)

# Check if request was successful
if response.status_code == 200:
    data = response.json() 
    pprint.pprint(data)
else:
    print(f"Error: {response.status_code}, {response.text}")
