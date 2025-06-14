# Remote-Keylogger
Captures keystrokes on a target machine and sends the logs to a remote server and stores them on a text file.

##  Features

- Real-time keystroke capture using pynput
- Remote log delivery via TCP socket
- Reconnection attempts if the connection drops
- Lightweight, extensible codebase 

##  Requirements

- Python 3.x
- pynput

## Usage

Run the socket server with the attacker's IP and port set, on the attacker's machine to listen for incoming logs.
Run the Keylogger with attacker's IP and port set, on the target machine.
