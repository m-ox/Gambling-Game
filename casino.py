import numpy

class Casino():

    # essential variables
    credits = 100
    fingers = 5
    finger_bet = 1
    bet_amount = None
    finger_bet_accepted = False
    yes_list = ["yes", "y", "yeah", "ok"]
    no_list = ["no", "n"]

    def __init__(self):
        self.intro()
        self.main_menu()

    
    def die(self):
        roll = numpy.random.randint(1, 7, size = 4) # default_rng() is the not depreciated random integer function... 
        return roll


    def intro(self):
        input("\nYou step outside of the casino and begin to pass a darkened alley way to head home.\n")
        input("A seedy lookin' feller catches your eye and gestures yer way.\n")
        input("As he motions to you and you get closer, you notice his hand is missin' two fingers.\n")


    def main_menu(self):
        gamble_time = input("\"Sir, would ya be interested in some... high reward gamblin'?\" He flashes a repugnant smile.\n\n  (YEAH)   (NO)   >>> ").lower()

        if gamble_time == "let's cut to the chase" or gamble_time == 'ff':
            input("\n\"Alright, make your bet...\"\n")
            self.place_bets()

        elif gamble_time in self.yes_list:
            input("\n\"That's what I like to hear. The game is like this:")
            input("\n\"I have a couple dice here... Whichever of us two can roll the highest combo, wins a matched amount put in.\"")
            game_accept = input("\n\"What do you say?\"\n\n  (YEAH)   (NO)   >>> ")

            if game_accept in self.yes_list:
                input("\n\"Alright, make your bet...\"\n")
                self.place_bets()

            elif game_accept in self.no_list:
                input("\n\"Oh. Ok. Nevermind then.\"\nSuddenly the man seems to disappear into the air.")
                exit()

            else:
                input("\n\"I couldn't quite make that out... Lemme start over...\"\n")
                self.main_menu()

        elif gamble_time in self.no_list:
            input("\n\"Oh. Ok. Nevermind then. The fades away. Was that a ghost?\"")
            exit()

        else:
            input("\n\"I couldn't quite make that out... Lemme start over...\"\n")
            self.main_menu()


    def place_bets(self):
        print(f"You currently have {self.credits} credits.\n")

        self.bet_amount = input("How much would you like to bet? | (5) (10) (50) (custom) >>> ")

        if self.bet_amount == 'custom':
            special_bet = input("\nWhat would you like to bet? | (1. custom credit amount) (2. credits and finger) >>> ").lower()

            if special_bet == '1' or special_bet == "credits" or special_bet == "custom credit amount":
                print(f"\nYou currently have {self.credits} credits.\n")
                self.bet_amount = int(input("Wager credit amount: "))
                
                if self.bet_amount > 0:
                    print(f"\nYou are wagering {self.bet_amount}.\n")
                    self.credits -= self.bet_amount
                    self.rolling_rolling()

                else:
                    input("\n\"I couldn't quite make that out... Lemme start over...\"\n")
                    self.place_bets()


            elif special_bet == '2' or special_bet == "credits and finger" or special_bet == "finger":
                special_bet_accept = input("\nWARNING! Wagering a finger is technically free, but the monetary gain/loss is multiplied by ten fold!\n\nDo you wish to proceed?\n\n  (YEAH)   (NO)   >>> ").lower()

                if special_bet_accept in self.yes_list:
                    print(f"\nYou currently have {self.credits} credits.\n")

                    self.bet_amount = int(input("How much would you like to bet? >>> "))

                    if self.bet_amount > 0:
                        self.finger_bet = 5
                        print(f"\nYou are wagering {self.bet_amount} and a finger.\n")
                        self.credits -= self.bet_amount
                        self.finger_bet_accepted = True
                        self.rolling_rolling()
                    else:
                        input("\n\"I'm not sure you understand I don't understand what you're saying...\"\n")
                        self.place_bets()

                else:
                    print("It's okay, don't make any hasty decisions...\n")
                    self.place_bets()

            else:
                input("\n\"I couldn't quite make that out... Lemme start over...\"\n")
                self.place_bets()


        elif self.bet_amount == '5':
            print(f"\nYou currently have {self.credits} credits.")
            self.bet_amount = 5
            self.credits -= self.bet_amount
            print(f"\nYou are wagering {self.bet_amount} credits.\n")
            self.rolling_rolling()

        elif self.bet_amount == '10':
            print(f"\nYou currently have {self.credits} credits.")
            self.bet_amount = 10
            self.credits -= self.bet_amount
            print(f"\nYou are wagering {self.bet_amount} credits.\n")
            self.rolling_rolling()

        elif self.bet_amount == '50':
            print(f"\nYou currently have {self.credits} credits.")
            self.bet_amount = 50
            self.credits -= self.bet_amount
            print(f"\nYou are wagering {self.bet_amount} credits.\n")
            self.rolling_rolling()

        else:
            input("\n\"I couldn't quite make that out... Lemme start over...\"\n")
            self.place_bets()


    def rolling_rolling(self):
        input("\"Alright, let 'er roll...\"\n")
        input(' . \n')
        input(' . \n')
        input(' . \n')
        roll_results = self.die()
        print(f'You rolled a {roll_results[0]} and a {roll_results[1]}!\n\nThe creepy man rolled a {roll_results[2]} and a {roll_results[3]}!\n')

        # WIN
        if (roll_results[0] + roll_results[1]) > (roll_results[2] + roll_results[3]):
            print(f"You won your {self.bet_amount} credits and a matched amount from the weird guy.\n")
            self.credits += self.bet_amount * 2 * self.finger_bet
            finger_bet = 1
            print(f"You now have {self.credits} credits.\n")
            self.play_again()

        # LOSE
        if (roll_results[0] + roll_results[1]) < (roll_results[2] + roll_results[3]):

            if self.finger_bet_accepted == True:
                self.credits -= self.bet_amount * (self.finger_bet * 4 - 1)
                finger_bet = 1
                self.finger_bet_accepted = False

                if self.credits <= 0:
                    print("You have lost all your money to this weird guy, but more importantly-- have to give up your finger!\n")
                    print("Suddenly, your wagered finger simply vanishes off your hand! The freaky guy laughs. Clearly, this guy is a horrible vengeful spirit who collects fingers.\n")
                    print("You are also broke. Game over.")
                    exit()
                
            elif self.credits <= 0:
                input("You have lost all your money to this weird guy!\n")
                print("The man cackles and begins to spin off the ground, levitate and promptly disappears with all of your cash.")
                exit()

            print(f"You now have {self.credits} credits.\n")
            self.play_again()

        # DRAW
        if (roll_results[0] + roll_results[1]) == (roll_results[2] + roll_results[3]):
            input("You tied! Re-roll...\n")
            self.credits += self.bet_amount
            self.rolling_rolling()

    def play_again(self):
        play_again = input("Do you want to play again? >>> ").lower()
        
        if play_again in self.yes_list:
            print("\nOkay, you want to play again...\n")
            self.main_menu()

        elif play_again in self.no_list:
            print("\nSuddenly the man fades away because he was a ghost the whole time with a bitter grudge against fully fingered people and now all he does all night next to this casino that regularly emptied his pockets every other day back when he was alive is gamble scruffy looking nerds and try and get them to lose their fingers for big ghost coin winnings but ultimately when daytime comes if they do win they money they won from him was ghost money and now it is gone it fades with the day, man. So yeah, he wasn't even real.\n")
            exit()

        else:
            print("\n\"I couldn't quite make that out... Lemme start over...\"\n")

Casino()
        