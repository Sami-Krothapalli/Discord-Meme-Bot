import os
import discord
import requests
import json
from dotenv import load_dotenv

load_dotenv()


def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

class MyClient(discord.Client):
    async def on_ready(self):
      print('Logged on as {0}!'.format(self.user))
    
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')
            
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())
        
        if message.content.startswith('$eman'):
            await message.channel.send('Eman sucks at Valorent')

intents = discord.Intents.default()
intents.message_content = True
    
client = MyClient(intents=intents)
token = os.getenv('DISCORD_BOT_TOKEN')
client.run(token)