string=input("Enter any string")
letters=0
digits=0
for c in string:
        if(c.isdigit()):
            digits+=1
        if(c.isalpha()):
            letters+=1
print("Number of letters are:",letters)
print("Number of digits are:",digits)
