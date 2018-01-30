from collections import deque
from itertools import permutations
import string

# Oprdacht 1
print("\n\nOpdracht 3 ")

def check(a,i): # ga na of i aan a toegevoegd kan worden
     n = len(a)
     return not (i in a or
     # niet in dezelfde kolom
     i+n in [a[j]+j for j in range(n)] or
     # niet op dezelfde diagonaal
     i-n in [a[j]-j for j in range(n)])
     # niet op dezelfde diagonaal

def printQueens(a):
     n = len(a)
     for i in range(n):
         for j in range(n):
             if a[i] == j:
                 print("X",end= " ")
             else:
                 print("*",end= " ")
         print("\n")

def rsearch(N):
    global a
    for i in range(N):
     if check(a,i):
         a.append(i)
         if len(a) == N and a not in b:
             b.append(a)
             a = []
             return True # geschikte a gevonden
         else:
             if rsearch(N):
                 rsearch(N)
                 return True
         del a[-1] # verwijder laatste element
    return False
a = [] # a geeft voor iedere rij de kolompositie aan
b = []
t = 0

rsearch(6)
# print(a)
#printQueens(a)
print(b)


# Opdracht 2
print("\n\nOpdracht 2 ")
class ListNode:
    def __init__(self,data,next_node):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return str(self.data)

class MyCircularList:
    def __init__(self):
        self.tail = None

    def __repr__(self):
        s = ''
        current = self.tail.next
        if current:
            s = s + str(current)
            current = current.next
        while current != self.tail.next:
            s = s + " -> " + str(current)
            current = current.next
        if not s: # s == '':
            s = 'empty list'
        return s

    def append(self,e):
        if not self.tail: # self.head == None:
            self.tail = ListNode(e,None)
            self.tail.next = self.tail
        else:
            n = ListNode(e, self.tail.next)
            self.tail.next = n
            self.tail = n


    def delete(self, e):
       if self.tail:
            if self.tail.data == e:
                if self.tail.next == self.tail:
                    self.tail = None # prints empty list
                else:
                    current = self.tail

                    while current.next != self.tail:
                        current = current.next

                    current.next = current.next.next
                    self.tail = current

            elif self.tail.next != self.tail:
                current = self.tail

                while current.next.data != e and current.next != self.tail:
                    current = current.next
                if current.next.data == e:
                    current.next = current.next.next

    def showLevelOrder(self, queue = deque()):
            for layer in self.root.showLevelOrder():
                print(' '.join([str(l) for l in layer]))


mylist = MyCircularList()
mylist.append(1)
print(mylist)
mylist.append(2)
print(mylist)
mylist.append(3)
print(mylist)
mylist.append(4)
print(mylist)
mylist.delete(4)
print(mylist)


