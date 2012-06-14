import uuid
import numpy as np

class Group:
  """Group class: represents a site, blog or any impression source."""

  def __init__(self, impressionLambda, impressionSource=None, category=None):
    """
    Constructor.

    Parameters:
      - lambdaa: lambda of the Poisson distribuction, can be none if impressionSource is given, can be a list (one element for each simulation time).
      - impressionSource: Source of impressions, must be None if lambdaa is given. Not Implemented Yet.
      - category: category of group, not used yet.
    """
    self.id = uuid.uuid4()
    self.impressionLambda = impressionLambda
    self.impressionSource = impressionSource

  def numberOfImpressions(self, t=None):
    """Generate the number of impressions that will be issued in a instant of time"""
    if type(lambdaa) != list:
      return np.random.poisson(lambdaa)
    else:
      return np.random.poisson(lambdaa[t])

  def generateImpressions(self, t):
    if (impressionSource == None):
      impressions = []
      for i in xrange(self.numberOfImpressions(t)):
        impressions.append(Impression(self.id, t, None)) # Initialize an Impression from the group ID, in the simulation time t, with None click, the click will be updated latter.
      return impressions
    else:
      raise NotImplementedError("Not implemented yet")
