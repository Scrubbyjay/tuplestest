def TupleTest(tupleArr, n) :
    #initialising variables
    tupLen = len(tupleArr)
    good = 0
    i = 0

    #checking numbers  
    while (i + 2 < tupLen) :
        count = 0
        if (tupleArr[i] == tupleArr[i + 1]) :
            count += 1
        if (tupleArr[i] == tupleArr[i + 2]) :
            count += 1
        if (tupleArr[i + 1] == tupleArr[i + 2]) :
            count += 1
        if (count == 1) :
            good += 1
        i += 1
    return (good)
    
    
#test case
if __name__=="__main__":
    tupleArr = [1,2,7,8,7,2]
    #one good set 787

    #tupleArr = [1,1,1,2,1]
     #112, 121 two good sets

    n = len(tupleArr)
    print(TupleTest(tupleArr, n))
