import random
import socket
import threading

# list of quotes
quotes = ["A day without sunshine is like, you know, night.",
          "Be the change you wish to see in the world.",
          "The only way to do great work is to love what you do.",]

def handle_client(client_socket):
    """Handles a single client's request for a quote"""
    # Send a random quote to the client
    client_socket.send(random.choice(quotes).encode())
    client_socket.close()

def main():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_socket.bind(('192.168.169.136', 5555))

    # Listen for incoming connections
    server_socket.listen()

    while True:
        # Accept a new client connection
        client_socket, client_address = server_socket.accept()

        # Handle the client in a new thread
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == '__main__':
    main()
