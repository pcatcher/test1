counter = 0

string1 = input("Please type few brackets:")

for i in string1:
    if (i==')'):
        counter = counter - 1
        if (counter < 0 ):
            print('error1')
            exit()
    else: 
        counter = counter + 1

if (counter!=0): print('error2')
else: print('okay')

change1 = 1
change2 = 2
