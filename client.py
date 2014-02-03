import time
# thrift 0.9.1
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.Thrift import TException

import gen_py.ping_pong.ping_pong

socket = TSocket.TSocket('localhost', 9900)
transport = TTransport.TBufferedTransport(socket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = gen_py.ping_pong.ping_pong.Client(protocol)

while (1):
    try:
        transport.open()
        print "pinging ..."
        print client.ping()
        transport.close()
        time.sleep(1)
    except TException, tx:
        print "%s" % (tx.message)
