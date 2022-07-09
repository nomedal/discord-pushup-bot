FROM python:3.10
ADD pushupbot.py .
RUN pip install discord.py asyncio
CMD [ "python3", "./pushupbot.py" ]
