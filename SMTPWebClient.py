from socket import *
msg = b'\r\n I love computer networks!'
endmsg = b'\r\n.\r\n'

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'localhost'

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver,25))
recv = clientSocket.recv(1024)
print(recv)
if recv[:3] != b'220': #220 is start reply code
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = b'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != b'250': #250 is OK reply code
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
mailFromCommand = b'MAIL FROM: <padkewun@gmail.com>\r\n'
clientSocket.send(mailFromCommand)
recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != b'250': #250 is OK reply code
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcptToCommand = b'RCPT TO: <kjh398@nyu.edu>\r\n'
clientSocket.send(rcptToCommand)
recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != b'250': #250 is OK reply code
    print('250 reply not received from server.')

# Send DATA command and print server response.
dataCommand = b'DATA\r\n'
clientSocket.send(dataCommand)
recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != b'354': #354 is ready for body message reply code
    print('354 reply not received from server.')

# Send message data.
clientSocket.send(msg)
clientSocket.send(endmsg)

# Message ends with a single period.
recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != b'250': #250 is OK reply code
    print('250 reply not received from server.')

# Send QUIT command and get server response.
quitCommand = b'QUIT\r\n'
clientSocket.send(quitCommand)
clientSocket.close
print(recv1)
if recv1[:3] != b'221': #221 is ending reply code
    print('221 reply not received from server.')
