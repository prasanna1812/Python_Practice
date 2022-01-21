'''Given an list with N elements, task is to find the count of factors of a number X
   which is product of all list elements.
	Input : 3 5 7
	Output : 8
	3 * 5 * 7 = 105, the factors of 105 are 1,
	3, 5, 7, 15, 21, 35, 105 whose count is 8'''
input_list=[]
fac_list=[]
fac_counter=0
list_mul=1
index=0
num_elements=(int(input("enter the no of elements that would be present in the list\n")))
while(num_elements>0):
	input_list.append((int)(input()))
	num_elements=num_elements-1
#input_list.append(input('enter the list elements'))
print(input_list)
for index in range(0,len(input_list)):
	list_mul=list_mul*(input_list[index])
print(list_mul)
index=1
while(index<=list_mul):
	if(list_mul%index==0):
		fac_list.append(index)
		fac_counter=fac_counter+1
	else:
		pass
	index=index+1
print("\n The count is:",fac_counter)



