import requests
from bs4 import BeautifulSoup
import unidecode
import datetime
from bs4 import SoupStrainer

makaluURL = 'http://www.nepalska-restaurace-makalu.cz/'
m_rep = "MAKALUREPLACEME"

page = requests.get(makaluURL)
data = page.content

soup = BeautifulSoup(data, 'html.parser')

all_days_menus = soup.findAll('p', attrs={'class': None})

all_days_menus = tuple(map(str, all_days_menus[10:15]))

# Mon = 0    # Tues = 1     # Wed = 2     # Thurs = 3     # Fri = 4
today_as_a_number = datetime.datetime.today().weekday()
todays_menu = all_days_menus[today_as_a_number]
todays_menu = str(todays_menu).replace("img/TMenuN.png", "")


todays_menu = todays_menu.replace('<br/>', '<br/><br/>')
todays_menu = todays_menu.replace('class="cena">', 'class="cena">   ')

# Read in the file
with open('index.html', 'r') as file:
    filedata = file.read()

# Replace MAKALUREPLACEME
filedata = filedata.replace(m_rep, unidecode.unidecode(str(todays_menu)))
filedata = filedata.replace('>Makalu<', ' style="font-size:18px; color:#091034;">Makalu<')

# Write the file out again
with open('index.html', 'w') as file:
    file.write(filedata)



