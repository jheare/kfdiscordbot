# kfdiscordbot
Making a Knowledge Fight Discord bot

## data

*(From 5th November 2022)*
__THE LASTEST EPISODE ON THIS REPO IS 739__
This was originally taken off of a GDrive file made by Anonymous Wonk Rexford Tugwell and then edited by CelestAI - https://www.reddit.com/user/CelestAI - on Reddit.

The OG spreadsheet got deleted.

The rest of the data is taken from CelestAI's github repo - https://github.com/RainbowBatch/kfdb

## folders

### misc
Misc just has me sketching out user stories and a potential schema

### refine data
This is the war crimes I committed to get the json into a format I was happy with. It's a lot of for loops but it did the job.

__Sub-folder 'whatsmissing'__
This is what episodes have no people data, no themes data, and no notable bits. These _do_ have deep dive data as that's just automatically extracted from episode transcripts. The rest of the data should be added but that might have to manually which...eep.

## 'the plan' such as it is

Now that I have all of the data formatted how I like I'm gonna try and make a search engine using Whoosh
https://pypi.org/project/Whoosh/ 

If the search engine works for the Discord bot I might as well actually make a search engine tbh.

## get bot

https://discord.com/api/oauth2/authorize?client_id=1031221257846398986&permissions=395137068032&scope=bot

^^^^ That's the link to invite the discord bot to your server