hexstring= '0e3647e8592d35514a081243582536ed3de6734059001e3f535ce6271032'
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
import binascii
#def sbXORcipher(hexstring):
	nums = binascii.unhexlify(hexstring)
	strings = (''.join(chr(num ^ key) for num in nums) for key in range(256))
	decoded = max(strings, key=lambda s: get_english_score(bytes(s,'utf-8')))
	print (decoded)
	#return decoded
