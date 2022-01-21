'''Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
	If the given string is already ends with 'ing' then add 'ly' instead.
	If the string length of the given string is less than 3, leave it unchanged '''
input_str=(str)(input("enter a valid string\n"))
input_str=input_str.lower()
#print(input_str)
str_len=len(input_str)
if(str_len>=3):
	if((input_str[str_len-3]=='i')&(input_str[str_len-2]=='n')&(input_str[str_len-1]=='g')):
		#print("ing letters are present in the string")
		input_str=input_str+'ly'
		print(input_str)
	else:
		input_str=input_str+'ing'
		print(input_str)
else:
	print("no operation performed on the string:",input_str)