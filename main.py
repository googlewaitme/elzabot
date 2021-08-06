import settings
import asyncio
from aiogram import Bot, Dispatcher, types
import aiogram
import random
from photo import Photo


async def post_in_channel():
    theme = random.choice(settings.photo_themes)
    photo_url = Photo().get_url_random_photo(theme)
    media = types.MediaGroup()
    media.attach_photo(photo_url, '🥀  f r e e d o m  🥀')
    await bot.send_media_group(
        media=media, chat_id=settings.CHANNEL_ID)


async def send_help(event: types.Message):
    await event.answer(settings.messages['HELP_TEXT'])


async def send_quote(event: types.Message):
    Photo().download_random_photo()
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('img.jpg'))
    await event.answer_media_group(media=media)


def give_dispatcher(bot):
    disp = Dispatcher(bot=bot)
    disp.register_message_handler(send_quote, commands={"quote"})
    disp.register_message_handler(send_help, commands={"help", "start"})
    return disp


def repeat_check(coro, loop):
    asyncio.ensure_future(coro(), loop=loop)
    time_for_wait = random.randint(10800, 21600)
    loop.call_later(time_for_wait, repeat_check, coro, loop)


if __name__ == '__main__':
    bot = Bot(token=settings.BOT_TOKEN)
    disp = give_dispatcher(bot)

    loop = asyncio.get_event_loop()
    loop.call_later(5, repeat_check, post_in_channel, loop)
    aiogram.utils.executor.start_polling(disp, skip_updates=True, loop=loop)
