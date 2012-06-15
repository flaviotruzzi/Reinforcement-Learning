import numpy as np
from Agent import *
from Campaign import *
from Group import * 
from Impression import *
import random

class Simulator:
  """Simulator Class"""

  def __init__(self, period, ngroups=None, ncampaigns=None, groups=None, campaigns=None, pCTR = None):
    """Construtor.
    
    Parameters:
      ngroups: number of groups.
      ncampaigns: number of campaigns
      groups: groups, should be None if ngroup is given.
      campaigns: campaigns, should be None if ncampaigns is given.
      period: period of the simulation.
    """

    self.groups = {}

    if ngroups != None:
      for i in xrange(ngroups):
        group  = Group(np.random.randint(100))
        self.groups[group.ID] = group
    else:
      if type(groups) == list:
        for i in groups:
          self.groups[i.ID] = i
      elif type(groups) == dict:
        self.groups = groups
      else:
        raise Exception("ngroups or groups must be setted.")

    self.campaigns = {}

    if ncampaigns != None:
      for i in xrange(ncampaigns):
        campaign = Campaign(np.random.randint(3000),'CPC',CPC=np.random.rand())
        self.campaigns[campaign.ID] = campaign
    else:
      if type(campaigns) == list:
        for i in campaigns:
          self.campaigns[i.ID] = i 
      elif type(campaigns) == dict:
        self.campaigns = campaigns
      else:
        raise Exception("ncampaigns or campaigns must be setted.")

    self.period = period
    
    self.pCTR = {}

    if pCTR == None:
      for i in self.groups:      
        self.pCTR[i] = {}
        for j in self.campaigns:
          self.pCTR[i][j] = np.random.rand()
    else:
      self.pCTR = pCTR
   

  def setAgent(self, agentClass):
    """Set the class of the agent"""
    self.agent = agentClass(self.campaigns, self.groups)

  def generateEvents(self, impressions):
    """Generate Events of clicks"""
    counter = {}

    for i in self.groups:      
      counter[i] = {}
      for j in self.campaigns:
        counter[i][j] = 0

    for i in impressions:
      counter[i.groupID][impressions[i].ID] += 1
      
    for i in counter.keys():
      for j in counter[i].keys():
        n = counter[i][j]
        if n > 0:
          counter[i][j] = np.random.binomial(n, self.pCTR[i][j]) 
     
    self.clicked =[]
    for group in counter.keys():
      acc = 0
      for value in counter[group].values():
        acc += value
      impressionsToUpdate = random.sample(impressions.keys(),acc)
      self.setClick(impressionsToUpdate)
      for i in impressionsToUpdate:
        self.clicked.append(i)
      

  def setClick(self, impressions):
    for i in impressions:
      i.click = True


  def simulate(self):
    if hasattr(self, 'agent') != True:
      raise Exception("Agent Class should be setted.")

    self.campaign0 = []
    self.campaign1 = []

    for t in xrange(self.period): # Para cada tempo i em tau
      print "Time: " + repr(t)
      impressions = []

      for i in self.groups:
        impressions.append(self.groups[i].generateImpressions(t))

      if len(impressions) > 0:
        allocated = self.agent.allocate(impressions)
        self.generateEvents(allocated)    
        self.agent.updateState(self.clicked)
     
      self.campaign0.append(self.campaigns.values()[0].spentBudget)
      self.campaign1.append(self.campaigns.values()[1].spentBudget)

#      for i in allocated:
#        print i

