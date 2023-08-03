from asyncio import SendfileNotAvailableError
import discord

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='', intents=intents)
from bot2token import tok1en


tavsiye = ['atıkları ayır ve geri donustur','atık yağları lavaboya  dökme atık yağ toplama kutularına dök','arabalara filtre takın veya  filtresiz fabrikaları uyarın']

soyle = ()

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'atık temizlemeyi öğrenmek için temizle  , insanları biliçlendir meyi öğrenmek için biliçlendir , resim için resim yazın')



@bot.command()
async def temizle(ctx):
    await ctx.send(f'atiklari temizlemeyi öğrenmek için cevre 1 , atik yağlari temizlemeyi öğrenmek için cevre_iki  , duman sorununu çözmeyi öğrenmek için cevre_uc yazin')

@bot.command()
async def cevre(ctx,number:int ):
    if int(number) == 1:
            await ctx.send(tavsiye[number - 1]) 
    if int(number) == 2:
            await ctx.send(tavsiye[number - 1]) 
    if int(number) == 3:
            await ctx.send(tavsiye[number - 1])     
        
@bot.command()
async def biliçlendir(ctx):
    await ctx.send(f'okularda ders verilebilir veya bröoşür asılabilir sosyal medyaya çevre kirliliği ile ilgili içerikler paylaşılabilir')
                   
@bot.command()
async def resim(ctx):
    with open('cevre_bot\img\mem2.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    

bot.run(tok1en)