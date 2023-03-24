class Node:
    def __init__(self, coeff=0, exp=0):
        self.coeff = coeff
        self.exp = exp
        self.next = None
        self.prev = None
        
class Polynomial:
    def __init__(self):
        self.head = None
        
    def insert(self, coeff, exp):
        node = Node(coeff, exp)
        if self.head is None:
            self.head = node #1
        else:
            current = self.head #1
            while current.next is not None:
                current = current.next #2
            current.next = node #3
            node.prev = current #4
            
    def simplify(self):
        current = self.head
        while current is not None:
            exp = current.exp #1
            temp = current.next #2
            while temp is not None:
                if temp.exp == exp:
                    current.coeff += temp.coeff #3
                    temp.prev.next = temp.next #4
                    if temp.next is not None:
                        temp.next.prev = temp.prev #5
                temp = temp.next #3
            current = current.next #4
            
    def sort(self):
        if self.head is None:
            return
        current = self.head #1
        while current.next is not None:
            temp = current.next #2
            while temp is not None:
                if current.exp < temp.exp:
                    current.exp, temp.exp = temp.exp, current.exp #3
                    current.coeff, temp.coeff = temp.coeff, current.coeff #4
                temp = temp.next #3
            current = current.next #4
            
    def display(self):
        current = self.head
        while current is not None:
            if current.coeff != 0:
                print(f"{current.coeff}x^{current.exp} ", end="")
            current = current.next
        print("")
        
p = Polynomial()
p.insert(-2, 5)
p.insert(5, 2)
p.insert(7, 3)
p.insert(-8, 4)
p.insert(10, 0)
p.insert(-3, 3)

print("До приведення подібних членів: ")
p.display()

p.simplify()
p.sort()

print("Після приведення подібних членів та сортування: ")
p.display()
