import requests
import json

def instadownloader(link):
    import requests

    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "a63f4e1196msh17c5bd4aee6fc87p106434jsn790c6f4016ec",
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