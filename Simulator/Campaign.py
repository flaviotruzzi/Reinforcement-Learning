import uuid

class Campaign:
  """Campaign class.  
  """  

  def __init__(self, budget, model='CPC', initialPeriod=0, validPeriod=0, CPC=None):
    """Constructor.

    Parameters:
      - budget: budget of the campaign
      - model: can be 'CPC', 'CPA', 'CPL', 'CPS'. Only CPC is implemented yet. 
      - initialPeriod: instant of the simulation that the campaign will be available. 0 = Beginning.
      - validPeriod: last instant of the simulation that the campaign still valid. 0 = end of simulation.
      - CPC: cost per click that this campaign accept to pay.
    """
    self.ID = uuid.uuid4()
    self.budget = budget
    self.model = model
    self.initialPeriod = initialPeriod
    self.validPeriod = validPeriod
    self.spentBudget = 0
    self.CPC = CPC 

  def update(self, impressionsAllocated):
    """Update the campaign with the allocated impressions. Only impressions that result in change of spent budget is given.
    """
    if self.model == 'CPC':
      self.updateCPC(impressionsAllocated)
    elif self.model == 'CPA':
      self.updateCPA(impressionsAllocated)
    elif self.model == 'CPL':
      self.updateCPL(impressionsAllocated)
    elif self.model == 'CPS':
      self.updateCPS(impressionsAllocated)

  def updateCPC(self, impressionsAllocated):
    """Update CPC campaign by summing all the spent budget with impressions.
    """
#    for i in impressionsAllocated:
    self.spentBudget += self.CPC

  def updateCPA(self, impressionsAllocated):
    raise NotImplementedError("TODO")
  
  def updateCPL(self, impressionsAllocated):
    raise NotImplementedError("TODO")
  
  def updateCPS(self, impressionsAllocated):
    raise NotImplementedError("TODO")
