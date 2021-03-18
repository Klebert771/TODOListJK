#coding:utf-8
import myClassData as data
import messageAfficher as message
import datetime
import pickle


def CreateToDoList():
    message.CreationListToDoList()
    toDoListObject = data.ToDoList()
    toDoListObject.nomToDo = input("Entrez un titre à votre tâche")
    toDoListObject.nomToDo = str(toDoListObject.nomToDo)
    toDoListObject.libelleToDo = input("Entrez un Libellez à votre tâche")
    toDoListObject.libelleToDo = str(toDoListObject.libelleToDo)
    toDoListObject.dateCreate = datetime.date.today()
    toDoListObject.dateRunHeure =  GetDateToDoList()
    message.AcceptSave()
    SaveToDoList(toDoListObject)

def SaveToDoList(*ToDoList):
    with open("C:\\toDoListData.txt", "a") as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(ToDoList)

def UpdateToDOList():
    pass

def DeleteTodoList():
    pass

def PrintToDoList():
    pass

def SearchToDoList():
    pass

def GetDateToDoList():
    A = input("Entrez l'année : ")
    A = int(A)
    M = input("Entrez le mois : ")
    M = int(M)
    d = input("Entrez le mois : ")
    d = int(d)
    DateJour = str(A,"-",M,"-",d)
    return DateJour