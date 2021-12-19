import pytest
import requests
import json
import logging
from Admin.utils.body_data import body_data
from Admin.utils.url_paths import Path

log = logging.getLogger()
log.setLevel(logging.INFO)


@pytest.mark.usefixtures("set_authentication", 'create_end_point')
class Test011:

    @pytest.fixture(scope='class')
    def create_end_point(self, request):
        log.info(Path.product)
        response = requests.post(self.BASE_URL + Path.product, headers=self.header, data=json.dumps(
            body_data.get_save_product(self)))
        request.cls.path = '/'.join([Path.product, str(response.json()['data']['data']['id'])])
        yield

    def test_011_deleted_data(self):
        log.info(self.BASE_URL + self.path)
        response = requests.delete(self.BASE_URL + self.path, headers=self.header)
        assert response.status_code == 200, '[FAILED] Response Error [{}]'.format(response.status_code)
        assert response.json()['success'] is True, '[FAILED] Success is {response.json()["success"]}'
        assert response.json()['reason'] == 'Record deleted successfully', \
            '[FAILED] Reason is {response.json()["reason"]}'
        log.info(json.dumps(response.json(), indent=3))

    def test_011_already_deleted_data(self):
        response = requests.delete(self.BASE_URL + self.path, headers=self.header)
        assert response.status_code == 200, '[FAILED] Response Error [{}]'.format(response.status_code)
        assert response.json()['success'] is False, '[FAILED] Success is {response.json()["success"]}'
        assert response.json()['reason'] == 'Record not found', \
            '[FAILED] Reason is {response.json()["reason"]}'
        log.info(json.dumps(response.json(), indent=3))
