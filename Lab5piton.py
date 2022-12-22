import utils
import Lab2PY
import inspect
print("1). a).")
def process():
    print("CHOOSE A NUMBER")
    inpt=int(input("Enter int value: "))
    if type(inpt)!=int:
        return "FALSE NUMBER"
    print(utils.process_item(inpt))
#process()

print("1). b).")
def processB():
    ok=1
    while(ok):
        inpt=input("Enter int value: ")
        if inpt!="q":
            if not inpt.isdigit():
                print("INPUT IS NOT INTEGER")
            else:
                print(utils.process_item(int(inpt)))
        else:
            ok=0
#processB()

print("2).")
def sumAnon(*values, **valuesk):
    sumi=lambda **x: sum(x.values())
    sumix=0
    for a in valuesk.values():
        sumix+=a
    return sumix, sumi(**valuesk)

print(sumAnon(1, 2, 45, d=1, b=4, e=2))

print("3).")
def checkVowel(x):
    lista=["a", "e", "i","o", "u"]
    splittext=[]
    funcl=[]
    fn=0
    for a in range(len(x)):
        splittext.append(x[a])
    fn=lambda a: a  in "aeiou"
    vowel_list = [char for char in x if char.lower() in "aeiou"]
    vowel_filter=list(filter(lambda x: x in "aeiou", x))
    for a in splittext:
        if fn(a):
            funcl.append(a)
    print(funcl, vowel_list, vowel_filter)
checkVowel("Programming in Python is fun")

print("4).")
def checkForDictionaries(*x, **y):
    listOfDictionaries=[]
    for a in x:
        #print(a)
        ok=0
        if type(a)==dict:
            if len(a.keys())>=2:
                for b in a:
                    #print(b)
                    if(type(b)==str):
                        if len(b)>=3:
                            ok=1
        if ok==1:
            listOfDictionaries.append(a)
    for a in y.values():
        ok=0
        nr=0
        for b in a:
            nr+=1
            if(type(b)==str):
                if len(b)>=3:
                    ok=1
        if nr>=2 and ok==1:
            listOfDictionaries.append(a)
    print(listOfDictionaries)
checkForDictionaries( {1: 2, 3: 4, 5: 6}, 

 {'a': 5, 'b': 7, 'c': 'e'}, 

 {2: 3}, 

 [1, 2, 3],

 {'abc': 4, 'def': 5},

 3764,

 dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},

 test={1: 1, 'test': True})

print("5).")
def checkIntNumbers(x):
    listint=[]
    for a in x:
        if type(a)==dict:
            for b in a.values():
                if type(b) == int or type(a)==float:
                    listint.append(b)
        else:
            if type(a) == int or type(a)==float:
                listint.append(a)
    print(listint)
checkIntNumbers([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0])


print("6).")
def evenOdd(x):
    oddlist=[]
    evenlist=[]
    finallist=[]
    if type(x)!=list:
        return "NOT LIST"
    else:
        for a in x:
            if a%2==0:
                evenlist.append(a)
            else:
                oddlist.append(a)
        if len(oddlist)==len(evenlist):
            for a in range(len(oddlist)):
                finallist.append(tuple((evenlist[a], oddlist[a])))
    return finallist

print(evenOdd([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))

print("7).")
def process2(**y):
    list1=[]
    listfilters=[]
    listfinal=[]
    listfinal1=[]
    ok1=0
    ok2=0
    ok3=0
    list1=Lab2PY.fibonacci(1000)
    for a in y.keys():
        if a=="filters":
            ok1=1
        if a=="offset":
            ok2=1
        if a=="limit":
            ok3=1
    if ok1==1:
        for b in y["filters"]:
            listfilters.append(b)
        nr=len(listfilters)
        for a in list1:
            nr1=0
            for b in listfilters:
                if b(a):
                    nr1+=1
            if nr1==nr:
                listfinal.append(a)
    if ok2==1:
        offset= y["offset"]
        print(listfinal)
        while offset!=0:
            listfinal.pop(offset-1)
            offset-=1
    if ok3==1:
        for a in range(y["limit"]):
            listfinal1.append(listfinal[a])
    print(listfinal1)

def sum_digits(x):

    return sum(map(int, str(x)))

process2(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],

    limit=2,

    offset=2)

def multiply_by_two(x):

    return x * 2

def add_numbers(a, b):

    return a + b


def multiply_by_three(x):

    return x * 3

print("8).")
def print_arguments(function):
    def augmented_function(*args, **kwargs):
        print("The arguments are:", end=" ")
        for a in args:
            print(a, end=' ')
        for a in kwargs:
            print(a, end=' ')
        print("The returned value is", end=" ")
        return function(*args, **kwargs)
    return augmented_function

def multiply_output(function):
    def multiply_by_two_function(*args, **kwargs):
        return 2*function(*args, **kwargs)
    return multiply_by_two_function

def augment_function(function, decorators):
    lists=[]
    values=[]
    for a in decorators:
            lists.append(a)
    def decorate(*args, **kwargs):
        for a in lists:
            values.append(a(function))
        for a in values:
            print(a(*args, **kwargs))
        return  function(*args, **kwargs)
    return decorate
a=print_arguments(add_numbers)
b=print_arguments(multiply_by_two)
x=a(1, 2)
print(x)
y=b(6)
print(y)
augmented_multiply_by_three = multiply_output(multiply_by_three)
x = augmented_multiply_by_three(10)  # this will return 2 * (10 * 3)
print(x)
decorated_function = augment_function(add_numbers, [print_arguments, multiply_output]) 

x = decorated_function(3, 4)  # this will print: Arguments are: (3, 4), {} and will return (2 * (3 + 4))
print(x)

def pairsint(**listint):
    listdict=[]
    for a in listint.values():
        for b in a:
            dicti=dict()
            dicti["sum"]=b[0]+b[1]
            dicti["prod"]=b[0]*b[1]
            dicti["pow"]=b[0]**b[1]
            listdict.append(dicti)
    return listdict
print(pairsint(pairs = [(5, 2), (19, 1), (30, 6), (2, 2)] ))