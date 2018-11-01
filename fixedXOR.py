def fixedXOR(XORint1,XORint2):
	try:
		output=XORint1^XORint2
		return output
	except (RuntimeError, TypeError, NameError, ValueError):
		print("Error Encountered!")


