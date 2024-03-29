import sys
# thrift 0.9.1
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.Thrift import TException

import gen_py.ping_pong.ping_pong

class ping_pong_server(gen_py.ping_pong.ping_pong.Processor):
    def __init__(self, my_address, my_port):
        self.my_address = my_address
        self.my_port = my_port

    def startServer(self):
        processor = gen_py.ping_pong.ping_pong.Processor(self)
        transport = TSocket.TServerSocket(host=self.my_address, port=self.my_port)
        tfactory = TTransport.TBufferedTransportFactory()
        pfactory = TBinaryProtocol.TBinaryProtocolFactory()

        server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

        print 'Starting the server...'
        server.serve()
        print 'done.'


    def ping(self):
        print "received ping()"
        return "pong"

ping_pong_server('localhost', 9900).startServer();
