import time

def readcsv(filename, linenumber):
    import csv
    data = list(csv.reader(open(filename + ".csv")))
    return data   

def schoolpo8finder(data,name):
    info = []
    for i in range(0, len(data)):
        try:
            if (str(name)).lower() in (str(data[i][4])).lower():
                info.append(data[i][4])
                info.append(data[i][60])

                
        except:
            print("")

    try:
        for i in range(0, len(info)):
            if i % 2 == 0:
                try:
                    e = float(info[i])
                    print(print(info[i+1] + ": progress 8 score is " + info[i]))
                except:
                    print(info[i] + ": progress 8 score is " + info[i+1])
            
    except:
        print("")

        
def listfl(data):
    array = []
    import sys
    for i in range(1,len(data)-1):
        try:
            if float(data[i][60]) < float(100):
                array.append(float(data[i][60])) 
        except:
            array.append(float(0))
    return array

def listnames(data):
    array = []
    for i in range(0,len(data)):
        try:
            array.append(str(data[i][4]))
        except:
            array.append("null")
    return array


def combind(array, names):
    newarray = []
    for i in range(0, len(names)):
        try:
            hold = [names[i],array[i]]
            newarray.append(hold)
        except:
            print("")
    return newarray

    
def schoolranker(data):
    swaps = True
    array = listfl(data)
    names = listnames(data)
    newranking = combind(array, names)
    j = 0
    while swaps == True:
        swaps = False
        j += 1
        for i in range(0, len(array)-1):
            if newranking[i][1] < newranking[i+1][1]:
                hold = newranking[i]
                newranking[i] = newranking[i+1]
                newranking[i+1] = hold
                swaps  = True
    return newranking

def output(data, slient):
    print("\n\n\n\n")
    listrank = schoolranker(data)
    rank = open("rank.txt","w")
    if slient == 1:
        for i in range(0, len(listrank)):
            print(str(i+1) + ". " + str(listrank[i][0]) + " with average progress 8 score of " + str(listrank[i][1]))
            rank.write(str(i+1) + ". " + str(listrank[i][0]) + " with average progress 8 score of " + str(listrank[i][1]))
            rank.write("\n")
    else:
        for i in range(0, len(listrank)):
            rank.write(str(i+1) + ". " + str(listrank[i][0]) + " with average progress 8 score of " + str(listrank[i][1]))
            rank.write("\n")
    rank.close()

def readingrank(find):
    file = open("rank.txt","r")
    try:
        for i in range(0, 10000):
            hold = file.readline()
            if find.lower() in str(hold).lower():
                print(hold)
        file.close()
    except:
        file.close()


        
print("starting up")
filename = input("filename without csv? ")
data = readcsv(filename, 5680)
print("data loaded")
print("\n")
while True:
    print("\n")
    choice = input("would you like to do?\n1.generate rank text file\n2.search for progress 8 average\n3.search for ranking number by school\n > ")
    if choice == "1":
        print("making rank table")
        output(data, 1)
        print("done")
    elif choice == "2":
        schoolname = input("what is the name of the school? ")
        print("\n\n")
        print("here is what is found in csv:")
        schoolpo8finder(data, schoolname)
        
    elif choice == "3":
        find = input("name of school? ")
        try:
            print("here is what's been found? ")
            readingrank(find)
        except:
            print("please wait..")
            output(data, 0)
            print("here is what's been found? ")
            readingrank(find)




    
