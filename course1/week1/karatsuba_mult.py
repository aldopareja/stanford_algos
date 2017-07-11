import random


#karatsuba
# params: a,b: numbers to multiply, must be strings
# returns: a*b: integer type
def karatsuba(a,b):
	if len(a)*len(b) == 0:
		return 0
	if len(a)<=2 and len(b)<=2:
		return int(a)*int(b)
	ak = len(a)//2
	bk = len(b)//2
	a1 = a[:ak]
	b1 = b[:bk]
	a2 = a[ak:]
	b2 = b[bk:]
	ak = len(a)-ak
	bk = len(b)-bk
	a1b1 = karatsuba(a1,b1)
	a1b2 = karatsuba(a1,b2)
	b1a2 = karatsuba(b1,a2)
	a2b2 = karatsuba(a2,b2)

	ab = 10**(ak+bk)*a1b1 + 10**ak*a1b2 + 10**bk*b1a2 + a2b2
	return ab


maxLen = 10
maxVal = 10**maxLen-1

#testing loop
while True:
	a = random.randint(0,maxVal)
	b = random.randint(0,maxVal)
	if a*b != karatsuba(str(a),str(b)):
		print('inputs',a,b)
		print(karatsuba(str(a),str(b)),a*b)
		break