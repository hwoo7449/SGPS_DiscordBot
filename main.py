import discord
import functions as f
from discord.ext import commands
 
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())
 
@bot.event
async def on_ready():
    print('Done')
    await bot.change_presence(status=discord.Status.online, activity=None)
    
@bot.command(aliases=['s', '검색'])
async def search(ctx, *args):
    name: str = ""
    for i in args:
        if name == "":
            name += i
        else:
            name += " " + i
            
    text = f.FindGameSearch(name)
    await ctx.send(text)
    await ctx.send(name)
    
bot.run(f.GetToken())