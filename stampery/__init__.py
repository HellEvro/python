import json
import base64
import hashlib
import requests

class Client:
    def __init__(self, apiSecret, beta=False):
        self.apiSecret = apiSecret

        md5 = hashlib.md5()
        md5.update(apiSecret)
        self.clientId = md5.hexdigest()[:15]

        auth = base64.b64encode(self.clientId + ':' + apiSecret)
        self.headers = {'Authorization': auth}

        if not beta:
            self.endpoint = 'https://stampery.herokuapp.com/api/v2'
        else:
            self.endpoint = 'https://stampery-beta.herokuapp.com/api/v2'

    def hash(self, data):
        h = hashlib.sha256()
        h.update(data)
        return h.hexdigest()

    def stamp(self, data, file=None):
        if file is None:
            self.__stampData(data)
        else:
            self.__stampFile(data, file)

    def __stampData(self, data):
        r = requests.post(self.endpoint + '/stamps/', json=data, headers=self.headers)
        return r.json()

    def __stampFile(self, data, file):
        files = {'file': ('filsename', file), 'data': (None, json.dumps(data))}
        r = requests.post(self.endpoint + '/stamps/', files=files, data=data, headers=self.headers)
        return r.json()

    def get(self, hash):
        r = requests.get(self.endpoint + '/stamps/' + hash)
        return r.json()
