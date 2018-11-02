import binascii
encoded = b''
key = b'ICE'
with open('stanza.txt', 'r') as file:
  string= file.read()
  print (string)
#def repeatingXOR(string,key):
unencoded = bytes(string,'utf-8')
for i in range(len(unencoded)):
    keynum = i%len(key)
    encoded += bytes(chr(unencoded[i]^key[keynum]),'utf-8')
print(encoded)
encoded_hex = binascii.hexlify(encoded)
print(encoded_hex)
#    return encoded_hex
