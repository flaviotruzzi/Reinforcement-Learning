import numpy as np


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
      group  = Group(np.random.randint(100))
      self.groups[group.id] = group
    else:
      if type(groups) == list:
        for i in groups:
          self.groups[i.id] = i
      elif type(groups) == dict:
        self.groups = groups
   
    self.campaigns = []

    if ncampaigns != None:
      campaign = Campaign(np.random.randint(3000),'CPC',CPC=np.random.rand())
      self.campaigns[campaign.id] = campaign
    else:
      if type(campains) == list:
        for i in campaigns:
          self.campaigns[i.id] = i 
      elif type(campaigns) == dict:
        self.campaigns = campaigns

    self.period = period
    
    self.pCTR = {}

    if pCTR == None:
      for i in self.groups:      
        self.pCTR[i.id] = {}
        for j in self.campaigns:
          self.pCTR[i.id][j.id] = np.random.rand()
    else:
      self.pCTR = pCTR
    

  def setAgent(self, agentClass):
    """Set the class of the agent"""
    self.agent = agentClass(self.campaigns, self.groups)

  def generateEvents(self, impressions):
    """Generate Events of clicks"""
    counter = {}

    for i in self.groups:      
      counter[i.id] = {}
      for j in self.campaigns:
        counter[i.id][j.id] = 0

    for i in impressions.keys():
      counter[i.groupID][impressions[i].id] += 1
      
    for i in counter.keys():
      for j in counter[i].keys():
        n = counter[i][j] 
        counter[i][j] = np.random.binomial(n, self.pCTR[i][j]) 
     
    self.clicked =[]
    for group in counter.keys():
      acc = 0
      for value in counter[group]:
        acc += value
      impressionsToUpdate = random.sample(impressions.keys(),acc)
      self.setClick(impressionsToUpdate)
      for i in impressionsToUpdate:
        self.clicked.append(i)
      

  def setClick(self, impressions):
    for i in impressions
      i.click = True


  def simulate(self):
    if hasattr(self, agent) != True:
      raise Exception("Agent Class should be setted.")

    for t in xrange(period): # Para cada tempo i em tau
      print "Time: " + t 
      impressions = []

      for i in self.groups:
        impressions.append(i.generateImpressions(t))

      allocated = self.agent.allocate(impressions)

      self.generateEvents(allocated)
    
      self.agent.updateState(self.clicked)
      
      for i in allocated:
        print i

