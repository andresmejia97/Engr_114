import pandas as pd
import numpy as np

def clean_data(df):
    df_ar = np.array(df)
    df_ar1 = df_ar[:,2]
    return df_ar1
    