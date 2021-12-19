import pytest
import requests
import json
import logging
from Admin.utils.body_data import body_data
from Admin.utils.url_paths import Path

log = logging.getLogger()
log.setLevel(logging.INFO)


@pytest.mark.usefixtures("set_authentication", "create_body")
class Test004:

    @pytest.fixture(scope='class')
    def create_body(self, get_body):
        get_body(body_data.get_register_user_data)

    # @pytest.marker.s
    def test_004_save_success(self):
        response = requests.post(self.BASE_URL + Path.user_register, headers=self.header,
                                        data=json.dumps(self.body))
        log.info(json.dumps(response.json(), indent=3))
        assert response.status_code == 200, '[FAILED] Response Error [{}]'.format(response.status_code)
        assert response.json()['success'] is True, '[FAILED] Success is True'
        assert response.json()['reason'] == 'User Registered Successfully',\
            "[FAILED] {}".format(response.json()['reason']['name'][0])

    def test_004_save_failure(self):
        response = requests.post(self.BASE_URL + Path.user_register, headers=self.header,
                                        data=json.dumps(self.body))
        log.info(json.dumps(response.json(), indent=3))
        assert response.status_code == 200, '[FAILED] Response Error [{}]'.format(response.status_code)
        assert response.json()['success'] is False, '[FAILED] Success is True'
        assert response.json()['reason'] == 'User Already Exists',\
            "[FAILED] {}".format(response.json()['reason']['name'][0])
