
#okay, let's do the n armed bandit problem
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import random

N = 5
epochs = 1000
eta = 0.01
bandits = np.array([[1,0.1],[1,0.1],[1,0.5],[100,0.1],[1,0.1]])
print bandits.shape


def arm(mu,sigma):
	return np.random.normal(mu,sigma)

def etaGreedy(eta,means):
	rand = random.random()
	if eta>rand:
		choice = np.random.randint(0,N-1)
	else: 
		choice = np.argmax(means)
	return choice

def agent(qtotal,qcounts, reward,qindex):
	#update the q-arrays:
	qtotal[qindex] += reward
	qcounts[qindex]+=1

	#construct means:
	means = []
	for i in xrange(len(qtotal)):
		means.append(qtotal[i]/qcounts[i])
	means = np.array(means)
	#eta greedy selection
	choice = etaGreedy(eta, means)
	return choice



def play():
	qtotal = np.zeros(N)
	qcounts = np.zeros(N)
	qindex = 0
	#first select a bandit randomly
	rand = np.random.randint(0,N-1)
	reward = arm(bandits[rand][0],bandits[rand][1])
	choice = agent(qtotal,qcounts,reward,rand)
	for i in xrange(epochs):
		reward = arm(bandits[choice][0],bandits[choice][1])
		choice = agent(qtotal,qcounts,reward,choice)
		#print qtotal
		i+=1
	print qtotal
	print qcounts
	print np.sum(qtotal)
	print "done!"

play()

	





