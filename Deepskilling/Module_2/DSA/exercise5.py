class Node:

    def __init__(self, task):
        self.task = task
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add_task(self, task):

        new_node = Node(task)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    def display(self):

        temp = self.head

        while temp:
            print(temp.task)
            temp = temp.next


tasks = LinkedList()

tasks.add_task("Design UI")
tasks.add_task("Write Code")
tasks.add_task("Testing")

tasks.display()