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

df_2 = df_2.drop(columns=['Province/State', 'Lat', 'Long'])
'''
i=0
tmp=0
for i in range(1, len(df_2)-1):

    #print(df_2.iat[i,0], df_2.iat[i+1,0], i)
    if df_2.iat[i,0] == df_2.iat[i+1,0]:
        for j in range(1, df_2.shape[1]):
            df_2.iat[i, j] = df_2.iat[i, j]+df_2.iat[i+1,j]
        df_2 = df_2.drop([i+1])
        #i=i-1
    i=i+1
    '''
print(df_2.iat[0,0])
df_2.to_csv('covid_19-confirmed_global.csv', index=True)

df_2=df_2.T
print(df_2)
dates.remove('Province/State')
dates.remove('Country/Region')
dates.remove('Lat')
dates.remove('Long')
print(len(df_2), len(dates))
#df_2['date']=dates
df_2.to_csv('covid_19-confirmed_global.csv', index=True)
