import os
import json
import time
import uvloop
import asyncio
import subprocess
from logger import logger
from tasks import ping, wget
from utiles import Validator
from pyrogram import Client, filters
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()
app = Client(
    "Watchtower",
    bot_token=os.environ["BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
)
loop = asyncio.get_event_loop()
app.loop = loop
validator = Validator()


def jsonify(message):
    return json.loads(str(message))


async def add_usage(message):
    await message.reply_text(
        text=f"Wrong command!\n\nUsage:\n/add `&lt;name>` `&lt;ip>` `&lt;port:int>` `&lt;ping=default/wget>` `&lt;interval:int>`"
    )
    return


def init():
    # TODO: add procedure to retrieve scheduled tasks from redis
    pass

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Hello, Welcome to watchtower bot\n\n/add `&lt;name>` `&lt;ip>` `&lt;port:int>` `&lt;ping=default/wget>` `&lt;interval:int>`\n/list - show servers list and state",
    )


@app.on_message(filters.command("add") & filters.private)
async def add_server(client, message):
    args = message.text.split()
    if len(args) != 6 or not validator.validate_input(args):
        await add_usage(message)
        return

    name, ip, port, method, interval = args[1:]
    fn = wget if method == "wget" else ping
    scheduler.add_job(
        fn,
        "interval",
        seconds=int(interval),
        kwargs={
            "message": message,
            "name": name,
            "ip": ip,
            "port": port,
        },
    )
    # TODO: create function to save redis database on disk
    # database.save()
    logger.info(f"Scheduled for {name} with address: {ip}:{port} / method: {method}")
    await message.reply_text(text=f"{name} scheduled successfully")


@app.on_message(filters.command("list") & filters.private)
async def server_list(client, message):
    await message.reply(
        text="You didn't add any server before.\nUse /add to add new server",
    )


if __name__ == "__main__":
    scheduler.start()
    init()
    app.run()
