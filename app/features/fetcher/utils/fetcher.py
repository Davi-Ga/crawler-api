import requests
import json

class UriFetcher:
    @classmethod
    def fetch_uris(cls, url):
        response = requests.get(url)
        print(response)
        data = response.json()
        uris = [item['uri'] for item in data['dados']]
        return uris

    @classmethod
    def fetch_uri_data(cls, url):
        response = requests.get(url)
        data = response.json()
        return data
    
    @classmethod
    def fetch_author(cls, url):
        response = requests.get(url)
        data = response.json()
        uri=data['dados'][0]['uri']
        data = cls.fetch_uri_data(uri)
        return data