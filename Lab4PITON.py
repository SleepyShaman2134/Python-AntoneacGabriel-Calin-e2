from genericpath import isfile
import os 
import sys
print("1).")
def readFiles(director):
    if(not os.path.isdir(director)):
        return False
    print(os.listdir(director))

readFiles("C:\Games\Python")

print("2).")
def aisAll(director, fisier="fisier.txt.txt"):
    if(not os.path.isdir(director)):
        return False
    listfiles=os.listdir(director)
    listA=[]
    for a in listfiles:
        if a[0]=='A':
            listA.append(a)
    #print(listA)
    file= open(os.path.abspath(fisier), "wt+")
    for a in listA:
        file.write(os.path.abspath(a))
        file.write("\n")
aisAll("C:\Games\Python")

print("3).")
def my_path(my_path):
    print(my_path)
    if os.path.isfile(os.path.abspath(my_path)):
        file=open(my_path, "r").read()
        counter=20
        listchar=[]
        index=0
        while counter>0:
            listchar.append(file[index])
            index+=1
            counter-=1
        return listchar
    if os.path.isdir(os.path.abspath(my_path)):
        listfiles=os.listdir(my_path)
        listexts=[]
        for b in listfiles:
            file=os.path.splitext(b)
            listexts.append(file[1])
        listext=[]
        listuple=[]
        print(listfiles)
        for a in listexts:
            if not a in listext and a!='':
                counter=sum(a in s for s in listfiles)
                listext.append(a)
                listuple.append(tuple((a, counter)))
        sorted_by_counter = sorted(listuple, key=lambda tup: tup[1], reverse=True)
        return sorted_by_counter

print(my_path("C:\Games\Python"))

print("4).")
def checkForUniExt():
    n = sys.argv
    director=n[1]
    listdir=os.listdir(director)
    listvis=[]
    for a in range(len(listdir)):
        ok=0
        exta=os.path.splitext(listdir[a])
        #print(exta)
        for b in range(len(listdir)):
            if listdir[a]!=listdir[b]:
                extb=os.path.splitext(listdir[b])
                if exta[1]==extb[1]:
                    ok=1
        if ok==0:
            listvis.append(listdir[a])
    return listvis
#print(checkForUniExt())


listfinal=[]
print("5).")
def searchIt(target, to_search):
    try:
        if os.path.isfile(os.path.abspath(target)):
            file=open(target, "r").read()
            ext=os.path.splitext(target)
            print(file.find(to_search), target, ext[1])
            if file.find(to_search)!=-1 and ext[1]!="":
                listfinal.append(target)
        if os.path.isdir(os.path.abspath(target)):
            listfiles=os.listdir(target)
            for a in listfiles:
                searchIt(a, to_search)
            return listfinal
        raise ValueError
    except ValueError:
        print("target is not a file or a director")
        return -1
print(searchIt("Cefwfw", "salut"))

print("6).")
def callBack():
    return -1
def sevenAgain(target, to_search, errorfound):
    try:
        if os.path.isfile(os.path.abspath(target)):
            file=open(target, "r").read()
            ext=os.path.splitext(target)
            print(file.find(to_search), target, ext[1])
            if file.find(to_search)!=-1 and ext[1]!="":
                listfinal.append(target)
        if os.path.isdir(os.path.abspath(target)):
            listfiles=os.listdir(target)
            for a in listfiles:
                searchIt(a, to_search)
            return listfinal
        raise ValueError
    except ValueError:
        errorfound()
print(searchIt("Cefwfw", "salut"), callBack())

print("7).")
def checkDetails(file):
    dictionar=dict()
    if os.path.isfile(os.path.abspath(file)):
        dictionar.setdefault("Full_path", os.path.abspath(file))
        dictionar.setdefault("File_size", os.path.getsize(file))
        ext=os.path.splitext(file)
        dictionar.setdefault("File_extension", ext[1])
        if  open(file, "r").readable() and open(file, "w").writable():
            dictionar.setdefault("File_can_rw", True)
        else:
            dictionar.setdefault("File_can_rw", False)
        print(dictionar)
       
checkDetails("C:\Games\Python\Atest.txt")

print("8)")
def checkFileAbsolete(director):
    listabso=[]
    try:
        listdir=os.listdir(director)
        #print(listdir)
        for a in listdir:
            if os.path.isfile(os.path.abspath(a)):
                listabso.append(os.path.abspath(a))
        print(listabso)
    except:
        print("SOMETHING WENT WRONG")
checkFileAbsolete("C:\Games\Python")