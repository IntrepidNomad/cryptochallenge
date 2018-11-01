import base64

def hex2base64(hexstring):
	vhex = bytes.fromhex(hexstring)
	vbase64 = base64.b64encode(vhex)
	print(vbase64)

