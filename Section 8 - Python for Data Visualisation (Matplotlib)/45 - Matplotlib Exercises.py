import matplotlib.pyplot as plt
import numpy as np
import os

# Change Working Directory
os.chdir('./Section 8 - Python for Data Visualisation (Matplotlib)')

# Data
x = np.arange(0,100)
y = x*2
z = x**2

# Command to show plot would be plt.show()

def saveImg(fig,name:str):
    fig.savefig(f"results/{name}.png")

# Exercise 1
fig_1 = plt.figure()
ax_1 = fig_1.add_axes([0,0,1,1])
ax_1.set_title('Exercise 1')
ax_1.plot(x,y)
plt.show()
saveImg(fig_1,"Exercise 1")

# Exercise 2
fig_2 = plt.figure()
ax_2_1 = fig_2.add_axes([0,0,1,1])
ax_2_2 = fig_2.add_axes([0.2,0.5,0.2,0.2])
ax_2_1.plot(x,y)
ax_2_2.plot(x,y)
plt.show()
saveImg(fig_2,"Exercise 2")

# Exercise 3
fig_3 = plt.figure()
ax_3_1 = fig_3.add_axes([0,0,1,1])
ax_3_2 = fig_3.add_axes([0.2,0.5,0.4,0.4])

# Propeties for Main Figure
ax_3_1.set_xlabel('X')
ax_3_1.set_ylabel('Z')

# Properties for Inserted Figure
ax_3_2.set_xlim([20,22])
ax_3_2.set_ylim([30,50])
ax_3_2.set_title('zoom')
ax_3_2.set_xlabel('X')
ax_3_2.set_ylabel('Y')

# Plot Values
ax_3_1.plot(x,z)
ax_3_2.plot(x,y)

plt.show()
saveImg(fig_3,"Exercise 3")

# Exercise 4
fig_4, ax_4 = plt.subplots(nrows=1,ncols=2)
plt.tight_layout()

ax_4_1 = ax_4[0]
ax_4_2 = ax_4[1]

# Plot Values
ax_4_1.plot(x,y,color='blue',ls='--')
ax_4_2.plot(x,z,color='red')

plt.show()
saveImg(fig_4,"Exercise 4 (a)")

# Exercise 4 Part 2
fig_4b, ax_4b = plt.subplots(nrows=1,ncols=2,figsize=(8,2))
plt.tight_layout()

ax_4b_1 = ax_4b[0]
ax_4b_2 = ax_4b[1]

# Plot Values
ax_4b_1.plot(x,y,color='blue',ls='--')
ax_4b_2.plot(x,z,color='red')

plt.show()
saveImg(fig_4b,"Exercise 4 (b)")




