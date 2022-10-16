import json

def getting_episode_numbers_by_name(name):
    with open(r'KFEpisodeData.json', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
        for x in data:
            if name in data[x]:
                print(x)

getting_episode_numbers_by_name("jeff sessions")