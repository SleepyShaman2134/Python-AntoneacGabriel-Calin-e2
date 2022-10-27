print("1). UNION, INTERSECTION, DIFFERENCE")
def operations(a, b):
    return a+b, [value for value in a if value in b], [value for value in a if value not in b], [value for value in b if value not in a]
print(operations([2, 4, 5, 'test'], ['salut', 2, 3, 20]))
print("2). NUMBER OF LETTERS")
def countLetters(a):
    if(type(a)!=str):
        return "FALSE"
    b=dict()
    for i in range(len(a)):
        counter=0
        if a[i] not in b:
            b.setdefault(a[i], 0)
            for j in range(i, len(a)):
                if a[i].lower()==a[j]:
                    counter+=1
            b.update({a[i] : counter})
    print(b.items())

countLetters("Ana has apples.")

print("3). COMPARE 2 DICTIONARIES")
def comparedict(a, b):
    if len(a)!=len(b):
        print("Not equal")
    else:
        flag=0
        for i in a:
            if a.get(i)!=b.get(i):
                flag=1
                break
    if flag==0:
        print("True")
    else:
        print("False")
comparedict({"name": "Gabriel", "age": 21}, {"name":"Gabrie", "age": 21})

print("4). BUILD XML")
def XML(tag, content, **elements):
    if type(tag)!=str and type(content)!=str:
        return "False"
    s="<"+tag+" "
    for i in elements:
        s+=f'{i} = \"{elements.get(i)}\"'
    s+=">"+content+" </"+ tag+ ">"
    print(s)
XML("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ")

print("5). VALIDATION RULES")
def validaterules(tuples, dictionary):
    if(type(dictionary)!=dict):
        return "False"
    if type(tuples)!=set:
        return "False"
    for i in dictionary:
        ok=0
        for j in tuples:
            if j[0]==i: 
                first=j[1]
                middle=j[2]
                end=j[3]
                if dictionary[i].find(first) or first!="":
                    ok=1
                    first=dictionary[i].find(first)
                if dictionary[i].find(middle) or middle!="":
                    ok=1
                    middle=dictionary[i].find(middle)
                if dictionary[i].find(end) or end!="":
                    ok=1
                    end=dictionary[i].find(end)
                if first==-1:
                    return False
                if middle==-1:
                    return False
                if end==-1:
                    return False
                if type(first)==int and type(middle)==int and type(end)==int:
                    if first>middle and first>end and middle>end:
                        return False
                if type(first)==int and type(middle)==int:
                    if first>middle:
                        return False
                if type(middle)==int and type(end)==int:
                    if middle>end:
                        return False
                if type(first)==int and type(end)==int:
                    if first>end:
                        return False
        if ok==0:
            return False
    return True


print(validaterules({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}, {"key1": "come inside, it's too cold out", "key2": "start middle winter"}))

print("6). UNIQUE AND UNUNIQUE")
def order(list1):
    tuples=()
    o=[]
    c=0
    b=0
    i=0
    for i in range(len(list1)):
        if list1.count(list1[i])>1:
            o.append(list1[i])
    
    o= list(dict.fromkeys(o))
    for i in o:
        c+=1
    for i in list1:
        if list1.count(i)==1:
            b+=1
    tuples=tuple((b, c))
    print(tuples)

order([1, 2, 1, 3, 4, 5, 2, 3])

print("7). sets made into dictionary")
def setsToDictionary(*sets):
    dictionar=dict()
    for a in range(len(sets)):
        if(type(sets[a])!=set):
            return False
    for a in range(len(sets)):
        print(sets[a])
        for b in range(a+1, len(sets)):
            print(sets[a].union(sets[b]))
            dictionar.setdefault("{} | {}".format(sets[a],sets[b]), sets[a].union(sets[b]))
            dictionar.setdefault("{} & {}".format(sets[a],sets[b]), sets[a].intersection(sets[b]))
            dictionar.setdefault("{} - {}".format(sets[a],sets[b]), sets[a].difference(sets[b]))
            dictionar.setdefault("{} - {}".format(sets[b],sets[a]), sets[b].difference(sets[a]))
    print(dictionar.keys())
setsToDictionary({1,2}, {2, 3})

print("8). SNAKEY")
def startToEnd(mapping):
    if(type(mapping)!=dict):
        print("PING")
        return False
    ok=0
    head="start"
    i=0
    listrep=[]
    while ok==0:
        listrep.append(head)
        if head in mapping:
            head=mapping[head]
            if head in listrep:
                ok=1
                print(listrep)

startToEnd({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'})

print("9). VARIABLE EVERYWHERE")
def variable(*values, **kvalues):
    counter=0
    for a in values:
        if a in kvalues.values():
            counter+=1
    print(counter)

variable(1, 2, 3, 4, x=1, y=2, z=3, w=5)

