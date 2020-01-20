import requests
from bs4 import BeautifulSoup
import unidecode

# beautifulsoup magic
gingillaURL = 'https://gingilla.cz/cz-poledni-menu'
page = requests.get(gingillaURL)
data = page.content
soup = BeautifulSoup(data, 'html.parser')
all_widgets = soup.findAll('div', attrs={'class': "homepage-widget"})

# Read in the file
with open('index.html', 'r') as file:
    filedata = file.read()

# Replace GINGILLAREPLACEME
m_rep = "GINGILLAREPLACEME"
filedata = filedata.replace(m_rep, unidecode.unidecode(str(all_widgets[0])))
filedata = filedata.replace('Cely tyden', '')

# make the gingilla menu item black so the user knows we got this far
filedata = filedata.replace('>Gingilla<', ' style="font-size:18px; color:#091034;">Gingilla<')

# Write the file out again
with open('index.html', 'w') as file:
    file.write(filedata)


