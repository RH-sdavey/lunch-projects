import requests
from bs4 import BeautifulSoup
import unidecode
import datetime
from bs4 import SoupStrainer

mitrovskiURL = 'https://www.mitrovski.cz/menu/'
m_rep = "MITROVSKIREPLACEME"

page = requests.get(mitrovskiURL)
data = page.content

soup = BeautifulSoup(data, 'html.parser')

all_days_menus = soup.findAll('section', attrs={'class': 's'})
# Mon = 0
# Tues = 1
# Wed = 2
# Thurs = 3
# Fri = 4
# today_as_a_number = datetime.datetime.today().weekday()

# Read in the file
with open('index.html', 'r') as file:
    filedata = file.read()

# Replace MITROVSKIREPLACEME
filedata = filedata.replace(m_rep, unidecode.unidecode(str(all_days_menus)))
filedata = filedata.replace(',', '')
filedata = filedata.replace('[<section', '<section')


filedata = filedata.replace('>Mitrovski<', ' style="font-size:18px; color:#091034;">Mitrovski<')
#
#
#
# Write the file out again
with open('index.html', 'w') as file:
    file.write(filedata)
#
#
