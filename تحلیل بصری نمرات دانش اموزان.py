import pandas as pd
import matplotlib.pylab as plt
from bidi.algorithm import get_display
from arabic_reshaper import reshape
import seaborn as sns
df = pd.DataFrame({
    "name":["Ali","Sara","Reza","Nilo","Zahra","Hasan","Maryam","Javad"],
    "group":["A","B","A","B","A","B","A","B"],
    "score":[18.5, 14.2, 11.8, 19.3, 16.7, 15.5, 10.4, 15.2],
    "age":[21, 22, 20, 23, 22, 21, 19, 24]
})
# نمودار ستونی میانگین نمره
g = sns.barplot(data=df, x="group",y="score", estimator="mean")
plt.title(get_display(reshape("نمودار ستونی میانگین نمرات")),fontsize=14)
g.figure.set_size_inches(5,5)
plt.show()
print("-----------------------------------------------------------------------")
# نمودار جعبه ای
g = sns.boxplot(data=df,x="group",y="score")
plt.title(get_display(reshape("نمودار جعبه ای")),fontsize=14)
g.figure.set_size_inches(5,5)
plt.show()
print("-----------------------------------------------------------------------")
# نمودار هیستوگرام
g = sns.histplot(data=df,x="score",bins=8)
plt.title(get_display(reshape("نمودار هیستوگرامی")),fontsize=14)
g.figure.set_size_inches(5,5)
plt.show()
print("-----------------------------------------------------------------------")
# نمودار پراکندگی
g = sns.scatterplot(data=df,x="age",y="score",hue="group",style="group")
plt.title(get_display(reshape("نمودار پراکندگی")),fontsize=14)
g.figure.set_size_inches(5,5)
plt.show()