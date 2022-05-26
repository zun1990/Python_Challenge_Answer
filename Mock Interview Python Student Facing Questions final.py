#!/usr/bin/env python
# coding: utf-8

# <h3> Mock Interview Python Screening test </h3>
# 

# In[34]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
dataframe = pd.read_csv('adult_census_data.csv')
dataframe.head(10)


# In[35]:


print(dataframe.isna().sum())


# <b> Q1. After importing the adult_census_data.csv file, please filter this to include only the following criteria: </b>
# <p>
# 
# <li> State-Gov</li>
# <li> Bachelors </li>
# <li> Never-Married </li>
# <li> Adm-Clerical </li> 
# <li> Not-in-familiy </li>
# <li> White </li>
# <li> Male </li> 
# <li> United States </li>
# <li> <=50K </li> 
# 
# <b> Feel free to any method to complete this tasks. However, we recommend you use either list filtering [], or .loc to complete this task.</b>

# <b> Put your code below </b>

# In[36]:


df = dataframe[[' State-gov',' Bachelors',' Never-married',' Adm-clerical', ' Not-in-family', ' White', ' Male',' United-States', ' <=50K']]
print(df.head(10))


# <b> Currently, the dataframe you are using has the following column names: </b>
# 
# [' State-gov', ' Bachelors', ' Never-married',
#        ' Adm-clerical', ' Not-in-family', ' White', ' Male', ' United-States', ' <=50K']
#        
#      
# <b> Q2. Please re-name all the newly filtered columns in the pandas DataFrame to the following: </b>
# 
# Employment Type, Degree Status, Marriage-Status, Job-Role, Family-Role, Ethnicity, Gender, Country, Earnings
# 
# E.g. State-Gov becomes Employment Type, Bachelors becomes Degree Status, etc.

# <b> Put your code below </b>

# In[37]:


df_1 = df.rename(columns = {' State-gov':'Employment Type', ' Bachelors':'Degree Status', ' Never-married':'Marriage-Status', ' Adm-clerical':'Job-Role', ' Not-in-family':'Family-Role', ' White':'Ethnicity', ' Male':'Gender', ' United-States':'Country', ' <=50K':'Earnings'})
print(df_1)


# <b> Q3. The Job Role Columns holds the job information for each individual in this census snapshot. Using this column, create a Bar Chart that shows the count of 'Unique' Jobs per Job Group in the "Job-Role" Column in ascending order, as per the provided image below </b>
# 

# <b> Put your code below </b>

# In[38]:


count_unique_job = df_1['Job-Role'].value_counts()
count_unique_job.plot(kind = 'bar')
plt.xlabel('Job Roles')
plt.ylabel('No of jobs')
plt.title ('No of Unique jobs per Group')
plt.show()


# <b> Q4. Please create two bar plots as per below that show:
#     
#     1) The number of individuals who have a High School Graduate Diploma AND earn <=50K in the United States
#     2) The number of individuals who have a High School Graduate Diploma AND earn >50K in the United States 
# 
# Please note you will be looking specifically at the *Job Role* column

# <b> Put Your Code Below </b>

# In[39]:


# first condition
df_2 = df_1[(df_1['Degree Status'] == ' HS-grad') & (df_1['Country'] == ' United-States') & (df_1['Earnings'] ==' <=50K')]
first_condition = df_2['Job-Role'].value_counts()
first_condition.plot(kind = 'bar')
plt.xlabel('Job Roles')
plt.ylabel('Number of Individuals')
plt.title('Number of individuals earnings <=50K')
plt.show()


# In[40]:


# Second Condition
df_3 = df_1[(df_1['Degree Status'] == ' HS-grad') & (df_1['Country'] == ' United-States') & (df_1['Earnings'] ==' >50K')]
second_condition = df_3.value_counts('Job-Role')
second_condition.plot(kind = 'bar')
plt.ylabel('Number of Individuals')
plt.title('Number of individuals earnings >50K')
plt.show()


# 
# 

# <H2> Challenge Question </H2>
# 
# <b> Q5. Which Job Role has the highest <i> proportion </i> of individuals who earn >50K? </b>

# <b> Put your code below </b>

# In[41]:


df_4 = df_1[df_1['Earnings'] ==' >50K']
c1 = df_4['Job-Role'].value_counts(normalize = True)
print(c1)

