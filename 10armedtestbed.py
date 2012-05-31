# -*- coding: utf-8 -*-

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

    self.rewards = np.zeros(1000) # Vetor acumulando recompensas por play

    self.actions = np.zeros(1000) # Vetor acumulando qtas ações foram ótimas...

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
        self.rewards[j] += r
        if a == np.argmax(self.qstar):
          self.actions[j] += 1
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
        self.rewards[j] += r
        if a == np.argmax(self.qstar):
          self.actions[j] += 1
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

s = 2000
fig = pl.figure()
pl.plot(greedy.rewards/s, label="$Greedy$")
pl.plot(egreedy.rewards/s, label="$\epsilon-greedy = 0.1$")
pl.plot(e2greedy.rewards/s, label="$\epsilon-greedy = 0.05$")
pl.plot(e3greedy.rewards/s, label="$\epsilon-greedy = 0.01$")
pl.xlabel("$Plays$")
pl.ylabel("$Average\:reward$")
pl.legend(loc='bottom right')

fig = pl.figure()
pl.plot(100*greedy.actions/s, label="$Greedy$")
pl.plot(100*egreedy.actions/s, label="$\epsilon-greedy = 0.1$")
pl.plot(100*e2greedy.actions/s, label="$\epsilon-greedy = 0.05$")
pl.plot(100*e3greedy.actions/s, label="$\epsilon-greedy = 0.01$")
pl.xlabel("$Plays$")
pl.ylabel("$Optimality\,\%$")
pl.legend(loc='bottom right')

pl.show()

