import pandas as pd

def fix_meta():
	adf = pd.read_csv("catchmentMetadata.csv")
	ldf = pd.read_csv("stations_to_lat_lon.csv")
	df = adf.merge(ldf, on="grdc_no")
	
	df["new_lat.x"] = df["lat"]
	df["new_lon.x"] = df["long"]
	
	df = df.drop("lat", axis=1)
	df = df.drop("long", axis=1)
		
	df.to_csv("catchmentmetadata.csv", index=false)
