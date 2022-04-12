from googleapiclient.discovery import build
from urllib.request import HTTPError

class Yt:
    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id

    def get_yt_videos(self):
        service = build('youtube', 'v3', developerKey=self.api_key)

        request = service.search().list(
                part = 'snippet',
                channelId=self.channel_id,
        )

        try:
            response = request.execute()
        except HTTPError as e:
            print('Error response status code : {0}, reason : {1}'.format(e.status_code, e.error_details))
       
        videos_data = []

        for item in response["items"]:
            if item["id"]["kind"] == "youtube#video":
                videos_data.append(item)

        return videos_data

    def create_video_url(self, videoID):
        return "https://www.youtube.com/watch?v=" + videoID

