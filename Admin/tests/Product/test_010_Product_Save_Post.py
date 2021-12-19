import pytest
import requests
import json
import logging
from Admin.utils.body_data import body_data
from Admin.utils.url_paths import Path

log = logging.getLogger()
log.setLevel(logging.INFO)


@pytest.mark.usefixtures("set_authentication", 'create_body')
class Test010:

    @pytest.fixture(scope='class')
    def create_body(self, get_body):
        get_body(body_data.get_save_product)

    def test_010_success(self):
        response = requests.post(self.BASE_URL + Path.product, headers=self.header, data=json.dumps(self.body))
        assert response.status_code == 200, '[FAILED] Response Error [{}]'.format(response.status_code)
        assert response.json()['success'] is True, '[FAILED] Success is {response.json()["success"]}'
        assert response.json()['reason'] == 'Record added successfully', \
            '[FAILED] Reason is {response.json()["reason"]}'
        log.info(json.dumps(response.json(), indent=3))

    def test_010_failure(self):
        response = requests.post(self.BASE_URL + Path.product, headers=self.header, data=json.dumps(self.body))
        assert response.status_code == 422, '[FAILED] Response Error [{}]'.format(response.status_code)
        assert response.json()['success'] is False, '[FAILED] Success is {response.json()["success"]}'
        assert response.json()['reason']['name'][0] == 'The name has already been taken.', \
            '[FAILED] Reason is {response.json()["reason"]}'
        log.info(json.dumps(response.json(), indent=3))