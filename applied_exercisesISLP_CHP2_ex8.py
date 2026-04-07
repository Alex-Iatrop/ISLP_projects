import pandas as pd
import matplotlib.pyplot  as plt


college = pd.read_csv("College.csv")

print(college.head())


college2 = pd.read_csv("College.csv", index_col=0)
print(college2.head())


college3 = college.rename({"Unnamed: 0": "College"}, axis = 1)

college3 = college3.set_index("College")

college = college3

# print(college.describe())

#Question  d

# pd.plotting.scatter_matrix(college[["Top10perc","Apps","Enroll"]])
# plt.show()

#Question e use of the boxplot() method
# fig, ax = plt.subplots(figsize = (8,8))
# college.boxplot("Outstate", by = 'Private',ax=ax)
# plt.show()

#Question f:
# Create a new qualitative variable, called Elite, by binning the
# Top10perc variable into two groups based on whether or not the
# proportion of students coming from the top 10% of their high
# school classes exceeds 50%.
# My answer  see below
elite_colleges = (college["Top10perc"]>50)
print(college[elite_colleges])
# Books answer
college["Elite"] = pd.cut(college["Top10perc"]/100,[0,0.5,1],labels = ["No","Yes"])
print(college["Elite"].value_counts("Yes"))

print(college.head())


# fig, ax = plt.subplots(figsize = (8,8))
# college.boxplot("Outstate", by="Elite", ax = ax)
# plt.show()

# Question g

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Plot histograms on specific axes
college.hist("Outstate", bins=15, color='blue', alpha=0.7)
# college.set_title('Histogram of Outstate')

college.hist("Accept", bins=15, color='green', alpha=0.7)
# college.set_title('Histogram of Accept')

# plt.tight_layout()
plt.show()