#Writng in the file
'''
fout=None
try:
    fout=open("d:/filehandling1.txt","w")
    msg=input("type some message")
    fout.write(msg)
except FileNotFoundError as ex1:
    print("Cannot create the file",ex1)
except OSError as ex2:
    print("Cannot write the data in the file",ex2)
finally:
    if fout!=None:
        fout.close()
        print("File closed")
       ''' 
#writing and reading in the same file with the help of 'with' statement
l=0
try:
    with open("d:/filehandling1.txt","w+") as fin:
        msg=input("Enter the string")
        fin.write(msg)
        fin.seek(0)
        print(fin.read())
except FileNotFoundError:
    print("file not found")


'''
#Reading data from the file
fout=None
try:
    fout=open("d:/filehandling1.txt","r")
    m=fout.read()
    print(m)
    l=fout.readline()
    print(l)
    s=fout.readlines()
    print(s)
except FileNotFoundError as ex1:
    print("the file doesnt exist",ex1)
except OSError as ex2:
    print("Cannot read the data in the file",ex2)
finally:
    if fout!=None:
        fout.close()
        print("File closed")


#Writng the multiple lines till user dont hit enetr on new line and print number of lines
fout=None
try:
    fout=open("d:/filehandling1.txt","w")
    print('Type your message and to stop hit enter')
    l=0
    while True:
        str=input()
        if len(str)==0:
            break
        fout.write(str+"\n")
        l+=1
    print("Total line =",l)
except FileNotFoundError as ex1:
    print("the file doesnt exist",ex1)
except OSError as ex2:
    print("Cannot read the data in the file",ex2)
finally:
    if fout!=None:
        fout.close()
        print("File closed")



#Checking the uppercase lowercase and digit in the file
fout=None
try:
    fout=open("d:/filehandling1.txt","r")
    m=fout.read()
    up=lo=d=sp=0
    print(m)
    for i in m:
        if i.isupper():
            up+=1
        elif i.islower():
            lo+=1
        elif i.isdigit():
            d+=1
        else:
            sp+=1
    print(up,lo,d,sp)
    l=fout.readline()
    print(l)
    s=fout.readlines()
    print(s)
except FileNotFoundError as ex1:
    print("the file doesnt exist",ex1)
except OSError as ex2:
    print("Cannot read the data in the file",ex2)
finally:
    if fout!=None:
        fout.close()
        print("File closed") 


#Reading the multiple lines and print the number of lines
fout=None
lines=0
try:
    fout=open("d:/filehandling1.txt","r")
    while True:
        text=fout.readline()
        if text=="":
            break
        lines+=1
        print(text,end="")
    print("Total line =",lines)
except FileNotFoundError as ex1:
    print("the file doesnt exist",ex1)
except OSError as ex2:
    print("Cannot read the data in the file",ex2)
finally:
    if fout!=None:
        fout.close()
        print("File closed")


#Reading and writing in a single code
fout=None
try:
    fout=open("d:/filehandling1.txt","w+")
    print('Type your message and to stop hit enter')
    l=0
    while True:
        str=input()
        if len(str)==0:
            break
        fout.write(str+"\n")
        l+=1
    print("Total line saved in the file =",l)
    print("Press any key to read the file")
    input()
    l=0
    fout.seek(0,1)
    while True:
        text=fout.readline()
        if text=="":
            break
        l+=1
        print(text,end="")
    print("Total line after reading the file=",l)
except FileNotFoundError as ex1:
    print("the file doesnt exist",ex1)
except OSError as ex2:
    print("Cannot read the data in the file",ex2)
finally:
    if fout!=None:
        fout.close()
        print("File closed")


'''






