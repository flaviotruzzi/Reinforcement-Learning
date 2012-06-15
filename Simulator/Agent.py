

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
    """Receive an update from the simulator. It's a list with each impression that had an event."""
    raise NotImplementedError("You should have implemented it")

