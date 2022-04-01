import discord
from discord import Client

client = discord.Client()
@client.event
async def on_ready():
    print("Le bot est prêt !")
client.run("OTU5MzUxNTI4MjQwNjA3Mjgz.YkanvA.dhp0cV7zxFSgkvUw8SkGdb2OsBs")


'''class MyBot(Client):
    def init(self):
        super().init()

    async def on_ready(self):
        self.log.infolog(f"{self.user} has connected to Discord!") '''


