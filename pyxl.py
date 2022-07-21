import pandas as pd
import openpyxl

readfile = pd.read_csv('GFDLNFO_BACKADJUSTED_01012021.csv')

file_to_be_read = readfile.loc[
    (readfile['Close']>200)&
    (readfile['Ticker'].str.startswith('BANKNIFTY'))&
    (readfile['Time'].str.startswith('10:00'))
]

file_to_be_read.style.hide_index()

#
print(file_to_be_read)