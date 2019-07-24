string=input("Enter a list of numbers:")
lists=string.split(',')
minNum=int(lists[0])
for i in lists:
    if(int(i)<minNum):
        minNum=int(i)
print("Minimum number in the list is:",minNum)
