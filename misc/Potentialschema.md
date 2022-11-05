# Potential Schema

Trying to work out a potential schema so that the for loops can get changed to an indexed search engine.

## Idea for search engine - 
This was suggested to me on Reddit and sounds like a good idea. It looks as though you can have multiple indices which helps for the multitude of queries I think people are going to want to make

https://github.com/darenr/python-whoosh-simple-example/blob/master/example.py

## Ideas (Draft)

Index: People

Index: Subject _(Key words from episodes picked up in transcripts)_

Alternative spellings? (entity sourcetexts)

Themes: List of themes (should be able to search for partial matches in items)

_Additional info (not indices)_

Episode number

Episode Title


___The below refers to the files found in the github repo: https://github.com/RainbowBatch/kfdb ___

## What raw data is in raw_entities that's excluded from final.json? (before sort)

__Extremely important information__
* Key words from episodes as picked up in the transcripts
* Entity sourcetexts (which appear to be good alternative spellings/formats of existing topics?)

## What raw data is in the final.json file? (before sort)

__Extremely important information__
* Episode title
* Notable bits (Example 'ya busted')
* Themes (example '"Black face isn't racist"')
* Episode number
* People

__Medium important information__
* Dates the episode covers
* Download link

__Slightly relevant to people__
* Category - (Subject? - example: 'present day')
* Release date

__Not particularly relevant to anyone__
* Episode summary/"details.html" (there is html episode description, is less relevant than meta-data above)
* Embed player url - you can probably embed on Discord but I'm not sure if this is useful or not
* Episode length
* Episode type (Says 'present day' which is the same as the category)
* Beverage

## SK used by wiki

* "sortkey": "#_EPISODE_0011:February 10, 2017",

__"# + EPISODE + NUMBER : Clean title"__