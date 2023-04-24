import pandas as pd
from tqdm import tqdm
from hemisphere import *
from new_hydro_corr import *


def updateDict(cat, dataDict, df_et, df_t, df_p, odd_cats, flowDf):
	r_et, r_t, r_p, odd_cat = get_corr(cat, df_et, df_t, df_p, flowDf)
	dataDict["grdc_no"].append(cat)
	dataDict["correlation_q_et"].append(r_et)
	dataDict["correlation_q_t"].append(r_t)
	dataDict["correlation_q_p"].append(r_p)
	odd_cats["Catchments_w_no_data"].append(odd_cat)
	return dataDict, odd_cats


def saveDict(dataDict, df, odd_cats):
	# turn into dataframe
	corrDf = pd.DataFrame.from_dict(dataDict)
	oddDf = pd.DataFrame.from_dict(odd_cats)
	# merge with metadata
	outDf = df.merge(corrDf, on="grdc_no")
	outDf.to_csv("correlation_augmented_metadata.csv", index=False)
	oddDf.to_csv("odd_catchments.csv", index=False)


def fix_cats(df):
	newCats = []
	catIsNA = df['grdc_no'].isna()
	for i,cat in enumerate(df['grdc_no']):
		if catIsNA[i]:
			newCats.append(None)
		else:
			newCats.append(str(int(cat)))
	df['grdc_no'] = newCats
	return df	


def correlate_and_merge():
	# read in the metadata
	df = pd.read_csv("catchmentMetadata.csv")
	df = fix_cats(df)
	# create an dict to hold the correlations
	dataDict = {"grdc_no":[], "correlation_q_et":[], "correlation_q_t":[], "correlation_q_p":[]}
	odd_cats = {"Catchments_w_no_data":[]}
	# calculate the correlations
	hemi_dict, catchments = sort_hemispheres()
	df_et = pd.read_csv("/home/takagij/sandbox/evaporation.csv")	
	df_t = pd.read_csv("/home/takagij/sandbox/temperatures.csv")
	df_p = pd.read_csv("/home/takagij/sandbox/precipitation.csv")
	flowDf = pd.read_csv("newallDailyFlowData.csv")
	numIts = len(catchments)
	loop = tqdm(total=numIts)
	for i, cat in enumerate(catchments):
		dataDict, odd_cats = updateDict(str(cat), dataDict, df_et, df_t, df_p, odd_cats, flowDf)
		if i % 10 == 0 and i > 0:
			saveDict(dataDict, df, odd_cats)
		loop.update(1)
	loop.close()
