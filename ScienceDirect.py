import pandas as pd
import numpy as np


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
           
        return file

        
    
    