import socket
import sys
import threading

class ChatServer:
    def __init__(self, host='localhost', port=10000):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = {}
    #function to handle client connections
    def handle_client(self, connection, client_address):
        print("Connection from", client_address)
        current_username = None
        try:
            #Registration phase
            connection.send("Welcome to the Chat Server! Please enter your username: ".encode('utf-8'))
            current_username = connection.recv(2048).decode('utf-8').strip()
            self.clients[current_username] = connection
            print(f"User {current_username} registered.")
            connection.send(f"Hello {current_username}. To chat, type: 'TargetName: Message'".encode('utf-8'))
            
            #MAIN CHAT LOOP
            while True:
                message=connection.recv(2048).decode('utf-8')
                if not message:
                    break
                if message=='BYE':
                    print("Client requested to close the connection. Goodbye!")
                    break
                print(f"Received from {current_username}: {message}")
                #Routing Logic
                if ':' in message:
                    #Split target and content
                    target_name, content=message.split(':',1)
                    target_name=target_name.strip()
                    #Look for target in dictionary
                    if target_name in self.clients:
                        target_socket=self.clients[target_name]
                        target_socket.send(f"{current_username} says: {content}".encode('utf-8'))
                    else:
                        connection.send(f"User {target_name} not found.".encode('utf-8'))
                else:
                    connection.send("Invalid message format. Use 'TargetName: Message'.".encode('utf-8'))

        except Exception as e:
            print("Error:", e)
        finally:
            #Cleanup on disconnect
            if current_username in self.clients:
                del self.clients[current_username]
            print("Closing connection from", client_address)
            connection.close()


    #Main accept loop
    def start(self):
        try:
            # Bind and open the socket for listening to 5 connections
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5) 
            print(f"Server started on {self.host}:{self.port}")
            print("Waiting for connections...")
            
            while True:
                # 1. Accept new connection
                client_socket, client_address = self.server_socket.accept()
                # 2. Spawn a new thread for this client
                thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
                thread.start()
        except Exception as e:
            print(f"Server failed to start: {e}")
if __name__ == "__main__":
    server = ChatServer()
    server.start()
