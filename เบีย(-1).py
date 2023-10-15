#Split group
from scipy.stats import ttest_ind
group1 = df_new2[df_new2['Age_Group']=='Middle-age']
group2 = df_new2[df_new2['Age_Group']=='Old-age']
#Create empty list
pvalueList = []
#For loop (change column name each loop)
for columnName in df_new6.columns:
  print(columnName)
  try:
    t, pvalue = ttest_ind(group1[columnName], group2[columnName]) #get pvalue
    pvalueList.append(pvalue) #append p value to your List
  except:
    continue
A2 = sorted(pvalueList)
print(A2)

A2 = sorted(pvalueList)
print(A2)

#ใช้ dataframe เรียงข้อมูลของ columns กับ pvalue