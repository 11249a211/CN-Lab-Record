import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 12346))
server.listen(1)

print("Chat Server is waiting for a client...")

conn, addr = server.accept()
print("Client connected:", addr)
print("Type 'exit' to close the chat.")

while True:
    message = conn.recv(1024).decode()
    if not message or message.lower() == "exit":
        print("Client disconnected.")
        break

    print("Client:", message)

    reply = input("You: ")
    conn.sendall(reply.encode())

    if reply.lower() == "exit":
        break

conn.close()
server.close()
print("Chat Server closed.")

output:
Chat Server is waiting for a client...
Client connected: ('127.0.0.1', 54322)
Type 'exit' to close the chat.
Client: Hello!
You: Hi there!
Client: How are you?
You: Doing well, thank you.
Client: exit
Client disconnected.
Chat Server closed.
