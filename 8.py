'''8. Print the following pattern (for length n)
	1
	2 2
	3 3 3
	4 4 4 4
	5 5 5 5 5'''
len=(int)(input("enter the length of the pattern\n"))
loop=1
pt_len=0
while(loop<=len):
	for pt_len in range(0,loop):
		print(loop,"\r")
		#print("\r")
	loop=loop+1
