import pytest
import requests
import json
import logging

log = logging.getLogger()
log.setLevel(logging.INFO)

PATH = '/api/product_category/1'


@pytest.mark.usefixtures("set_authentication")
class Test018:
    def test_018(self):

        response = requests.get(self.BASE_URL + PATH, headers=self.header)
        assert response.status_code == 200, '[FAILED] Response Error [{}]'.format(response.status_code)
        log.info(json.dumps(response.json(), indent=3))
