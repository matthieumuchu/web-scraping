import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.investopedia.com/")

print(result.status_code)

#print(result.headers)

source_code= result.content
#print(source_code)

soup= BeautifulSoup(source_code, 'lxml')
#soup= BeautifulSoup(source_code, 'html.parser')
#soup= BeautifulSoup(source_code, 'html5lib')

links= soup.find_all("a")
#print(links)
#print("\n")

for link in links:
    if "AMD" in link.text:
        print(link)
        print(link.attrs['href']) #give me the content in the link tag attribute
