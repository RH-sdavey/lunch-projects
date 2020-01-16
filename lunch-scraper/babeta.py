import requests
from bs4 import BeautifulSoup
import unidecode


babetaURL = 'http://babeta-rest.cz/#dayfood'
m_rep = "BABETAREPLACEME"

page = requests.get(babetaURL)
data = page.content
soup = BeautifulSoup(data, 'html.parser')

daymenu= soup.find('table', attrs={'id': "tablepress-4"})


# Read in the file
with open('index.html', 'r') as file:
    filedata = file.read()

# # Replace BABETAREPLACEME
filedata = filedata.replace(m_rep, unidecode.unidecode(str(daymenu)))

filedata = filedata.replace('>Babeta<', ' style="font-size:18px; color:#091034;">Babeta<')
#
# Write the file out again
with open('index.html', 'w') as file:
    file.write(filedata)


