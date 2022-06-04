# first run python -m Pyro5.nameserver in a seperate console window (we need a nameserver)
import Pyro5.api
import NumIntPar

@Pyro5.api.expose
class PiCalculation(object):
    def calculatePi(self,steps):
        numThreads=4
        piObject=NumIntPar.calcPiInThreads() #create an instance of the class calcPiInThreads
        pi=piObject.calcPi(steps,numThreads)  #invoke method for parallel computation of pi
        return pi

daemon=Pyro5.api.Daemon()   #make a Pyro daemon
ns=Pyro5.api.locate_ns()    #find the name server
uri=daemon.register(PiCalculation)   #register the PiCalculation class as a pyro object
ns.register("pi.calculation",uri)      #register the object with a name in the name server

print("Ready")
daemon.requestLoop()  #start the event loop of the server to wait for calls






