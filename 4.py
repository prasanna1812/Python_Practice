'''Given a string of lowercase characters from ‘a’ – ‘z’.
   We need to write a program to print the characters of this string in sorted order.
	Input : 'python'
	output: 'hnopty' '''
input_string=(str)(input("enter a valid lowercase string\n"))
#print(input_string)
new_string=(sorted(input_string))
com_string=""
new_string=com_string.join(new_string)
print(new_string)
#test_string=join(new_string)		