import requests
import zipfile
import io
import os
import xml.etree.ElementTree as ET
# Define API URL
api_url = "https://opendart.fss.or.kr/api/corpCode.xml"

# Define API Key 
api_key = "b590faa8f6fd1afca5b3491fa2017d2c32552bba"

#찾고 싶은 회사  
company = "HD현대"

# Define Parameters (Modify based on API documentation)

params = {
    "crtfc_key": api_key,  # 인증키 (Required)
    "bgn_de": "20240101",  # 조회 시작일 (YYYYMMDD)
    "end_de": "20240131",  # 조회 종료일 (YYYYMMDD)
    "corp_code": "",       # 기업 코드 (Optional)
    "page_no": "1",        # 페이지 번호
    "page_count": "10"     # 페이지당 출력 건수
}

# Make API request
response = requests.get(api_url, params=params, stream=True)

# Check if request was successful
if response.status_code == 200:
    # Create a BytesIO object to handle the binary ZIP data
    zip_file = io.BytesIO(response.content)

    # Extract ZIP file contents
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        extract_path = "dart_corp_codes"
        zip_ref.extractall(extract_path)  # Extract to a folder
        extracted_files = zip_ref.namelist()
        print(f"Extracted files: {extracted_files}")

        # Assume there's only one XML file inside
        xml_filename = extracted_files[0]  # Typically, there's only one file
        xml_path = os.path.join(extract_path, xml_filename)

        # Parse the XML file to find 삼성전자's corp_code
        tree = ET.parse(xml_path)
        root = tree.getroot()

        found = False
        print(f"회사 이름 {company}로 검색한 결과")
        for corp in root.findall("list"):
            corp_name = corp.find("corp_name").text
            corp_code = corp.find("corp_code").text
            
            if company in corp_name:
                print(f"{corp_name}의 corp_code: {corp_code}")
                found = True


        if not found:
            print(f"{company}의 corp_code를 찾을 수 없습니다.")

else:
    print(f"Error: {response.status_code}, {response.text}")
