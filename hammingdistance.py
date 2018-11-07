def hammingdistance(string1,string2):
    if len(string1)!=len(string2):
        raise ValueError("Strings must have the same size")
    bytes1 = bytes(string1,'ascii')
    bytes2 = bytes(string2,'ascii')
    bits1=b''
    bits2=b''
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
    return distance
