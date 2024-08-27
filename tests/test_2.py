import requests
import pytest

class TestYandexDisk:
    def setup_method(self):
        self.headers = {'Authorization' : 'OAuth y0_AgAAAAAmBsbuAADLWwAAAAEPEUueAACAaO-_DA9Ay4wv_hS37dmy_5wZTQ'}
        
    def test_creat_folder(self):
       params = {'path': 'Image11'}
       response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params)
       
       assert response.status_code == 201
       
    def test_creat_folder_again(self):
        params = {'path': 'Image11'}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params)

        assert response.status_code == 409
        
    def test_unauthorized(self):
        self.headers = {'Authorization' : 'OAuth y0_AgAAAAAmBsbuAADLWwAAAAEO9suAAADRoOsjTzRBZYmvIUKMfSjGHZG'}
        params = {'path': 'Image105'}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params)

        assert response.status_code == 401
        
   

    
