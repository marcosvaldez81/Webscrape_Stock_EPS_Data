##################################

# Marcos Valdez
# I find trading the markets quite interesting. 
# So I decided to make a script to pull EPS data history from a passed in ticker.

##################################


from bs4 import BeautifulSoup
import requests 
import json


ticker = "PSTG"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Safari/537.36'}   
#url = "https://finance.yahoo.com/quote/PSTG?p=PSTG&.tsrc=fin-srch"

url = "https://finance.yahoo.com/quote/PSTG"
url2 = "https://finance.yahoo.com/quote/PSTG/analysis?p=PSTG"

response = requests.get(url2, headers = headers)
soup = BeautifulSoup(response.content, 'lxml') #lxml is the best parser for web scraping

header = soup.find_all("div", id= "Main")[0]
#print(header)



test = header.find("div", id="mrt-node-Col1-0-AnalystLeafPage")

#print(test)

table = test.find("div", id= "Col1-0-AnalystLeafPage-Proxy")

earnings_history = table.find_all("table",class_="W(100%) M(0) BdB Bdc($seperatorColor) Mb(25px)")[2]
earnings_history_title = table.find_all("table",class_="W(100%) M(0) BdB Bdc($seperatorColor) Mb(25px)")[2].find("span").get_text()

dates = table.find_all("table",class_="W(100%) M(0) BdB Bdc($seperatorColor) Mb(25px)")[2].find_all("tr")

dates_list = dates[0].find_all("span") # list of date values from table


print(earnings_history_title, "for stock = ")


# would need to do a double for loop maybe, could format the print statements.

for i in range(1,len(dates_list)):
    print(dates_list[i].get_text())



print(dates[1].find_all("span"))


# def get_EPS(ticker):
#     """ This function is to fetch recent EPS data from passed in ticker """
#     ticker = str(ticker)
#     
#     url = "https://finance.yahoo.com/quote/" + ticker + "/analysis?p=" + "PSTG"
#     request = requests.get(url)
# #     if request:
# #         print("works")
# #     else:
# #         print("err")






# 
# response = requests.get(url, headers = headers)
# if response:
#     print("yes")
#     
#     soup = BeautifulSoup(response.content, 'lxml') #lxml is the best parser for web scraping
#     print(soup.title)
#     
# else:
#     print("err")