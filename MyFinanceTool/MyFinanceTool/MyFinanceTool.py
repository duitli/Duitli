import yahoo_finance as yf
import numpy as np
import pandas as pd
import urllib.request as re
import pandas_datareader as web
import datetime


def main():
    a = 1 

    start = datetime.datetime(2016,1,1)
    end = datetime.date.today()
    aplOption = web.Options("AAPL", "yahoo")
    apple = web.get_data_google("AAPL",start, end)

    print (apple.head())
    



def pullData(stock):
    fileLine = stock + '.txt'
    urltovisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1y/csv'
    with urllib.request.urlopen(urltovisit) as f:
        sourceCode = f.read().decode('utf-8')
    splitSource = sourceCode.split('\n')

    for eachLine in splitSource:
        splitLine = eachLine.split(',') # <---(here ',' instead of '.')
        if len(splitLine) == 6: # <----( here, 6 instead of 5 )
            if 'values' not in eachLine:
                saveFile = open(fileLine,'a')
                linetoWrite = eachLine+'\n'
                saveFile.write(linetoWrite)

    print('Pulled', stock)
    print('...')
    time.sleep(.5)



if __name__ == "__main__":
    main()