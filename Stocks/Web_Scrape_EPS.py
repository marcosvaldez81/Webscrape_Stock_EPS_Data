##################################

# Marcos Valdez
# I find trading the markets quite interesting. 
# So I decided to make a script to pull EPS data history from a passed in ticker.

##################################


from bs4 import BeautifulSoup
import requests 

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Safari/537.36'}   

def get_eps(ticker):
    """ This function will take passed in ticker and  """
    
    url2 = "https://finance.yahoo.com/quote/" + ticker + "/analysis?p=" + ticker

    response = requests.get(url2, headers = headers)

    soup = BeautifulSoup(response.content, 'lxml') #lxml is the best parser for web scraping
    
    header = soup.find_all("div", id= "Main")[0]
    
    test = header.find("div", id="mrt-node-Col1-0-AnalystLeafPage")
    table = test.find("div", id= "Col1-0-AnalystLeafPage-Proxy")
    earnings_history_title = table.find_all("table",class_="W(100%) M(0) BdB Bdc($seperatorColor) Mb(25px)")[2].find("span").get_text()
    earnings_history_table = table.find_all("table",class_="W(100%) M(0) BdB Bdc($seperatorColor) Mb(25px)")[2].find_all("tr")
    dates_list = earnings_history_table[0].find_all("span") # list of date values from table
    
    # eps estimate row
    estimate = earnings_history_table[1].find_all("span")
    eps_estimate_title = estimate[0].get_text()
    
    print(earnings_history_title, "for ticker = $" + str(ticker))
    print()
    
    print("\t\t",dates_list[1].get_text() ,"\t", dates_list[2].get_text(), "\t",
          dates_list[3].get_text(),"\t", dates_list[4].get_text())
    
    print("-----" * 15)
    print()
    
    # eps estimate row
    print(eps_estimate_title, "\t ", estimate[1].get_text(), "  \t  ", estimate[2].get_text(),
           "    \t  ", estimate[3].get_text(), "    \t  ", estimate[4].get_text())
    
    # eps actual row
    eps_actual = earnings_history_table[2].find_all("span")
    eps_actual_title = eps_actual[0].get_text()
    print(eps_actual_title,"    \t ", eps_actual[1].get_text(),"     \t  ", eps_actual[2].get_text(),
           "    \t  ", eps_actual[3].get_text(), "    \t  ", eps_actual[4].get_text())
    
    
    #difference Row:
    difference = earnings_history_table[3].find_all("span")
    difference_title = difference[0].get_text()
    print(difference_title,"    \t ", difference[1].get_text(), "     \t  ", difference[2].get_text(),
           "    \t  ", difference[3].get_text(), "    \t  ", difference[4].get_text())
    # surprise row
    surprise = earnings_history_table[4].find_all("span")
    surprise_title = surprise[0].get_text()
    print(surprise_title,"    \t", surprise[1].get_text(), "    \t  ", surprise[2].get_text(),
           "    \t  ", surprise[3].get_text(), "    \t  ", surprise[4].get_text())



get_eps("AAPL")

