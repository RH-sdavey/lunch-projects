import requests
from bs4 import BeautifulSoup
import unidecode

sedivehoURL = 'https://www.usedivehovola.com/denni-obedove-menu'
m_rep = "SEDIVEHOVOLAREPLACEME"

page = requests.get(sedivehoURL)
data = page.content

soup = BeautifulSoup(data, 'html.parser')

all_days_menus = soup.find('div', attrs={'id': 'comp-k3d9vgie'})


# Read in the file
with open('index.html', 'r') as file:
    filedata = file.read()

# Replace SEDIVEHOVOLAREPLACEME
filedata = filedata.replace(m_rep, unidecode.unidecode(str(all_days_menus)))
filedata = filedata.replace('>Sediveho Vola<', ' style="font-size:18px; color:#091034;">Sediveho Vola<')

# Write the file out again
with open('index.html', 'w') as file:
    file.write(filedata)


