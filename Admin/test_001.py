import json
import requests
import logging

def test_001():
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')


    BASE_URL = 'http://3.140.144.29'
    PATH = '/api/login'

    body = {
        "email":"flevar@gmail.com",
        "password":"flevar@123"
    }
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
    }

    response_status = requests.post(BASE_URL+PATH, headers=headers, data=json.dumps(body))

    print(response_status)

    response_data = response_status.json()
    print(response_data['data']['data']['token'])
    token = response_data['data']['data']['token']

    headers= {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiY2NkZmUzYTMwNjg2YzVjNzVkYjFhZmYzZjhlOWZlZmY5NGVjZTQwZTg0NzlmYjhkYzMzNTMwMzRiMGNkZTE1OGYxMWY0MzkxZjJkMzI0MGEiLCJpYXQiOjE2Mzc5MDQ4NTAuOTUxMDI5LCJuYmYiOjE2Mzc5MDQ4NTAuOTUxMDMzLCJleHAiOjE2Njk0NDA4NTAuOTQ1NSwic3ViIjoiNSIsInNjb3BlcyI6W119.eTuS8DhJUJGb_gqJb_NQt6N-hWfnnOMDrFDR1vHLSQ5PKW-Us0tKGOHgJhTPc8kNmrc3EnZl6RFZeAPfmShU8oDPYB3_M1MnXlEXFTiU5enC1PTlXLJST95Duk0tB8fgU-NJwGSmJUVWr75daeo1DNmKyVuxChF0toa0eT98YbsU-8-GFkOMsDS76dUxU-YzRxuuEmBgGpsDgRvXjKB6tmIK7yPJt1iKHJOo-kEMN4qcao4Qil9vNpGh9XKd7BPesmvepe5WrTVDecs1ORq4E4-nW2r09XFzbK1p1LSUSm5bXZtwqJy_929OICkgTNGJiAWAeezmKdOSYNzFv-SCPfS7aOQEBsnu0A5bH-Gliry6h9HDi4mcCMnLpAkXnfvKU9g2XHdSHrDpmWYruW2mdva1bWfQcZiRu_6RMLNEl6xhfD-DXnsvqnQEBbbmKdeWZeV3pQLS6LIdDaVaF56gnRDWX0Bv_WCIJUNVbbTWze_RrAcniRaOcFiRUj3nMSEkHsGsNkG6JTERv_2c71ZiX5kbmgrYujMYypl2mORmyRHQWoW-0-MDuMJVpb47VjNssxLyBNEpCd3V5GM7UMjU5EkSeE4ojYlT9CxDArtSqyYJl-byxdxvocNXOVpE8dfyfZ10-2bDnT6AHGiF3ziZvLhllHmg-ZKwwdhdZDtdQ8M",
    }

    PATH = '/api/users/1'


    response_status = requests.get(BASE_URL+PATH, headers=headers)

    print(response_status)
