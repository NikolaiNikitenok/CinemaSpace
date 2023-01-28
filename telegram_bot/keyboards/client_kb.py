from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#

mainMenu = InlineKeyboardMarkup(row_width=2)
btnMy = InlineKeyboardButton(text="🔍Предпочтения", callback_data='btnMy')
btnCode = InlineKeyboardButton(text="📔Поиск по коду", callback_data='btnCode')
btnVIP = InlineKeyboardButton(text="💎VIP", callback_data='btnVIP')
btnStar = InlineKeyboardButton(text="🌟Выбор знаменитостей", callback_data='btnStar')
btnRandom = InlineKeyboardButton(text="🎲Случайный фильм", callback_data='btnRandom')
btnLink = InlineKeyboardButton(text="📌Наши ссылки", callback_data='btnLink')
btnSettings = InlineKeyboardButton(text="⚙️Настройки", callback_data='btnSettings')

mainMenu.insert(btnMy).insert(btnCode).insert(btnVIP).insert(btnStar).insert(btnRandom).insert(btnLink).add(btnSettings)
# В настройки: кнопку поддержки подключить

#

Code = InlineKeyboardMarkup(row_width=2)
# Описание функции, кнопка поиска, кнопка назад
btnCodeSearch = InlineKeyboardButton(text="🔍Начать поиск", callback_data='btnCodeSearch')
btnBackCode = InlineKeyboardButton(text="⬅️Назад", callback_data='btnBackCode')

Code.insert(btnCodeSearch).add(btnBackCode)

#

VIP = InlineKeyboardMarkup(row_width=2)
btnBuy = InlineKeyboardButton(text="Купить 💎VIP💎", callback_data='btnBuy')
btnVIPMore = InlineKeyboardButton(text="📖Подробнее📖", callback_data='btnVIPMore')
btnBackVIP = InlineKeyboardButton(text="⬅️Назад", callback_data='btnBackVIP')

VIP.insert(btnBuy).insert(btnVIPMore).add(btnBackVIP)

#

VIPMore = InlineKeyboardMarkup()
btnBackVIPMore = InlineKeyboardButton(text="⬅️Назад", callback_data='btnBackVIPMore')

VIPMore.insert(btnBackVIPMore)

#

Link = InlineKeyboardMarkup(row_width=2)
btnUrl1 = InlineKeyboardButton(text="Tik-Tok", url='https://www.tiktok.com/@_cinemaspace_')
btnUrl2 = InlineKeyboardButton(text="Telegram", url='https://t.me/cinemaspacehd')
btnUrl3 = InlineKeyboardButton(text="По рекламе", url='https://t.me/nikolalllkaa')
btnUrl4 = InlineKeyboardButton(text="Бот с фильмами", url='https://t.me/Tiktokfilmandserialbot?start=Cinemaspace')
btnBackLink = InlineKeyboardButton(text="⬅️Назад", callback_data='btnBackLink')

Link.insert(btnUrl1).insert(btnUrl2).insert(btnUrl3).insert(btnUrl4).add(btnBackLink)

#

b1 = KeyboardButton('/Help')
b2 = KeyboardButton('/Map')
b3 = KeyboardButton('/Films')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b1).insert(b2).add(b3)
