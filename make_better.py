
def make_better(df, filename):
	filename = filename.split('_')
	filename = filename[2]
	filename = filename.split('.')
	filename = filename[0]
	# print(filename)
	# print(df)
	# print(df[df.columns[1]])
	df[str(filename)] =list(df[df.columns[1]])
	df = df.drop(df.columns[1], axis = 1)
	return df

def make_better_temp_and_precip(df, filename):
	filename = filename.split('_')
	filename = filename[1]
	filename = filename.split('.')
	filename = filename[0]
	# print(filename)
	# print(df)
	# print(df[df.columns[1]])
	df[str(filename)] =list(df[df.columns[1]])
	df = df.drop(df.columns[1], axis = 1)
	return df

