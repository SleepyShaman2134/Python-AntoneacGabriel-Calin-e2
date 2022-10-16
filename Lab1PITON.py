from re import sub
import re
print("1). FIRST OF THE FIRST")
def function()  :
    x=[int(x) for x in input("Enter int values: ").split()]
    y=0
    m=0
    maxim=0
    length=len(x)
    maxnumber=max(x)
    print(int(maxnumber/2))
    for d in range(1, int(maxnumber/2)):
        m=0
        for i in range(length):
            if(x[i]%d==0):
                m=m+1
            if m==length:
                y=d
        if(y!=1):
            print(y)


print("2). COUNT AND COUNT")
def vowel_count(str):
    count = 0
    vowel = set("aeiouAEIOU")
    for alphabet in str:
      
        if alphabet in vowel:
            count = count + 1
    print("No. of vowels :", count)

vowel_count("salut")

print("3). I AM GONNA FIND IT")
def substring(substring, string):
    nr=0
    c=len(substring)
    print(c)
    for a in range(0, len(string), c):
        if string[a:a+c]==substring:
            nr+=1
    print(nr)

substring("aba", "abaabaabaabadasdfa")
print("4). SHRINK SNAKE")
def lowercamelcase(string):
     converted = re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower() 
     print (converted)

lowercamelcase("CamilaCuDouaCocoase")

print("5). POLYMERIZATION")
def spiralFusion(matrix):
    counter=0
    for a in range(0, len(matrix)//2):
        for b in range(0+ counter, len(matrix)-a):
            print(str(matrix[a][b]), end='')
        for b in range(1+ counter ,len(matrix)-a):
            print(str(matrix[b][len(matrix)-counter-1]), end='')
        for b in range(1 + counter,len(matrix)-a):
            print(str(matrix[len(matrix)-counter-1][len(matrix)-b-1]), end='')
        for b in range(1 + counter, len(matrix)-a-1):
            print(str(matrix[len(matrix)-b-1][a]), end='')
        counter+=1
    print()
spiralFusion(["firs", "n_lt", "oba_", "htyp"])

print("6). LOOK FOR TWIN")
def validatePalindrom(number):
    temp=number
    rev=0
    while temp>0:
        div=temp%10
        rev=rev*10+div
        temp//=10
    if(number==rev):
        print("True")
    else:
        print("False")

validatePalindrom(121)

print("7). EXTRACT TRUE SELF")
def extractNumber(string):
    number=0
    ok=0
    for a in range(len(string)):
        if(string[a].isdigit()):
            number=number*10 + int(string[a])
            ok=1
        if(ok==1 and (not string[a].isdigit())):
            break
    print(number)
extractNumber("asd123asd123")

print("8). NUMBER THE GOOD")
def binary(number):
    counter=0
    binarynumber=format(number, 'b')
    for a in range(len(binarynumber)):
        if(int(binarynumber[a])==1):
            counter+=1
    print(counter)
binary(24)
print("9). WHO IS THE BIGGEST")
def commonCharacter(string):
    maxim=0
    maximw=' '
    for a in range(len(string)):
        count=0
        for b in range(a, len(string)):
            if string[a].lower()==string[b].lower() and string[a]!=" ":
                count+=1
        if(maxim<count):
            maxim=count
            maximw=string[a]
    print(str(maxim)+ " " + str(maximw))

commonCharacter("An apple is not a tomato")

print("10). ARE YOU REAL")
def text(string):
    counter=0
    for a in range(len(string)):
        if(string[0]==" "):
            print("THIS IS NOT A TEXT!")
            break
        if(string[len(string)-1]==" "):
            print("THIS IS NOT A TEXT!")
            break
        if(string[a-1]==string[a]):
            print("THIS IS NOT A TEXT!")
            counter=0
            break
        if(string[a]==" " or string[a]==string[len(string)-1]):
            counter+=1
    print(counter)
text("I have Python exam")