import requests
import pprint

# Define API URL
api_url = "https://opendart.fss.or.kr/api/list.json"

# Define API Key 
api_key = "b590faa8f6fd1afca5b3491fa2017d2c32552bba"


# Define Parameters (Modify based on API documentation)

params = {
    "crtfc_key": api_key,  # 인증키 (Required)
    "corp_code": "01390344",
    "bgn_de": "20230101",  # 조회 시작일 (YYYYMMDD)
    "end_de": "20250130",  # 조회 종료일 (YYYYMMDD)
    "pblntf_ty": 'A',
    '''A : 정기공시
        B : 주요사항보고
        C : 발행공시
        D : 지분공시
        E : 기타공시
        F : 외부감사관련
        G : 펀드공시
        H : 자산유동화
        I : 거래소공시
        J : 공정위공시'''
    "sort": 'crp'
}

# Make API request
response = requests.get(api_url, params=params, stream=True)

# Check if request was successful
if response.status_code == 200:
    data = response.json() 
    pprint.pprint(data['list'])
else:
    print(f"Error: {response.status_code}, {response.text}")
