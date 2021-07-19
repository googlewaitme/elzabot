from environs import Env


env = Env()
env.read_env('.env.test')

messages = {
    'HELP_TEXT': 'Это Эзин бот!'
}

photo_themes = [
    'night japan',
    'night city',
    'neon city',
    'cat',
    'dog',
    'nature',
    'russia',
    'japan',
    'canada',
    'USA',
]

BOT_TOKEN = env.str('BOT_TOKEN')
CHANNEL_ID = env.str('CHANNEL_ID')


# from unsplash
SECRET_CODE = env.str('SECRET_CODE')
CLIENT_ID = env.str('CLIENT_ID')
REDIRECT_URI = env.str('REDIRECT_URI')
