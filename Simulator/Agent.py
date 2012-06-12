

class Agent:
  """Base Agent class that allocate campaigns to impressions."""

  def __init__(self, campaigns, groups):
    self.campaigns = campaigns
    self.groups = groups


  def allocate(self, impressions):
    """Impressions is a list with all impressions to allocate in that episode. 
    Return: dict = { impression : campaign, ... }"""
    raise NotImplementedError("You should have implemented it")

  def updateState(self, state):
    """Receive an update from the simulator. It's a dictionary.
    state[impressionID] is another dictionary.
    state[impressionID]['click'] = bool returning if the ad was clicked or not.
    state[impressionID]['action'] = Say which action was made, None if any action was made.
    state[impressionID]['sales'] = Say if any sale was made, returning the monetary value of the sale, None if any sale was made.
    state[impressionID]['lead'] = Say if any lead was made, None if any lead was made."""
    raise NotImplementedError("You should have implemented it")

