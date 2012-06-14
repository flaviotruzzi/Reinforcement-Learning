import uuid

class Impression:
  """Impression class"""


  def __init__(self, groupID, period, click, action=None, lead=None, sales=None):
    """Constructor:

       Arguments:
        - groupID: group that generated this impression;
        - period: instant of simulation time that this impression was issued;
        - click: this impression was clicked or not;
        - action, lead, sales: not used yet.
    """
    self.groupID = groupID
    self.ID = uuid.uuid4()
    self.period = period
    self.click = click
    self.action = action
    self.lead = lead
    self.sales = sales
    self.campaignID = None

  def allocate(self, campaignID):
    """Allocate an impression to a campaign.

    Parameters:
      - campaignID: ID of the allocated campaign.
    """
    if self.campaignID == None:
      self.campaignID = campaignID
    else:
      raise AllocationException("This Impression has already been allocated")

class AllocationException(Exception):
  """Base Exception class for allocation issues."""
  def __init__(self, value):
    self.value = value

  def __str__(self):
    return repr(self.value)
