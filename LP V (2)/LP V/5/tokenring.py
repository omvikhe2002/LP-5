# 5. Implement token ring based mutual exclusion algorithm.


class TokenRing:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.token = 0

    def send_data(self, sender, receiver, data):
        print("Token passing:", end="")
        for i in range(self.token, sender):
            print(f" {i % self.num_nodes}->", end="")
        print(f" {sender}")
        print(f"Sender {sender} sending data: {data}")

        for i in range(sender + 1, receiver):
            print(f"Data {data} forwarded by {i}")

        print(f"Receiver {receiver} received data: {data}\n")
        self.token = sender

if __name__ == "__main__":
    num_nodes = int(input("Enter the number of nodes: "))
    token_ring = TokenRing(num_nodes)

    while True:
        sender = int(input("Enter sender: "))
        receiver = int(input("Enter receiver: "))
        data = input("Enter data: ")

        token_ring.send_data(sender, receiver, data)

        send_again = input("Do you want to send again? (yes/no): ")
        if send_again.lower() != "yes":
            break




'''lelts break down the Python code:

TokenRing Class:

This class represents a token ring network.
It has an __init__ method that initializes the number of nodes in the ring and sets the initial token position to 0.
It has a send_data method that simulates sending data from a sender to a receiver in the token ring network.

Main Part:

It prompts the user to enter the number of nodes in the token ring network.
It creates an instance of the TokenRing class based on the user's input.
It enters a loop to repeatedly ask the user for sender, receiver, and data to be transmitted.
After each transmission, it asks the user if they want to send again. If the user responds with "yes", the loop continues; otherwise, the program exits.

Sending Data:

When sending data, the send_data method prints the progress of the token passing from the sender to the receiver.
It also prints messages indicating the transmission of data from the sender to the receiver and any nodes in between forwarding the data.
Overall, the code simulates the token passing and data transmission in a token ring network based on user input. It's a simplified version that demonstrates the basic concept without relying on external libraries.'''