import pandas as pd
import datetime
import numpy as np

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
#print(len(df_2), len(dates))
#df_2['date']=dates

Africa = ['Algeria',
          'Cabo Verde',
          'Central African Republic',
          'Comoros',
          'Congo (Brazzaville)',
          'Congo (Kinshasa)',
          'Cote d Ivoire',
          'Eswatini',
          'Guinea-Bissau',
          'Mali',
          'Rwanda',
          'Sierra Leone',
          "Cote d'Ivoire",
'Angola',
'Benin',
'Botswana',
'Burkina Faso',
'Burundi',
'Cameroon',
'Cape Verde',
'Central Africa',
'Chad',
'Comor',
'Democratic Republic of Congo',
'the republic of Congo',
'Ivory coast',
'Djibouti',
'Egypt',
'Equatorial Guinea',
'Eritrea',
'Ethiopia',
'Gabon',
'Gambia',
'Ghana',
'Guinea',
'Guinea Bissau',
'Kenya',
'Lesotho',
'Liberia',
'Libya',
'Madagascar',
'Malawi',
'Marley',
'Mauritania',
'Mauritius',
'Morocco',
'Western Sahara',
'Mozambique',
'Namibia',
'Niger',
'Nigeria',
'Reunion',
'Luanda',
'Sao Tome and Principe',
'Senegal',
'Seychelles',
'Lion Rock',
'Somalia',
'South Africa',
'Sudan',
'South Sudan',
'Swadini',
'Tanzania',
'Togo',
'Tunisia',
'Uganda',
'Zambia',
'Zimbabwe',
'Tunisia',
'Uganda',
'Sahrawi Arab Democratic Republic',
'Zambia',
'Zimbabwe',
'Somaliland',
'South Sudan']

Asia = ['Taiwan*',
        'Afghanistan',
        'Diamond Princess',
        'Korea, South',
        'Kyrgyzstan',
        'Armenia',
        'Qatar',
        'Tajikistan',
        'Timor-Leste',
        'Uzbekistan',
        'West Bank and Gaza',
'Azerbaijan',
'Burma',
'Bahrain',
'Bangladesh',
'China',
'Bhutan',
'Brunei',
'Cambodia',
'Christmas Island',
'Cocos (Keeling) Islands',
'Cyprus',
'Georgia',
'India',
'Indonesia',
'Iran',
'Iraq',
'Israel',
'Japan',
'Jordan',
'Kazakhstan',
'Korea',
'Korea',
'Kuwait',
'Kyrgyz',
'Laos',
'Lebanon',
'Malaysia',
'Maldives',
'Mongolia',
'Myanmar',
'Nepal',
'Oman',
'Pakistan',
'Palestine',
'Philippines',
'Kada',
'Russia',
'Saudi Arabia',
'Singapore',
'Sri Lanka',
'Syria',
'Tajik',
'Thailand',
'East Timor',
'Turkey',
'Turkmenistan',
'United Arab Emirates',
'Uzbek',
'Vietnam',
'Yemen',
'Abkhazia',
'Republic of China',
'Alzach',
'Northern Cyprus',
'South Ossetia',
'Akrotiri and Dekella']

Europe=['Helsinki',
        'Czechia',
        'Holy See',
        'Malta',
        'North Macedonia',
'France',
'Bosnia and Herzegovina',
'Germany',
'Gibraltar',
'Greece',
'Guernsey',
'Hungary',
'Iceland',
'Ireland',
'Isle of Man',
'Italy',
'Jersey',
'Latvia',
'Liechtenstein',
'Lithuania',
'Luxembourg',
'Macedonia',
'Maltese',
'Moldova',
'Monaco',
'Montenegro',
'Netherlands',
'Norway',
'Poland',
'Portugal',
'Romania',
'Russia',
'San Marino',
'Serbia',
'Slovakia',
'Slovenia',
'Spain',
'Svalbard',
'Sweden',
'Switzerland',
'Ukraine',
'United Kingdom',
'Vatican',
'Kosovo',
'Along the Nest River',
'Donnetsk',
'Lugansk',
'Aland Islands',
'Albania',
'Andorra',
'Austria',
'Belarus',
'Belgium',
'Poch',
'Bulgaria',
'Croatia',
'Czech Republic',
'Denmark',
'Estonia',
'Faroe Islands',
'Finland']

