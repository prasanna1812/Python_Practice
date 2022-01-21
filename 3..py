'''2. Integers X and K are given. The task is to find largest K-digit number divisible by X.
    (Hint - Use max function)
	Input : X = 83, K = 5
	Output : 99932 is the largest 5 digit number that is divisible by 83.'''
import math
X=(int)(input("enter the number that will be used for dividing the larger number"))
K=(int)(input("enter the number of digits"))
div_list=[]
min_number=(pow(10,(K-1)))
#min_number=min_number-1
max_number=(pow(10,K))-1
max_div_num=0
Index=0
#print(min_number)
#print(max_number)
while(min_number<=max_number):
	if(min_number%X==0):
		div_list.append(min_number)
	min_number=min_number+1
#print("the list of divisible numbers is")
#print(div_list)
print("the highest number divisible by input number is")
print(min(div_list))

