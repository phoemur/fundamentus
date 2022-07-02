from fundamentusfii import get_data
import pandas as pd
import waitingbar


def data_to_csv():
    data = get_data()
#    data = {outer_k: {inner_k: float(inner_v) for inner_k, inner_v in outer_v.items()} for outer_k, outer_v in data.items()}

    df_data = pd.DataFrame.from_dict(data).transpose().reset_index() #transposing
    df_data = df_data.rename(columns={'index':'Ticker'}) #rename 'index' columns to 'ticker'
    df_data.to_csv(r'fundamentusfii.csv', sep=';', index=False, mode='w') #save csv

if __name__ == '__main__':
    start_msg = waitingbar.WaitingBar('Starting download data...')
    data_to_csv()
    start_msg.stop()
    print('Check data at "funamentusii.csv" file.')

    