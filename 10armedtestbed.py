import numpy as np
import sys
import pylab as pl
from matplotlib import rc

rc('text', usetex=True)

class nArmedBandit:
  
  def __init__(self, n = 10, s = 2000, plays = 1000, epsilon = 0.1):
    self.n = n
    self.s = s
    self.plays = plays
    self.epsilon = epsilon

    self.estimated_q = np.zeros(n)
    self.total_counts = np.zeros(n)
    self.total_accs = np.zeros(n)

    self.rewards = np.zeros((1000, 2000))

  def initTask(self):
    self.qstar = np.random.normal(loc = 0, scale = 1, size = self.n)
    self.accumulated = np.zeros(self.n)
    self.counts = np.zeros(self.n)
    self.q = np.zeros(self.n)

  def eGreedyAction(self):
    if (np.random.uniform() < self.epsilon):
      return np.random.randint(0,self.n)
    else:
      return np.argmax(self.q)

  def greedyAction(self):
    return np.argmax(self.q)

  def updateQ(self, r, a):
    self.accumulated[a] += r
    self.counts[a] += 1
    self.q[a] = self.accumulated[a]/self.counts[a]

  def testBedGreedy(self):
    sys.stdout.write("\n TestBed Greedy\n")
    for i in xrange(self.s):
      self.initTask()
      for j in xrange(self.plays):
        a = self.greedyAction()
        r = np.random.normal(loc=self.qstar[a],scale=1)
        self.updateQ(r, a)
        sys.stdout.write("\r Task: " + repr(i)) 
        sys.stdout.flush()
        self.rewards[j,i] = r
      self.estimated_q += self.q
      self.total_counts += 1
      self.total_accs += self.accumulated
    sys.stdout.write("\n Finished")


  def testBedEGreedy(self):
    sys.stdout.write("\n TestBed E-Greedy\n")
    for i in xrange(self.s):
      self.initTask()
      for j in xrange(self.plays):
        a = self.eGreedyAction()
        r = np.random.normal(loc=self.qstar[a],scale=1)
        self.updateQ(r, a)
        sys.stdout.write("\r Task: " + repr(i))
        sys.stdout.flush()
        self.rewards[j,i] = r
      self.estimated_q += self.q
      self.total_counts += 1
      self.total_accs += self.accumulated
    sys.stdout.write("\n Finished")


greedy = nArmedBandit()
egreedy = nArmedBandit(epsilon=.1)
e2greedy = nArmedBandit(epsilon=.05)
e3greedy = nArmedBandit(epsilon=0.01)

greedy.testBedGreedy()
egreedy.testBedEGreedy()
e2greedy.testBedEGreedy()
e3greedy.testBedEGreedy()

fig = pl.figure()
pl.plot(greedy.rewards.mean(axis=1), label="Greedy")
pl.plot(egreedy.rewards.mean(axis=1), label="$\epsilon$-Greedy = 0.1")
pl.plot(e2greedy.rewards.mean(axis=1), label="$\epsilon$-Greedy = 0.05")
pl.plot(e3greedy.rewards.mean(axis=1), label="$\epsilon$-Greedy = 0.01")
pl.legend()
pl.show()
