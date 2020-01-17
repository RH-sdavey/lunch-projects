import requests
from bs4 import BeautifulSoup
import unidecode

# beautifulsoup magic
coloseumURL = 'https://www.coloseum.cz/cs/restaurace/brno/denni-menu'
page = requests.get(coloseumURL)
data = page.content
soup = BeautifulSoup(data, 'html.parser')
all_days_menus = soup.findAll('section', attrs={'class': "block-pizzacoloseum-content"})

# clean up the beautifulsoup results before we add it to index.html
all_days_menus = str(all_days_menus).replace('150 g', '150 g<br/><br/>')
all_days_menus = str(all_days_menus).replace('</span>', '</span><br/><br/>')
all_days_menus = str(all_days_menus).replace('150 g', '')
all_days_menus = str(all_days_menus).replace('[', '<b>Menu Stays the same all week, just the soup is different</b>')

# Read in the file
with open('index.html', 'r') as file:
    filedata = file.read()

# Replace COLOSEUMREPLACEME
m_rep = "COLOSEUMREPLACEME"
filedata = filedata.replace(m_rep, unidecode.unidecode(str(all_days_menus)))

# make the menu item black so the user knows we go this far
filedata = filedata.replace('>Coloseum Pizzeria<', ' style="font-size:18px; color:#091034;">Coloseum Pizzeria<')

# Write the file out again
with open('index.html', 'w') as file:
    file.write(filedata)
