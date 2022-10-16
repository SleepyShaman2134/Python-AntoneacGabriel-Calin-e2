from operator import le

print("1). FIBBONACI")
def Fibonacci(n):
    x1=1
    x2=1
    list=[x1, x2]
    index=2
    counter=0
    while(counter<=n):
        temp=x1+x2
        x1=x2
        x2=temp
        list.append(x2)
        counter=counter+1
    print(list)

Fibonacci(7)
print("2). PRIME NUMBERS")
def primeNumbers(list):
    length=len(list)
    listg=[]
    for a in range(length):
        counter=0
        for i in range(2, int(list[a]/2)):
            if(list[a]%i==0):
                counter+=1
        if(counter==0):
            listg.append(list[a])
    print(listg)


primeNumbers([25, 3, 10, 980, 2])
print("3). OPERATORS")
def operators(lista, listb):
    lengtha=len(lista)
    lengthb=len(listb)
    listunion=list(set(lista+listb))
    listinterstect=[value for value in lista if value in listb]
    listab=[value for value in lista if value not in listb]
    listba=[value for value in listb if value not in lista]
    print( listunion)
    print(listinterstect)
    print(listab)
    print(listba)

operators([1, 4, 5], [1, 2, 3, 6])
print("4). COMPOSE")
def compose(listn, listm, point):
    lengthm=len(listm)
    lengthn=len(listn)
    listc=[]
    index=point
    listc.append(listn[point])
    for a in range(0, lengthm):
        print(lengthn)
        if(index+listm[a]<=lengthn):
            listc.append(listn[index+listm[a]])
            index+=listm[a]
        else:
            listc.append(listn[index+listm[a]-lengthn])
            index+=listm[a]
    print(listc)

compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)

print("5). DIAGONAL")
def diagonal(matrix):
    lengthw=len(matrix[0])
    for a in range(lengthw):
        matrix[a][a]=0
    print(matrix)
diagonal([[1, 2, 4, 5],[1, 3, 3, 4], [1, 2, 3, 4], [1, 2, 4, 5]])

print("6). COINCIDENCE")
def coincidence(coincidence, *list_of_lists):
    finalList=[]
    semiList=[]
    counter=0
    unionlist=[]
    for a in list_of_lists:
        lengthlist=len(a)
        for b in range(lengthlist):
            unionlist+=a[b]
    lengthunion=len(unionlist)
    visited=[]
    for a in range(lengthunion):
        lengthvisit=len(visited)
        counter=0
        countervalid=0
        if(lengthvisit==0):
            visited.append(unionlist[a])
            lengthvisit=len(visited)
            for c in range(lengthvisit-1, lengthunion):
                if(visited[a]==unionlist[c]):
                    counter+=1
            if(counter==coincidence):
                semiList.append(unionlist[a])
        for b in range(lengthvisit):
            if(unionlist[a]!=visited[b]):
                countervalid+=1
        if(countervalid==lengthvisit):
            visited.append(unionlist[a])
            lengthvisit=len(visited)
            for c in range(a, lengthunion):
                if(visited[lengthvisit-1]==unionlist[c]):
                    counter+=1
            if(counter==coincidence):
                semiList.append(unionlist[a])
    finalList=[]
    finalcoincidence=[]
    temporaryList=[]
    lengthSemi=len(semiList)
    for a in range(lengthSemi):
        for b in list_of_lists:
            temporaryList=[]
            finalcoincidence=[]
            lengthlist=len(b)
            for c in range(lengthlist):
                lengthc=len(b[c])
                for d in range(lengthc):
                    if(semiList[a]==b[c][d]):
                        temporaryList.append(c+1)
                        finalcoincidence.append(semiList[a])
            finalList.append(temporaryList)
            finalList.append(finalcoincidence)
    for a in range(0,len(finalList), 2):
        print(str(finalList[a+1][0]) + " has classes " + str(finalList[a]))
        
   

coincidence(2, ([1,2,3], [2,3,4],[4,5,6], [4,1, "test"]))

print("7). ALL PALINDROM")
def palindrom(list):
    nmpalindrom=0
    maxpalindrom=[]
    maxim=0
    for a in list:
        if(type(a)!=type(int)):
            print("NOT INT")
            return 
    for a in list:
        maxtemp=0
        temp=a
        rev=0
        while temp>0:
            dig=temp%10
            maxtemp+=1
            rev=rev*10+dig
            temp=temp//10
        if(a==rev):
            nmpalindrom+=1
            if(maxtemp>maxim):
                maxpalindrom=a
    print(tuple((nmpalindrom, maxpalindrom)))

palindrom([121, 142, 31, 11, 11211])

print("8). ASCII LISTS")
def ascii(liststr, x=1, flag=True):
    print(flag)
    list_of_lists=[]
    list=[]
    for a in liststr:
        if(not isinstance(a, str)):
            print("NOT STR")
            return
    for a in liststr:
        lengthstr=len(a)
        list=[]
        for b in range(lengthstr):
            if(flag==True):
                if ord(a[b])%x==0:
                    list+=a[b]
            else:
                print(ord(a[b]))
                if(ord(a[b])%x!=0):
                    list.append(a[b])
        list_of_lists.append(list)
    print(list_of_lists)

ascii(["test", "hello", "lab002"], 2, False)

print("9). CAN'T SEE")
def spectators(matrix):
    n=0
    listtpl=[]
    if(not all(isinstance(ele, list) for ele in matrix)):
        print("NOT MATRIX")
        return
    for a in matrix:
        n+=1
    
    lengthcolumn=len(a)
    print(lengthcolumn)
    for b in range(0, lengthcolumn):
        for x in range(0, n):
            if(x!=0):
                if(matrix[x][b]<matrix[x-1][b]):
                   #print(matrix[x][b], matrix[x-1][b])
                    listtpl.append(tuple([x, b]))
    print(listtpl)



spectators([[1, 2, 3, 2, 1, 1],

[2, 4, 4, 3, 7, 2],

[5, 5, 2, 5, 6, 4],

[6, 6, 7, 6, 7, 5]] )


print("10). B TO A MATRIX TUPLE")
def tupling(*list_of_lists):
    n=0
    list1=[]
    listfinal=[]
    maxim=0
    for a in list_of_lists:
        n+=1
        if(maxim<len(list_of_lists)):
            maxim=len(list_of_lists)
    for a in list_of_lists:
        if maxim!=len(a):
            while(len(a)<maxim):
                a.append(None)
    for a in range(0, len(list_of_lists)):
        list1=[]
        for b in range(0, n):
            list1.append(list_of_lists[b][a])
        listfinal.append(tuple(list1))
    print(listfinal)

tupling([1,2,3], [5, 6, 7], ["a", "b", "c"])

print("11). THE LAST IS THE ONE")
def last(listp):
    listp.sort(key=lambda a:a[1][2])
    print(listp)
last([('abc', 'bcd'), ('abc', 'zza')])

print("12). H A I S A C A N T A M")
def sing(liststr):
    finallist=[]
    c=len(liststr)
    for a in range(c-1):
        #print(liststr[a])
        for b in range(a+1, c):
            newlist=[]
            if liststr[a][-2:]==liststr[b][-2:]:
                newlist.append(liststr[a])
                newlist.append(liststr[b])
                finallist.append(newlist)
                break
    for a in range(len(liststr)):
        ok=0
        for b in finallist:
            for c in range(len(b)):
                if(liststr[a]==b[c]):
                    ok=1
        if(ok!=1):
            finallist.append(liststr[a])
    print(finallist)

sing(['ana', 'banana', 'carte', 'arme', 'parte', 'lupta'])
