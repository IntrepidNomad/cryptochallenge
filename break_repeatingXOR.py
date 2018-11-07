import base64
import heapq
import io
import operator
file = '6.txt'
data = open(file,'r')
data = data.read().strip('/n')
data = base64.b64decode(data)
unbased = data
import binascii
#def break_repeatingXOR(base64_strings):
    unbased = base64.b64decode(base64_strings)
    key_distances=[]
from hammingdistance import hammingdistance
    for keysize in range(2,40):
        chunk1 = str(unbased[0:keysize-1].ljust(keysize,b'\0'),'ascii')
        chunk2 = str(unbased[keysize:2*keysize-1].ljust(keysize,b'\0'),'ascii')
        chunk3 = str(unbased[keysize*2:keysize*3-1].ljust(keysize,b'\0'),'ascii')
        chunk4 = str(unbased[keysize*3:keysize*4-1].ljust(keysize,b'\0'),'ascii')
        distance1=hammingdistance(chunk1,chunk2)
        distance2=hammingdistance(chunk2,chunk3)
        distance3=hammingdistance(chunk3,chunk4)
        distance4=hammingdistance(chunk4,chunk1)
        average_distance = (distance1+distance2+distance3+distance4)/4
        key_distances.append(average_distance/keysize)

    keysize_totry = heapq.nsmallest(3,range(len(key_distances)), key_distances.__getitem__)
    keysize_totry=[x.__add__(2) for x in keysize_totry]
    print(keysize_totry)
    data_stream = io.BytesIO(data)
    blocks=[]
#    data_stream.read(4)
    for keylength in keysize_totry:
        i=0# break ciphertext into blocks
        while (data_stream):
            blocks.append(data_stream.read(keylength).ljust(keylength,b'\0'))
            i+=1

        # transpose blocks
        transposed_blocks = []
        for x in range(keylength-1):
            for slice in blocks:
                transposed_blocks[x]+=slice[x]

        # try SingleByteXORCipher on each block
        for block in transposed_blocks:
            strings = (''.join(chr(num ^ key) for num in block) for key in range(256))
            block_key += bytes(strings.index(max(strings, key=lambda s: get_english_score(bytes(s,'utf-8')))))
        # join keys

        # decrypt
        for i in range(len(unbased)):
            keynum = i%len(block_key)
            decoded += bytes(chr(unbased[i]^block_key[keynum]),'utf-8')

    # select best candidate
        print(decoded)

test = 'testing'
testch1= test[0:9].ljust(9,'\0')
print(testch1)
i = range(205)
print(i[::10])
