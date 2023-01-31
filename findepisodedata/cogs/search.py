import discord
from discord import app_commands
from discord.ext import commands

import simplejson as json
import requests

class Search(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Search cog is loaded')

    @commands.command()
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync()
        await ctx.send(
            f"Synced {len(fmt)} commands to the server"
        )
        return

    #@commands.Command()
    @app_commands.command(name="episodebyperson", description="Find episodes featuring...")
    async def episodebyperson(self, interaction: discord.Interaction, person: str):
        jsontosend = {
        "fields": ["people_tostring", "topics_tostring"],
        "queries": [person]
        }
        personsearch = requests.post("https://62fm88kr45.execute-api.us-east-1.amazonaws.com/prod/standardquery", data = json.dumps(jsontosend))
        formatresp = json.loads(personsearch.text)
        formatbody = json.loads(formatresp['body'])
        episode_array = []
        searchurl = "http://fin.apps-kf-search-prod.s3-website-us-east-1.amazonaws.com/"
        footertext = "Want to see more detail? Check out the search engine"
        footericon = "https://pbs.twimg.com/profile_images/1071046862080221184/MaGfASpN_400x400.jpg"
        for i in formatbody:
            episode_array.append(i)
        if len(episode_array) == 1:
            messagestring = "\n * ".join(episode_array)
            embed=discord.Embed(title=f"`{person}` -s in episode:", description="* " + messagestring, url=searchurl)
            embed.set_footer(text=footertext, icon_url=footericon)
            await interaction.response.send_message(embed=embed)
        if len(episode_array) > 1:
            messagestring = "\n * ".join(episode_array)
            embed=discord.Embed(title=f"`{person}` is in episodes:", description="* " + messagestring, url=searchurl)
            embed.set_footer(text=footertext, icon_url=footericon)
            await interaction.response.send_message(embed=embed)
        else:
            embed=discord.Embed(title="Nothing found!", url=searchurl)
            embed.set_image(url="https://media.tenor.com/5U4tWWKQGDkAAAAM/alex-jones-crying.gif")
            await interaction.response.send_message(embed=embed)

    @app_commands.command(name="alexsays", description="When did Alex say...")
    async def alexsays(self, interaction: discord.Interaction, alexsays: str):
        jsontosend = {
        "fields": ["alex_says_tostring"],
        "queries": [alexsays]
        }
        alexsayssearch = requests.post("https://62fm88kr45.execute-api.us-east-1.amazonaws.com/prod/standardquery", data = json.dumps(jsontosend))
        formatresp = json.loads(alexsayssearch.text)
        formatbody = json.loads(formatresp['body'])
        episode_array = []
        for i in formatbody:
            episode_array.append(i)
        print(len(episode_array) == 1)
        searchurl = "http://fin.apps-kf-search-prod.s3-website-us-east-1.amazonaws.com/"
        footertext = "Want to see more detail? Check out the search engine"
        footericon = "https://pbs.twimg.com/profile_images/1071046862080221184/MaGfASpN_400x400.jpg"
        if len(episode_array) == 1:
            messagestring = "\n * ".join(episode_array)
            embed=discord.Embed(title=f"Alex says `{alexsays}` in episode:", description=messagestring, url=searchurl)
            embed.set_footer(text=footertext, icon_url=footericon)
            await interaction.response.send_message(embed=embed)
        if len(episode_array) > 1:
            messagestring = "\n * ".join(episode_array)
            embed=discord.Embed(title=f"Alex says `{alexsays}` in episodes:", description=messagestring, url=searchurl)
            embed.set_footer(text=footertext, icon_url=footericon)
            await interaction.response.send_message(embed=embed)
        else:
            embed=discord.Embed(title="Nothing found!", url=searchurl)
            embed.set_image(url="https://media.npr.org/assets/img/2022/08/05/ap22216570430921-2dceca1166ed5d3a06b0c717f3a7da7c80c6c9c9-s1100-c50.jpg")
            await interaction.response.send_message(embed=embed)
        

    @app_commands.command(name="topics", description="When do they talk about...")
    async def topics(self, interaction: discord.Interaction, topic: str):
        jsontosend = {
        "fields": ["topics_tostring"],
        "queries": [topic]
        }
        topicsearch = requests.post("https://62fm88kr45.execute-api.us-east-1.amazonaws.com/prod/standardquery", data = json.dumps(jsontosend))
        formatresp = json.loads(topicsearch.text)
        formatbody = json.loads(formatresp['body'])
        episode_array = []
        searchurl = "http://fin.apps-kf-search-prod.s3-website-us-east-1.amazonaws.com/"
        footertext = "Want to see more detail? Check out the search engine"
        footericon = "https://pbs.twimg.com/profile_images/1071046862080221184/MaGfASpN_400x400.jpg"
        for i in formatbody:
            episode_array.append(i)
        if len(episode_array) == 1:
            messagestring = "\n * ".join(episode_array)
            embed=discord.Embed(title=f"`{topic}` comes up in episode:", description="* " + messagestring, url=searchurl)
            embed.set_footer(text=footertext, icon_url=footericon)
            await interaction.response.send_message(embed=embed)
        if len(episode_array) > 1:
            messagestring = "\n * ".join(episode_array)
            embed=discord.Embed(title=f"`{topic}` comes up in episodes:", description="* " + messagestring, url=searchurl)
            embed.set_footer(text=footertext, icon_url=footericon)
            await interaction.response.send_message(embed=embed)
        else:
            embed=discord.Embed(title="Nothing found!", url=searchurl)
            embed.set_image(url="https://static.independent.co.uk/2022/09/22/21/SEI126493450.jpg")
            await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Search(bot))