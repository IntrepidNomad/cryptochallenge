import base64
import heapq
import io
import operator
from englishscore import get_english_score
file = '6.txt'
data = open(file,'r')
data = data.read().strip('/n')
data = base64.b64decode(data)
unbased = data
decoded_list=[]
import binascii
#def break_repeatingXOR(base64_strings):
    #unbased = base64.b64decode(base64_strings)
    key_distances=[]
from hammingdistance import hammingdistance
    for keysize in range(2,41):
        chunk1 = str(unbased[0:keysize-1].ljust(keysize,b'\0'),'utf-8')
        chunk2 = str(unbased[keysize:2*keysize-1].ljust(keysize,b'\0'),'utf-8')
        chunk3 = str(unbased[keysize*2:keysize*3-1].ljust(keysize,b'\0'),'utf-8')
        chunk4 = str(unbased[keysize*3:keysize*4-1].ljust(keysize,b'\0'),'utf-8')
        distance1=hammingdistance(chunk1,chunk2)
        distance2=hammingdistance(chunk2,chunk3)
        distance3=hammingdistance(chunk3,chunk4)
        distance4=hammingdistance(chunk4,chunk1)
        average_distance = (distance1+distance2+distance3+distance4)/4
        key_distances.append(average_distance/keysize)
    print(key_distances[27])
    keysize_totry = heapq.nsmallest(8,range(len(key_distances)), key_distances.__getitem__)
    keysize_totry=[x.__add__(2) for x in keysize_totry]
    print(keysize_totry)

    for keylength in keysize_totry:
        blocks=[]
        data_stream = io.BytesIO(data)
#data_stream.read(2)
        # break ciphertext into blocks
        while True:
            block_data= data_stream.read(keylength)
            if block_data ==b'':
                break
            else:
                blocks.append(data_stream.read(keylength).ljust(keylength,b'\0'))
        # transpose blocksdata_stream = io.BytesIO(data)
        transposed_blocks = []
        for x in range(keylength):
            transposed_blocks.append(b'')
            for y in range(len(blocks)):
                transposed_blocks[x]+=bytes([blocks[y][x]])
        # try SingleByteXORCipher on each block
        block_key=b''
        strings=[]
        for block in transposed_blocks:
            strings=[]
            for key in range(256):
                strings.append('')
                for num in block:
                    strings[key]+= chr(num ^ key)
            block_key += bytes([strings.index(max(strings, key=lambda s: get_english_score(bytes(s,'utf-8'))))])
        # join keys


        # decrypt
        decoded=b''
        for i in range(len(unbased)):
            keynum = i%len(block_key)
            decoded += bytes(chr(unbased[i]^block_key[keynum]),'utf-8')

    # select best candidate
        decoded_list.append(decoded)
        print(decoded_list)
    answer = max(decoded_list,key=lambda s: get_english_score(s)).decode('utf-8')
    print(answer)
