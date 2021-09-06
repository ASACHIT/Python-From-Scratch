import requests
import wget
from bs4 import BeautifulSoup


def download_images(direct_url, image_name):
    wget.download(direct_url, image_name)


class Assets:
    def __init__(self, url: str):
        self.url = url

    def pull_images(self, download: bool = False):
        htmlcontent = requests.get(f"{self.url}").text
        noodle_soup = BeautifulSoup(htmlcontent, "html.parser")
        anchors = noodle_soup.find_all("img")
        filtered_list = list(set(anchors))
        for images in filtered_list:
            print(self.url + images["src"])
        if download == True:
            filename = images["src"]
            download_images(direct_url=self.url, image_name=filename)

    def get_all_links(self):
        htmlcontent = requests.get(f"{self.url}").text
        noodle_soup = BeautifulSoup(htmlcontent, "html.parser")
        anchors = noodle_soup.find_all("a")
        for href in anchors:
            print(href["href"])


# prints all images links founds in page
Assets("https://itsnp.org/").pull_images()

Assets("https://itsnp.org/").get_all_links()  # prints all links founds in page
