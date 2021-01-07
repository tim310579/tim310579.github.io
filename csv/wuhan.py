import pandas as pd
import datetime

df = pd.read_csv('covid-19.txt')

dates = list(df.columns)
#dates2 = dates
i=0
#print(dates[0])
for item in dates:
    if i > 3:
        month, day, year = item.split('/')
        #print(month, day, year)
        dates[i] = str(year)+'/'+str(month)+'/'+str(day)
    i = i+1
#print(dates)
df.columns = dates
df_2 = df.copy()
for i in range(5, df.shape[1]):
    for j in range(0, len(df)):
        df_2.iat[j, i] = df.iat[j, i] - df.iat[j,i-1]
        #print(df.iat[j,i], df.iat[j,i-1], df.iat[j, i] - df.iat[j,i-1])
df_2.to_csv('covid_19-confirmed_global.csv', index=False)
