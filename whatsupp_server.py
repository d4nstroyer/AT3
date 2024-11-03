# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 21:30:59 2024

@author: Danny
"""

import socket
from datetime import datetime

# Function to filter and replace specific words in messages
def filter_words(message):
    replacements = {
        "damn": "****",
        "stupid": "*****",
        "idiot": "*****",
        "*smile*": "(^_^)",
        "*sad*": "(T_T)"
    }
    for word, replacement in replacements.items():
        message = message.replace(word, replacement)
    return message

def start_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the address and port
    server_socket.bind(('localhost', 65432))
    
    # Listen for incoming connections
    server_socket.listen(1)
    print("Whatsupp Server is waiting for client to connect")
    
    # Wait for a connection
    connection, client_address = server_socket.accept()
    
    # Get the current time of connection
    connection_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{client_address} entered the chat room at {connection_time}")
    
    while True:
        # Receive the message from the client
        message = connection.recv(1024).decode('utf-8')
        
        if message.lower() == 'exit':
            print("Client exited the chat room.")
            break
        
        # Filter banned words from the client's message
        filtered_message = filter_words(message)
        print(f"Message from client: {filtered_message}")
        
        # Get server's response, then filter it before sending
        response = input("Server (type 'exit' to end): ")
        filtered_response = filter_words(response)
        
        # Send the filtered response to the client
        connection.sendall(filtered_response.encode('utf-8'))
        
        # Print the server's own filtered response to keep a log of what was sent
        print(f"Server: {filtered_response}")
        
        if response.lower() == 'exit':
            print("Server ended the connection.")
            break
    
    # Close the connection
    connection.close()
    server_socket.close()
    print("Server closed the connection.")

if __name__ == "__main__":
    start_server()