# Opdracht 3
print("\n\nOpdracht 3 ")
class BSTNode:
    def __init__(self,element,left,right):
        self.element = element
        self.left = left
        self.right = right

    def __repr__(self,nspaces=0):
        s1 = ''
        s2 = ''
        s3 = ''
        if self.right != None:
            s1 = self.right.__repr__(nspaces + 3)
        s2 = s2 + ' '*nspaces + str(self.element) + '\n'
        if self.left != None:
            s3 = self.left.__repr__(nspaces + 3)
        return s1 + s2 + s3

    def insert(self,e):
        parent = self
        current = None
        found = False

        if parent.element < e:
            current = parent.right
        elif parent.element > e:
            current = parent.left
        else:
            found = True;

        while not found and current:
            parent = current
            if parent.element < e:
                current = parent.right
            elif parent.element > e:
                current = parent.left
            else:
                found = True

        if not found:
            if parent.element < e:
                parent.right = BSTNode(e,None,None)
            else:
                parent.left = BSTNode(e,None,None)
        return not found

    def insertArray(self,a, low=0, high=-1):
        if len(a) == 0:
            return
        if high == -1:
            high = len(a)-1
        mid = (low+high+1)//2
        self.insert(a[mid])
        if mid > low:
            self.insertArray(a,low,mid-1)
        if high > mid:
            self.insertArray(a,mid + 1,high)

    def search(self,e):
        current = self
        found = False
        while not found and current:
            if current.element < e:
                current = current.right
            elif current.element > e:
                current = current.left
            else:
                found = True
        if found:
            return current
        else:
            return None

    def search2(self,e):
        if self.element == e:
            return self
        parent = self.getParent(e)
        if parent == None:
            return None
        if parent.element < e:
            return parent.right
        return parent.left

    def getParent(self,e):
        parent = self
        current = None
        found = False

        if parent.element < e:
            current = parent.right
        elif parent.element > e:
            current = parent.left;
        else:
            return None

        while not found and current:
            if current.element == e:
                found = True
            else:
                parent = current
                if current.element < e:
                    current = current.right
                else:
                    current = current.left
        if found:
            return parent
        else:
            return None

    def parentMinRightTree(self):
        parent = self.right
        current = parent.left
        while current.left:
            parent = current
            current = current.left
        return parent

    def delete(self,e):
        parent = self.getParent(e);

        if parent == None:
            return False
        if parent.element < e:
            current = parent.right
            if current.left == None:
                parent.right = parent.right.right
                return True
            else:
                if current.right == None:
                    parent.right = parent.right.left
                    return True
        else:
            current = parent.left
            if current.left == None:
                parent.left = parent.left.right
                return True
            else:
                if current.right == None:
                    parent.left = parent.left.left
                    return True
        if current.right.left == None:
            current.element = current.right.element
            current.right = current.right.right
            return True
        node = current.parentMinRightTree()
        current.element = node.left.element
        node.left = node.left.right
        return True

    def max(self):
        if self.right:
            return self.right
        else:
            return self.element

    def showLevelOrder(self):
        q = deque()
        q.append(self)
        def iterator(layerSize):
            for i in range(layerSize):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                yield node.element
        while (q):
            yield iterator(len(q))

class BST:
    def __init__(self,a=None):
        if a:
            mid = len(a)//2
            self.root = BSTNode(a[mid],None,None)
            self.root.insertArray(a[:mid])
            self.root.insertArray(a[mid+1:])
        else:
            self.root = None

    def __repr__(self):
        if self.root:
            return str(self.root)
        else:
            return 'null-tree'

    def search(self,e):
        if self.root and e:
            return self.root.search(e)
        else:
            return None

    def insert(self,e):
        if e:
            if self.root:
                return self.root.insert(e)
            else:
                self.root = BSTNode(e,None,None)
                return True
        else:
            return False

    def delete(self,e):
        if self.root and e:
            if self.root.element == e:
                if self.root.left == None:
                    self.root = self.root.right
                elif self.root.right == None:
                    self.root = self.root.left
                elif self.root.right.left == None:
                    self.root.element = self.root.right.element
                    self.root.right = self.root.right.right
                else:
                    node = self.root.parentMinRightTree();
                    self.root.element = node.left.element
                    node.left = node.left.right
                return True
            else:
                return self.root.delete(e)
        else:
            return False

    def max(self):
        if self.root:
            if self.root.right is not None:
                return self.root.right.max()
            else:
                return self.root.element
        else:
            return "Empty Tree"

    def rsearch(self, e):
        return self.find(self.root, e)

    def find(self, currentNode, e):
        if currentNode is None:
            return False
        elif currentNode.element == e:
            return currentNode;
        elif e < currentNode.element:
            return self.find(currentNode.left, e)
        else:
            return self.find(currentNode.right, e)

    def rinsert(self, e):
        if self.root == None:
            self.root = BSTNode(e,None,None)
        else:
            return self._rinsert(self.root, e)

    def _rinsert(self, currentNode, e):
        if currentNode.element > e:
            if currentNode.left:
                self._rinsert(currentNode.left,e)
            else:
                currentNode.left = BSTNode(e,None,None)
        elif currentNode.element <= e:
            if currentNode.right:
                self._rinsert(currentNode.right,e)
                return True;
            else:
                currentNode.right = BSTNode(e,None,None)

    def showLevelOrder(self):
        for layer in self.root.showLevelOrder():
            print(' '.join([str(l) for l in layer]))


