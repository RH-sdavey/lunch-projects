import requests
from bs4 import BeautifulSoup
import unidecode

pupekURL = 'https://www.uhovezihopupku.cz/menu/'
p_rep = "PUPEKREPLACEME"

page = requests.get(pupekURL)
data = page.content
soup = BeautifulSoup(data, 'html.parser')

dnes = soup.find('div', class_='menu_dnes')

dnes = str(dnes).replace("/img/polevka_2.png", '')
dnes = str(dnes).replace('menu_jidlo_polevka">', 'menu_jidlo_polevka">POLEVKA: ')
dnes = str(dnes).replace('DNES', '')
dnes = str(dnes).replace('<div class="dnes"></div>', '')
dnes = str(dnes).replace(' Kc', ' Kc<tr></tr><tr></tr>')

dnes = str(dnes).replace('<th class="menu_text_stale_jidlo"', '<tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><th class="menu_text_stale_jidlo"')

# Read in the file
with open('index.html', 'r') as file:
    filedata = file.read()

# Replace PUPEKREPLACEME
filedata = filedata.replace(p_rep, unidecode.unidecode(str(dnes)))
filedata = filedata.replace('>Pupek<', ' style="font-size:18px; color:#091034;">Pupek<')

# Write the file out again
with open('index.html', 'w') as file:
    file.write(filedata)
