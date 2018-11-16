import seaborn as sns

tips = sns.load_dataset('tips')

# distribution plot
print(sns.distplot(tips['total_bill']))

# join plot
print(sns.jointplot(x='total_bill', y='tip', data=tips))

# pair plot: comparing each numeric variable
print(sns.pairplot(tips, hue='sex'))

