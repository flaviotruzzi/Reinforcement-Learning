from stupidAgent import *
from Simulator import *

s = Simulator(1000, ngroups=3, ncampaigns=2)
s.setAgent(stupidAgent)
s.simulate()
