import re

def extractwords(string1):
    print("1).")
    if type(string1)==str:
        nr=string1.count(" ")
        r=re.findall("[\w^,]+", string1)
        return r

print(extractwords("Salut sunt Calin 1231"))

def long_length_substr(regex, string1, x):
    print("2).")
    if type(regex)==str and type(string1)==str and type(x)==int:
        r=re.findall(regex, string1)
        list1=[]
        for a in r:
            if len(a)==x:
                list1.append(a)
    return list1
print(long_length_substr("[\w^,]+", "Salut sunt Calin 1231", 4))

def list_of_regex(string1, listregex):
    print("3).")
    if type(string1)==list and type(listregex)==list:
        list1=[]
        for a in string1:
            ok=0
            for b in listregex:
                if re.match(b, a):
                    ok=1
            if ok==1:
                list1.append(a)
    return list1
print(list_of_regex(["Salut sunt Calin 1231", "d", "", "da", "213"], ["[\w^,]+", "\w"]))

def xml_attributes(xmlpath, attributes):
    print("4).")
    listattributes=[]
    with open(xmlpath,"r") as file:
        for x in re.findall("<\w+.*?>",file.read()):
            for att in attributes.items():
                if all([re.search(att[0]+"\s*=\s*\""+att[1] + "\"", x,flags=re.I)]):
                    listattributes.append(x)
    return listattributes
print(xml_attributes("C:\Games\Python\\text.xml", {"size description":"Small"}))

def xml_attributes2(xmlpath, attributes):
    print("5).")
    listattributes=[]
    with open(xmlpath,"r") as file:
        for x in re.findall("<\w+.*?>",file.read()):
            for att in attributes.items():
                if any([re.search(att[0]+"\s*=\s*\""+att[1] + "\"", x,flags=re.I)]):
                    listattributes.append(x)
    return listattributes
print(xml_attributes2("C:\Games\Python\\text.xml", {"size description":"Small"}))

def censoring(word):
    print("6).")
    if word[0] not in "aeiouAEIOU" and word[len(word)-1] not in "aeiouAEIOU":
        return word
    else:
        changeword=""
        for i in range(0,len(word)):
            if i%2==0:
                changeword+=word[i]
            else:
                changeword+='*'
        return changeword
print(censoring("ALELUIA"))

def substitute(stringCNP):
    print("7).")
    sum=0
    verify=[2,7,9,1,4,6,3,5,8,2,7,9]
    for a in range(len(stringCNP)-1):
        sum+=int(stringCNP[a])*verify[a]
    sum=sum%11
    if(int(stringCNP[len(stringCNP)-1])==sum):
        return re.match("^[1-9]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[0-2]|99)(00[1-9]|0[1-9]\d|[1-9]\d\d)\d$",stringCNP) != None
    else:
        return "INVALID"
# ^[1-9]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[0-2]|99)(00[1-9]|0[1-9]\d|[1-9]\d\d)\d$
print(substitute("1980429330246"))

