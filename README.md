# Simple Chat Application (TCP/IP)
Multi threaded application build using TCP sockets library and Tkintern for the GUI. Allows chatting with different users in real time utilizing a server, includes handling of different edge cases such as unexpected disconnects.

## Requirements
Having python installed.

## Structure
* `server.py`: Script ran to host the server, allows for communication between client-client, client-server and vice versa. Shows the needed IP for conveniece after lunch.
* `client_gui.py`: Client application, launches a GUI and acts as client to send and receive communication with host (server)
* `Run Server.bat`': Batch script to launch server enviorment. Make sure it is in the same folder as the server.py script
* `Run Client.bat`: Batch script to launch client enviorment. Make sure it is in the same folder as the client.py script

## Usage Instructions
### Start server
Either run the `Run Server.bat` batch script, or run the `server.py` from the IDE of your choice.

The console will display info like users joining, disconnecting, registering, etc.

*The server will start on your IPv4 address, and will also display what address it started on in the console. You must be within the same network for it to work as intended*

### Connect Clients
Run `client_gui.py` or double-click `Run Client.bat`. A window will open and you will need to enter the following:

* **Server IP:** Enter the IP of the host (auto-filled as 'localhost' by default).
* **Username:** Enter a unique username (cannot be 'Server'). 
**Note**: Host and Client can run on different machines or on the same one using localhost

### Chatting
Thats pretty much it. Once there are at least 2 users online you can select the one you want to chat with. You can freely jump back and forth between the user list and the chat window, along with notifications displaying if a new message is received while not directly in the chat window.

If a user disconnects completely while you are in a chat with them, it will move you back to the user list to choose a different online user.

If you disconnect from the server It will auto complete your last login info for convenience.

## Technical Details
* **Protocol**:
    * `LIST: user1, user2, ...` - Server broadcasts active user list.
    * `MSG: SenderName: Content` - Standard message format.
* **Concurrency**: The server spawns a new `threading.Thread` for every connected client to ensure non-blocking communication.
* * **Networking**: Uses `socket.AF_INET` (IPv4) and `socket.SOCK_STREAM` (TCP).
