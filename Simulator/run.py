from stupidAgent import *
from Simulator import *
from pylab import *

s = Simulator(1000, ngroups=5, ncampaigns=13)
s.setAgent(stupidAgent)
s.simulate()

plot((0,999),(s.campaigns.values()[0].budget,s.campaigns.values()[0].budget), '--', label="Budget Campanha 1")
plot((0,999),(s.campaigns.values()[1].budget,s.campaigns.values()[1].budget), '--', label="Budget Campanha 2")
plot((0,999),(s.campaigns.values()[2].budget,s.campaigns.values()[2].budget), '--', label="Budget Campanha 3")


plot(s.campaign0, label="Campanha 1")
plot(s.campaign1, label="Campanha 1")
plot(s.campaign2, label="Campanha 2")

legend(loc='lower right')


figure(2)

plot(s.groups.values()[0].impressions, label="Group 1 Impressions")
plot(s.groups.values()[1].impressions, label="Group 2 Impressions")
plot(s.groups.values()[2].impressions, label="Group 3 Impressions")


ion()
show()
