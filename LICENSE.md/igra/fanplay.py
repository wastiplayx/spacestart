#import some moduls from python
import discord
import asyncio
import os
from discord.ext import commands
from discord.utils import get
client = commands.Bot( command_prefix = ".")
client.remove_command("help")
# events 
@client.event
async def on_ready():
	print("[LOG] {0} запущено".format(client.user))
	await client.change_presence(status = discord.Status.online,activity = discord.Game("$help"))
@client.event
async def on_member_join(member):
    guild = client.get_guild(member.guild.id)
    channel = client.get_channel(702488510745149461)
    u = len(guild.members)
    await channel.edit(name = "Пользователи:{0}".format(u))
@client.event
async def on_member_remove(member):
    guild = client.get_guild(member.guild.id)
    channel = client.get_channel(702488510745149461)
    u = len(guild.members)
    await channel.edit(name = "Пользователи:{0}".format(u))
@client.command()
async def help(ctx):
    embed = discord.Embed(title = "вы смотрите команду .help",description = "Привет {0} ты смотриш команду .help".format(ctx.message.author),colour = discord.Color.purple)
    embed.add_field(name = "Зачем это бот",value="Бот создано исключительно в развлекательных целях",inline=False)
    embed.add_field(name = "Есть ли команды у бота",value = "Возможно будет скоро",inline = False)
    embed.set_footer(text = "Aвтор:wastiplayx#9098",icon_url = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBw4NDQ0ODQ0NDQ4NDQ0NDQ8NDQ8NDQ0NFREWFhURExMYHSggGBolGxMTITEhJSkrLi4uFx8zODMsNygtLisBCgoKDQ0NDw0NDisZFRkrKystNys3KysrKy0rKystKysrKysrLSsrKysrKysrKysrKysrKysrKysrKysrKysrK//AABEIAOEA4QMBIgACEQEDEQH/xAAaAAEAAwEBAQAAAAAAAAAAAAAAAQIDBAUH/8QAKhABAQACAQIGAgIBBQAAAAAAAAECEQMhMRJBUWFxkQQyE6GBIkJScoL/xAAUAQEAAAAAAAAAAAAAAAAAAAAA/8QAFBEBAAAAAAAAAAAAAAAAAAAAAP/aAAwDAQACEQMRAD8A+SAAAAAUAAAQkAFbnJ7gsM7nVd0GwwAbjGW+60zvyDQVmcqwAAAAAAAAAAAAAAAAAACLlIrln6MwWyytVAAAAAAABbHKz3VAbS7Swa457BYAAAAAAAAAAAAABTkv9rss7ugqAACmeYLZZaZ3kZ2gLfyU/kqgDWcvq0l25lsctA6BXHLawAANcLuLMsL1+WoAAAAAAAAAAAAIyuoxaclZgArnloEcmeuzEt2gAAAAAAFsctN8ctxzJxugdIjDLcSA3lYNeO9AWAAAAAAAAAAABnyXqonLvUAVz5XdX5cvL7ZAAAAAAAAAAAvx5ardzNuPLYLr8XeqLYXrAagAAAAAAAAAAUGFRldRLLmy8gZ27QAAlAAAAAAAAAC2N1VUg6Ymd58xnxZLg3AAAAAAAAAARl2vwlXLtQZObK7rbmvRjICBpjw5Xy++jXH8b1v0Dnhp3Y8eM8onp7A4NDtvh9vtFmHsDj0adfgw9Z9ngw9vsHJo07NYeyZ4fYHFod+pfRW8ON8gcI6cvxvS/bLLiynl9dQVwuq6HNY24stz4B1QRj2nwkAAAAAAAABGfapU57/poOPky3U4Z694qA6MbvWvLvq2LTt52/8AauWXTXDl9e3sDTXbpLq9b3ti2Vnlj6eUVnbfTXz1TsE+LrvXkeLrvXfyQAeKeG9t6qcspqa63ogBPi671/g8XW3XpPJACcda6z+oprp211W2jLpN3t/YF9un/qozy1vfn2626Z5cvp29+tZ2gtnns48tVRIO/DtPiJV4/wBZ8RYAAAAAAAABTn/Wrq83634BwoTUAAAtMrOzonNMsbL0s7fLlAddmv8AKPF5MZy35aXnlmtAvf8AH2a+PtTLlx66n+2zt5pnLj13PKTtATtMm9+yn881rXlpllyWg2z5pMdTrdOe3fdAAAAmITAd3H+s+IsrxfrFgAAAAAAAAIry/rfhdny/rfgHEhKAAAAAAAAAAAAAAAEoSDt4f1i6nF+sXAAAAAAAIACM50qS9gefUJqAAAAAAAAAAAAAAAEiZAdvF2iyMJqRIAAAAAAAAAAMOfh31jmr0GfLwzL2oOIWzws7qgAAAAAAAAAAA04+O3sCkjp4eHXWtOPimPyuAAAAAAAAAAAAAACMsZe7Dk/H/wCLoAcGWFneIehZtlnwS9ugOMb5fjXy1VLw5TyBmL/x30v1T+O+l+gUF5x5elaY/j3z6AwWxwt7R1Y/jyd+rWTQOfj/AB/X6dEmuwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA//9k=")
    await ctx.send(embed = embed)





  
#run our bot
t = os.environ.get("token")
client.run(str(t))