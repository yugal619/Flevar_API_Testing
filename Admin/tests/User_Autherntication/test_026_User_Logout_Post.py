import pytest
import requests
import json
import logging
from Admin.utils.body_data import body_data
from Admin.utils.url_paths import Path

log = logging.getLogger()
log.setLevel(logging.INFO)


@pytest.mark.usefixtures("set_authentication")
class Test026:

    def test_026_login(self):
        response = requests.post(self.BASE_URL + Path.user_login, headers=self.header,
                                        data=json.dumps(body_data.body))
        log.info(json.dumps(response.json(), indent=3))
        assert response.status_code == 200, '[FAILED] Response Error [{}]'.format(response.status_code)
        assert response.json()['reason'] == 'User Login Successfully', \
            '[FAILED] User not able to Login'

    def test_026_logout(self):
        response = requests.post(self.BASE_URL + Path.user_logout, headers=self.header)
        log.info(json.dumps(response.json(), indent=3))
        assert response.status_code == 200, '[FAILED] Response Error [{}]'.format(response.status_code)
        assert response.json()['reason'] == 'User Logout Successfully', \
            '[FAILED] User not able to Logout'
