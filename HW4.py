"""Homework Assignment #4: Lists
In this assignment we practice working with Lists, in combination with defining our own functions."""

myUniqueList = []
myLeftovers  = []

def AddToList(a):
    if a not in myUniqueList:
        myUniqueList.append(a)
        return True, myUniqueList
    else:
        myLeftovers.append(a)
        return False, myLeftovers
  
print(AddToList(10))