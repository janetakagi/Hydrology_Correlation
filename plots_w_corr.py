import pandas as pd
import matplotlib.pyplot as plt


def mk_plots():
    df = pd.read_csv("correlation_augmented_metadata.csv")
    # print(df)
    variables = ['meanPercentDC_Imperfectly','meanPercentDC_ModeratelyWell','meanPercentDC_Poor','meanPercentDC_SomewhatExcessive','meanPercentDC_VeryPoor','meanPercentDC_Well'] 
    # variables = ['strmOrder','Magnitude','strmDrop','WSNO','length_km','area_sqkm','drain_den','gelev_m','garea_sqkm','gord','PathLength','TotalLength','cls1','cls10','cls11','cls12','cls2','cls3','cls4','cls5','cls6','cls7','cls8','cls9','Dam_SurfaceArea','Dam_Count','HydroLakes_Area_sqkm','MeanPopden_2000','MeanPopden_2005','MeanPopden_2010','MeanPopden_2015','MeanHumanFootprint','meanPercentDC_Imperfectly','meanPercentDC_ModeratelyWell','meanPercentDC_Poor','meanPercentDC_SomewhatExcessive','meanPercentDC_VeryPoor','meanPercentDC_Well']
    for var in variables:
        plt.scatter(df[var],df["correlation_q_et"],label='evaporation')
        plt.scatter(df[var],df["correlation_q_t"],label='temperature')
        plt.scatter(df[var],df["correlation_q_p"],label='precipitation')
        plt.ylabel("coefficient of correlation")
        plt.yscale("log")
        plt.xlabel(var)
        plt.legend()
        plt.savefig(var+'correlation_logscale.png')
        plt.show()


mk_plots()
