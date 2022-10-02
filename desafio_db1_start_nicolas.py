# Não se esqueça de inserir a chave do bot no final antes de rodar! #

# Bibliotecas necessárias:
# discord
# BeautifulSoup4
# google

import discord
from discord.ext import commands
from googlesearch import search
import asyncio

prefix = '.'
needed_intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=needed_intents)

@bot.event
async def on_ready():
    print("Bot online.")

### Pinga o bot###
@bot.command()
async def ping(ctx):
    await ctx.send(f'_pong!_ ({round (bot.latency * 1000)} ms de latência)')

### Pesquisa no google ###
@bot.command()
async def google(ctx,*, query):
		author = ctx.author.mention
		await ctx.channel.send(f"Resultado da sua pesquisa, {author}:")
		async with ctx.typing():
				for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
						await ctx.send(f"\n {j}")

### Timer simples. Tem muito o que melhorar aqui###
@bot.command()
async def timer(ctx, timeInput):
    try:
        try:
            time = int(timeInput)
        except:
            convertTimeList = {'s':1, 'm':60, 'h':3600, 'd':86400, 'S':1, 'M':60, 'H':3600, 'D':86400}
            time = int(timeInput[:-1]) * convertTimeList[timeInput[-1]]
        if time > 86400:
            await ctx.send("O timer não pode passar de 1 dia.")
            return
        if time <= 0:
            await ctx.send("Nada de tempo negativo!")
            return
        if time >= 3600:
            message = await ctx.send(f"Timer: {time//3600} h {time%3600//60} min {time%60} s")
        elif time >= 60:
            message = await ctx.send(f"Timer: {time//60} min {time%60} s")
        elif time < 60:
            message = await ctx.send(f"Timer: {time} s")
        while True:
            try:
                await asyncio.sleep(5)
                time -= 5
                if time >= 3600:
                    await message.edit(content=f"Timer: {time//3600} h {time %3600//60} min {time%60} s")
                elif time >= 60:
                    await message.edit(content=f"Timer: {time//60} min {time%60} s")
                elif time < 60:
                    await message.edit(content=f"Timer: {time} s")
                if time <= 0:
                    await message.edit(content="0 s")
                    await ctx.send(f"{ctx.author.mention} _Bip! Bip!_ Acabou o tempo!")
                    break
            except:
                break
    except:
        await ctx.send(f"Não posso cronometrar **{timeInput}**....") 

### INSIRA A CHAVE TO BOT AQUI ###	
bot.run('BOT_KEY')