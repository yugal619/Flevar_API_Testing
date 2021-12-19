import pytest
import requests
import json
import logging
from Admin.utils.body_data import body_data
from Admin.utils.url_paths import Path

log = logging.getLogger()
log.setLevel(logging.INFO)


@pytest.mark.usefixtures("set_authentication", "create_new_path")
class Test019:

    @pytest.fixture(scope='class')
    def create_new_path(self, request):
        response = requests.post(self.BASE_URL + Path.product_category, headers=self.header,
                                        data=json.dumps(body_data.get_save_product_category(self)))
        request.cls.path = '/'.join([Path.product_category, str(response.json()['data']['data']['id'])])
        yield

    def test_019_delete_data(self):
        response = requests.delete(self.BASE_URL + self.path, headers=self.header)
        assert response.status_code == 200, '[FAILED] Response Error [{}]'.format(response.status_code)
        assert response.json()['success'] is True
        log.info(json.dumps(response.json(), indent=3))
        assert response.json()['reason'] == 'Record deleted successfully', \
            '[FAILED] Response Error Message is different : [{}]'.format(response.json()['reason'])

    def test_019_already_deleted_data(self):
        response = requests.delete(self.BASE_URL + self.path, headers=self.header)
        assert response.status_code == 200, '[FAILED] Response Error [{}]'.format(response.status_code)
        assert response.json()['success'] == False, '[FAILURE] [{}]'.format(response.json())
        assert response.json()['reason'] == 'Record not found', \
            '[FAILED] Response Error Message is different : [{}]'.format(response.json()['reason'])
