import time
response = input("Please enter your code (0 to 999999) : ")

if((response >= 999999) or (response <= 0)):
    response = input("Please enter your code (0 to 999999 only !) : ")
else:
    codeFromMin = 0
    codeFromMax = 999999

    # Code research from 0 to response
    found = False

    start = time.time()

    while found == False:
        
        if(response != codeFromMin):
            codeFromMin += 1
        else:
            found = True
            end = time.time()
            print "Time from 0 to code :", round(end - start,2), "sec"


    # Code research from 999999 to response
    found = False

    start = time.time()

    while found == False:
        
        if(response != codeFromMax):
            codeFromMax -= 1
        else:
            found = True
            end = time.time()
            print "Time from 999999 to code :", round(end - start,2), "sec"