# (c) @biisal
# (c) adars h-goel
import os
import sys
import glob
import asyncio
import logging
import importlib
from pathlib import Path
from pyrogram import idle
from .bot import StreamBot
from .vars import Var
from aiohttp import web
from .server import web_server
from .utils.keepalive import ping_server
from biisal.bot.clients import initialize_clients

LOGO = """
 ____ ___ ___ ____    _    _     
| __ )_ _|_ _/ ___|  / \  | |    
|  _ \| | | |\___ \ / _ \ | |    
| |_) | | | | ___) / ___ \| |___ 
|____/___|___|____/_/   \_\_____|"""

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

ppath = "biisal/bot/plugins/*.py"
files = glob.glob(ppath)
StreamBot.start()
loop = asyncio.get_event_loop()

async def start_services():
    print('\n')
    print('------------------- Initalizing Telegram Bot -------------------')
    bot_info = await StreamBot.get_me()
    StreamBot.username = bot_info.username
    print("------------------------------ DONE ------------------------------")
    print()
    print(
        "---------------------- Initializing Clients ----------------------"
    )
    await initialize_clients()
    print("------------------------------ DONE ------------------------------")
    print('\n')
    print("--------------------- Initializing Web Server ---------------------")
    await server.setup()
    await web.TCPSite(server, Var.BIND_ADDRESS, Var.PORT).start()
    print("------------------------------ DONE ------------------------------")
    print()
    print("------------------------- Service Started -------------------------")
    print("                        bot =>> {}".format(bot_info.first_name))
    if bot_info.dc_id:
        print("                        DC ID =>> {}".format(str(bot_info.dc_id)))
    print(" URL =>> {}".format(Var.URL))
    print("------------------------------------------------------------------")
    print('----------------------------- DONE ---------------------------------------------------------------------')
    print('\n')
    print('---------------------------------------------------------------------------------------------------------')
    print('---------------------------------------------------------------------------------------------------------')
    print(' follow me for more such exciting bots! https://github.com/biisal')
    print('---------------------------------------------------------------------------------------------------------')
    print('\n')
    print('----------------------- Service Started -----------------------------------------------------------------')
    print('                        bot =>> {}'.format((await StreamBot.get_me()).first_name))
  #  print('                        server ip =>> {}:{}'.format(bind_address, Var.PORT))
    print('                        Owner =>> {}'.format((Var.OWNER_USERNAME)))
    print(LOGO)
    try: 
        await StreamBot.send_message(chat_id=Var.OWNER_ID[0] ,text='<b>ᴊᴀɪ sʜʀᴇᴇ ᴋʀɪsʜɴᴀ 😎\nʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ !!</b>')
    except Exception as e:
        print(f'got this err to send restart msg to owner : {e}')
    await idle()

if __name__ == '__main__':
    try:
        loop.run_until_complete(start_services())
    except KeyboardInterrupt:
        logging.info('----------------------- Service Stopped -----------------------')
