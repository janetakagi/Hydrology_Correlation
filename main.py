from new_hydro_corr import *
from merge_meta import *
from mergeet import *
from mergetemps import *
from mergeprecip import *
from make_better import *
from hemisphere import *
from df_merge import *


def main():
	# fix_meta()
	# northern_flow, southern_flow = mk_hemi_flow_dfs()
	# new_southern_flow = shift_southern_date(southern_flow)
	# merge_north_south(new_southern_flow, northern_flow)
	# collect_evap()
	# collect_precip()
	# collect_temp()
	# correlate_and_merge()
	# df = pd.read_csv('correlation_augmented_metadata.csv')
	# df = df.drop('Unnamed: 5', axis=1)
	# df.to_csv('correlation_augmented_metadata.csv')

if __name__ == '__main__':
	main()
