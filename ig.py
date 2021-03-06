from time import sleep
from instabot import Bot
import glob
import os
import requests

if os.path.isfile("config/file.json"):
    os.remove("config/file.json")
cookie_del = glob.glob("config/*cookie.json")
if len(cookie_del) > 0:
    os.remove(cookie_del[0])

class Ig:
    def __init__(self, ig_login, ig_password):
        self.login = ig_login
        self.password = ig_password
        self.bot = Bot()
        
    def get_ig_posts(self):
        self.bot.login(username = self.login, password = self.password)
        sleep(2)
        return self.bot.get_your_medias()

    def create_ig_post(self, title, photo, fileName, videoUrl):
        self.bot.login(username = self.login, password = self.password, ask_for_code=True)
        sleep(4)
        r = requests.get(photo, allow_redirects=True)
        open(fileName, 'wb').write(r.content)
        self.bot.upload_photo(fileName, caption="New video "+ title + "uploaded on my channel. You can watch it here: " + videoUrl + "!")