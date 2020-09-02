from pandas import *
import numpy
import matplotlib.pyplot as plt

data = { 
    'name': ['Khem', 'som', 'Tou', 'Boey'],
    'age': [20, 30, 28, 28],
    'gender': ['Male', 'Female', 'Male', 'Male'],
    'money': [200 , 500 , 900 ,100]

}

#kind='scatter' กราฟแบบจุด
df = DataFrame(data)
df.plot(kind='scatter', x='name', y='age', color='red') 
plt.show()

#kind='scatter' กราฟแบบเส้น
ax = plt.gca()
df.plot(kind='line', x='name', y='age', color='green', ax=ax) 
df.plot(kind='line', x='name', y='money', color='pink', ax=ax)
plt.show()

'''
data2 = ['20', '50','60', '70']

x = pandas.Series(data2)
print(x)
'''