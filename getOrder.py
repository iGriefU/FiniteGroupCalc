from tabulate import tabulate ## darstellung als tabelle


import sys

def howTo():
    print("""How to use:\n 
    python getOrder.py [(ma] [groupSize] [number]

    - This calculates the order of number in Z[10]([ma],[groupSize])

    Example: python getOrder.py m1 9 4
    // This calculates the order of 4 in multiplicative group 9 without 0

    Example: python getOrder.py a 14
    // This prints a table with all orders of every number of Z(14,+)

    IF you omit 'number' a table with all number gets printed.
    """)

def mathFalse():
    print("Your number has to be a valid element of your group!")
##error prevention
if len(sys.argv)<3:
    print("\n\t\t!!!!   You forgot an argument   !!!\n")
    howTo()
    exit()

## vars def
op = sys.argv[1]
try:
    groupSize = int(sys.argv[2])
except:
    print("\n\t\t!!!!   You forgot an argument   !!!\n")
    howTo()
    exit()
num=0
try:
    num = int(sys.argv[3])
except:
    pass

# m or a check
if num:
    if op=="m" or op=="M":
        if(groupSize>num): # e.g. getOrder.py m 7 7 is invalid 'cause 7 isnt in Z*(7,*)
            counter=1
            mul=num
            if(num==1):
                print(f"ord({sys.argv[3]}) is: " + str(counter) )
            else:
                while(True):
                        prev=num
                        num= num*mul % groupSize
                        counter+=1
                        print(f"{prev} * {mul} = {num} mod {groupSize}")
                        if(num==1):
                            print(f"ord({sys.argv[3]}) is: " + str(counter) )
                            break
        else:
            mathFalse()
            
    if op=="a" or op=="A":
        if(groupSize>=num): ## e.g. getOrder.py a 6 9 is invalid 'cause 9 isnt in Z(6,+)
            counter=1
            add=num
            if(num==0):
                print(f"ord({sys.argv[3]}) is: " + str(counter) )
            else:
                while(True):
                    num = (num+add) % groupSize
                    counter+=1
                    if(num==0):
                        print(f"ord({sys.argv[3]}) is: " + str(counter) )
                        break
        else:
            mathFalse()
############################################# TABLE PART
else:
    if op=="m" or op=="M":
        data=[]
        for n in range(1,groupSize):
            counter=1
            mul=n
            num=n
            if(num==1):
                data.append([n,1])
            else:
                while(True):
                        prev=num
                        num= num*mul % groupSize
                        counter+=1
                        print(f"{prev} * {mul} = {num} mod {groupSize}")
                        if(num==1):
                            data.append([n,counter])
                            break
            print("#########")
        print(tabulate(data,headers=["a","ord(a)"]))           
            
    if op=="a" or op=="A":
        data=[]
        for n in range(groupSize):
            counter=1
            add=n
            num=n
            if(num==0):
                data.append([n,1])
            else:
                while(True):
                    prev=num
                    num = (num+add) % groupSize
                    counter+=1
                    print(f"{prev} + {add} = {num} mod {groupSize}")
                    if(num==0):
                        data.append([n,counter])
                        break
            print("#########")
        print(tabulate(data,headers=["a","ord(a)"]))
