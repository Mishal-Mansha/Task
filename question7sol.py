class characterCount:
    string=""
    def func1(self,string):
       try:
           int(string)
           print("This is an integer")
           return 0

       except ValueError:
           self.string = string

    def func2(self):
        return len(self.string)

text=characterCount()
text.func1("abc")
print("Total number of characters in string are:",text.func2())
