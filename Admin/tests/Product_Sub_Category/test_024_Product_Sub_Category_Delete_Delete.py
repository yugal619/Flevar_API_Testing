import pytest
import requests
import json
import logging
from Admin.utils.body_data import body_data
from Admin.utils.url_paths import Path

log = logging.getLogger()
log.setLevel(logging.INFO)


@pytest.mark.usefixtures("set_authentication", "create_end_point")
class Test024:

    @pytest.fixture(scope='class')
    def create_end_point(self, request):
        response = requests.post(self.BASE_URL + Path.product_category, headers=self.header,
                                        data=json.dumps(body_data.get_save_sub_category_product(self)))
        request.cls.path_created = f"{Path.product_category}/{str(response.json()['data']['data']['id'])}"
        yield

    def test_024_delete_data(self):
        response = requests.delete(self.BASE_URL + self.path_created, headers=self.header)
        assert response.status_code == 200, '[FAILED] Response Error [{}]'.format(response.status_code)
        assert response.json()['success'] is True
        assert response.json()['reason'] == 'Record deleted successfully', \
            '[FAILED] Response Error Message is different : [{}]'.format(response.json()['reason'])

    def test_024_already_deleted_data(self):
        response = requests.delete(self.BASE_URL + self.path_created, headers=self.header)
        assert response.status_code == 200, '[FAILED] Response Error [{}]'.format(response.status_code)
        assert response.json()['success'] is False
        assert response.json()['reason'] == 'Record not found', \
            '[FAILED] Response Error Message is different :[{}]'.format(response.json()['reason'])
