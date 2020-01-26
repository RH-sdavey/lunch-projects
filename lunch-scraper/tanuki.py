import requests
from bs4 import BeautifulSoup
import unidecode

tanukiURL = 'http://www.tanukisushi.cz/denni-menu-ibc'
m_rep = "TANUKIREPLACEME"

page = requests.get(tanukiURL)
data = page.content
soup = BeautifulSoup(data, 'html.parser')

all_days_menus = soup.findAll('div', attrs={'class': "daily-menu"})

# Read in the file
with open('index.html', 'r') as file:
    filedata = file.read()

# Replace TANUKIREPLACEME
filedata = filedata.replace(m_rep, unidecode.unidecode(str(all_days_menus)))
filedata = filedata.replace('>Tanuki<', ' style="font-size:18px; color:#091034;">Tanuki<')
filedata = filedata.replace('http://tanukisushi.cz/data/upload/images/menu.jpg', '')
filedata = filedata.replace('http://tanukisushi.cz/data/upload/images/menu.jpg', '')
filedata = filedata.replace('[', '')
filedata = filedata.replace(']', '')


# Write the file out again
with open('index.html', 'w') as file:
    file.write(filedata)


