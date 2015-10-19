__author__ = 'Nathan A. Smith'

import random
import time

myMagic8Ball = {1: "Yes",
                2: "No",
                3: "Maybe",
                4: "Reconsider",
                5: "Are You Dumb?",
                6: "Sure, if that's what you want to do",
                7: "Send in the clowns",
                8: "Hey, get a load of this guy I'm talking to.",
                9: "Jackball, he's my cousin...are you him?",
                10: "You Bet.",
                11: "I think we have a bad connection.",
                12: "Hold on, I can't contact the spirits...Jerry, go grab my bongos.",
                13: "There's a tiny man in here...someone call Art Bell",
                14: "Consider it over brefkast",
                15: "Don't sign any contracts with Gene Gebell",
                16: "I hear the Clam Bucket is hiring...maybe you can wait tables.",
                17: "Maybe don't quit your day job.",
                18: "Why are you asking me?",
                19: "Go get it",
                20: "Kenny Slag says yes."}


def magic8ball():
    input("What do you want? ")
    my_rand_num = random.randrange(1, 20)
    print("Contacting the Spirit World via Peenman's Crank Radio...")
    time.sleep(3)
    # print(my_rand_num)
    print(myMagic8Ball[my_rand_num])


def main():
    play = 'Y'
    while play != 'N' and play != 'n':
        magic8ball()
        play = input("Play again? (Y/N): ")
    else:
        print("Jeez....finally, I can get rid of this weirded up jackball.")


if __name__ == "__main__":
    main()
