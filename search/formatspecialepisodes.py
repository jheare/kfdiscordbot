class FormatSpecialEpisodes:

    def __init__(self):
        self.boop = "Boop"
        self.number_to_return = []

    def change_multipart_ep_description(self, episode_title):
        if "Obama" in episode_title:
            base_number = "230"
        else:
            base_number = "130"
        if "A" in episode_title:
            return [base_number + ".1"]
        if "B" in episode_title:
            return [base_number + ".2"]
        if "C" in episode_title:
            return [base_number + ".3"]
        if "D" in episode_title:
            return [base_number + ".4"]
        if "E" in episode_title:
            return [base_number + ".5"]
        
    def change_roulette(self, episode_title):
        if "#1" in episode_title:
            return ["10.1"]
        else:
            return ["182.1"]

    def is_roulette(self, episode_title):
        if "Roulette" in episode_title:
            return True

    def mad_at_the_crew(self, episode_title):
        if "Mad At The Crew" in episode_title:
            return True

    def spiritual(self, episode_title):
        if "Spiritual Correction" in episode_title:
            return True
    
    def TWTWYTT(self, episode_title):
        if "TWTWYTT" in episode_title:
            return True

    def halloween(self, episode_title):
        if "Halloween" in episode_title:
            return True

    def repost(self, episode_title):
        if "Repost" in episode_title:
            return True

    def check_special_names(self, episode_title):
        if self.is_roulette(episode_title):
            return self.change_roulette(episode_title)
        if self.mad_at_the_crew(episode_title):
            return ["630.5"]
        if self.spiritual(episode_title):
            return ["41.5"]
        if self.TWTWYTT(episode_title):
            return ["62.5"]
        if self.halloween(episode_title):
            return ["86.5"]
        if self.repost(episode_title):
            return ["585.5"]