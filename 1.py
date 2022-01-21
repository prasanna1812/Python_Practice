'''progrram to find the multiplication of the factors of a particular number'''
In_Num=(int)(input("enter a valid integer\n"))
Fact_List=[]
Index=0
Counter=1
Mul=1
while(Counter<In_Num):

	if(In_Num%Counter==0):
	    	Fact_List.append(Counter)
	    	Index=Index+1
	Counter=Counter+1
Index=0
#print(Index)
print("the factors of the entered number are\n")	
print(Fact_List)
#print(Counter)
for Index in range(len(Fact_List)):
	#print("printing index")
	#print(Index)
	Mul=Mul*(Fact_List[Index])
	#Index=Index+1
print("Mutiplication of the factors of entred number\n")
print(Mul)
