from os import environ
import aiohttp
from pyrogram import Client, filters

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
API_KEY = environ.get('API_KEY', 'deca8552d6bfa7f9e86bc34290214c116036d5de')

bot = Client('pdiskshortner bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)

@bot.on_message(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hi I am one and Only a personal Bot to short links from droplink website  Made with ♥️ by @NP_technology')

@bot.on_message(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'hey, bro I can convert big/long link to a short link of droplink  Made with ♥️ by @NP_technology')

@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    try:
        short_link = await get_shortlink(link)
        await message.reply(f'''<code>{short_link}</code>.

({short_link})
        
This link as been shortened by @np_technology for free subscribe to our YouTube channel to get more awesome thinks like this https://youtube.com/channel/UCJ58-uPHipMiP4-uVmp0iRw [Short Link]({short_link})''', quote=True)
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)


async def get_shortlink(link):
    url = 'http://droplink.co/api'
    params = {'api': API_KEY, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]


bot.run()
