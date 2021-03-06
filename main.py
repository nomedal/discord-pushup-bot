import discord
from discord.ext import commands, tasks
import random
import asyncio
from datetime import datetime
import os

class PushupBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def my_background_task(self):
        await self.wait_until_ready()
        channel = self.get_channel(message_channel_id) # channel ID goes here
        while not self.is_closed():
            now=datetime.strftime(datetime.now(),'%H:%M')
            value = random.randint(120, 170)
            if now == send_time:
                await channel.send("Today we will do %d pushups." % value)
                await asyncio.sleep(60) # task runs every 60 seconds

if __name__ == "__main__":
    send_time='05:00'
    token = os.getenv("DISCORD_BOT_TOKEN")
    message_channel_id = 792133366295822337

    client = PushupBot()
    client.run(token)
