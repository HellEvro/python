import json
import base64
import hashlib
import requests
from retrying import retry

class Client:
    def __init__(self, apiSecret, beta=False):
        self.apiSecret = apiSecret

        md5 = hashlib.md5()
        md5.update(apiSecret)
        self.clientId = md5.hexdigest()[:15]

        auth = base64.b64encode(self.clientId + ':' + apiSecret)
        self.headers = {'Authorization': 'Basic ' + auth}

        if not beta:
            self.endpoint = 'https://api.stampery.com/v2'
        else:
            self.endpoint = 'https://stampery-api-beta.herokuapp.com/v2'

    def hash(self, data):
        h = hashlib.sha256()
        h.update(data)
        return h.hexdigest()

    def stamp(self, data, file=None):
        if file is None:
            self.__stampData(data)
        else:
            self.__stampFile(data, file)

    def retryError(exception):
        return isinstance(exception, Exception)

    @retry(retry_on_exception=retryError, stop_max_attempt_number=3, wait_fixed=2000)
    def __stampData(self, data):
        r = requests.post(self.endpoint + '/stamps/', json=data, headers=self.headers)
        if r.status_code != 200:
            raise Exception('Error sending request')
        else:
            return r.json()

    @retry(retry_on_exception=retryError, stop_max_attempt_number=3, wait_fixed=2000)
    def __stampFile(self, data, file):
        files = {'file': ('filename', file), 'data': (None, json.dumps(data))}
        r = requests.post(self.endpoint + '/stamps/', files=files, data=data, headers=self.headers)
        if r.status_code != 200:
            raise Exception('Error sending request')
        else:
            return r.json()

    def get(self, hash):
        r = requests.get(self.endpoint + '/stamps/' + hash)
        return r.json()
