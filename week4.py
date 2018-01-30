
import random
import math

#Opdrach 1
print("Opdracht 1\n\n")
class HashEntry:
    def __init__(self, element):
        self.element = set()
        self.element.add(element)

class ChainingHashing:
    def __init__(self, length):
        self.length = length
        self.hashTable = [None] * self.length
        self.used = 0

    def __repr__(self):
        s = "HashTable: \n"
        for i in range(self.length):
            if self.hashTable[i] != None:
                s += "Entry : "+ str(i) + str(self.hashTable[i].element) + "\n"
        s += "Length : " + str(self.length) + "\n"
        s += "Used : " + str(self.used) + "\n"
        return s

    def getPos(self,e):
        return hash(e) % self.length

    # hash element and insert in table
    def insert(self,e):
        key = self.getPos(e)
        if self.hashTable[key] == None:
            Entry = HashEntry(e);
            self.hashTable[key] = Entry
            self.used += 1
            return True

        elif(self.hashTable[key]):
            if e not in self.hashTable[key].element:
                self.hashTable[key].element.add(e)
                self.used += 1
            else:
                return False

        if self.used > (0.75 * self.length):
            self.rehash()
        return True

    def search(self,e):
        key = self.getPos(e)
        if self.hashTable[key] != None:
            for element in self.hashTable[key].element:
                if element == e:
                    return True
        else:
            return False

    # Delete element, return true when deleted, false if e is not deleted
    def delete(self, e):
        key = self.getPos(e)
        if self.search(e):
           print("DELETING ", e, "\n")
           self.hashTable[key].element.remove(e)
           self.used -= 1
        else:
            return False

    # maak tabel 2 keer zo groot
    def rehash(self):
        oldTable = self.hashTable
        oldLength = self.length
        newLength = oldLength * 2
        self.reset(newLength)

        for i in range(oldLength):
            if oldTable[i] is not None:
                for element in oldTable[i].element:
                    self.insert(element)

        print(self)

    def reset(self, newLength):
        self.length = newLength
        self.used = 0
        self.hashTable = [None] * newLength

hashTable = ChainingHashing(10)
randomBrokenNumbers = [random.uniform(1, 1000) for i in range(200)]
for i in randomBrokenNumbers:
    hashTable.insert(i)

print("All element inserted HashTable \n", hashTable)

for i in range(100):
    hashTable.delete(randomBrokenNumbers[i])

print("Final HashTable \n", hashTable)

#Opdracht 2
print("Opdracht 2\n\n")

hashDic = {}
sameHash = 0
theHash = None
randomBrokenNumbers2 = [random.uniform(0, 1) for i in range(10000)]
for i in randomBrokenNumbers2:
    if i not in hashDic.keys():
        nHash = hash(i) % (2**32)
        if nHash in hashDic.values():
            sameHash = i
            theHash = nHash
        hashDic[i] = nHash

for key, value in hashDic.items():
    if(value == theHash):
        print("hash(",sameHash, ") % (2**32) == hash(", key,") % (2**32) == ", value)


#Opdracht 3
print("Opdracht 3 \n\n")
def B(n, k):
    rij = [0 for n in range(k+1)]
    oldrij = [0 for n in range(k+1)]
    rij[0] = 1
    x = 1
    for j in range(n + 1):
        oldrij = rij[:]
        for i in range(x):
            rij[i] = oldrij[i] + oldrij[i-1]
        rij[0] = 1
        if x < k+1:
            x += 1
    return rij[k]

print("B(100,50) = ", B(100,50))

#Opdracht 4
print("Opdracht 4 \n\n")
def F(n):
    m=[1,2,5,10,20,50,100,200,500,1000,2000,5000,10000]
    invert = -1

    n+=1

    while invert*-1 < len(m):
        if n >= m[invert]:
            break
        del m[-1]

    A = [[0 for y in range (n)]for x in range(len(m))]
    for i in range(len(m)):
        for j in range(n):
            if j >= m[i]:
                A[i][j] = A[i-1][j] + A[i][j-m[i]]
            if j < m[i]:
                A[i][j] = A[i-1][j]
            if j == 0 or i == 0:
                A[i][j]=1
    return A[len(m)-1][n-1]

print(F(7))
print(F(10000))
