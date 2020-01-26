import requests
from bs4 import BeautifulSoup
import unidecode

unionURL = 'http://www.restauraceunion.cz/denni-menu/'
m_rep = "UNIONREPLACEME"

page = requests.get(unionURL)
data = page.content
soup = BeautifulSoup(data, 'html.parser')

main_menu = soup.find('div', attrs={'class': "entry-content"})


# Read in the file
with open('index.html', 'r') as file:
    filedata = file.read()

# # Replace UNIONREPLACEME
filedata = filedata.replace(m_rep, unidecode.unidecode(str(main_menu)))
filedata = filedata.replace('width="600"></iframe></p>', 'width="800"></iframe></p>')
filedata = filedata.replace('>Union<', ' style="font-size:18px; color:#091034;">Union<')

# Write the file out again
with open('index.html', 'w') as file:
    file.write(filedata)


