import Pyro5.api
from utils import processInput

steps=processInput()

request_pi=Pyro5.api.Proxy("PYRONAME:pi.calculation")  #use name server object uri shortcut

print(request_pi.calculatePi(steps))     #print result

