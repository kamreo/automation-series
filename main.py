import os
from dotenv import load_dotenv
from yt import Yt
from ig import Ig
from datetime import datetime
from urllib.parse import urlparse

load_dotenv()

API_KEY = os.getenv('API_KEY') 
CHANNEL_ID = os.getenv('CHANNEL_ID') 
IG_LOGIN = os.getenv('IG_LOGIN')
IG_PASS = os.getenv('IG_PASS')

yt = Yt(API_KEY, CHANNEL_ID)
ig = Ig(IG_LOGIN, IG_PASS)

videos = yt.get_yt_videos()

for video in videos:
    video_date = datetime.strptime(video["snippet"]["publishTime"], "%Y-%m-%dT%H:%M:%SZ")
    if (datetime.today() - video_date).days == 0:
        file_name = a = urlparse(video["snippet"]["thumbnails"]["high"]["url"])
        ig.create_ig_post(video["snippet"]["title"], video["snippet"]["thumbnails"]["high"]["url"], os.path.basename(a.path) ,yt.create_video_url(video["id"]["videoId"]))