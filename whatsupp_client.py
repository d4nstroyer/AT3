# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 20:39:43 2024

@author: Danny
"""

import socket

# Function to filter and replace specific words in client messages
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

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect the socket to the server's address and port
    client_socket.connect(('localhost', 65432))
    print("Connected to the Whatsupp Server")
    
    while True:
        # Get message input from the client and filter it
        message = input("Client (type 'exit' to end): ")
        filtered_message = filter_words(message)
        
        # Send the filtered message to the server
        client_socket.sendall(filtered_message.encode('utf-8'))
        
        # Print the client's own message to keep a log of what was sent
        print(f"Client: {filtered_message}")
        
        if message.lower() == 'exit':
            print("Client ended the connection.")
            break
        
        # Receive the server's response
        response = client_socket.recv(1024).decode('utf-8')
        
        if response.lower() == 'exit':
            print("Server ended the connection.")
            break
        
        print(f"Server: {response}")
    
    # Close the connection
    client_socket.close()
    print("Client closed the connection.")

if __name__ == "__main__":
    start_client()

