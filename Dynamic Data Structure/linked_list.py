# Creating the Node class contains two parameters Data|Next
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        
# Creating the Linked list
class LinkedList:

    # Starting with the head pointing to None
    def __init__(self):
        self.head = None
    
    # Push function that takes new data as parameter
    def push(self, new_data):

        # Creat an Object (Node) from the Data passed
        new_data = Node(new_data)

        # Head points to the Node while the Node's next takes Head's old value
        new_data.next = self.head
        self.head = new_data
    
    # Print function
    def printList(self):

        # Temp variable takes head's Value and prints the vlaue, Looping in pointers and printing pointed values
        temp = self.head
        while(temp):
            print(temp.data, end=" | ")
            temp = temp.next

if __name__=='__main__':
    liste = LinkedList()

    liste.push(4)
    liste.push(5)
    liste.push(65)
    liste.push(32)

    liste.printList()
