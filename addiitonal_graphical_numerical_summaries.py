import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Auto.csv")

print(df.columns)

# fig, ax  = plt.subplots(figsize = (8,8))
# ax.plot(df["horsepower"],df["mpg"],"o")
# plt.show()



#### An alternative way to do it is
# ax = df.plot.scatter("horsepower","mpg")
# ax.set_title("Horsepoper vs MPG")
# fig = ax.figure
# fig.savefig("horsepowervsmpg.png")
# plt.show()


#### 3rd method
fig , axes = plt.subplots(ncols=3, figsize =(15, 5))
df.plot.scatter('horsepower', 'mpg', ax=axes [1])
plt.show()
