import requests
import json

def instadownloader(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "e1af712655msha34c5349f608efcp186b23jsn01af1c8ca0a6",
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