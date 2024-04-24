# 6. Implement Bully and Ring algorithm for leader election.


class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.is_coordinator = False

    def initiate_election(self, nodes):
        for node in nodes:
            if node.id > self.id:
                print(f"Node {self.id} sends election message to Node {node.id}")
                node.start_election(nodes)
        self.is_coordinator = True
        print(f"Node {self.id} becomes the coordinator.")

    def start_election(self, nodes):
        for node in nodes:
            if node.id > self.id:
                print(f"Node {self.id} sends election message to Node {node.id}")
                node.start_election(nodes)
        self.is_coordinator = True
        print(f"Node {self.id} becomes the coordinator.")

if __name__ == "__main__":
    # Create nodes
    nodes = [Node(i) for i in range(1, 6)]

    # Simulate Bully Algorithm
    print("Bully Algorithm:")
    # Node with highest ID starts the election
    nodes[-1].initiate_election(nodes)

    # Simulate Ring Algorithm
    print("\nRing Algorithm:")
    # Node with lowest ID starts the election
    nodes[0].start_election(nodes)



'''let break down the Python code for leader election using the Bully and Ring algorithms:

Node Class:

The Node class represents a node in the distributed system.
Each node has an ID and a boolean flag (is_coordinator) indicating whether it is the coordinator or not.
It has methods initiate_election and start_election to initiate and start the election process, respectively.
initiate_election Method:

This method is called when a node decides to initiate an election.
It iterates through all nodes with higher IDs and sends election messages to them by calling their start_election method.
After sending messages, it sets its own is_coordinator flag to True and declares itself as the coordinator.
start_election Method:

This method is called when a node receives an election message.
Similar to initiate_election, it iterates through all nodes with higher IDs and sends election messages to them by calling their start_election method.
After sending messages, it sets its own is_coordinator flag to True and declares itself as the coordinator.
Main Part:

It creates a list of nodes, each with an ID from 1 to 5.
It simulates the Bully algorithm by initiating the election process from the node with the highest ID (nodes[-1]).
It simulates the Ring algorithm by initiating the election process from the node with the lowest ID (nodes[0]).
Output:

The code prints out messages indicating the progress of the election process, including which node sends an election message to which other node, and which node becomes the coordinator.'''