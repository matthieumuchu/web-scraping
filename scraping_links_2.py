import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.use.or.ug/content/listed-securities")

print(result.status_code)

#print(result.headers)

source_code= result.content
#print(source_code)

soup= BeautifulSoup(source_code, 'lxml')
#soup= BeautifulSoup(source_code, 'html.parser')
#soup= BeautifulSoup(source_code, 'html5lib')

urls=[]
for td_tag in soup.find_all("td"):
    a_tag = td_tag.find('a')
    urls.append(a_tag.attrs['href'])


print(urls)
