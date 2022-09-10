import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Change to current working directory
os.chdir('Section 10 - Python for Data Visualisation (Pandas Built-In Data Visualisation)')

# Save Figure Function
def saveFig(fig,name:str):
    try:
        fig.savefig(f"results/{name}.png")
    except AttributeError:
        fig.get_figure().savefig(f"results/{name}.png")

# Load DataFrame
df = pd.read_csv('data/df3')

# -- Exercise 1 --
# Set Style
sns.set_style('white')

# Plot
fig1 = df.plot.scatter(x='a',y='b',c='red',s=50,figsize=(12,3))
saveFig(fig1,"Question 1")
plt.show()

# -- Exercise 2 --
fig2 = df['a'].plot.hist()
saveFig(fig2,"Question 2")
plt.show()

# -- Exercise 3 --
# Set Style
plt.style.use('ggplot')

# Plot
fig3 = df['a'].plot.hist(bins=30,alpha=0.5)
saveFig(fig3,"Question 3")
plt.show()

# -- Exercise 4 --
fig4 = df[['a','b']].plot.box()
saveFig(fig4,"Question 4")
plt.show()

# -- Exercise 5 --
fig5 = df['d'].plot.kde()
saveFig(fig5,"Question 5")
plt.show()

# -- Exercise 6 --
fig6 = df['d'].plot.kde(ls='--',lw=3)
saveFig(fig6,"Question 6")
plt.show()