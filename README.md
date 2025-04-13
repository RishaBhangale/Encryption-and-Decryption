# Secure Socket Communication with Custom Encryption

This project demonstrates a simple client-server application that establishes secure communication using custom encryption and decryption functions. Both the client and server leverage socket programming and implement a two-stage encryption algorithm, consisting of a substitution cipher and a column transposition cipher.

## Overview

The system comprises two Python scripts:

- **client.py:**  
  The client script reads a plaintext message from the user, encrypts it using the provided key, and sends it to the server. After sending the message, the client listens for a response, decrypts the incoming message, and displays it.

- **server.py:**  
  The server script waits for a connection from the client. When a message is received, it decrypts the data using a key supplied by the user, displays the decrypted message, and sends a response back after encrypting it with a user-provided key.

## Features

- **Custom Encryption/Decryption:**  
  The encryption algorithm is implemented in two parts:
  1. **Substitution Cipher:**  
     Performs a character substitution based on a computed shift that uses the ASCII values of the key characters. The shift operation uses a predefined list of prime numbers to determine whether to add or subtract ASCII values.
  2. **Column Transposition Cipher:**  
     After the substitution, the message is further encrypted using a column transposition method. The key is split based on whether its characters’ ASCII values are prime, and these components determine the transposition order.
  
- **Socket Communication:**  
  The application uses Python’s socket library to create a client-server model over localhost on port 8000. The server listens for incoming connections and the client initiates the connection and transmits the encrypted message.

## Prerequisites

- **Python 3:**  
  Ensure you have Python 3 installed. Download it from [python.org](https://www.python.org/).

- **Standard Libraries:**  
  The project uses Python's standard libraries (`socket`, `string`, `math`). No external packages are required.

## Installation and Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```
   
2. **Make Python Scripts Executable (Optional):**  
   To run the Python scripts directly from the terminal:
   - Add the following shebang line to the top of each Python file:
     ```python
     #!/usr/bin/env python3
     ```
   - Make the file executable by running:
     ```bash
     chmod +x client.py
     chmod +x server.py
     ```

## Usage

1. **Start the Server:**  
   Open a terminal and run the server script:
   ```bash
   python server.py
   ```
   The server will display the hostname and wait for an incoming connection.

2. **Run the Client:**  
   In another terminal, run the client script:
   ```bash
   python client.py
   ```
   - The client prompts you to enter a message and a key for encryption.
   - It encrypts the message, sends it to the server, and then waits for the server’s response.
   - When a response is received, the client prompts for a key to decrypt it and displays the original message.

3. **Bidirectional Communication:**  
   The server, upon receiving the message, will prompt for a key to decrypt it, display the decrypted text, and then ask for a message and key to send back to the client. This allows for a simple interactive session using custom encryption and decryption on both ends.

## Encryption Details

- **Substitution Cipher:**  
  The `encrypt` function computes a shift value based on the characters in the key, adjusted by checking positions against a list of prime numbers. Each character in the plaintext is then shifted within a reference set of characters (uppercase, digits, lowercase, and space).

- **Column Transposition Cipher:**  
  The `coltran_encrypt` function transposes the text into a matrix form based on the length of the key. The rows are then rearranged according to the sorted order of key components (prime vs. composite values). The decryption process reverses this ordering to retrieve the original plaintext.

## Contact

For questions, suggestions, or contributions, please open an issue on the GitHub repository or contact the maintainer at rishabhbhangale@gmail.com

---
