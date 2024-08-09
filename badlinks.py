import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord import SelectOption
from discord.ui import View, Button, button
import time
import random
import requests
import asyncio
import datetime
import json
import os
import re

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.guilds = True

client = discord.Client(intents=intents)

def badlinks_message( cn, message, text ):
    check = False
    text = text.lower()
    text = text.strip()
    match = re.search(r"(teenleaks\.xyz)", text)
    if match:
        check = True
        print('Found Bad Link')
        return check    
        
    match = re.search(r"(discord\.gg|discord\.com/invite|discordapp\.com/invite)", text)
    if match:
        check = True
        print('Found Bad Link')
        return check    
    
    match = re.search(r"(tiktok\.com)", text)
    if match:
        check = True
        print('Found Bad Link')
        return check
    
    match = re.search(r"(dpdz\.xyz)", text)
    if match:
        check = True
        print('Found Bad Link')
        return check
        
    match = re.search(r"(verham93\.de)", text)
    if match:
        check = True
        print('Found Bad Link')
        return check
        
    match = re.search(r"(t\.me|tg\.com|telegram\.com)", text)
    if match:
        check = True
        print('Found Bad Link')
        return check   
        
    match = re.search(r"(mega\.io|mega\.com|mega\.nz)", text)
    if match:
        check = True
        print('Found Bad Link')
        return check
        
    match = re.search(r"(cyberdrop\.com|cyberdrop\.net|cyberdrop\.org|thothub\.com|pornhub\.com|thothub\.ru|thothub\.su|bunkrr\.su|bunkrr\.com|bunkrr\.ru|bunkrr\.sk|bunkr\.su|bunkr\.com|bunkr\.ru|bunkr\.sk)", text)
    if match:
        check = True
        print('Found Bad Link')
        return check
        
        
    if text in badlinks:
        check = True
        print('Found Bad Link')
        
    return check
  
@client.event
async def on_message( message ):
    channel = message.channel
    if badlinks_message( channel, message, message.content ):
        await asyncio.sleep(4.1)
        await message.delete()
        mention = message.author.mention
        await channel.send(f'Csúnyán beszéltél {mention}. Ezért töröltem az üzeneted. Mosd ki a fogad!!!')
        return
client.run("TOKEN")
