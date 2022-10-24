import json

def getting_episode_numbers_by_name(name):
    with open('../findepisodedata/KFEpisodeData.json', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
        for x in data:
            if name in data[x]:
                print(x)

#testing names with non ascii characters
getting_episode_numbers_by_name("marina abramović")
#there's a discrepancy in whether or not data is in non ascii or latin I think
getting_episode_numbers_by_name("marina abramovic")
#testing PJDUBBS aka a latin character name
# getting_episode_numbers_by_name("paul joseph watson")