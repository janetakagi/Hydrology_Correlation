import pandas as pd
import datetime
import copy


def sort_hemispheres():
	meta_data = pd.read_csv("catchmentMetadata.csv")
	basin_id_list = []
	hemi_dict = {}
	for latitude, catchment in meta_data.loc[:,['new_lat.x','grdc_no']].itertuples(index=False):
		new_cat = int(round(catchment))
		if float(latitude) > 0:
			#if new_cat in hemi_dict:
			#	print(f'{new_cat}: northern')
			hemi_dict[new_cat] = 'northern'
		elif float(latitude) < 0:
			#if new_cat in hemi_dict:
			#	print(f'{new_cat}: southern')
			hemi_dict[new_cat] = 'southern'
		basin_id_list.append(new_cat)
	# hemi_dict contains the catchment as the key and the hemisphere as the value
	# basin_id_list contains a list of catchments from the metadata file
	return hemi_dict, basin_id_list


def mk_hemi_flow_dfs():
	df = pd.read_csv('allDailyFlowData.csv')
	hemi_dict, basin_id_list = sort_hemispheres()
	northern_cats = ['date']
	southern_cats = ['date']
	for cat in df.columns[4:]:
		if not cat.endswith('(1)') and not cat.endswith('Year'):
			if int(cat) in hemi_dict:
				if hemi_dict[int(cat)] == 'southern':
					southern_cats.append(cat)
				elif hemi_dict[int(cat)] == 'northern':
					northern_cats.append(cat)
	northern_flow = df[northern_cats]
	southern_flow = df[southern_cats]
	return northern_flow, southern_flow	


def shift_southern_date(southern_flow): # shifts data back 4 months for southern hemisphere
	delta = datetime.timedelta(days=122)
	newDates = []
	df = southern_flow
	for date in df['date']:
		dt = datetime.datetime.strptime(date, '%Y-%m-%d')
		dt = dt - delta
		newDates.append(dt)
	df['date'] = newDates
	return df


def merge_north_south(southern_flow, northern_flow): # merges northern and new southern data and saves to csv file
	sdf = southern_flow
	ndf = northern_flow
	sdf['date'] = sdf['date'].astype('datetime64[ns]')
	ndf['date'] = ndf['date'].astype('datetime64[ns]')
	df = ndf.merge(sdf, on="date", how='left')
	df.to_csv("newallDailyFlowData.csv", index=False)

