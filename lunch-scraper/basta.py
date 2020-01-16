import requests
from bs4 import BeautifulSoup
import unidecode

bastaURL = 'https://www.bastacatering.cz/basta-canteen/menu/'
b_rep = "BASTAREPLACEME"

page = requests.get(bastaURL)
data = page.content
soup = BeautifulSoup(data, 'html.parser')

dates = soup.find_all('h2', 'nadpis_den')
courses = soup.find_all('h3', 'nadpis_menu')
jidlo = soup.find_all('span', class_="jidlo")

# Read in the file
with open('index.html', 'r') as file:
    filedata = file.read()

# Replace Basta Soup
filedata = filedata.replace(b_rep, '<p style="font-size:30px; color:white;">Polevka</p>{}'.format(b_rep))
for polevka in jidlo[0:3]:
    filedata = filedata.replace(b_rep, unidecode.unidecode(str(polevka)) + " <br/>{}".format(b_rep))

# Replace Basta Hotovky
filedata = filedata.replace(b_rep, '<br/>{}'.format(b_rep))
filedata = filedata.replace(b_rep, '<p style="font-size:30px; color:white;">Hotovky</p>{}'.format(b_rep))
for hotovka in jidlo[4:7]:
    filedata = filedata.replace(b_rep, unidecode.unidecode(str(hotovka)) + " <br/>{}".format(b_rep))

# Replace Basta Minutky
filedata = filedata.replace(b_rep, '<br/>{}'.format(b_rep))
filedata = filedata.replace(b_rep, '<p style="font-size:30px; color:white;">Minutky</p>{}'.format(b_rep))
for minutka in jidlo[8:10]:
    filedata = filedata.replace(b_rep, unidecode.unidecode(str(minutka)) + " <br/>{}".format(b_rep))

# Replace Basta Salat
filedata = filedata.replace(b_rep, '<br/>{}'.format(b_rep))
filedata = filedata.replace(b_rep, '<p style="font-size:30px; color:white;">Salat</p>{}'.format(b_rep))
for salat in jidlo[9:13]:
    filedata = filedata.replace(b_rep, unidecode.unidecode(str(salat)) + " <br/>{}".format(b_rep))

# Get rid of the final b_rep
filedata = filedata.replace(b_rep, '')
filedata = filedata.replace('  ', '')
filedata = filedata.replace('>Basta<', ' style="font-size:18px; color:#091034;">Basta<')



# Write the file out again
with open('index.html', 'w') as file:
    file.write(filedata)
