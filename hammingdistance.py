string1="this is a test"
string2="wokka wokka!!!"
bits1=''
bits2=''
#def hammingdistance(string1,string2):
    if len(string1)!=len(string2):
        raise ValueError("Strings must have the same size")
    bytes1 = bytes(string1,'ascii')
    bytes2 = bytes(string2,'ascii')
    for byte in bytes1:
        bits1+=format(byte,'b').zfill(8)
    for byte in bytes2:
        bits2+=format(byte,'b').zfill(8)

    print(bits1)
    print(bits2)
    distance = 0

    len(bits1)
    len(bits2)
    for i in range(len(bits1)):
        if bits1[i]!=bits2[i]:
            distance+=1
#    return distance
print(distance)