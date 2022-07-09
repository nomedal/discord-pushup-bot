# discord-pushup-bot
A simple bot with a simple purpose. To post how many pushups one should do every morning at 06:00. 

It randomizes between 120 and 170 pushups, but can be set to an arbitrary range, or fixed number.

It is fully self-hosted using python 3.10

# Dependencies
```
discord, random, asyncio, datetime
```
# Usage
The variables below needs to be added either as an environment variable, server variable(for server use) or as clear text.
`"DISCORD_BOT_TOKEN"` is your personal bot token.
`CHANNEL_ID` is your numerical channel ID.
`CUSTOM ACTIVITY STATUS` is an optional custom activity status for your bot. Can be commented out or removed if not wanted.

It's highly recommended using `screen` when running the bot undockerized.

To run from terminal:
```
python3 pushupbot.py
```
