import pytest
import requests
import json
import logging

from utils.body_data import body_data

PATH = '/api/login'


@pytest.mark.usefixtures("set_base_url")
class Test003:
    def test_003(self):

        response_status = requests.post(self.BASE_URL + PATH, headers=self.header,
                                        data=json.dumps(body_data.body))
        logging.error('This is an error message {}'.format(response_status))
