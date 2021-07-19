from unsplash.api import Api
from unsplash.auth import Auth
import wget
import os
import settings


class Photo:
    def __init__(self):
        secret_code = settings.SECRET_CODE
        client_id = settings.CLIENT_ID
        redirect_uri = settings.REDIRECT_URI
        self.auth = Auth(client_id, secret_code, redirect_uri)
        self.api = Api(self.auth)

    def download_random_photo(self, theme_of_photo='cyberpunk'):
        photo = self.random_photo(theme_of_photo)
        photo_url = self.give_url(photo)
        self.download_by_url(photo_url)

    def get_url_random_photo(self, theme_of_photo='cyberpunk'):
        photo = self.random_photo(theme_of_photo)
        photo_url = self.give_url(photo)
        return photo_url

    def give_url(self, photo):
        return photo.urls.regular

    def download_by_url(self, url):
        wget.download(url, 'img.jpg')

    def random_photo(self, theme_of_photo='cyberpunk'):
        return self.api.photo.random(query=theme_of_photo)[0]

    def delete(self, photo_name='img.jpg'):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), photo_name)
        os.remove(path)


if __name__ == "__main__":
    photo = Photo()
    photo.download_random_photo('japan city')
    input('Please tup enter to delete photo')
    photo.delete()
