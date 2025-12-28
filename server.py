import socket
import sys
import threading

#function to handle client connections
def handle_client(connection, client_address):
    print("Connection from", client_address)
    connection.send("Welcome to the Chat Server! Type BYE to end chat.".encode('utf-8'))
    try:
        while True:
            message=connection.recv(2048).decode('utf-8')
            if not message:
                break
            if message=='BYE':
                print("Client requested to close the connection.")
                break
            print(f"Received from {client_address}: {message}")
            #optionally send a response back to client // REMOVE THIS LINE IF NOT NEEDED
            response = f"Server received: {message}"
            connection.send(response.encode('utf-8'))

    except Exception as e:
        print("Error:", e)
    finally:
        print("Closing connection from", client_address)
        connection.close()

#setup server socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print("connecting to {} port {}".format(*server_address))
sock.bind(server_address)

#start listening for incoming connections
sock.listen(5)
while True:
    connection, client_address = sock.accept()
    client_thread = threading.Thread(target=handle_client, args=(connection, client_address))
    client_thread.start()
    

