import msgpackrpc
import md5

class Stampery:
    apiEndpoints = {'prod' : ['api.stampery.com', 4000],
                     'beta' : ['api-beta.stampery.com', 4000]}
    amqpEndpoints = {'prod' : ['young-squirrel.rmq.cloudamqp.com', 5672, 'consumer', '9FBln3UxOgwgLZtYvResNXE7', 'ukgmnhoi'],
                     'beta' : ['young-squirrel.rmq.cloudamqp.com', 5672, 'consumer', '9FBln3UxOgwgLZtYvResNXE7', 'beta']}

    def __init__(self, secret, branch = 'prod'):
        self.clientSecret = secret
        self.clientId = md5.new(secret).hexdigest()
        self.apiEndpoint = self.apiEndpoints[branch] or self.apiEndpoints['prod']
        self.amqpEndpoint = self.amqpEndpoints[branch] or self.amqpEndpoints['prod']

    def start(self):
        print self.apiEndpoint
        print self.amqpEndpoint
