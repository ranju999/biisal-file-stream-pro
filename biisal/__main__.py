import os
import asyncio
import logging
from aiohttp import web
from .bot import StreamBot  # ✅ Pyrogram Bot Client
from .vars import Var
from .server import web_server
from .utils.keepalive import ping_server
from biisal.bot.clients import initialize_clients
from pyrogram import idle  # ✅ Ensure Pyrogram's idle() is imported

# ✅ Debugging Logs Enable करें
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

async def keep_alive():
    """Server को Active रखने के लिए Keep-Alive Task"""
    while True:
        await asyncio.sleep(600)
        await ping_server()

async def start_services():
    """बॉट और वेब सर्वर स्टार्ट करने के लिए Main Function"""
    print("Initializing Telegram Bot...")

    # ✅ बॉट को पहले स्टार्ट करें
    await StreamBot.start()

    # ✅ अब get_me() काम करेगा
    bot_info = await StreamBot.get_me()
    print(f"✅ Bot Started as: {bot_info.first_name}")

    # ✅ Clients Initialize करें
    await initialize_clients()

    print("Initializing Web Server...")
    app = await web_server()  # ✅ Fix: Ensure web_server() is awaited
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, Var.BIND_ADDRESS, Var.PORT)
    await site.start()
    print("✅ Web Server Started on {}:{}".format(Var.BIND_ADDRESS, Var.PORT))

    # ✅ Keep-Alive Task चलाएँ
    asyncio.create_task(keep_alive())

    # ✅ बॉट को Running Mode में रखें
    await idle()

if __name__ == '__main__':
    try:
        asyncio.run(start_services())  # ✅ Proper Async Execution
    except KeyboardInterrupt:
        logging.info('❌ Service Stopped!')
        
