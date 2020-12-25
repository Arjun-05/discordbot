import discord
from discord.ext import commands
import datetime
import numpy
import random

bot = commands.Bot(command_prefix='Your Prefix', help_command=None, description=None)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('On the lookout for Bugs!'))
    print('Logged on as {0}!'.format(bot.user))

hello_aliases = ["Hi", "hi", "HI"]
@bot.command(aliases=hello_aliases)
async def hello(ctx):
    hello_list = ["Halla!", "Ola!", "Hello!", "Vanakkam!", "Namashkar!", "Ciao!", "Pronto!", "Hallo!", "Supprabatham!", "Bonjour!" , "Privyet!", "Konichiwa!", "Yee Hao!"]
    if ctx.author == bot.user:
        return
    else:
        hello_str = random.choice(hello_list)
        await ctx.send(hello_str)

@bot.command()
async def constants(ctx):
    con_str = "`π = " + str(numpy.pi) + '\n' + "e = " + str(numpy.e) + "`"
    await ctx.send(con_str)

@bot.command()
async def rsum(ctx):
    a = random.randrange(1, 50)
    b = random.randrange(1, 50)
    x = a + b
    randostr = "`" + str(a) + "+" + str(b) + "=" + str(x) + "`"
    await ctx.send(randostr)

@bot.command()
async def rtimes(ctx):
    a = random.randrange(1, 20)
    b = random.randrange(1, 20)
    x = a * b
    randostr = "`" + str(a) + "*" + str(b) + "=" + str(x) + "`"
    await ctx.send(randostr)

@bot.command()
async def rsub(ctx):
    a = random.randrange(1, 50)
    b = random.randrange(1, 50)
    x = a - b
    randostr = "`" + str(a) + "-" + str(b) + "=" + str(x) + "`"
    await ctx.send(randostr)

@bot.command()
async def rdiv(ctx):
    a = random.randrange(1, 20)
    b = random.randrange(1, 20)
    x = a / b
    randostr = "`" + str(a) + "÷" + str(b) + "=" + str(x) + "`"
    await ctx.send(randostr)

@bot.command()
async def date(ctx):
    date_now = datetime.datetime.now()
    date_str = "`" + date_now.strftime("%b") + " " + date_now.strftime("%d") + ", " + date_now.strftime("%Y") + "`"
    await ctx.send(date_str)

@bot.command()
async def time(ctx):
    time_now = datetime.datetime.now()
    time_str = "`" + time_now.strftime("%H") + ":" + time_now.strftime("%M") + ":" + time_now.strftime("%S") + "`"
    await ctx.send(time_str)

suggest_aliases = ["suggestion"]
@bot.command(aliases = suggest_aliases)
async def suggest(ctx, *, suggestion):
    me = bot.get_user(Your ID)
    await  ctx.send("Check your DM for confirmation!")
    await ctx.author.send("Your suggestion was sent. Meanwhile, have a :cupcake:")
    await me.send(suggestion)

@bot.command()
async def whoami(ctx):
    who_str = ctx.author
    await ctx.send(who_str)

whoru_aliases = ["whoareyou"]
@bot.command(aliases = whoru_aliases)
async def whoru(ctx):
    who_str = bot.user
    await ctx.send(who_str)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Commands", description="This embed shows all the available commands",
                          color=discord.Colour.green())
    embed.add_field(name="Prefix", value="<", inline=False)
    embed.add_field(name="Help", value="help - Shows this message", inline=True)
    fun_str = "whoami - Returns who you are!" + '\n' + "whoareu - Who I am!"
    embed.add_field(name="Fun", value=fun_str, inline=True)
    gen_str = "hello - Sends a Hello!" + '\n' + "time - Returns the current time" + '\n' + \
              "date - Returns the current date" + '\n' + "suggest - Sends a suggestion to the Bot's Owner"
    embed.add_field(name="Utility/General", value=gen_str, inline=False)
    math_str = "constants - Returns the value of pi and e" + '\n' + \
               "rsum - Returns the sum of 2 random numbers from 1 to 50" + '\n' + \
               "rsub - Returns the difference of 2 random numbers from 1 to 50" + '\n' + \
               "rtimes - Returns the product of 2 random numbers from 1 to 20" + '\n' + \
               "rdiv - Returns the quotient when 2 random numbers from 1 to 20 are divided"
    embed.add_field(name="Math Stuff", value=math_str, inline=False)
    embed.add_field(name='\n' + "Invite the bot to your server",
                    value="OAuth2 Link")
    embed.set_footer(text="Please use the suggest command for suggestions and bug reports.")
    await ctx.send(embed=embed)

bot.run('Your Token')
