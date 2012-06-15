from Agent import * 

class stupidAgent(Agent):
  """Stupid Agent."""

  def __init__(self, campaigns, groups):
    Agent.__init__(self, campaigns, groups)

    campaigns = campaigns.values()
    campaigns.sort(key = lambda x: x.budget, reverse = True)

    self.campaignsX = list(campaigns)


  def allocate(self, impressions):
    result = {}

    for group in impressions:
    
      for impression in group:
      
        while ((impression.campaignID == None) and (len(self.campaignsX) > 0)):
  
          if len(self.campaignsX) > 0:

            if (self.campaignsX[0].spentBudget <= self.campaignsX[0].budget):

              result[impression] = self.campaignsX[0]
              impression.allocate(self.campaignsX[0].ID)

            else:

              self.campaignsX.pop(0)

          else:

            impression.allocate(None)

    return result

  def updateState(self, state):
    for impression in state:
      self.campaigns[impression.campaignID].update(impression)
    
    
   
