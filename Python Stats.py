#!/usr/bin/env python
# coding: utf-8

# ## Assignment 3 : descriptive stats
# **Author:** Lucretia Maswabela: 216023710 <br>
# **Date:** 14 April 2023 <br>
# **Github url:** https://github.com/LuHmD/Descriptive-statistical-analysis 

# In[8]:


get_ipython().system('pip install opendatasets')
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import opendatasets as od


# In[12]:


nft_df = pd.read_csv("NFT_Sales.csv")


# In[13]:


nft_df.head()


# In[19]:


#Dropping any rows with missing values
nft_df.dropna(inplace=True)


# In[20]:


# Dropping any duplicate rows
nft_df.drop_duplicates(inplace=True)


# In[21]:


nft_df.info()


# In[22]:


nft_df.describe()


# ## Descriptive Stats

# In[23]:


columnmean = ['Sales_USD_cumsum','Active_Market_Wallets_cumsum','Primary_Sales_cumsum','Secondary_Sales_cumsum','Sales_USD','Active_Market_Wallets','Primary_Sales']
mean = nft_df[columnmean].mean()
print('Mean: \n',mean, '\n')


# In[24]:


columnmedian =["Sales_USD_cumsum", "Sales_USD"]
median = nft_df[columnmedian].median()
print('Median: \n' , median, '\n')


# In[25]:


columnmode =["Sales_USD_cumsum"]
mode = nft_df[columnmode].mode()
print('Mode: \n' , mode, '\n')


# In[21]:


columnsd =["Sales_USD_cumsum", "Sales_USD"]
standard_deviation = nft_df[columnsd].std()
print('Standard deviation: \n' , standard_deviation, '\n')


# In[22]:


columnrange =['Sales_USD_cumsum','Active_Market_Wallets_cumsum','Primary_Sales_cumsum','Secondary_Sales_cumsum','Sales_USD','Active_Market_Wallets','Primary_Sales']
rangev = nft_df[columnsd].max() - nft_df[columnsd].min()
print('Range: \n' , rangev, '\n')


# In[23]:


columnmin =['Sales_USD_cumsum','Active_Market_Wallets_cumsum','Primary_Sales_cumsum','Secondary_Sales_cumsum','Sales_USD','Active_Market_Wallets','Primary_Sales']
minimum = nft_df[columnmin].min()
print('Minimum: \n' , minimum, '\n')


# In[24]:


columnmax =['Sales_USD_cumsum','Active_Market_Wallets_cumsum','Primary_Sales_cumsum','Secondary_Sales_cumsum','Sales_USD','Active_Market_Wallets','Primary_Sales']
maximum = nft_df[columnmax].max()
print('Maximum: \n' , maximum, '\n')


# In[25]:


columnsum =['Sales_USD_cumsum','Active_Market_Wallets_cumsum','Primary_Sales_cumsum','Secondary_Sales_cumsum','Sales_USD','Active_Market_Wallets','Primary_Sales']
sum = nft_df[columnsum].sum()
print('Sum: \n' , sum, '\n')


# In[26]:


columnvariance =['Sales_USD_cumsum','Active_Market_Wallets_cumsum','Primary_Sales_cumsum','Secondary_Sales_cumsum','Sales_USD','Active_Market_Wallets','Primary_Sales']
variance = nft_df[columnvariance].var()
print('Variance: \n' , variance, '\n')


# In[27]:


IQR = nft_df.describe(percentiles=[.25, .5, .75])
q1 = IQR.loc['25%']
q3 = IQR.loc['75%']
iqr = q3 - q1
print('Inter-quartile Range: \n' ,iqr, '\n')


# In[28]:


columnkurtosis =['Sales_USD_cumsum','Active_Market_Wallets_cumsum','Primary_Sales_cumsum','Secondary_Sales_cumsum','Sales_USD','Active_Market_Wallets','Primary_Sales']
kurtosis = nft_df[columnkurtosis].kurtosis()
print('Kurtosis: \n', kurtosis, '\n')


# In[29]:


columnskewness =['Sales_USD_cumsum','Active_Market_Wallets_cumsum','Primary_Sales_cumsum','Secondary_Sales_cumsum','Sales_USD','Active_Market_Wallets','Primary_Sales']
skewness = nft_df[columnskewness].skew()
print('Skewness: \n', skewness, '\n')


# In[50]:


columnpercentiles = df.describe(percentiles=[0.25, 0.5, 0.75])
print('Percentiles: \n', columnpercentiles, '\n')


