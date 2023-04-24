import numpy as np
import os
import pandas as pd
from make_better import make_better_temp_and_precip


def collect_precip():
	root = "/home/takagij/Basin_Precip_TS_for_model/"
	numSeen = 0
	for filename in os.listdir(root):
		if filename.endswith(".csv"):
			if numSeen == 0:
				bigDf = pd.read_csv(root+filename)
				bigDf = make_better_temp_and_precip(bigDf, filename)
			else:
				littleDf = pd.read_csv(root+filename)
				littleDf = make_better_temp_and_precip(littleDf, filename)
				bigDf = bigDf.merge(littleDf,on="Date")
			numSeen += 1
	bigDf.to_csv("precipitation.csv")

