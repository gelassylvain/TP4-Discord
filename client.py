import discord
from discord import Client

##ACTIVATION DU BOT
##IL EST DESORMAIS EN LIGNE SUR DISCORD
client = discord.Client()
client.run("OTU5MzUxNTI4MjQwNjA3Mjgz.YkanvA.A2ISMx69gNUoHZWIm4NcshBnyu8")
class MyBot(Client):
    def init(self):
        super().init()

    async def on_ready(self):
        self.log.infolog(f"{self.user} has connected to Discord!")