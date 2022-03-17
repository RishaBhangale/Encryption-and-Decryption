import socket
import string
import math
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,    
        71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151]

#Encrypt Cipher
def encrypt(pt,key):
    key = [ord(i) for i in key]
    shift = 0
    for i in range(1, len(key)+1):
        if i in prime:
            shift -= key[i-1]
        else:
            shift += key[i-1]
    enc = ''.join([str(ref[(int(ref.index(str(t)))+shift)%63]) for t in pt])
    return enc

def decrypt(ct,key):
    key = [ord(i) for i in key]
    shift = 0
    for i in range(1, len(key)+1):
        if i in prime:
            shift -= key[i-1]
        else:
            shift += key[i-1]
    dec = ''.join([str(ref[(int(ref.index(str(t)))-shift)%63]) for t in ct])
    return dec

def coltran_encrypt(pt,key):
    plain_text = pt
    Key_input = key

    k_index = 0
    cipher = ""
    prime_key = []
    composite_key = []

    plain_text_len = float(len(plain_text))
    plain_text_list = list(plain_text)
    Key = [ord(i) for i in Key_input]

    for i in Key:
        if i in prime:
            prime_key.append(i)
        else:
            composite_key.append(i)

    prime_key_list = sorted(list(prime_key))
    composite_key_list = sorted(list(composite_key))
    Key_list = prime_key_list + composite_key_list

    col = len(Key)
    row = int(math.ceil(plain_text_len / col))

    fill_null = int((row * col) - plain_text_len)
    plain_text_list.extend('_' * fill_null)

    matrix = [plain_text_list[i: i + col] for i in range(0, len(plain_text_list), col)]
    print()

    for element in Key_list:
        curr_idx = Key.index(element)
        Key[curr_idx] = "/"
        cipher += ''.join([row[curr_idx] for row in matrix])
        k_index += 1

    return cipher

def coltran_decrypt(ct,key):
    cipher = ct
    Key_input = key
    message = ""
    k_index = 0
    prime_key = []
    composite_key = []
    key = list(Key_input)

    message_index = 0
    message_len = float(len(cipher))
    message_list = list(cipher)

    col = len(key)
    row = int(math.ceil(message_len / col))

    Key = [ord(i) for i in key]

    for i in Key:
        if i in prime:
            prime_key.append(i)
        else:
            composite_key.append(i)

    prime_key_list = sorted(list(prime_key))
    composite_key_list = sorted(list(composite_key))
    Key_list = prime_key_list + composite_key_list

    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]

    for element in Key_list:
        curr_idx = Key.index(element)
        key[curr_idx] = "/"

        for j in range(row):
            dec_cipher[j][curr_idx] = message_list[message_index]
            message_index += 1

    message = ''.join(sum(dec_cipher, []))

    null_count = message.count('_')
    if null_count > 0:
        return message[: -null_count]
    return message

def Encrypt(pt,key):
    v=encrypt(pt,key)
    return coltran_encrypt(v,key)

def Decrypt(ct,key):
    v=coltran_decrypt(ct,key)
    return decrypt(v,key)

ref = [st for st in string.ascii_uppercase]
ref.extend(list(map(str,[*range(0,10)])))
ref.extend([st for st in string.ascii_lowercase])
ref.extend([" "])
s=socket.socket()
host=socket.gethostname()
print("The host is:",host)
s.bind(('localhost',8000))
s.listen(1)
data=""

conn,client=s.accept()
print("Connected to ",client)
data=conn.recv(1024).decode()
key1 = (input("Enter key for decryption: "))
print("received from client {}".format(Decrypt(data,key1)))
rec=input("Enter Message to send: ")
key = (input("Enter key for encryption: "))
message=Encrypt(rec,key)
conn.send(bytes(message,'utf-8'))
conn.close()