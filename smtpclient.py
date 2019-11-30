from socket import *
import sys


####SMTP reply codes:

#200	(nonstandard success response, see rfc876)
#211	System status, or system help reply
#214	Help message
#220	<domain> Service ready
#221	<domain> Service closing transmission channel
#250	Requested mail action okay, completed
#251	User not local; will forward to <forward-path>
#252	Cannot VRFY user, but will accept message and attempt delivery
#354	Start mail input; end with <CRLF>.<CRLF>
#421	<domain> Service not available, closing transmission channel
#450	Requested mail action not taken: mailbox unavailable
#451	Requested action aborted: local error in processing
#452	Requested action not taken: insufficient system storage
#500	Syntax error, command unrecognised
#501	Syntax error in parameters or arguments
#502	Command not implemented
#503	Bad sequence of commands
#504	Command parameter not implemented
#521	<domain> does not accept mail (see rfc1846)
#530	Access denied (???a Sendmailism)
#550	Requested action not taken: mailbox unavailable
#551	User not local; please try <forward-path>
#552	Requested mail action aborted: exceeded storage allocation
#553	Requested action not taken: mailbox name not allowed
#554	Transaction failed

print ">>>>>>NOTE: all messages started with >> are from my client, and are debug notes"

msg = "Hiii this is Sofia and I am testing this smtp client"
my_uvic_email_adr = "thomasbesenski@uvic.ca"
sender_uvic_email_adr = "mcheng@uvic.ca"

# Choose a mail server (e.g. Google mail server) and call it mailserve

#######this is the url which is the mailserver at uvic
mailserver = "smtp.uvic.ca"
mailserver_ip=gethostbyname(mailserver)

# Create socket called clientSocket and establish a TCP connection with mailserver







########no need to bind it since this is a client socket
########port 25 is what the smtp server in uvic is bound to
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((mailserver_ip,25))


recv = clientSocket.recv(1024).decode()
print(recv)
########a 220 code is for the connection established amd the service is ready
if recv[:3] != '220':
	print('220 reply not received from server.')




# Send HELO command and print server response.
heloCommand = 'HELO thomasbesenski\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
### 250= requested mail action OKAY
if recv1[:3] != '250':
    print('>>250 reply not received from server.')
    
# Send MAIL FROM command and print server response.

mailfromcommand = "mail from: {}\r\n".format(sender_uvic_email_adr)
clientSocket.send(mailfromcommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('>>250 reply not received from server.')

# Send RCPT TO command and print server response. 

rcpttocommand = "rcpt to: <{}>\r\n".format(my_uvic_email_adr)
clientSocket.send(rcpttocommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('>>250 reply not received from server.')

# Send DATA command and print server response. 
#??????
clientSocket.send("data\r\n".encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
#####354= start mail input ending with \n.\n
if recv1[:3] != '354':
    print('>>354 reply not received from server.')
# Send message data.
#??????
end_msg = "\r\n.\r\n"
sending_message = msg +end_msg
print ">>this is the message about to be send\n " + sending_message
clientSocket.send(sending_message.encode())

recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('>>250 reply not received from server.')
# Message ends with a single period.
# Send QUIT command and get server response.

clientSocket.send("quit\n".encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
#####221 : closing transmission channel
if recv1[:3] != '221':
    print('>>221 reply not received from server.')

