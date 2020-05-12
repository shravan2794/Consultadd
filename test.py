from sys import argv
nameofprogram,filename=argv


print("Name of program is :", nameofprogram)
print("Name of file", filename)

while True:
    try:
        fh=open(filename)
        content=fh.read()
        print(content)
        fh.close()
        break

    
    except:
        print("The name is enter is wrong, provide")
        try_again=input("Y or N")
        if try_again=='Y':
            filename=input("Please enter correct file name")
        else:
            break
    