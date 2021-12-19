import pytest
import requests
import json
import logging
from Admin.utils.body_data import body_data
from Admin.utils.url_paths import Path

log = logging.getLogger()
log.setLevel(logging.INFO)


@pytest.mark.usefixtures("set_authentication", "create_body")
class Test023:

    @pytest.fixture(scope='class')
    def create_body(self, get_body):
        get_body(body_data.get_save_sub_category_product)

    def test_023_save_success(self):
        response = requests.post(self.BASE_URL + Path.product_sub_category, headers=self.header,
                                        data=json.dumps(self.body))
        assert response.status_code == 200, '[FAILED] Response Error [{}]'.format(response.status_code)
        assert response.json()['success'] is True, '[FAILED] Success is {response.json()["success"]}'
        assert response.json()['reason'] == 'Record added successfully', \
            '[FAILED] Reason is {response.json()["reason"]}'

    def test_023_save_failure(self):
        response = requests.post(self.BASE_URL + Path.product_sub_category, headers=self.header,
                                 data=json.dumps(self.body))
        assert response.status_code == 422, '[FAILED] Response Error [{}]'.format(response.status_code)
        assert response.json()['success'] is False, '[FAILED] Success is {response.json()["success"]}'
        assert response.json()['reason']['name'][0] == 'The name has already been taken.', \
            '[FAILED] Reason is {response.json()["reason"]}'
        log.info(json.dumps(response.json(), indent=3))

