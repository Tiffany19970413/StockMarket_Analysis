#!/usr/bin/env python
# coding: utf-8

# In[124]:


import pandas_datareader as pdr #從pdr中導入pandas_datareader抓取股票的api
import datetime #設定開始、結束日期
import matplotlib.pyplot as plt #視覺化開盤價、收盤價，plt自命名 
import numpy as np #股票市場分析的線性代數、統計(返回陣列)
get_ipython().run_line_magic('matplotlib', 'inline')

start = datetime.datetime(2015,1,1)#開始日
end = datetime.datetime(2020,1,1)#結束日

#股票 = 從yahoo股市擷取('股票名稱','開始日','結束日')
google = pdr.get_data_yahoo('GOOGL',start,end)
facebook = pdr.get_data_yahoo('FB',start,end)
instagram = pdr.get_data_yahoo('IG',start,end)


# In[125]:


#下載csv檔，方便jupyter查閱、處理數據
google.to_csv('GOOGL_stock.csv')
facebook.to_csv('FB_stock.csv')
instagram.to_csv('FB_stock.csv')


# In[126]:


google.head(-1)


# In[127]:


"""總市值表 預防被股價圖誤導 查詢個股真正價值"""
#'開盤價'代替'交易總資金'(非實際市值)，求直覺表示

google['Market value'] = google['Open'] * google['Volume']
google.head()


# In[128]:


facebook.head(-1)


# In[129]:


instagram.head(-1)


# In[130]:


"""All of Stock 走勢圖 抓取基本資料 欄位標籤及數據"""
#matplotlib.pyplot->plot(),plt()
#plot.label('')預設英文
#x軸已由Datetime.date帶入

#擷取 All of Stock 欄位[標籤'Open']，繪出plot(略象限xy,圖形化字串label='開盤數據',等比圖框figsize=尺寸(寬，高))
google['Open'].plot(label='GOOGL price',figsize=(10,5))#放大重點股票
facebook['Open'].plot(label='FB price') 
instagram['Open'].plot(label='IG price') 

#繪圖
plt.legend() #圖表說明，預設英文，放置最前
plt.title('All of Stock Price',fontsize = 16) #標題
plt.ylabel('Price',fontsize = 14) #y軸名稱
plt.show() #秀圖表框，放置最後


# In[134]:


"""All of Stock 成交量 依據走勢圖數據"""
#matplotlib.pyplot->plot(),plt()
#plot.label('')預設英文
#x軸已由Datetime.date帶入

#擷取 All of Stock 欄位[標籤'Open']，繪出plot(略象限xy,圖形化字串label='成交量數據',等比圖框figsize=尺寸(寬，高))
google['Volume'].plot(label='GOOGL',figsize=(17,9))#放大重點股票
facebook['Volume'].plot(label='FB')
instagram['Volume'].plot(label='IG') 

#繪圖
plt.legend() #圖表說明，預設英文，放置最前
plt.ylabel('All of Volume Trade',fontsize = 16) #y軸名稱
plt.show()#秀圖表框，放置最後


# In[135]:


"""google總市值 預防被股價圖誤導 查詢個股真正價值"""
#'開盤價'代替'交易總資金'(非實際市值)，求直覺表示
#Market value無效重複欄位

google['Total Market value'] = google['Open'] * google['Volume'] #總市值Total Market value = 開盤價open *交易量Volume
google.head(-1)


# In[136]:


"""facebook總市值 預防被股價圖誤導 查詢個股真正價值"""
#'開盤價'代替'交易總資金'(非實際市值)，求直覺表示
#Market value無效重複欄位

facebook['Total Market value'] = facebook['Open'] * facebook['Volume'] #總市值Total Market value = 開盤價open *交易量Volume
facebook.head(-1)


# In[137]:


"""instagram總市值 預防被股價圖誤導 查詢個股真正價值"""
#'開盤價'代替'交易總資金'(非實際市值)，求直覺表示
#Market value無效重複欄位

