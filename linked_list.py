class Node:
    '''
    An oblect for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    '''
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return '%s' % self.data
        

class LinkedList:
    '''
    Singly linked list
    '''

    def __init__(self): 
        self.head = None

    def is_Empty(self):
        return self.head == None

    def size(self):
        '''
        Return the number of nodes in the list
        Takes 0(n) time
        '''

        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        
        return count

    def add(self, data):
        '''
        Adds nes node containing data at head of the list 
        '''
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    
    def search(self, key):
        '''
        Search for the first node containing data that matches the key
        '''
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def verify(self, index):
        if index is not None:
            print(index)
        else:
            print('not found')

    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append('[Head: %s]' % current.data)
            elif current.next_node is None:
                nodes.append('[Tail: %s]' % current.data)
            else:
                nodes.append('[%s]' % current.data)

            current = current.next_node
        return '->'.join(nodes)


l = LinkedList()
N = Node(10)
N2 = Node(20)
l.head = N
l.add(N2)
l.add(30)
search = l.search(10)
#print(l)
l.verify(search)

