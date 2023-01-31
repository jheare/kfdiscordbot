class ShortenMessage():

    def __init__(self):
        self.boop = "Boop"
        self.limitreached = "\nDISCORD LIMIT REACHED\nPLEASE USE SITE FOR MORE RESULTS"


    def shorten_message(self, message):
        print(len(message))
        message_huh = 2000 - len(message) - 57
        print(message_huh)
        print(len(message) - abs(message_huh))
        new_message = message[:-abs(message_huh)]
        newnewmessage = new_message + self.limitreached
        print(len(newnewmessage))
        return newnewmessage
        #new_message_length = len(message) 




#message = "19: March 3, 2017\n* 48: May 31, 2017\n* 53: June 12, 2017\n* 58: June 23, 2017\n* 62: August 19-26, 2015\n* 82: Oct. 27-Nov. 9, 2015\n* 83: November 10-12, 2015\n* 101: January 11, 2016\n* 105: March 18, 2014\n* 106: Drunk Special Report\n* 107: December 12, 2014\n* 108: November 30, 2017\n* 131: David Lynch Interview\n* 133: Operation Paul Revere\n* 168: Alex Vs. Bill Ayers\n* InfoWars Roulette #2\n* 204: Sweary Kerry's Larry\n* 206: March 4-5, 2009\n* 213: October 2, 2018\n* 215: March 11-12, 2009\n* 217: Space Liars and Dragon Moths\n* 223: A Progressive Space Diplomat\n* 224: March 20, 2009\n* 230B: Obama Deception, Part 2\n* 237: March 27, 2009\n* 240: March 30-31, 2009\n* 246: April 5-6, 2009\n* 249: Predicting 9/11\n* 250: Remote Poisoners And Crypto Bigotry\n* 251: January 8, 2019\n* 252: April 7-8, 2009\n* 254: April 9-10, 2009\n* 261: February 5-6, 2019\n* 281: April 4, 2019\n* 287: April 15-18, 2019\n* 293: May 2-3, 2019\n* 298: January 20-23, 2013\n* 300: May 21-22, 2019\n* 302: Discernment Overload\n* 303: January 29-31, 2013\n* 307: February 3-5, 2013\n* 309: June 10-11, 2019\n* 313: June 23-24, 2019\n* 317: February 19-20, 2013\n* 323: July 19, 2019\n* 326: July 26-29, 2019\n* 329: August 4-5, 2019\n* 333: August 16, 2019\n* 334: August 21-22, 2019\n* 335: March 15-22, 2013\n* 336: March 24-26, 2013\n* 342: September 6-11, 2019\n* 348: September 24-25, 2019\n* 352: April 17, 2013\n* 356: October 11, 2019\n* 386: January 8, 2020\n* 387: May 13, 2014\n* 389: January 15-17, 2020\n* 392: January 24, 2020\n* 394: January 31, 2020\n* 400: One Out Of Five Seems High\n* 423: April 20, 2020\n* 430: May 5-7, 2020\n* 435: May 18-21, 2020\n* 447: Bill Cooper Covers OKC Part 2\n* 454: December 17, 2013\n* 456: July 9-11, 2020\n* 470: ShadowGate\n* 471: August 14-16, 2020\n* 473: August 20-21, 2020\n* 480: September 9-10, 2020\n* 488: The First Debate Spectacular\n* 502: Dan's Cara-Vanity Project Part 1\n* 508: December 1-2, 2020\n* 516: December 31, 2020- January 1, 2021\n* 517: January 5-6, 2021\n* 527: February 4, 2021\n* 534: February 19, 2021\n* 541: March 17-18, 2021\n* 549: April 13-14, 2021\n* 551: April 20-21, 2021\n* 559: Noam Man's Land\n* 564: May 15-20, 2003\n* 568: June 19, 2021\n* 586: August 11-12, 2021\n* 603: October 3-4, 2021\n* 604: October 5, 2021\n* 623: July 2-3, 2003\n* No One Is Mad At The Crew\n* 631: December 20, 2021\n* 635: January 6-7, 2022\n* 644: February 2, 2022\n* 647: February 8, 2022"

# shorten = ShortenMessage()
# shorten.shorten_message(message)