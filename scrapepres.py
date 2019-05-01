from urllib.request import urlopen
from bs4 import BeautifulSoup
import pickle

obama_page = "https://millercenter.org/the-presidency/presidential-speeches/january-12-2016-2016-state-union-address"
bush_page = "https://millercenter.org/the-presidency/presidential-speeches/january-28-2008-state-union-address"
clinton_page = "https://millercenter.org/the-presidency/presidential-speeches/january-27-2000-state-union-address"
reagan_page = "https://millercenter.org/the-presidency/presidential-speeches/january-25-1988-state-union-address"
nixon_page = "https://millercenter.org/the-presidency/presidential-speeches/january-30-1974-state-union-address"

def Scraper(source_page):
    page = urlopen(source_page)

    soup = BeautifulSoup(page, 'html.parser')

    soup = soup.select_one(".transcript-inner")
    soup = soup.get_text()
    soup = str(soup)

    return soup

obamascript = Scraper(obama_page)
bushscript = Scraper(bush_page)
clintonscript = Scraper(clinton_page)
reaganscript = Scraper(reagan_page)
nixonscript = Scraper(nixon_page)

pickle.dump(obamascript, open("obama.pickle", "wb"))
pickle.dump(bushscript, open("bush.pickle", "wb"))
pickle.dump(clintonscript, open("clinton.pickle", "wb"))
pickle.dump(reaganscript, open("reagan.pickle", "wb"))
pickle.dump(nixonscript, open("nixon.pickle", "wb"))
