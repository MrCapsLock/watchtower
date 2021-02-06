import os
import subprocess
from logger import logger


async def ping(message, name, ip, port):
    logger.info(f'name {name} / ip {ip}')
    result = subprocess.run(
        f"ping -c 1 -W 10 {ip}".split(),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if result.returncode != 0:
        logger.info(f'name {name} / ip {ip}')
        await message.reply(text=f"{name} with ip:{ip} goes down.")
    return


async def wget(message, name, ip, port):
    result = subprocess.run(
        f"wget -nv -O - {ip}:{port}".split(),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if result.returncode != 0:
        await message.reply(text=f"{name} with ip:{ip} goes down.")
    return
