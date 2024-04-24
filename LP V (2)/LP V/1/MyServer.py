# 1. Implement multi-threaded client/server Process communication
# using RMI.

# pip install pyro4
# sepeeate terminal python -m Pyro4.naming
# run server 
# run clinet

# pyro4-ns  ---> tarminal command to run sever 
# 1st run this command on seperate terminal python -m Pyro4.naming
# and seperate terminal server and similaryly clinet file

import Pyro4

@Pyro4.expose
class MyRemoteClass(object):
    def addition(self, x, y):
        return x + y

    def mult(self, x, y):
        return x * y

def main():
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(MyRemoteClass)
    ns.register("MyRemoteClass", uri)
    print("Server is ready.")
    daemon.requestLoop()

if __name__ == "__main__":
    main()
