import requests
from bs4 import BeautifulSoup
import unidecode

# beautifulsoup magic
babetaURL = 'http://babeta-rest.cz/#dayfood'
page = requests.get(babetaURL)
data = page.content
soup = BeautifulSoup(data, 'html.parser')
daymenu= soup.find('table', attrs={'id': "tablepress-4"})

# Read in the file
with open('index.html', 'r') as file:
    filedata = file.read()

# text to be replaced in index.html
m_rep = "BABETAREPLACEME"
# Replace BABETAREPLACEME
filedata = filedata.replace(m_rep, unidecode.unidecode(str(daymenu)))

# make Babeta menu item black (and slightly larger) so user knows it finished scraping ok
filedata = filedata.replace('>Babeta<', ' style="font-size:18px; color:#091034;">Babeta<')

# Write the file out again
with open('index.html', 'w') as file:
    file.write(filedata)


