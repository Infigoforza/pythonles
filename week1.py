import re
import random

# Opdracht 1
def myMax(xs):
"""
Return the highest number of a list
Parameters
----------
xs : list
  list of ints and/or doubles


Return
------
- : Int or Float
 Returns the highest Int/FLoat
"""
    assert len(xs) > 0, 'list is empty!'

    highest = xs[0]

    for i in xs:
        assert type(i) == int or type(i) == float

        if i > highest:
            highest = it

    return highest

ys = [-1,-2,-3]
print ("\nOpdracht 1: ", myMax(ys))
print (ys)


# Opdracht 2
def getNumbers(xs):
"""
Return the digits in the string
Parameters
----------
xs : string

Return
------
- : list of ints
Just a print of the result, list of all digits in the given string.
"""
    return re.findall('\d+', xs)

print  ("\nOpdracht 2: ", getNumbers('een123zin45 6met-632meerdere+7777getallen'))

# Opdracht 3
def eratoshenes():
"""
print of all the correct prime numbers up to 1000
Parameters
----------
none

Return
------
xs : list of ints
returns list with the prime numbers
"""
    xs =  [i for i in range(2,1001)]
    for i in xs:
        x = i
        for j in range(1001):
            x += i
            if x <= 1000 and x in xs:
                xs.remove(x)
    return xs

print ("\nOpdracht 3: ", eratoshenes());


# opdracht 4
def birthDayChecker():
"""
Parameters
----------
none

Return
------
- : int
 return amount of lists with duplicated numbers
"""
    dups = list (map(hasDups, generateYears()))
    getOnlyDups = list (filter(lambda b : b == True, dups))

    return (len (getOnlyDups))

def generateYears():
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
    allYears = []
    for i in range(100):
        year = [random.randint(1,366) for x in range(23)]
        allYears.append(year)
    return allYears

def hasDups(xs):
"""
Checks if a list has duplicated items
----------
none

Return
----------
- : boolean
returns True if list contains duplicated item else False.
"""
    seen = set()
    for day in xs:
        if day in seen:
            return True
        else:
            seen.add(day)
    return False

print ("\nOpdracht 4: ", birthDayChecker())
