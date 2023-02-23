import pandas as pd

# 3 = humidity, 4 = temperature, 5 = rainfall, 6 = pressure

def call_API(w_type, n_data_pts):
    d = {'humidity':'3', 'temperature':'4', 'rainfall':'5', 'pressure':'6'}
    
    fields_n = d[w_type]

    url = f'https://api.thingspeak.com/channels/12397/fields/{fields_n}.csv?results={n_data_pts}'
    df = pd.read_csv(url)
    
    return df