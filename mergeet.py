import numpy as np
import os
import pandas as pd
from make_better import make_better


def collect_evap():
	root = "/home/takagij/Basin_ET_TS_for_model/"
	numSeen = 0
	for filename in os.listdir(root):
		if filename.endswith(".csv"):
			if numSeen == 0:
				bigDf = pd.read_csv(root+filename)
				bigDf = make_better(bigDf, filename)
			else:
				littleDf = pd.read_csv(root+filename)
				littleDf = make_better(littleDf, filename)
				bigDf = bigDf.merge(littleDf,on="Date")

			numSeen += 1
		#if index > 20:
		#	break
	bigDf.to_csv("evaporation.csv")

