from fundamentus import get_data
import pandas as pd
import waitingbar
import os, time, stat
from datetime import datetime


def data_to_csv():
    data = get_data()
    data = {outer_k: {inner_k: float(inner_v) for inner_k, inner_v in outer_v.items()} for outer_k, outer_v in data.items()}
    df_data = pd.DataFrame.from_dict(data).transpose().reset_index() #transposing
    df_data = df_data.rename(columns={'index':'Ticker'}) #rename 'index' columns to 'ticker'
    df_data.to_csv(r'fundamentus.csv', sep=';', index=False, mode='w') #save csv

def analise():
    df_fundamentus = pd.read_csv('fundamentus.csv',sep=';')
    df_fundamentus = df_fundamentus[
        (df_fundamentus['DY'] <= 1) & (df_fundamentus['DY'] >= 0.06 ) & 
        (df_fundamentus['P/L'] <= 10) & (df_fundamentus['P/L'] >= 0.01 ) &
        (df_fundamentus['P/VP'] <= 4) & (df_fundamentus['P/VP'] >= 0.01 ) &
        (df_fundamentus['ROE'] <= 0.7) & (df_fundamentus['ROE'] >= 0.001 ) &
        (df_fundamentus['EV/EBITDA'] >= 0.001 ) &
        (df_fundamentus['Ticker'].astype(str).str.contains('3|4'))].sort_values(by=["DY","P/L","P/VP"],ascending=False)
    return df_fundamentus.head(30)

def modi():
    filePath = 'fundamentus.csv'
    try:
        fileStatsObj = os.stat(filePath)
        modificationTime = time.ctime ( fileStatsObj [ stat.ST_MTIME ] )
    except OSError:
        print("Path '%s' does not exists or is inaccessible" %filePath)

    times = os.path.getmtime(filePath)
    return times

if __name__ == '__main__':
    start_msg = waitingbar.WaitingBar('Starting download data...')
    data_to_csv()
    start_msg.stop()
    print('Check data at "funamentus.csv" file.')
    print(analise())
    print("Last Modified Time : ", modi())
    print(datetime.now())
