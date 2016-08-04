import md5
import hashlib
import sha3

class Stampery:
    __apiEndpoints = {'prod' : ['api.stampery.com', 4000],
                     'beta' : ['api-beta.stampery.com', 4000]}
    __amqpEndpoints = {'prod' : ['young-squirrel.rmq.cloudamqp.com', 5672, 'consumer', '9FBln3UxOgwgLZtYvResNXE7', 'ukgmnhoi'],
                     'beta' : ['young-squirrel.rmq.cloudamqp.com', 5672, 'consumer', '9FBln3UxOgwgLZtYvResNXE7', 'beta']}

    def __init__(self, secret, branch = 'prod'):
        self.__clientSecret = secret
        self.__clientId = md5.new(secret).hexdigest()
        self.__apiEndpoint = self.__apiEndpoints[branch] or self.__apiEndpoints['prod']
        self.__amqpEndpoint = self.__amqpEndpoints[branch] or self.__amqpEndpoints['prod']

    def start(self):
        print self.hash("hello bitcoin")

    def hash(self, data):
        return hashlib.sha3_512(data).hexdigest().upper()
