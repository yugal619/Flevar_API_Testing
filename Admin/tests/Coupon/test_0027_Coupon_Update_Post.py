import pytest
import requests
import json
import logging
from Admin.utils.body_data import body_data
from Admin.utils.url_paths import Path

log = logging.getLogger()
log.setLevel(logging.INFO)


@pytest.mark.usefixtures("set_authentication", "create_end_point")
class Test0027:

    @pytest.fixture(scope='class')
    def create_end_point(self, request):
        response = requests.post(self.BASE_URL + Path.coupon, headers=self.header,
                                        data=json.dumps(body_data.get_save_coupon(self)))
        request.cls.path_created = '/'.join([Path.coupon, str(response.json()['data']['data']['id'])])
        yield

    def test_0027(self):
        response = requests.post(self.BASE_URL + self.path_created, headers=self.header,
                                 data=json.dumps(body_data.get_save_coupon(self)))
        log.info(json.dumps(response.json(), indent=3))
        assert response.status_code == 200, '[FAILED] Response Error [{}]'.format(response.status_code)
        assert response.json()['success'] is True, '[FAILED] Success is {response.json()["success"]}'
        assert response.json()['reason'] == 'Record added successfully', \
            '[FAILED] Reason is {response.json()["reason"]}'
