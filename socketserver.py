import socket


HOST = '0.0.0.0'  # attacker's IP address to bind the server socket to
PORT = 4444             # Port number to listen on
LOG_FILE = "received_logs.txt"

def start_server():
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the socket to the specified host and port
        server_socket.bind((HOST, PORT))
        # Enable the server to accept connections
        server_socket.listen(10)
        print(f"Server listening on {HOST}:{PORT}")

        # Main loop: wait for client connections
        while True:
            # Accept a new client connection
            conn, addr = server_socket.accept()
            print(f"Connection established from {addr}")

            try:
                # Use the connection in a context manager to ensure it's closed properly
                with conn:
                    # Receive data in a loop from the connected client
                    while True:
                        data = conn.recv(1024)  # Receive up to 1024 bytes
                        if not data:
                            # No data means client disconnected
                            print(f"[-] Connection closed by {addr}")
                            break
                        # Decode bytes to string
                        decoded = data.decode(errors='ignore')
                        print(f"{decoded}",end ='')
                        write_to_file(decoded)  # Save received data to the log file
            except Exception as e:

                print(f"[!] Error with connection {addr}: {e}")
            finally:
                conn.close()

def write_to_file(decoded):
    try:
        # Open the log file in append mode and write the new log data
        with open(LOG_FILE, "a") as f:
            f.write(decoded)
    except Exception as e:

        print(f"[!] Failed to write to file: {e}")


if __name__ == "__main__":
    start_server()

