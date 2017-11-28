import random

def machtv3(a,n):
    """ Calculate a ^ n
        Parameters
        ----------
        a : Int
          Int with base value
        n : Int
          Int the power for a

        Return
        ------
        m : Int
          returns the result
    """
    assert n > 0
    m = 1

    while n > 0:
        if n % 2 == 0:
            n = n / 2
            a = a * a
        else:
            m = m * a
            n -= 1

    return m

print (machtv3(2,64))

class myStack(list):
    def push(self, el):
        self.append(el)

    def pop(self):
        assert not self.isEmpty(), "Stack is empty"
        del self[-1]

    def peek(self):
        print (self)

    def isEmpty(self):
        return self == []

# print ("\nOpdracht 2: ")
# stack = myStack()
# # stack.pop()
# print ("Stack is empty: ", stack.isEmpty())
# stack.push(1)
# print ("Stack push 1: ", stack)
# stack.push(2)
# print ("Stack push 2: ", stack)
# stack.push(3)
# print ("Stack push 3: ", stack)
#
# print ("Stack is empty: ", stack.isEmpty())
# stack.pop()
# print ("Pop: ", stack)
#
# print ("\nOpdracht 3")

def checkString(s):
    """ stack machine with symbols
    Parameters
    ----------
    s : String
      String with symbols

    Return
    ------
    none
      print stack after each step
    """

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


def myBin(n):
    """Converts a number to an string with the binary represantation of the give number

    ----------
    n : Int
      A number that will be converted to bin

    Return
    ------
    - : String
      returns a string with binary representation
    """

    if n == 0:
        return ''
    else:
        return myBin(n // 2) + str(n % 2)

print ("\nOpdracht 4: ", "0b" + myBin(11))


count = 0
print ("\nOpdracht 5: ")
def swap(a,i,j):
    a[i],a[j] = a[j],a[i]
def qsort(a,low=0,high=-1):
    global count
    if high == -1:
        high = len(a) -1
    if low < high:
        swap(a,low, min(a))
        m = low
        for j in range(low+1,high+1):
            count += 1
            if a[j] < a[low]:
                m += 1
                swap(a,m,j)
        swap(a,low,m)
        if m > 0:
            qsort(a,low,m-1)
        qsort(a,m+1,high)

qlist = list (range(100))
qsort(qlist)
print(count)
