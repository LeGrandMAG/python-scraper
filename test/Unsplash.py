from wsgiref import headers
import requests
import os

alt_url = "https://unsplash.com/napi/search/photos?query=art&xp=&per_page=20&page=0"

class Unsplash:

    def __init__(self, search_term, per_page, quality):
        self.search_term = search_term
        self.per_page = per_page
        self.quality = quality
        
        



    def set_url(self):
        return f"https://unsplash.com/napi/search?query={self.search_term}&per_page={self.per_page}&xp=search-multi-word&page="

    def make_request(self):
        url = self.set_url()
        return requests.request("GET", url)

    def get_data(self):
        self.data = self.make_request().json()

    def save_path(self,name):
        download_dir = dirc
        if not os.path.exists(download_dir):
            os.mkdir(download_dir)
        return f"{os.path.join(os.path.realpath(os.getcwd()), download_dir, name)}.jpg"

    def download(self,url,name):
        filepath = self.save_path(name)
        with open(filepath, "wb") as f:
            f.write(requests.request("GET",url).content)

    def Scraper(self):
        self.make_request()
        self.get_data()
        for item in self.data['photos']['results']:
            name = item['id']
            url = item['urls'][self.quality]
            self.download(url,name)


term = str(input("What term are you looking for?: \n"))
dirc = str(input("What is  your directory name: \n"))
print("choose the quality of the picture you want to download\n")
print("1. Raw\t 2. Full\t 3. regular\t 4. small\t 5. thumb\n")
print("************************************************************\n")
iqual = int(input())
qual = str()

if iqual >=1:
    if iqual == 1:
        qual = "raw"
    elif iqual == 2:
        qual = "full"
    elif iqual ==3:
        qual = "regular"
    elif iqual ==4:
        qual = "small"
    else:
        qual = "thumb"


number = int(input("How many pictures do you want to download? (max 30) \n"))

if number >= 30:
    number = 30
    
scraper = Unsplash(term, number, qual)
scraper.Scraper()

print("**********************************************************\n")
print(">>>>> YOUR PICTURES HAVE BEEN SUCCESSFULLY DOWNLOADED <<<<<\n")

while True:
    exit = str(input("Press 'X' to exit \n\n"))

    if (exit == 'x' or exit == 'X'):
        print("Thank you for using our service!\n")
        break







unsplash_pic = "https://unsplash.com/ngetty/v3/search/images/creative?fields=display_set%2Creferral_destinations%2Ctitle&page_size=100&phrase=black-guy&sort_order=best_match&graphical_styles=&exclude_nudity=true&exclude_editorial_use_only=false"