import re
import random

# Opdracht 1

"""
description
Parameters
----------
xs : list
  list of ints and/or doubles


Return
------
none
 Just a print
"""

def myMax(xs):
    highest = 0
    if len(xs) == 0:
        raise Exception("List is empty")
    for i in xs:
        if i > highest and type(i) == int or type(i) == float:
            highest = i
        elif type(i) != int and type(i) != float:
            raise Exception("List contains other types than float or int")
    print ("\nOpdracht 1: ", highest)


ys1 = [1,2,3,4,8,12,8,19,33,88,12]
#ys2 = [1,2,3,4,8,'a']
#ys3 = []

myMax(ys1)
#myMax(ys2)
#myMax(ys3)


"""
description
Parameters
----------
xs : string

Return
------
none
Just a print of the result, list of all digits in the given string.
"""
# Opdracht 2
def getNumbers(xs):
    print  ("\nOpdracht 2: ", re.findall('\d+', xs))

getNumbers('een123zin45 6met-632meerdere+7777getallen')


"""
description
Parameters
----------
none

Return
------
none
print of all the correct prime numbers up to 1000
"""
# Opdracht 3
def eratoshenes():
    xs =  [i for i in range(2,1001)]
    for i in xs:
        x = i
        for j in range(1001):
            x += i
            if x <= 1000 and x in xs:
                xs.remove(x)
    print ("\nOpdracht 3: ", xs)

eratoshenes();


"""
description
Parameters
----------
none

Return
------
none
print of the amount of lists with duplicated numbers in it
"""
# opdracht 4
def birthDayChecker():
    dups = list (map(hasDups, generateYears()))
    getOnlyDups = list (filter(lambda b : b == True, dups))

    print ("\nOpdracht 4: ", (len (getOnlyDups)))


"""
Generate 100 lists, which represent a year and contains 23 random numbers from 1 to 365
Parameters
----------
none

Return
----------
allYears: list of lists with ints
list of lists with all years
"""
def generateYears():
    allYears = []
    for i in range(100):
        year = [random.randint(1,366) for x in range(23)]
        allYears.append(year)
    return allYears

"""
Checks if a list has duplicated items
----------
none

Return
----------
- : boolean
returns True if list contains duplicated item else False.
"""
def hasDups(xs):
    seen = set()
    for day in xs:
        if day in seen:
            return True
        else:
            seen.add(day)
    return False

birthDayChecker()