instagram['Total Market value'] = instagram['Open'] * instagram['Volume'] #總市值Total Market value = 開盤價open *交易量Volume
instagram.head(-1)


# In[138]:


"""總市值圖"""
#matplotlib.pyplot->plot(),plt()
#plot.label('')預設英文
#x軸已由Datetime.date帶入

#擷取 All of Stock 欄位[標籤'Open']，繪出plot(略象限xy,圖形化字串label='成交量數據',等比圖框figsize=尺寸(寬，高))
google['Total Market value'].plot(label='GOOGL',figsize=(15,7))#放大重點股票
facebook['Total Market value'].plot(label='FB') 
instagram['Total Market value'].plot(label='IG')

#繪圖
plt.legend() #圖表說明，預設英文，放置最前
plt.ylabel('Total Market value',fontsize = 16) #y軸名稱
plt.show()#秀圖表框，放置最後


# In[139]:


"""投資策略指標 注意最大出量"""
google['Total Market value'].argmax() #numpy.argmax元組型(陣列, 指定軸=None, 指定插入資料=None)-->沿轴最大值的數據


# In[140]:


"""擷取最大出量的意義"""
#重大消息在ppt
google.iloc[google['Total Market value'].argmax()] #pandas_datareader.iloc[]-->擷取指定行、列的數據


# In[141]:


"""計算google 7天,90天與200天的移動平均線"""
#擷取日線的收盤價數據，rolling(數據參數)
google['MA_7'] = google['Open'].rolling(7).mean()
google['MA_90'] = google['Open'].rolling(90).mean()
google['MA_200'] = google['Open'].rolling(200).mean()

google['Open'].plot(figsize=(15,7))#先畫收盤價的尺寸圖

#圖表說明的文字
google['MA_7'].plot(label='MA_7')
google['MA_90'].plot(label='MA_90')
google['MA_200'].plot(label='MA_200')

plt.legend() #圖表說明，預設英文，放置最前
plt.title('google MACD',fontsize = 16) #標題
plt.show()#秀圖表框，放置最後


# In[142]:


"""計算facebook 7天,90天與200天的移動平均線"""
#擷取日線的收盤價數據，rolling(數據參數)
facebook['MA_7'] = facebook['Open'].rolling(7).mean()
facebook['MA_90'] = facebook['Open'].rolling(90).mean()
facebook['MA_200'] = facebook['Open'].rolling(200).mean()

facebook['Open'].plot(figsize=(15,7))#先畫收盤價的尺寸圖

#圖表說明的文字
facebook['MA_7'].plot(label='MA_7')
facebook['MA_90'].plot(label='MA_90')
facebook['MA_200'].plot(label='MA_200')

plt.legend() #圖表說明，預設英文，放置最前
plt.title('facebook MACD',fontsize = 16) #標題
plt.show()#秀圖表框，放置最後


# In[146]:


"""計算instagram 7天,90天與200天的移動平均線"""
#擷取日線的收盤價數據，rolling(數據參數)
instagram['MA_7'] = instagram['Open'].rolling(7).mean()
instagram['MA_90'] = instagram['Open'].rolling(90).mean()
instagram['MA_200'] = instagram['Open'].rolling(200).mean()

instagram['Open'].plot(figsize=(15,7))#先畫收盤價的尺寸圖

#圖表說明的文字
instagram['MA_7'].plot(label='MA_7')
instagram['MA_90'].plot(label='MA_90')
instagram['MA_200'].plot(label='MA_200')

plt.legend() #圖表說明，預設英文，放置最前
plt.title('instagram MACD',fontsize = 16) #標題
plt.show()#秀圖表框，放置最後


# In[150]:


"""矩陣圖 探討兩個股間存在的依賴關係"""
from matplotlib.pyplot import scatter_matrix
import pandas as pd

social_comp = pd.concat([google['Open'],facebook['Open'],instagram['Open']],axis=1)
social_comp.columns=['GOOGL Open','FB Open','IG Opne']
plt.scatter_matrix(social_comp,figsize=(6,6),hist_kwds={'bins':50})


# In[ ]:




