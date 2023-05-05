import requests
import json

def instadownloader(link):
    import requests

    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "a280205aaemsh8edf101694dc13ep1fee9cjsnd9358534e79a",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    rest = json.loads(response.text)
    if 'error' in rest:
        return 'Bad'
    else:
        dict = {}
        if rest['Type'] =='Post-Image':
            dict['type']='image'
            dict['media']=rest['media']
            return dict
        elif rest['Type']=='Post-Video':
            dict['type']='video'
            dict['media']=rest['media']
            return dict
        elif rest['Type']=='Carousel':
            dict['type']='carousel'
            dict['media']=rest['media']
            return dict
        else:
            return 'Bad'