from discord.ext import commands

bot = commands.Bot(command_prefix="!") #cree une instance d'un bot qu'on met dans une variable bot qu'on va préfixer par "!" 

@bot.event
async def on_ready():
    print("Le bot est prêt.") 

@bot.command(name='del')
async def delete(ctx, number_of_messages: int):
        messages = await ctx.channel.history(limit=number_of_messages +1).flatten()

        for each_message in messages:
            await each_message.delete() 


bot.run("OTU5MzUxNTI4MjQwNjA3Mjgz.YkanvA.wDYC_Yk2auG2SH7Yjv2P18GWGm4")