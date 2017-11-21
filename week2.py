import random

def machtv3(a,n):
    assert n > 0

    m = 1
    while n > 0:
        if n % 2 == 0:
            n = n // 2
            m = a * 2
        else:
            n -= 1
            m =  m * 2
    print("Opdracht1: ", m)

machtv3(2,10)

class myStack(list):
    def push(self, el):
        self.append(el)

    def pop(self):
        if not self.isEmpty():
            del self[-1]
        else:
            raise Exception("Stack is empty!")
    def peek(self):
        print (self)
    def isEmpty(self):
        return self == []

print ("\nOpdracht 2: ")
stack = myStack()
# stack.pop()
print ("Stack is empty: ", stack.isEmpty())
stack.push(1)
print ("Stack push 1: ", stack)
stack.push(2)
print ("Stack push 2: ", stack)
stack.push(3)
print ("Stack push 3: ", stack)

print ("Stack is empty: ", stack.isEmpty())
stack.pop()
print ("Pop: ", stack)

print ("\nOpdracht 3")


"""
description
Parameters
----------
s : String
  String with symbols

Return
------
none
  print stack after each step
"""
def checkString(s):
    stringStack = myStack()
    for c in s:
        if c == '<' or c == '(' or c == '[':
            stringStack.push(c)
        elif c == '>' or c == ')' or c == ']':
            last = stringStack[-1]
            if c == '>' and last == '<':
                stringStack.pop()
            elif c == ')' and last == '(':
                stringStack.pop()
            elif c == ']' and last == '[':
                stringStack.pop()
            else:
                raise Exception("Incorrect element in string!")
        else:
            raise Exception("Incorrect string")
        print (stringStack)
checkString("([[<([])>]])")
#checkString("((<<]))")

"""
description
Parameters
----------
n : Int
  A number that will be converted to bin

Return
------
- : String
  returns a string with binary representation
"""
def myBin(n):
    if n == 0:
        return ''
    else:
        return myBin(n // 2) + str(n % 2)

print ("\nOpdracht 4: ", "0b" + myBin(11))


print ("\nOpdracht 5: ")
def swap(a,i,j):
    a[i],a[j] = a[j],a[i]

def qsort(a,low=0,high=-1):
    if high == -1:
        high = len(a) -1
    if low < high:
        swap(a,low, random.randint(low,high))
        m = low
    for j in range(low+1,high+1):
        if a[j] < a[low]:
            m += 1
            swap(a,m,j)
                # low < i <= m : a[i] < a[low]
                # i > m : a[i] >= a[low]
            swap(a,low,m)
                # low <= i < m : a[i] < a[m]
                # i > m : a[i] >= a[m]
        if m > 0:
            qsort(a,low,m-1)
            qsort(a,m+1,high)
    print (a)

qlist = [5,4,3,2,1]
qsort(qlist, 1, 4)
