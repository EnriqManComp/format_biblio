import pandas as pd
import utility
import numpy as np

class Ieee():
           
    def read(self,file_dir,header_activation):
        if not header_activation:
            file = pd.read_csv(file_dir,header=None,delimiter=',')
        file = pd.read_csv(file_dir,delimiter=',')
        return file
    def convert(self,file):
        new_file = pd.concat([file.iloc[:,0:2],file.iloc[:,5],file.iloc[:,16],file.iloc[:,28]],axis=1)
        new_file.columns = ['Title','Authors','Year','Keyword','Publisher']
        new_file = utility.conform(new_file,';')
        return new_file

class GoogleScholar():

    def read(self,file_dir,header_activation):
        if not header_activation:
            file = pd.read_csv(file_dir,header=None,delimiter=',')
        file = pd.read_csv(file_dir,delimiter=',')
        return file
    def convert(self,file):
        
        new_file = pd.concat([file.iloc[:,4],file.iloc[:,3],file.iloc[:,11]],axis=1)
        new_file.columns = ['Title','Authors','Year']
        
        return new_file
    
class ScienceDirect():
    
    def fix(self,line):
        value = line.split('{')[-1]
        value = value.split('}')[0]
        value = pd.Series(value)        
        return value        
        
    def read(self,file_dir):        
        file = pd.DataFrame([])
        file_column = pd.Series([])       
        with open(file_dir) as file_:
            file_lines = file_.readlines()
        
        for file_line in file_lines:
            if len(file_line) > 3:
                field = file_line.split()[0]
                if field == 'title':
                    value = self.fix(file_line)
                    file_column = pd.concat([file_column,value])                    
                if field == 'author':
                    value = self.fix(file_line) 
                    file_column = pd.concat([file_column,value])                    
                if field == 'year':
                    value = self.fix(file_line) 
                    file_column = pd.concat([file_column,value])                    
                if field == 'keywords':
                    value = self.fix(file_line)
                    file_column = pd.concat([file_column,value])                    
                if field == 'journal':
                    value = self.fix(file_line) 
                    file_column = pd.concat([file_column,value])                    
                if file_column.shape[0] == 5:
                    file_column_temp = pd.DataFrame(file_column)
                    file_column_temp = file_column_temp.T
                    file = pd.concat([file,file_column_temp],axis=0)
                    file_column = pd.Series([])                
        new_file = pd.concat([file.iloc[:,0],file.iloc[:,3],file.iloc[:,2],file.iloc[:,4],file.iloc[:,1]],axis=1)
        new_file.columns = ['Title','Authors','Year','Keyword','Publisher']
        new_file = utility.conform(new_file,',')
        return new_file