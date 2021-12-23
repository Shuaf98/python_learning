class BinarySearchNode():
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None
    
    def add_child(self, data):
        
        if data == self.data: #Need to check the value: If the value already exists, we don't continue-- we don't want duplicates 
            return

        if data < self.data: #Condition: If new data is less than the parent node
            if self.left: #Check that our left element is not a leaf node
                self.left.add_child(data) #If it self.left has a child, add data as a child to self.left's child.
            else:
                self.left = BinarySearchNode(data) #If the left node is empty though, then it is already a leaf. We designate it as a node, with left and right = None.
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchNode(data)
    

    def in_order_traversal(self): #SORTING ALGORITHM
        elements = []
        #We sort from smallest to largest, so start with left tree
        if self.left:
            elements += self.left.in_order_traversal() #This iterates until we get to the bottom most left node, adds that node, then recursively adds the previous ones to our list.
        
        #Once we are done adding each left node, we have reached the root. Now, we add the root:
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements


    def pre_order_traversal(self): #Node, then left, then right
        elements = []
        elements.append( self.data) #Add current root

        if self.left: #If there are left children, traverse through them (which will start by adding that child, then continue to traverse through t)
            elements += self.left.pre_order_traversal()
        
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self): #(Left, then Right, then node)
        elements = []
        
        if self.left: #If there are left children, traverse through them (which will start by adding that child, then continue to traverse through t)
            elements += self.left.post_order_traversal()
        
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append( self.data) #Add current root

        return elements

def build_tree(elements):
    root = BinarySearchNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root
    

numbers = [6,4,7,4,16,12,8,3]

numbers_tree = build_tree(numbers)
print(numbers_tree.in_order_traversal()) #Numbers tree starts at the root (self). Then, it traverses down to the left.
                                        #Then recursively comes back up to each parent (then adds the parent, then checks each parent's right, as it climbs back up)
print(numbers_tree.pre_order_traversal())
print(numbers_tree.post_order_traversal())