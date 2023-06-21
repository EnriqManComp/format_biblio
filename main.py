import searcher
import pandas as pd
import utility

ieeeObject = searcher.Ieee()
file_ieee = ieeeObject.read('.\Files\IEEE.csv',header_activation=True)
file_ieee = ieeeObject.convert(file_ieee)

sciencedirectObject = searcher.ScienceDirect()
file_sd = sciencedirectObject.read('.\Files\ScienceDirect.txt')

gsObject = searcher.GoogleScholar()
file_gs = gsObject.read('.\Files\Google_Scholar.csv',header_activation=True)
file_gs = gsObject.convert(file_gs)

file = utility.export_all(file_ieee,file_sd)
file = file.reset_index(drop=True)
file['Title'] = file['Title'].str.upper()
file.iloc[:, 3:-1] = file.iloc[:, 3:-1].fillna('')
file.iloc[:,3:-1] = file.iloc[:,3:-1].applymap(lambda x: x.upper())

df_keywords = pd.concat([file.iloc[:,3],file.iloc[:,4],file.iloc[:,5],file.iloc[:,6],file.iloc[:,7],file.iloc[:,8],file.iloc[:,9]])
df_title = pd.concat([file.iloc[:,0],file_gs.iloc[:,0]])
print(df_title.shape)
df_year = pd.concat([file.iloc[:,2],file_gs.iloc[:,2]])
df_title_year = pd.concat([df_title,df_year],axis=1)



#file_name = 'bibliokeyword.csv'
#df.to_csv(file_name, sep=';', index=False)
file_name = 'bibliotitle_year.csv'
df_title_year.to_csv(file_name, sep=';', index=False)

#file_name = '.\Exported files\IEEEconvert.csv'
#file_ieee.to_csv(file_name, sep=';', index=False)

#file_name = '.\Exported files\ScienceDirectconvert.csv'
#file_sd.to_csv(file_name, sep=';', index=False)




