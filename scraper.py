import pytrends
import csv
from pytrends.request import TrendReq
import pandas as pd

def scrape_file(filename):
    global pytrends
    pytrends = TrendReq(hl='en-US', tz=360)
    with open(filename) as fp:
       line = fp.readline()[:-1]
       scrape_word(line, True)
       line = fp.readline()[:-1]
       while line:
           scrape_word(line)
           line = fp.readline()[:-1]

def scrape_word(text, initial=False):

    kw_list = [text]
    pytrends.build_payload(kw_list=kw_list, cat=0, timeframe='today 5-y', geo='GB')

    # Interest Over Time
    interest_over_time_df = pytrends.interest_over_time()
    print(interest_over_time_df)
    flattened = interest_over_time_df[[text]].values.tolist()

    interest_flattened = [text]

    for i in range(len(flattened)):
        interest_flattened.append(flattened[i][0])

    print(interest_flattened)

    # if initial:
    #     with open('trends.csv','w') as result_file:
    #         wr = csv.writer(result_file, dialect='excel')
    #         wr.writerow(interest_flattened)
    # else:
    #     with open('trends.csv','a') as result_file:
    #         wr = csv.writer(result_file, dialect='excel')
    #         wr.writerow(interest_flattened)

def transpose(file):
    file_df=pd.read_csv(file)
    file_df= file_df.T
    file_df.to_csv('trends.csv')


if __name__ == "__main__":
    scrape_file('research_Paper_Search_Terms.txt')
    # transpose('trends.csv')
