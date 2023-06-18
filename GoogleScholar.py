import pandas as pd

class GoogleScholar():
    def read(self,file_dir,header_activation):
        if not header_activation:
            file = pd.read_csv(file_dir,header=None,delimiter=',')
        file = pd.read_csv(file_dir,delimiter=',')
        return file
    def convert(self,file):
        return pd.concat([file.iloc[:,4],file.iloc[:,3],file.iloc[:,11]],axis=1)