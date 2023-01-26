import socket

def fahrenheit_to_celcius(fahrenheit):
    return(fahrenheit - 32) * 5/9

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.169.136'
port = 5555

sock = socket.socket()
print("\nSocket created!")

sock.bind((host, port))
print("\nSocked is binding to", port)

sock.listen(1)

while True:
    print('\nWaiting for the connection...')
    connection, client_address = sock.accept()
    print(f'\nConnection from (client_address)')

    while True:
        data = connection.recv(5555)
        if data:
            temp = float(data.decode())
            print("Latest temperature: ", temp)
            cels = fahrenheit_to_celcius(temp)
            connection.sendall(str(cels).encode())
        else:
            print('\nNo more incoming data from', client_address)
            break

connection.close()


