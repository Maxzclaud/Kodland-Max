import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'You have logged in as {bot.user}')

@bot.command()
async def mem(ctx):
# Dan inilah cara Kamu mengganti nama file dari variabel!
    img_name=random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command("animal")
async def animal(ctx):
    await ctx.send(file=discord.File("images/thumb_cat.jpg"))

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("")