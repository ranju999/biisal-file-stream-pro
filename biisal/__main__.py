import os
import asyncio
import logging
from aiohttp import web
from .bot import StreamBot
from .vars import Var
from .server import web_server
from .utils.keepalive import ping_server
from biisal.bot.clients import initialize_clients

logging.basicConfig(
    level=logging.DEBUG,  # ✅ Debug logs enable करें
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

async def keep_alive():
    while True:
        await asyncio.sleep(600)  # ✅ हर 10 मिनट में Active रखने के लिए
        await ping_server()

async def start_services():
    print("Initializing Telegram Bot...")
    bot_info = await StreamBot.get_me()
    await initialize_clients()

    print("Initializing Web Server...")
    app = web.Application()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, Var.BIND_ADDRESS, Var.PORT)
    await site.start()

    print("Bot Started Successfully ✅")
    
    asyncio.create_task(keep_alive())  # ✅ Keep-Alive Task चलाएँ
    await idle()

if __name__ == '__main__':
    try:
        asyncio.run(start_services())  # ✅ Use asyncio.run()
    except KeyboardInterrupt:
        logging.info('Service Stopped!')
     
