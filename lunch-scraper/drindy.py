import requests
from bs4 import BeautifulSoup
import unidecode

drindyURL = 'http://www.drindy.cz/cs/'
m_rep = "DRINDYREPLACEME"

page = requests.get(drindyURL)
data = page.content
soup = BeautifulSoup(data, 'html.parser')

daily_menu = soup.findAll('div', attrs={'class': "inside-frame"})
daily_menu = str(daily_menu).replace('[', '')
daily_menu = str(daily_menu).replace(']', '')


# Read in the file
with open('index.html', 'r') as file:
    filedata = file.read()

# Replace DRINDYREPLACEME
filedata = filedata.replace(m_rep, unidecode.unidecode(str(daily_menu)))
filedata = filedata.replace('>Dr Indy<', ' style="font-size:18px; color:#091034;">Dr Indy<')

# Write the file out again
with open('index.html', 'w') as file:
    file.write(filedata)


