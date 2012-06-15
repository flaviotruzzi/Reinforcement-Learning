import uuid
import numpy as np
from Impression import *

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
    self.ID = uuid.uuid4()
    self.impressionLambda = impressionLambda
    self.impressionSource = impressionSource

    self.impressions = []

  def numberOfImpressions(self, t=None):
    """Generate the number of impressions that will be issued in a instant of time"""
    if type(self.impressionLambda) != list:
      return np.random.poisson(self.impressionLambda)
    else:
      return np.random.poisson(self.impressionLambda[t])

  def generateImpressions(self, t):
    if (self.impressionSource == None):
      impressions = []
      for i in xrange(self.numberOfImpressions(t)):
        impressions.append(Impression(self.ID, t, None)) # Initialize an Impression from the group ID, in the simulation time t, with None click, the click will be updated latter.
      self.impressions.append(len(impressions))
      return impressions
    else:
      raise NotImplementedError("Not implemented yet")
