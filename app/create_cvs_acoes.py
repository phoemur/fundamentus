from fundamentus import get_data
import pandas as pd
import waitingbar
import os, time, stat, datetime


def data_to_csv_acoes(VALUE):
    setor = VALUE
    print('data_to_csv_acoes',setor)
    data = get_data(1,setor=setor)
    data = {outer_k: {inner_k: float(inner_v) for inner_k, inner_v in outer_v.items()} for outer_k, outer_v in data.items()}
    df_data = pd.DataFrame.from_dict(data).transpose().reset_index() #transposing
    df_data = df_data.rename(columns={'index':'Ticker'}) #rename 'index' columns to 'ticker'
    df_data.to_csv(r'fundamentus.csv', sep=';', index=False, mode='w') #save csv

def analise_acoes(NUMBER):
    #recuperacao_judicial = ["TEKA4", "TCNO4", "RPMG3", "LUPA3","OIBR4","MWET4","MMXM3","INEP4","VIVR3","FRTA3","IGBR3","SLED3","FHER3","HOOT4"]
    df_fundamentus = pd.read_csv('fundamentus.csv',sep=';')
    #df_fundamentus = df_fundamentus[df_fundamentus['Ticker'].isin(recuperacao_judicial)]
    df_fundamentus = df_fundamentus[
        (df_fundamentus['DY'] <= 1) & (df_fundamentus['DY'] >= 0.06 ) & 
        (df_fundamentus['P/L'] <= 10) & (df_fundamentus['P/L'] >= 0.01 ) &
        (df_fundamentus['P/VP'] <= 4) & (df_fundamentus['P/VP'] >= 0.01 ) &
        (df_fundamentus['ROE'] <= 0.8) & (df_fundamentus['ROE'] >= 0.001 ) &
        (df_fundamentus['EV/EBITDA'] >= 0.001 ) & (df_fundamentus['P/EBIT'] > 0 ) &
        (df_fundamentus['Ticker'].astype(str).str.contains('1|2|3|4|4|6'))].sort_values(by=["DY","P/VP","P/L"],ascending=False)
    return df_fundamentus.head(NUMBER)

def check_file_acoes(VALUE):
    setor = VALUE
    print('check_file_acoes',setor)
    filePath = 'fundamentus.csv'
    try:
        fileStatsObj = os.stat(filePath)
        if os.path.exists(filePath):
            today = datetime.datetime.today()
            modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(filePath))
            duration = today - modified_date
            if duration.days > 2 or setor == 0 or 'setor' in locals():
                print('Your file is old and may have modifications ...')
                start_msg = waitingbar.WaitingBar('Starting download new data...')
                data_to_csv_acoes(setor)
                start_msg.stop()
        modificationTime = time.ctime ( fileStatsObj [ stat.ST_MTIME ] )
        c_time = os.path.getctime(filePath)
        dt_c = datetime.datetime.fromtimestamp(c_time)
        print('Created on:', dt_c)
        m_time = os.path.getmtime(filePath)
        dt_m = datetime.datetime.fromtimestamp(m_time)
        print('Modified on:', dt_m)
        return modificationTime
    except OSError:
        start_msg = waitingbar.WaitingBar('Starting download data...')
        data_to_csv_acoes(setor)
        start_msg.stop()

if __name__ == '__main__':
    print('Check data at "funamentus.csv" file.')
    print("Last Modified Time : ", check_file_acoes(5))
    print(analise_acoes(10))
