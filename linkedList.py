class linkedNode():

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


# Creating nodes 
node1 = linkedNode(3)
node2 = linkedNode(4)
node3 = linkedNode(4)
node4 = linkedNode(4)

# Linking nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None


def hasCycle(startingNode: linkedNode) -> bool:
    slow, fast = startingNode, startingNode

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True
    return False
