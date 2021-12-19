import pytest
import requests
import json
import logging
from Admin.utils.url_paths import Path

log = logging.getLogger()
log.setLevel(logging.INFO)


@pytest.mark.usefixtures("set_authentication")
class Test005:
    def test_005(self):

        response = requests.get(self.BASE_URL + Path.user, headers=self.header)
        assert response.status_code == 200, '[FAILED] Response Error [{}]'.format(response.status_code)
        assert response.json()['success'] is True, '[FAILED] Success is True'
        assert response.json()['reason'] == 'Users Fetched Successfully'
        log.info(json.dumps(response.json(), indent=3))
