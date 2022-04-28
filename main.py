import discord,asyncio,os
from discord.ext import commands, tasks
from datetime import datetime
import random


token = "DISCORD_BOT_TOKEN" # replace DISCORD_BOT_TOKEN with server token
bot = commands.Bot(command_prefix='.')
message_channel_id = CHANNEL_ID # replace CHANNEL_ID with numerical channel ID
send_time='06:00' # send time on 24 hour format

@bot.event
async  def on_ready():
    change_status.start()
    print('bot is active')

@tasks.loop(seconds=2)
async def change_status():
    channel = bot.get_channel(message_channel_id)
    await bot.change_presence(activity=discord.Game('CUSTOM ACTIVITY STATUS')) # optional custom activity status, can be commented out
    now=datetime.strftime(datetime.now(),'%H:%M')
    value = random.randint(120, 170) # number of pushups value range
    if now == send_time:
        await channel.send("Today we will do %d pushups." % value)
        await asyncio.sleep(61) # task runs every 61 seconds

bot.run(token)
