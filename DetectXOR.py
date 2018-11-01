file = '4.txt'
import binascii
def get_english_score(input):
        character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
        }
        return sum([character_frequencies.get(chr(byte), 0) for byte in input.lower()])

from SingleByteXORCipher import sbXORcipher
#def DetectXOR(file):

	with open(file,'r') as data:
		data_list = data.readlines()
		#list(map(lambda x:x.strip(),data_array))
	print(data_list)
	data_list[0].strip()
	data_decoded=[]
	data_list = [x.strip() for x in data_list]
	print(data_list)

	binascii.unhexlify(data_list[0])
	print(data_list[0])

	for line in data_list:
		nums = binascii.unhexlify(line)
		strings = (''.join(chr(num ^ key) for num in nums) for key in range(256))
		decoded = max(strings, key=lambda s: get_english_score(bytes(s,'utf-8')))
		data_decoded.append(decoded)
	final = max(data_decoded, key=lambda s: get_english_score(bytes(s,'utf-8')))
	print(data_decoded)
	print(final)
#	return decoded_decoded
