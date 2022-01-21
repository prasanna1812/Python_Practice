'''Write a function to check if the input number is prime or not'''
Input_Num=(int)(input("enter the number greater than one\n"))
Index=2
if(Input_Num>1):
	while(Index<Input_Num):
		if(Input_Num%Index==0):
			print("not a prime number")
			break
		else:
			Index=Index+1
			if(Index==Input_Num):
				print("entered number is a prime number")
else:
	print("enter a valid number")

