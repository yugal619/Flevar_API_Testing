import pytest
import requests
import json
import logging
from Admin.utils.url_paths import Path

log = logging.getLogger()
log.setLevel(logging.INFO)


@pytest.mark.usefixtures("set_authentication", "create_end_point")
class Test003:

    @pytest.fixture(scope='class')
    def create_end_point(self, request):
        response = requests.get(self.BASE_URL + Path.user, headers=self.header)
        request.cls.path_created = '/'.join([Path.user, str(response.json()['data']['data'][0]['id'])])
        yield

    def test_003(self):
        response = requests.get(self.BASE_URL + self.path_created, headers=self.header)
        assert response.status_code == 200, '[FAILED] Response Error [{}]'.format(response.status_code)
        assert response.json()['success'] is True, '[FAILED] Success is True'
        assert response.json()['reason'] == 'Record found'
        log.info(json.dumps(response.json(), indent=3))
