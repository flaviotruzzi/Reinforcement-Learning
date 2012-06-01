# -*- coding: utf-8 -*-

import numpy as np
import sys, bisect
import pylab as pl
from matplotlib import rc

rc('text', usetex=True)

qstar = np.random.normal(loc = 0, scale = 1, size = (10,2000))

class nArmedBandit:
  
  def __init__(self, qstar, n = 10, s = 2000, plays = 1000, epsilon = 0.1):
    self.n = n
    self.s = s
    self.plays = plays
    self.epsilon = epsilon

    self.estimated_q = np.zeros(n)
    self.total_counts = np.zeros(n)
    self.total_accs = np.zeros(n)

    self.rewards = np.zeros(1000) # Vetor acumulando recompensas por play

    self.actions = np.zeros(1000) # Vetor acumulando qtas ações foram ótimas...
    
    self.qstar = qstar
  def initTask(self):
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
        r = np.random.normal(loc=self.qstar[a,i],scale=1)
        self.updateQ(r, a)
        self.rewards[j] += r
        if a == np.argmax(self.qstar[:,i]):
          self.actions[j] += 1
      self.estimated_q += self.q
      self.total_counts += 1
      self.total_accs += self.accumulated
    sys.stdout.write("\n Finished")


  def testBedEGreedy(self):
    sys.stdout.write("\n TestBed E-Greedy, e=" + repr(self.epsilon) + "\n")
    for i in xrange(self.s):
      self.initTask()
      for j in xrange(self.plays):
        a = self.eGreedyAction()
        r = np.random.normal(loc=self.qstar[a,i],scale=1)
        self.updateQ(r, a)
        self.rewards[j] += r
        if a == np.argmax(self.qstar[:,i]):
          self.actions[j] += 1
      self.estimated_q += self.q
      self.total_counts += 1
      self.total_accs += self.accumulated
    sys.stdout.write("\n Finished")

  def softMaxAction(self, temperature):
    p = self.q/(temperature+.1e-1)
    p = np.cumsum((np.exp(p))/np.exp(p).sum())
    k = np.random.uniform()
    for i in xrange(10):
      if k <= p[i]:
        return i

  
  def testBedSoftMax(self, temperature):
    sys.stdout.write("\r TestBed SoftMax, T=" + repr(temperature) + "\n")
    for i in xrange(self.s):
      self.initTask()
      for j in xrange(self.plays):
        a = self.softMaxAction(temperature)
        r = np.random.normal(loc=self.qstar[a,i], scale=1)
        self.updateQ(r, a)
        self.rewards[j] += r
        if a == np.argmax(self.qstar[:,i]):
          self.actions[j] += 1
      self.estimated_q += self.q
      self.total_counts += 1
      self.totals_accs = self.accumulated
    sys.stdout.write("\n Finished")

  def testBedSimulatedAnnealing(self, temperature, alpha):
    sys.stdout.write("\r TestBed Simulated Annealing, Ti=" + repr(temperature) + "\n")
    backT = temperature
    for i in xrange(self.s):
      self.initTask()
      temperature = backT
      for j in xrange(self.plays):
        a = self.softMaxAction(temperature)
        r = np.random.normal(loc=self.qstar[a,i], scale=1)
        self.updateQ(r, a)
        self.rewards[j] += r
        if a == np.argmax(self.qstar[:,i]):
          self.actions[j] += 1
        temperature = alpha*temperature
      self.estimated_q += self.q
      self.total_counts += 1
      self.totals_accs = self.accumulated
    sys.stdout.write("\n Finished")




def bench():
  greedy = nArmedBandit(qstar=qstar)
  simulatedAnnealing = nArmedBandit(qstar=qstar)
  egreedy = nArmedBandit(epsilon=.1,qstar=qstar)
  e2greedy = nArmedBandit(epsilon=.05,qstar=qstar)
  e3greedy = nArmedBandit(epsilon=0.01,qstar=qstar)
  softMax10 = nArmedBandit(qstar=qstar)
  softMax01 = nArmedBandit(qstar=qstar)
  softMax05 = nArmedBandit(qstar=qstar)

  simulatedAnnealing.testBedSimulatedAnnealing(temperature=10, alpha=.99)
  greedy.testBedGreedy()
  egreedy.testBedEGreedy()
  e2greedy.testBedEGreedy()
  e3greedy.testBedEGreedy()
  softMax10.testBedSoftMax(10)
  softMax01.testBedSoftMax(0.1)
  softMax05.testBedSoftMax(0.5)

  s = 2000
  fig = pl.figure()
  pl.plot(greedy.rewards/s, label="$Greedy$")
  pl.plot(egreedy.rewards/s, label="$\epsilon-greedy = 0.1$")
  pl.plot(e2greedy.rewards/s, label="$\epsilon-greedy = 0.05$")
  pl.plot(e3greedy.rewards/s, label="$\epsilon-greedy = 0.01$")
  pl.plot(softMax10.rewards/s, label="$SoftMax (T=10)$")
  pl.plot(softMax01.rewards/s, label="$SoftMax (T=0.1)$")
  pl.plot(softMax05.rewards/s, label="$SoftMax (T=0.5)$")
  pl.plot(simulatedAnnealing.rewards/s, label="$Simulated\:Annealing (T=10, \alpha=.9)$")

  pl.xlabel("$Plays$")
  pl.ylabel("$Average\:reward$")
  pl.legend(loc='lower right')

  fig = pl.figure()
  pl.plot(100*greedy.actions/s, label="$Greedy$")
  pl.plot(100*egreedy.actions/s, label="$\epsilon-greedy = 0.1$")
  pl.plot(100*e2greedy.actions/s, label="$\epsilon-greedy = 0.05$")
  pl.plot(100*e3greedy.actions/s, label="$\epsilon-greedy = 0.01$")
  pl.plot(100*softMax10.actions/s, label="$SotMax (T=10)$")
  pl.plot(100*softMax01.actions/s, label="$SotMax (T=0.1)$")
  pl.plot(100*softMax05.actions/s, label="$SotMax (T=0.5)$")
  pl.plot(100*simulatedAnnealing.rewards/s, label="$Simulated\:Annealing (T=10, \alpha=.9)$")

  pl.xlabel("$Plays$")
  pl.ylabel("$Optimality\,\%$")
  pl.legend(loc='lower right')

  pl.show()

