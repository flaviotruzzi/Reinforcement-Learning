import numpy as np  

class Impression:
  
  def __init__(self, CTR):
    self.CTR = abs(np.random.normal(loc=CTR,scale=.1))



class Group:

  def __init__(self, h=None, CTR=None):

    if h == None:
      self.h = np.random.randint(low=2000,high=5000)
    else:
      self.h = h

    if CTR == None:
      self.CTR = abs(np.random.normal(loc=0,scale=.2))
    else:
      self.CTR = CTR
    
  def getImpression(self):
    
    if self.h > 0:
      self.h -= 1
      return Impression(self.CTR)
    else:
        return None


#class Simulator:

#  def __init__(self,

