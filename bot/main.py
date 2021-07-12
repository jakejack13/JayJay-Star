from typing import *

import discord
import os

script_dir = os.path.dirname(__file__)
token_path = "../lib/token.txt"
f = open(os.path.join(script_dir, token_path), "r")
TOKEN = f.read()
client = discord.Client()


async def main_loop():
    """The main loop of JayJay-Star"""
    pass


@client.event
async def on_ready():
    print("Welcome, JayJay")
    await main_loop()


client.run(TOKEN)
