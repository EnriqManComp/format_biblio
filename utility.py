import pandas as pd
import numpy as np

def count_keywords(file,sign):
    keywords = file.loc[:,'Keyword']
    max_keywords = 0
    for i in range(file.shape[0]): 
        key = keywords.iloc[i]
        key = str(key)
        if key != 'nan':
            splited_keywords = key.split(sign)
            if (len(splited_keywords)>max_keywords):
                max_keywords = len(splited_keywords)
    return max_keywords
        

def split_keywords(keywords,sign):
    keywords = str(keywords)
    if keywords == 'nan':
        return keywords,True           
    splited_keywords = keywords.split(sign)
    splited_keywords_df = pd.DataFrame([])
    for i in range(len(splited_keywords)):
        splited_keywords_df = pd.concat([splited_keywords_df,pd.Series(splited_keywords[i])],axis=1)
    return splited_keywords_df,False
    
def conform(file,sign):
    max_columns = count_keywords(file,sign)
    print(max_columns)
    df = pd.DataFrame(np.nan, index=range(file.shape[0]), columns=range(max_columns))
    for i in range(df.shape[0]):
        split_keywords_df,empty = split_keywords(file.iloc[i,3],sign)
        if empty == False:
            for j in range(split_keywords_df.shape[1]):
                df.at[i,j] = split_keywords_df.iloc[0,j]
    columns = []
    for i in range(max_columns):
        columns.append('keyword'+str(i+1))
    df.columns = columns    
    new_file = pd.concat([file.iloc[:,0:3].reset_index(drop=True),df,file.iloc[:,-1].reset_index(drop=True)],axis=1)
    return new_file
    
def export_all(file1,file2):
    dim = file1.shape[1] - file2.shape[1]
    choice_max_key = {'1': file1, '2': file2}
    if dim <= 0:
        file_choice = choice_max_key['2']
        columns = file_choice.columns        
    else:
        file_choice = choice_max_key['1']
        columns = file_choice.columns        
    keywords1 = file1.iloc[:,3:-1]
    keywords2 = file2.iloc[:,3:-1]
    df = pd.DataFrame(np.nan, index=range(2*file_choice.shape[0]), columns=range(file_choice.shape[1]-4))
    for i in range(df.shape[0]):
        if i < 20:
            for j in range(keywords1.shape[1]):
                df.at[i,j] = keywords1.iloc[i,j]
        else:
            for j in range(keywords2.shape[1]):
                df.at[i,j] = keywords2.iloc[i-20,j]
    three_field_concat = pd.concat([file1.iloc[:,:3], file2.iloc[:,:3]],axis=0)
    three_field_concat = three_field_concat.reset_index(drop=True)
    last_field_concat = pd.concat([file1.iloc[:,-1], file2.iloc[:,-1]],axis=0)
    last_field_concat = last_field_concat.reset_index(drop=True)
    all_field_concat = pd.concat([three_field_concat,df,last_field_concat],axis=1)
    all_field_concat.columns = columns
    return all_field_concat
    
    






