from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os, hashlib

from aiogram.types import InputTextMessageContent, InlineQueryResultArticle, InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

#Кнопка ссылка
urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='Топ 250 фильмов', url='https://www.kinopoisk.ru/lists/movies/top250/')
urlButton2 = InlineKeyboardButton(text='Топ 250 сериалов', url='https://www.kinopoisk.ru/lists/movies/series-top250/')
urlkb.add(urlButton, urlButton2)


@dp.message_handler(commands='ссылка')
async def url_command(message : types.Message):
    await message.answer('Варианты каталогов:', reply_markup=urlkb)



@dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    text = query.query or 'echo'
    link = 'https://ru.wikipedia.org/wiki/' + text
    result_id: str = hashlib.md5(text.encode()).hexdigest()

    articles = [types.InlineQueryResultArticle(
        id=result_id,
        title='Информация из Википедии:',
        url=link,
        input_message_content=types.InputTextMessageContent(
            message_text=link
        )
    )]
    await query.answer(articles, cache_time=1, is_personal=True)


executor.start_polling(dp, skip_updates=True)
