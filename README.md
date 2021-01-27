# discord-pushup-bot
A simple bot with a simple purpose. To post how many pushups one should do every morning at 05:00. 

It randomizes between 120 and 170 pushups, but can be set to an arbitrary range, or fixed number.

This repo has extra files for Heroku auto deployment and hosting compatibility, but the program itself is not dependent on these files. Meaning you can host it yourself without using Heroku.

# Dependencies
```
discord, random, asyncio, datetime, os
```
# Usage
`"DISCORD_BOT_TOKEN"` is your personal bot token, and needs to be added either as an environment variable, server variable(for server use) or as clear text. 

To run from terminal:
```
python main.py
```

To run for server, see server specific setup guide. 