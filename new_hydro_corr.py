import numpy as np
import pandas as pd
import scipy
from scipy import stats
from hemisphere import *


def get_merged_data(basinId, number, allflowDf):
    # read in the flow
    flowDf = allflowDf
    # keep only the "date" and "basinId"  columns
    flowDf = flowDf[["date",number]]
    # read in the atmospheric data
    temp = basinId
    # change the name of "Date" to "date" so we can merge
    temp["date"] = temp["Date"]  # add a new column "date" that looks just like "Date"
    temp = temp.drop("Date", axis=1)  # get rid of "Date"
    # add the temperature Df into the flow Df
    mergedDf = flowDf.merge(temp, on="date")  # "on" -> name of column to merge on
    # get rid of nans with masks
    maskQ = np.array(~mergedDf[number+'_x'].isna())  # this is the daily flow
    maskP = np.array(~mergedDf[number+'_y'].isna())  # this is the atm data
    mask = np.logical_and(maskQ, maskP)
    # mask1: 1 0 1 0
    # mask2: 0 0 1 1
    # mask : 0 0 1 0
    # apply the mask
    mergedDf = mergedDf[mask]
    return mergedDf


def compare(atm_data, flow, cat):
    if len(atm_data) < 2:
        return None, cat
    r, p = scipy.stats.pearsonr(atm_data, flow)
    return str(r), None


def get_corr(cat, df_et, df_t, df_p, allflowDf):
	if cat in df_et:
		bId = df_et.loc[:,['Date', cat]]
		merged_df = get_merged_data(bId, cat, allflowDf)
		r_et, odd_cat = compare(merged_df[cat+'_y'], merged_df[cat+'_x'], cat)
	else:
		r_et, odd_cat = None, None
	if cat in df_t:
		bId = df_t.loc[:,['Date', cat]]
		merged_df = get_merged_data(bId, cat, allflowDf)
		r_t, odd_cat = compare(merged_df[cat+'_y'], merged_df[cat+'_x'], cat)
	else:
		r_t = None
	if cat in df_p:
		bId = df_p.loc[:,['Date', cat]]
		merged_df = get_merged_data(bId, cat, allflowDf)
		r_p, odd_cat = compare(merged_df[cat+'_y'], merged_df[cat+'_x'], cat)
	else:
		r_p = None
	return r_et, r_t, r_p, odd_cat

