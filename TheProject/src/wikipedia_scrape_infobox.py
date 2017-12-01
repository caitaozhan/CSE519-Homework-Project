import numpy as np
import pandas as pd
import warnings

import wikipedia

artist_df = pd.read_csv('../CSE519-2017-111634527/TheProject/music_data/billboard_artist.csv', na_values=['NA'])

#artist_df = pd.concat([artist_df,pd.DataFrame(columns=['WikiWordCount'])])
artist_df = pd.concat([artist_df,pd.DataFrame(columns=['WikiWordCount','URL'])])

artist_error = 0

for i in range(0, 10): #range(len(artist_df)): #range(0, 10):
	artist_data = artist_df.iloc[i,:]

	artist = artist_data.Artist
	#print "Artist: ", artist
	
	wordcount = np.NaN
	url = ''
	try:
		wikiPage = wikipedia.page(artist)
		
		wordcount = len(wikiPage.content.split())
		#print "Wikipedia wordcount: ", wordcount

		url = wikiPage.url
	except Exception as e:
		print e
		artist_error += 1

	artist_data.WikiWordCount = wordcount
	artist_data.URL = url
	artist_df.iloc[i,:] = artist_data

print "Artists with error: ", str(artist_error)

artist_df.to_csv('billboard_artist_info.csv', sep=',', index=False)