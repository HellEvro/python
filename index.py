import md5
import hashlib
import sha3
import msgpack
import msgpackrpc
import pika

class Stampery():
    __eventHandlers = {}
    __apiEndpoints = {'prod' : ['api.stampery.com', 4000],
                     'beta' : ['api-beta.stampery.com', 4000]}
    __amqpEndpoints = {'prod' : ['young-squirrel.rmq.cloudamqp.com', 5672, 'consumer', '9FBln3UxOgwgLZtYvResNXE7', 'ukgmnhoi'],
                     'beta' : ['young-squirrel.rmq.cloudamqp.com', 5672, 'consumer', '9FBln3UxOgwgLZtYvResNXE7', 'beta']}

    def __init__(self, secret, branch = 'prod'):
        self.__clientSecret = secret
        self.__clientId = md5.new(secret).hexdigest()[0:15]
        self.__apiEndpoint = self.__apiEndpoints[branch] or self.__apiEndpoints['prod']
        self.__amqpEndpoint = self.__amqpEndpoints[branch] or self.__amqpEndpoints['prod']

    def start(self):
        self.__apiLogin(self.__apiEndpoint)
        self.__amqpLogin(self.__amqpEndpoint)

    def hash(self, data):
        return hashlib.sha3_512(data).hexdigest().upper()

    def on(self, eventType, callback):
        if(hasattr(callback, '__call__')):
            self.__eventHandlers[eventType] = callback
        else:
            raise ValueError('Event callback is not callable.')

    def __emit(self, eventType, *args):
        if(eventType in self.__eventHandlers):
            self.__eventHandlers[eventType](*args)

    def stamp(self, hash):
        print "\nStamping \n%s" % hash
        try:
            self.__apiClient.call('stamp', hash.upper())
        except Exception as e:
            self.__emit("error", e)

    def __apiLogin(self, endpoint):
        self.__apiClient = msgpackrpc.Client(msgpackrpc.Address(endpoint[0], endpoint[1]), unpack_encoding='utf-8')
        req = self.__apiClient.call_async('stampery.3.auth', self.__clientId, self.__clientSecret)
        req.join()
        self.__auth = req.result
        print "logged %s  Auth %s" % (self.__clientId, self.__auth)

    def __amqpLogin(self, endpoint):
        credentials = pika.PlainCredentials(endpoint[2],endpoint[3])
        params = pika.ConnectionParameters(endpoint[0],endpoint[1],  endpoint[4], credentials)
        amqpConn = pika.BlockingConnection(params)
        print('[QUEUE] Connected to Rabbit!')
        self.__emit("ready")

        def callback(ch, method, properties, body):
            hash = method.routing_key
            proof = msgpack.unpackb(body)
            ch.basic_ack(delivery_tag = method.delivery_tag)
            self.__emit("proof", hash, proof)

        channel = amqpConn.channel()
        channel.basic_consume(callback, queue = self.__clientId + '-clnt')

        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()
            print("\nClosing the client")
