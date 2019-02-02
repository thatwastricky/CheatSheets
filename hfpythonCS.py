#! /usr/local/bin/python3 

"""
This is a Python "cheat sheet" I made while reading "Head First Python" by Paul Barry.
It contains examples of the language's syntax core concepts.
The examples do NOT cover or follow the entire book's progression, also sometimes more concepts are integrated in one.
Finally, I'm from Italy, so some variables names or strings might be in Italian.

Please consider purchasing the original book, it's great,
-Riccardo Aldera (thatwastricky) 2018/10/19
"""

print("CHAPTER 1---------------------------------------------------------")

#list declaration
lista = ["elem1", "elem2", 3, '4'] #mutable
listaImmutabile = {1,2,3} #immutable or dictionary

#print() BIF (Build In Function) and list element access
print(lista[3])
print(lista[0:2]) #from 0 to 2 (not included)

#some BIF for lists
lista.pop() #remove last element (and return it)
lista.append(4) #append a single element to the list
lista.extend(["elem6",6]) #extend the list with a collection of element
lista.remove("elem6") #remove a single element
lista.insert(4, "elem5") #insert an element at a given position
print(lista)

#get BIF doc
#print(str(help(print)))

#for cycle
print("for -> ",end="")
for iterator in lista :
    print(iterator,end=" ")
print()

#while cycle and for with range()
count = 0
print("while:")
while count < len(lista) :
    for ws in range(count) : #range(n) returns a int list from 0 to n (not included)
        print("->",end="") #the end= parameter specify what is appended to the end of the printed string (by default is newline)
    print(lista[count])
    count = count+1
del count #delete the variable (remove the definition)

#matrix (2D list)
matrice = [[1,2],[3,4]]
for x in range(len(matrice)) :
    for y in range(len(matrice[x])) :
        print(matrice[x][y],end="")
    print()

#if and isinstance()
if not isinstance(lista, list) :
    print("lista is not a list")
elif isinstance(lista, list) :
    print("lista is a " + str(type(lista)))
else :
    print("reached unreachable code")

#function definition with optional arguments initialized with a default value
def printtriangle(size, triangleatom="*") :
    count = 1    
    for r in range(size) :
        for c in range(count) :
            print(triangleatom,end="")
        count = count+1
        print()

printtriangle(4)
printtriangle(4,"+")

print("\nCHAPTER 2---------------------------------------------------------")

#some BIFs for list
print(list(enumerate(lista,1))) #assign an index (starting from the int argument) to each element of a list
print(id(lista)) #return ad unique id for an object
print(id(lista[0])) #the id for the list is different from the id of the first object
iterstr = iter("ab") #convert a string to a iterator
print(next(iterstr)) ; next(iterstr) #iterate in the iterator/string starting from -1, also chain two instruction in one line usign ;
print(next(iterstr, "end")) #the second argument give a default value to next() for when it goes out of bounds

#import single function or all module
from os import getcwd
print("we are working in the directory: " + getcwd()) #with "from...import..." it's like we defined the function in our code, so there is no need to specify the namespace
import os
print("we are still in: " + os.getcwd()) #we are now referring to a function in a different module so we have to specify its namespace

print("\nCHAPTER 3---------------------------------------------------------")

#create test file in the standard way try-except-finally
try :
    test = open("test.txt", "w") #"w" is the mode, and it stands for "write"
    print(">file opened")
    if os.path.exists("test.txt") :
        print(">check for file's path existance passed") #useless since, if it does not exists, open() create a new file with the specified path
    test.write("hello\n")
    test.write("world\n")
    print(">successfully wrote to file")
except :
    print("error in creating the file")
    pass #keyword for "do not do anything else"
finally :
    test.close()

#open and read from file with python "with" syntax
try :
    with open("test.txt","r") as test :
        for line in test :
            print(line,end="")
        test.seek(0) #"rewind" the file readed
        print(test.readline() + "(again)") #alternative way to print a line
except :
    print("error in reading from the file")
    pass

print("\nCHAPTER 4---------------------------------------------------------")

#some BIFs for strings
splittable = "ciao : come : stai"
print("splitting by ':' -> " + str(splittable.split(":"))) #split() return a list so we have to cast it to a str in order to print it
strippable = "     5 ws at the start of this string"
print("stripped string -> " + strippable.strip())

#pickle
import pickle
with open("lista.pickle","wb") as savedata : #the mode is "wb" because it stands for "write as/in binary"
    pickle.dump(lista, savedata)
    print(">saved 'lista' to 'lista.pickle'")
    lista = [0]
    print(">after re-inizialization 'lista' is now: " + str(lista))