America=['Anguilla',
         'El Salvador',
         'Grenada',
         'MS Zaandam',
         'US',
'Antigua and Barbuda',
'Aruba',
'Bahamas',
'Barbados',
'Belis',
'Belize',
'Bermuda',
'British Virgin Islands',
'Canada',
'Cayman Islands',
'Clipperton Island',
'Costa Rica',
'Cuba',
'Gulaso',
'Dominica',
'Dominican Republic',
'Salvador',
'Greenland',
'Granada',
'Guadeloupe',
'Guatemala',
'Haiti',
'Honduras',
'Jamaica',
'Martinique',
'Mexico',
'Mongera',
'Navassa Island',
'Nicaragua',
'Panama',
'Puerto Rico',
'Saint Barthélemy',
'Saint Kitts and Nevis',
'Saint Lucia',
'Saint Martin',
'Saint-Pierre and Miquelon',
'Saint Vincent and the Grenadines',
'Trinidad and Tobago',
'Turks and Caicos Islands',
'United States',
'U.S. Virgin Islands',
'Sint Maarten',
'Bonech',
'Saint Yudasius',
'Sabah',
'Argentina',
'Bolivia',
'Brazil',
'Chile',
'Colombia',
'Ecuador',
'Falkland Islands',
'French Guyana',
'Guyana',
'Paraguay',
'Peru',
'Suriname',
'Uruguay',
'Venezuela']

Oceania=['American Samoa',
         'Vanuatu',
'Australia',
'Baker Islands',
'Island',
'Fiji',
'French Polynesia',
'Guam',
'Howland Island',
'Garvis i.',
'Johnston Island',
'Kingman Reef',
'Giribas',
'Marshall Islands',
'Micronesia',
'Midway island',
'Noru',
'New Caledonia',
'New Zealand',
'Niue',
'Norfolk Island',
'Northern Mariana Islands',
'Palau',
'Pamela atoll',
'Papua New Guinea',
'Pitcairn Islands',
'Samoa',
'Solomon Islands',
'Tokelau',
'Tonga',
'Tuvalu',
'Vanado',
'Wake Island',
'Wallis and Futuna Islands']

for i in range(df_2.shape[1]):
    if df_2.iat[0, i] in Africa:
        #print("find 1")
        df_2.iat[0, i] = "Africa"
    elif df_2.iat[0, i] in Asia:
        df_2.iat[0, i] = "Asia"
    elif df_2.iat[0, i] in Europe:
        df_2.iat[0, i] = "Europe"
    elif df_2.iat[0, i] in America:
        df_2.iat[0, i] = "America"
    elif df_2.iat[0, i] in Oceania:
        df_2.iat[0, i] = "Oceania"
    else:
        print(df_2.iat[0, i], i)
    
df_2.to_csv('covid_19-confirmed_global.csv', index=True)

df_final=pd.DataFrame(0, index=range(0,350),columns = ['Africa', 'Asia', 'Europe', 'America', 'Oceania'])

#df_final.columns = ['Africa', 'Asia', 'Europe', 'America', 'Oceania']
#df_final['Africa'] = df_final['Africa'].astype('int')
for i in range(df_2.shape[1]):
    for j in range(1, len(df_2)):
        if df_2.iat[0,i]=="Africa":
            df_final.iat[j-1,0] = df_final.iat[j-1,0] + df_2.iat[j,i]
        elif df_2.iat[0,i]=="Asia":
            df_final.iat[j-1,1] = df_final.iat[j-1,1] + df_2.iat[j,i]
        elif df_2.iat[0,i]=="Europe":
            df_final.iat[j-1,2] = df_final.iat[j-1,2] + df_2.iat[j,i]
        elif df_2.iat[0,i]=="America":
            df_final.iat[j-1,3] = df_final.iat[j-1,3] + df_2.iat[j,i]
        elif df_2.iat[0,i]=="Oceania":
            df_final.iat[j-1,4] = df_final.iat[j-1,4] + df_2.iat[j,i]
#cols=[1,2,3,4,5]
#df_final = df_final[[cols]]
print(df_final)
df_final.to_csv('covid_19-confirmed_global_continent.csv', index=True)

