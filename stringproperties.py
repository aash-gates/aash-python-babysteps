program to check the properties of the givin string IBM Digital Nation

string = "aashikJKrishnan"     # Change the string text between the quotation marks to see what the program does

if string.isspace():
    print("only white spaces")
	
elif string.isalpha():
    print("only letters")
	
elif string.isdigit():
    print("only digits")
	
elif string.isalnum():
    print("digits and letters")
	
else:
    print("digits, letters, and/or symbols")
    
#end-of-the-program