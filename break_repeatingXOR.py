file = '6.txt'
import binascii
def break_repeatingXOR(base64_strings):
    unhexed = binascii.unhexlify(base64_strings)
    key_distances=[]

    for keysize in range(2,40):
        chunk1 = unhexed[0,keysize-1].ljust(keysize,'\0')
        chunk2 = unhexed[keysize,2*keysize-1].ljust(keysize,'\0')
        chunk3 = unhexed[keysize*2,keysize*3-1].ljust(keysize,'\0')
        chunk4 = unhexed[keysize*3,keysize*4-1].ljust(keysize,'\0')
        distance1=hammingdistance(chunk1,chunk2)
        distance2=hammingdistance(chunk2,chunk3)
        distance3=hammingdistance(chunk3,chunk4)
        distance4=hammingdistance(chunk4,chunk1)
        average_distance = (distance1+distance2+distance3+distance4)/4
        key_distances[keysize-2]=average_distance/keysize

    keysize_totry = heapq.nsmallest(key_distances,3)
    for keylength in keysize_totry:
        # break ciphertext into blocks
        # transpose blocks
        # try SingleByteXORCipher on each block
        # join keys
        # decrypt

    # select best candidate 