with open("lista.pickle","rb") as readdata :
    lista = pickle.load(readdata)
    print(">after reading from 'lista.pickle', 'lista' is now: " + str(lista))

print("\nCHAPTER 5---------------------------------------------------------")

#dealing with data in a list
dati = ["a","c","b"]
dati2 = sorted(dati) #copied sorting
dati = [c.upper() for c in dati] #Python special syntax for declaring lists, called "list comprehension"
dati.sort() #normal sorting
print(dati)
print(dati2)

#sets
listaConDuplicati = [3,3,15,23, "ciao"] #sets, like lists, can contain different types of values 
insieme = set(listaConDuplicati)
print(insieme) #sets can't contain duplicated value

print("\nCHAPTER 6---------------------------------------------------------")

#dict type
dictionary = {"nomi" : "gianni" , "cognomi" : ["rossi","biondi"]}
dictionary["eta"] = str(32)
print(dictionary["nomi"] + "\n" + dictionary["cognomi"][1] + "\n" + dictionary["eta"])
print(dictionary)

#class
class Classe :
    def __init__(self,value=0):
        self.attributo=value
    def getattributo(self):
        return self.attributo
c = Classe("prova")
print(c.getattributo()) #access to attribute of class using method
print(c.attributo) #access to attribute of class using . (BAD PRACTICE, only did that to see if it was possibile)

#extend a class (inheritance)
class NamedList(list) :
    def __init__(self,value="") :
        list.__init__([]) #inizialize the "list part" contained in the new class
        self.nome=value #give the list a name (extended part of the class)
    def tostr(self) :
        return "Nome Lista: " + self.nome + ", contiene: " + str(self) #the new istance is itself a list, but with the extra attribute "name"
n = NamedList("Gianni")
n.extend([1,2,3])
print(n.tostr())

#check methods of a class
print("methods of " + str(type(lista)) + " : " + str(dir(lista)))

print("\nCHAPTER 7---------------------------------------------------------")

#create a web server
"""
from http.server import HTTPServer, CGIHTTPRequestHandler

port = 8080 #specify the port through which communicate with the server
httpd = HTTPServer((“”,port), CGIHTTPRequestHandler) #create a HTTP server
print(“Starting simple_httpd on port: “ + str(httpd.server_port))
httpd.serve_forever() #keep the server active
#put this in the same dir of index.html (home-page)
#to access the newly created web server connect to "http://localhost:8080/"
"""

#access a method value as a property attribute
class Valore :
    def __init__(self, val) :
        self.valore=val
    def getval(self) : #normal get method
        return self.valore
    @property
    def getvalp(self) : #access method as property
        return self.valore
v = Valore(2)
print("as attribute: " + str(v.valore) +
        "\nas returned from method: " + str(v.getval()) +
        "\nas property: " + str(v.getvalp))
        
print("\nCHAPTER 8---------------------------------------------------------")

#json
import json
datiDaSalvare = ["categoria", ["elem1","elem2"], "categoria2",["elem3","elem4"]]
print("the original data: " + str(datiDaSalvare))
transferFile = json.dumps(datiDaSalvare)
print("the stored data: " + str(transferFile)) #the way json store data is text-based hence the ""
recreatedFile = json.loads(transferFile)
print("the loaded data: " + str(recreatedFile))

print("\nCHAPTER 9---------------------------------------------------------")

#use os to interact with the system
import os
os.system("echo ciao") #execute in terminal
print("OS user ID: " + str(os.getuid()))
print("OS process ID: " + str(os.getpid()))
print("OS info (all): " + str(os.uname()))
print("OS info (sysname): " + os.uname()[0])

#DBMS included in python3 (SQLite)
import sqlite3

connection = sqlite3.connect("test.sqlite") #create db
cursor = connection.cursor() #create cursor
cursor.execute("""CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, name TEXT NOT NULL)""") #interact with db
cursor.execute("""DELETE FROM test WHERE name="Piero" """) #delete the former created entry
cursor.execute("""INSERT INTO test (name) VALUES (?)""", ("Piero",)) #SQL code with parameters
connection.commit() #save data
connection.close() #close connection

connection = sqlite3.connect("test.sqlite") #reconnect to db
cursor = connection.cursor() #create cursor
cursor.execute("""SELECT * FROM test """)
print(str(cursor.fetchall()))
connection.commit() #save data
connection.close() #close connection

print("\nCHAPTER 10--------------------------------------------------------")

print("Focused on webapp development with GAE (Google App Engine)")

print("\nCHAPTER 11--------------------------------------------------------")

#get user input (as a str)
testo = input("Insert some textual input: ")
print("you inserted: " + testo)
