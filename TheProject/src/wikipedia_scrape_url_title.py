import numpy as np
import pandas as pd
import warnings
import wikipedia

title_df = pd.read_csv('titles.csv')
title_df = pd.concat([title_df, pd.DataFrame(columns=['URL'])])

title_error = 0

for i in range(len(title_df)):
    print(i)
    title_data = title_df.iloc[i, :]

    title = title_data.Title
    artist = title_data.Artist
    keyword = title + ' ' + artist
    url = ''

    try:
        wikipage = wikipedia.page(title)        # first search trial
        url = wikipage.url
    except Exception as e:
        try:
            wikipage = wikipedia.page(keyword)  # second search trial
            url = wikipage.url
        except Exception as e2:
            print(e2)
            title_error = title_error + 1
            print('error: ' + str(title_error))

    title_data.URL = url
    title_df.iloc[i, :] = title_data

print('Titles with error: ', str(title_error))

title_df.to_csv('titles_url_new.csv', index=False)
