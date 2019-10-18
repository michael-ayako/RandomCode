#Finding positive prime numbers in a range
import sys
num = int(sys.argv[0])

#Funtion to fetch prime numbers
def fetchprimenumbers():
	z = ""
	v = 0
	primenums = []
	x = 2
	while x<num:
		count = 2
		chk = 0
		while count <= x:
			if x % count == 0 and  x != count:
				chk += 1	
			count += 1 
		if chk  == 0 :
			primenums.append(x)
			v +=1
		x += 1
	for q in primenums: 
		z = z + str(q)+" , "
	print("Prime numbers between the range of 2 and ",num," are "+ z)
	print("This range has "+str(v))


if(num<=2):
	print("This value cannot be equivalent to 2 or lower\n")
	exit()
else: 
	fetchprimenumbers()
	exit()



	