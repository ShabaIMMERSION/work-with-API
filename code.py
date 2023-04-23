import requests
val = input("Input valcode: ")
date = input("Input date: ")
url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={val}&date={date}&json"
r = requests.get(url)
if r.status_code == 200:
   data = r.json()
   print("Rate:", data[0]["rate"])
else:
   print("Помилка")


#soap = BeautifulSoup(responce, "lxml")
#mydivs = soap.find("div", {"class": "entry-content"})
#p = mydivs.find_all("p")

#author = p[1].find("strong").text
#a1 = p[1].find("a").text

#print(author + " - " + a1)
#print(p[2].text)