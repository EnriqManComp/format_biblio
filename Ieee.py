import pandas as pd


class Ieee():
    
        
    def read(self,file_dir,header_activation):
        if not header_activation:
            file = pd.read_csv(file_dir,header=None,delimiter=',')
        file = pd.read_csv(file_dir,delimiter=',')
        return file
    def convert(self,file):
        return pd.concat([file.iloc[:,0:2],file.iloc[:,5],file.iloc[:,16],file.iloc[:,21:23],file.iloc[:,28]],axis=1)
    
        

