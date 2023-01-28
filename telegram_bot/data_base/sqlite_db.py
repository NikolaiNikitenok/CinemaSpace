import sqlite3 as sq
from create_bot import bot


def sql_start():
    global base, cur
    base = sq.connect('cinema_space.db')
    cur = base.cursor()
    if base:
        print('База данных готова!')
    base.execute('CREATE TABLE IF NOT EXISTS films(img TEXT, name TEXT PRIMARY KEY, description TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO films VALUES (?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM films').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}')


async def sql_read2():
    return cur.execute('SELECT * FROM films').fetchall()


async def sql_delete_command(data):
    cur.execute('DELETE FROM films WHERE name == ?', (data,))
    base.commit()
