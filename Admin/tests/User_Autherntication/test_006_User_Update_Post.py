import pytest
import requests
import json
import logging
from Admin.utils.body_data import body_data
from Admin.utils.url_paths import Path

log = logging.getLogger()
log.setLevel(logging.INFO)

PATH = '/api/users'


@pytest.mark.usefixtures("set_authentication", "create_data")
class Test006:

    @pytest.fixture(scope='class')
    def create_data(self, request):
        response = requests.get(self.BASE_URL + PATH, headers=self.header)
        request.cls.path_created = '/'.join([Path.user, str(response.json()['data']['data'][0]['id'])])
        yield

    def test_006(self):
        # log.info(self.path_created)
        # log.info(body_data.get_user_update_data(self))
        response = requests.post(self.BASE_URL + self.path_created, headers=self.header,
                                        data=json.dumps(body_data.get_user_update_data(self)))
        # log.info(json.dumps(response.json(), indent=3))
        assert response.status_code == 200, '[FAILED] Response Error [{}]'.format(response.status_code)
