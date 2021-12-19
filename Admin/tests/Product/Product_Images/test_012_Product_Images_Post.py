import pytest
import requests
import json
import logging
from Admin.utils.body_data import body_data

log = logging.getLogger()
log.setLevel(logging.INFO)

PATH = '/api/product_images/2'


@pytest.mark.usefixtures("set_authentication")
class Test012:
    def test_012(self):

        response = requests.post(self.BASE_URL + PATH, headers=self.header,
                                        data=json.dumps(body_data.update_product))
        assert response.status_code == 200, '[FAILED] Response Error [{}]'.format(response.status_code)
        log.info(json.dumps(response.json(), indent=3))
