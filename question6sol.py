
string=input("Enter a comma seperated list of numbers:")
if(len(string)>=2):
    lists=string.split(",")
    list1=[]
    for i in lists:
        list1.append(int(i))
    list1.sort()
    print("Second minimum number is:",list1[1])
else:
    print("For second minimum numbber enter more than one number")
