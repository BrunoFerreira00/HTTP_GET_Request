from socket import *

# Setting the host and the port
HOST = "127.0.0.1"
PORT = 80 #HTTP Port

# Set TCP connection
server_socket = socket(AF_INET,SOCK_STREAM)
# Connect to the server
server_socket.connect((HOST, PORT))

# Request info
request = b"GET /dashboard/ HTTP/1.1\r\nHost: " + HOST.encode() + b"\r\n\r\n"
# Send Request
server_socket.send(request)

# Create response variable to store data
response = b""
#Open infinite loop
while True:
    # Get data from request
    data = server_socket.recv(1024)
    # If there's no data break
    if not data:
        break
    # Add data to the response
    response += data


# Get status code
status_code = int(response.split(b"\r\n")[0].split()[1])

# Separate headers from the body and extract headers from the response
headers = response.split(b"\r\n\r\n")[0]

# Print status code
print("Status code:",status_code)

# Print headers
print("Headers:")
for header in headers.split(b"\r\n"):
    print(header.decode())

# Close connection
server_socket.close()
    
