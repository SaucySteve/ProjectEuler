def euler1(totalNumber):
    totalNumber-=1
    listOfFives=list()
    listOfThrees=euler1_3s(totalNumber)
    listOfFives=euler1_5s(totalNumber,listOfThrees,listOfFives)
    total=0
    for i in listOfThrees:
        total+=i
    for x in listOfFives:
        total+=x
    print(total)
    

def euler1_3s(totalNumber):
    newNumber=totalNumber
    listOfThrees=list()
    while(newNumber>=3):
        if(newNumber%3==0):
            listOfThrees.append(newNumber)
            newNumber-=3
        elif(newNumber%3!=0):
            newNumber-=1
    return listOfThrees
def euler1_5s(totalNumber,listOfThrees,listOfFives):
    newNumber=totalNumber
    while(newNumber>=5):
        if(newNumber%5==0):
            if(newNumber) not in listOfThrees:
                listOfFives.append(newNumber)
            newNumber-=5
        elif(newNumber%5!=0):
            newNumber-=1
    return listOfFives
            
        
