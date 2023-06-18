import Ieee
import GoogleScholar
import ScienceDirect

'''
ieeeObject = Ieee.Ieee()
file = ieeeObject.read('IEEE.csv',header_activation=True)
file = ieeeObject.convert(file)
print(file.shape)
print(file.iloc[:,4])
'''
'''
googlescholarObject = GoogleScholar.GoogleScholar()
file = googlescholarObject.read('Google_Scholar.csv',header_activation=True)
file = googlescholarObject.convert(file)
print(file.shape)
print(file)
'''
sciencedirectObject = ScienceDirect.ScienceDirect()
file = sciencedirectObject.read('ScienceDirect.txt')
print(file)




