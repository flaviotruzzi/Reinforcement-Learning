import uuid

class Campaign:
  
  def __init__(self, budget, model='CPC', initialPeriod=0, validPeriod=0, CPC=None):
    self.ID = uuid.uuid4()
    self.budget = budget
    self.model = model
    self.initialPeriod = initialPeriod
    self.validPeriod = validPeriod
    self.spentBudget = 0
    self.CPC = CPC

  def update(self, impressionsAllocated):
    if model == 'CPC':
      self.updateCPC(impressionsAllocated)
    elif model == 'CPA':
      self.updateCPA(impressionsAllocated)
    elif model == 'CPL':
      self.updateCPL(impressionsAllocated)
    elif model == 'CPS':
      self.updateCPS(impressionsAllocated)

  def updateCPC(self, impressionsAllocated):
    for i in ImpressionsAllocated:
      self.spentBudget += self.CPC

  def updateCPA(self, impressionsAllocated):
    raise NotImplementedError("TODO")
  
  def updateCPL(self, impressionsAllocated):
    raise NotImplementedError("TODO")
  
  def updateCPS(self, impressionsAllocated):
    raise NotImplementedError("TODO")
