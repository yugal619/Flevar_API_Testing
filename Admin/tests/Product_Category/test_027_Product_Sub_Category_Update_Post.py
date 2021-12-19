import pytest
import requests
import json
import logging
from Admin.utils.body_data import body_data
from Admin.utils.url_paths import Path

log = logging.getLogger()
log.setLevel(logging.INFO)


@pytest.mark.usefixtures("set_authentication", "create_data")
class Test027:

    @pytest.fixture(scope='class')
    def create_data(self, request):
        response = requests.post(self.BASE_URL + Path.product_category, headers=self.header,
                                        data=json.dumps(body_data.get_save_product_category(self)))
        request.cls.path_created = '/'.join([Path.product_sub_category, str(response.json()['data']['data']['id'])])
        yield

    def test_027(self):
        response = requests.post(self.BASE_URL + self.path_created, headers=self.header,
                                        data=json.dumps(body_data.get_save_product_category(self)))
        assert response.status_code == 200, '[FAILED] Response Error [{}] \n Body :{}'.format(response.status_code, response.json())
        log.info(json.dumps(response.json(), indent=3))