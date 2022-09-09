from inspect import Attribute
from operator import index
from tempfile import TemporaryFile
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os

# Save Image Function
def saveFig(fig,name:str):
    try:
        fig.savefig(f"results/{name}.png")
    except AttributeError:
        fig.get_figure().savefig(f"results/{name}.png")

# Change Working Directory to current folder
os.chdir('Section 9 - Python for Data Visualisation (Seaborn)')

sns.set_style('whitegrid')  # Setting the Default Plot Style

# Check for titanic DataFrame. Saved as csv to avoid long loading times

titanic = pd.DataFrame()

try:
    titanic = pd.read_csv('data/titanic.csv')
except FileNotFoundError:
    titanic = sns.load_dataset('titanic')
    titanic.to_csv('data/titanic.csv',index=False)
    print('File saved!')

print(titanic.head())

# Exercise 1
fig1 = sns.jointplot(x='fare',y='age',data=titanic)
saveFig(fig=fig1,name="Question 1")
plt.show()

# Exercise 2
fig2 = sns.distplot(titanic['fare'],kde=False,color='red')
saveFig(fig2,"Question 2")
plt.show()

# Exercise 3
fig3 = sns.boxplot(x='class',y='age',data=titanic,order=['First','Second','Third'])
saveFig(fig3,"Question 3")
plt.show()

# Exercise 4
fig4 = sns.swarmplot(x='class',y='age',order=['First','Second','Third'],data=titanic)
saveFig(fig4,"Question 4")
plt.show()

# Exercise 5
fig5 = sns.countplot(x='sex',data=titanic)
saveFig(fig5,"Question 5")
plt.show()

# Exercise 6
tc = titanic.corr()
fig6 = sns.heatmap(tc,cmap='coolwarm')
saveFig(fig6,"Question 6")
plt.show()

# Exercise 7
fig7 = sns.FacetGrid(data=titanic,col='sex')
fig7.map(plt.hist,'age')
saveFig(fig7,'Question 7')
plt.show()