# In[31]:


columnfrequency =['Sales_USD_cumsum','Primary_Sales_cumsum']
frequency = nft_df[columnfrequency].value_counts()
print('Frequency: \n', frequency, '\n')


# ## Data Visualization

# In[32]:


plt.figure(figsize=(12,10))
correlations = nft_df.corr()
sns.heatmap(correlations, center=0, annot=True)


# In[33]:


plt.figure(figsize=(16,5), dpi=100)
plt.plot(nft_df.index,nft_df.Number_of_Sales, color='tab:green')
plt.gca().set(title='Daily NFT Sales.', xlabel='Date', ylabel='NFT')
plt.show()


# In[44]:


plot_df(df, x=nft_df.index, y=nft_df.AverageUSD_cum)
plt.show()


# In[35]:


sns.pairplot(nft_df[1:])


# In[45]:


#
plot_df(df, x=nft_df.index, y=nft_df.Active_Market_Wallets_cumsum, title='Active Market Wallets') 


# In[13]:


# A scatter plot
plt.scatter(nft_df['Sales_USD'], nft_df['Number_of_Sales'])
plt.title('NFT Sales')
plt.xlabel('Total USD Sales')
plt.ylabel('Number of Sales')
plt.show()


# In[14]:


# A histogram of the "Sales_USD" column
plt.hist(nft_df["Sales_USD"], bins=50)

plt.title("Distribution of NFT Sales in USD")
plt.xlabel("Sales in USD")
plt.ylabel("Frequency")

plt.show()


# In[ ]:





# ## Conclusion:
# 
# *Based on the data presented, it appears that NFTs have gained exponential adoption, but there may be a certain demographic or age group that is more interested in them. It also seems that many people are using multiple wallets, as the number of transactions does not directly correspond to the number of active wallets in the market. However, it is important to note that the data has limitations and may reveal more information in the future.
# 
# Overall, the data suggests that although NFTs are rapidly gaining popularity, there is still significant room for growth and a large portion of the population has yet to be introduced to the concept. Therefore, there is potential for the NFT market to expand and attract more users in the future.

# ## Reflection:
# 
# *Working with Excel and Python for statistical analysis has been a valuable learning experience for me. Excel was an excellent starting point as it had built-in formulas that made it easy for me to learn and implement statistics quickly. I found it fast to work with as the formulas were intuitive, and once I got to grips with them, I was able to use them confidently.
# On the other hand, Python was more complex to learn and understand. I had to start by finding the right data to use and then access the same CSV file in Jupyter Notebook, which took some time. It was not always straightforward to do the stats, but with practice, I was able to navigate the environment and use Python for statistical analysis.
# Jupyter Notebook was a new experience for me, and I found it took some time to understand the environment fully. However, with a bit of practice, I was able to get the hang of it, and I appreciate how powerful it can be for data analysis and visualization.
# 
# In the future, I would definitely use both Excel and Python for statistical analysis. However, I plan to spend more time improving my Python stats skills to understand it better for future statistical projects.
# If I could redo the assignment again, I would focus on improving the visual aesthetics of my data analysis. I realized that I lacked some knowledge on the appropriate diagrams to use for my set of data, which would have made it more readable and easier to analyze. By improving my understanding of data visualization, I can more effectively communicate my findings and make my data analysis more impactful.
# 
# Overall, working with Excel and Python has been an excellent learning experience, and I look forward to using both tools for future data analysis projects. With practice and continued learning, I believe I can become more skilled at using these tools and improve my ability to analyze and communicate complex data sets.
# Before embarking on these assignments, I had gaps in my programming and statistics knowledge. I had not used Excel for statistical analysis before and had limited experience with Python. Additionally, I was not familiar with the statistical formulas and techniques required for analyzing data.
# 
# However, through working on these assignments, I have been able to improve my skills and knowledge in both areas. I was able to gain a better understanding of Python and how to perform statistical analysis using libraries like Pandas and Numpy.
# Furthermore, these assignments have helped me gain a deeper understanding of statistical analysis in general. I have learned how to choose the appropriate statistical tests for different types of data, how to interpret the results, and how to present them in a clear and concise manner.
# 
# In conclusion, the assignments using both Excel and Python have improved my programming and statistical knowledge significantly. While I still have gaps in my knowledge and room for improvement, I feel more confident in my ability to perform basic statistical analysis using these tools. Moving forward, I plan to continue working with both Excel and Python to improve my skills and tackle more complex statistical analysis tasks.
# 

# In[ ]:




