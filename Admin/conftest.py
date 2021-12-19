import pytest
import requests
import json
import logging
from faker import Faker

from .utils.header import header_data
from .utils.body_data import body_data


@pytest.fixture(scope='class')
def set_base_url(request):
    request.cls.BASE_URL = 'http://3.140.144.29'
    request.cls.header = header_data.get_header()
    request.cls.fake = Faker()


@pytest.fixture(scope='class')
def set_authentication(request, set_base_url):
    PATH = '/api/login'
    response = requests.post(request.cls.BASE_URL + PATH, headers=request.cls.header,
                                    data=json.dumps(body_data.body))
    response_data = response.json()
    token = response_data['data']['data']['token']
    request.cls.header['Authorization'] = ' '.join(['Bearer', token])
    PATH = '/api/users/1'
    response = requests.get(request.cls.BASE_URL+PATH, headers=request.cls.header)
    assert response.status_code == 200, '[FAILED] Token not generated'
    logging.info('Token generated')


@pytest.fixture(scope='class')
def get_body(request, set_base_url):
    def get_body_from_method(method):
        request.cls.body = method(request.cls)
    return get_body_from_method

