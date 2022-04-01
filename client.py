import discord
from discord import Client

client = discord.Client()
@client.event
async def on_ready():
    print("Le bot est prêt !")

@client.event
async def on_message(message):
    print(message.content)

client.run("OTU5MzUxNTI4MjQwNjA3Mjgz.YkanvA.t_dvsKsybX8c8DVfIuRV8pAbKUw")


'''class MyBot(Client):
    def init(self):
        super().init()

    async def on_ready(self):
        self.log.infolog(f"{self.user} has connected to Discord!") '''