b = BST()
b.rinsert(1)
print(b)
b.rinsert(2)
print(b)
b.rinsert(3)
print(b)
b.rinsert(4)
print(b)
b.delete(4)
print(b)

print("Max = ", b.max())
print(b.rsearch(3))
print('----------------')

b = BST()
b.insert(4)
b.insert(2)
b.insert(1)
b.insert(3)
b.insert(6)
b.insert(5)
b.insert(7)

print(b)
b.showLevelOrder()

#Opdracht 4
print("Opdracht 4")

from itertools import permutations
from itertools import combinations
from collections import deque
import string
import operator

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def filterText(txt):
    return [word.strip(string.punctuation).lower() for word in txt.split() if not hasNumbers(word)]

def readFile(path):
    f = open(path, "r")
    data = f.read()
    f.close()
    return data

def writeFile(path, data):
    f = open(path,"r+")
    for key, value in data.items():
        f.write(key + " :: " + str(value) + "\n")
    f.close()

def analyzeWithDict(text):
    words = filterText(text)
    dic = {}
    for word in words:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    return dic

class Word:
    def __init__(self):
        self.count = 1
        self.branch = {}
        self.terminate = False

    def __repr__(self):
        return str(self.branch) + ":" + str(self.count) + "\n"

    def writeWords(self, string, f):
        for i in self.branch:
            s = string + str(i)
            value = str(self.branch[i].count)

            if self.branch[i].terminate:
                line = s + " :: " + str(value) + "\n"
                f.write(line)

            self.branch[i].writeWords(s, f)


class Trie:
	def __init__(self, file_name = None):
		self.root = Word()

	def __repr__(self):
		return str(self.root)

	def insert(self, string):
         if self.root:
             current = self.root
             for index, letter in enumerate(string):
                 if letter in current.branch:
                     current = current.branch[letter]
                     current.count += 1
                 else:
                     current.branch.update({ letter: Word() })
                     current = current.branch[letter]
                 if (index + 1) == len(string):
                     current.terminate = True
         else:
             return

	def writeWords(self, f):
		self.root.writeWords("", f)

trie = Trie()

def analyzeWTrie(text):
    words = filterText(text)
    for word in words:
        trie.insert(word)

# input source file
data = (readFile("kingjamesbible.txt"))

analyzedDictionary = analyzeWithDict(data)
writeFile("outputDict.txt", analyzedDictionary)

analyzeWTrie(data)

# write the trie to a file
f = open("outputTrie.txt", "w")
trie.writeWords(f)
f.close()


def compareFiles(dictPath, triePath):
    dic = toDictionary(dictPath)
    trie = toDictionary(triePath)

    print('dictonary length: ', len(dic))
    print('trie length: ', len(trie))

    shared_items = set(dic.items()) & set(trie.items())
    differences = { k : dic[k] for k in set(dic) - set(trie) }

    print('differences', differences)
    print('shared items', len(shared_items))
    print('are equel', dic == trie)

def toDictionary(path):
    dic = { }
    with open(path) as f:
        for line in f:
            key = line.split('::')[0].strip(string.whitespace)
            key = key.lower()
            value = line.split('::')[1].strip(string.whitespace)
            dic[key] = value
    return dic

compareFiles("outputDict.txt", "outputTrie.txt")


# wordcount = {}
# fileSource = "kingjamesbible.txt"
# wordcount = readFileIntoDic(fileSource)
# print(wordcount)
# writeDicTofile(wordcount)

trie = Trie()
word = "aapje"
trie.insert("aap")
