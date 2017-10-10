# Import libraries here
import random
from Tkinter import *
__author__ = 'AlexTheGreat'

# Declare lists for use in functions
cards = []
player1_hand = [0, 0]
player2_hand = [0, 0]
hands = []
flop = [0, 0, 0]
turn = [0]
river = [0]


def main():
    assemble_gui()
    # Initiate a new deck
    deck_of_cards()

    # Deal player 1 cards
    assign_player1_hand()

    # Deal player 2 cards
    assign_player2_hand()

    # Flop comes out
    the_flop()

    # turn
    the_turn()

    # river
    the_river()

    # Assemble the GUI
    assemble_gui()


def deck_of_cards():
    global cards

    cards = ["2S","2H","2D","2C","3S","3H","3D","3C","4S","4H","4D","4C","5S","5H","5D","5C",
             "6S","6H","6D","6C","7S","7H","7D","7C","8S","8H","8D","8C","9S","9H","9D","9C","TS","TH","TD","TC",
             "JS","JH","JD","JC","QS","QH","QD","QC", "KS","KH","KD","KC", "AS","AH","AD","AC"]
    #for x in range(0, 52):
        #print cards[x]

    card1 = random.choice(cards)


def hand_combinations():
    global hands
    for x in range(0, 13):
        hands = [i+j for i,j in zip(cards[::1], cards[0::1])]
        print(hands)


def assign_player1_hand():
    global cards
    global player1_hand
    card1 = random.choice(cards)

    print(len(cards))

    for x in range (0, len(cards)):
        if card1 == cards[x]:
            print("testing card matching system")
            print("card1 = ", card1)
            print("matched card = ", cards[x])
            del cards[x]
            print(len(cards))
            break

    card2 = random.choice(cards)

    for x in range(0, len(cards)):
        if card2 == cards[x]:
            print("testing card matching system")
            print("card2 = ", card2)
            print("matched card = ", cards[x])
            del cards[x]
            print(len(cards))
            break

    player1_hand = [card1, card2]
    print(player1_hand)


def assign_player2_hand():
    global cards
    global player2_hand
    card1 = random.choice(cards)

    print(len(cards))

    for x in range (0, len(cards)):
        if card1 == cards[x]:
            print("testing card matching system")
            print("card1 = ", card1)
            print("matched card = ", cards[x])
            del cards[x]
            print(len(cards))
            break

    card2 = random.choice(cards)

    for x in range(0, len(cards)):
        if card2 == cards[x]:
            print("testing card matching system")
            print("card2 = ", card2)
            print("matched card = ", cards[x])
            del cards[x]
            print(len(cards))
            break

    player2_hand = [card1, card2]
    print(player2_hand)


def the_flop():
    global cards
    global flop

    for i in range(0, 3):
        card = random.choice(cards)
        flop[i] = card

        for x in range(0, len(cards)):
            if card == cards[x]:
                print("flop card ", i+1, " test")
                print("flop card ", i+1, " = ", card)
                print("matched card = ", cards[x])
                del cards[x]
                print(len(cards))
                break

    print(flop)


def the_turn():
    global cards
    global turn

    card = random.choice(cards)
    turn[0] = card

    for x in range(0, len(cards)):
        if card == cards[x]:
            print("turn card = ", card)
            print("matched card = ", cards[x])
            del cards[x]
            print(len(cards))
            break

    print(turn)


def the_river():
    global cards
    global river

    card = random.choice(cards)
    river[0] = card

    for x in range(0, len(cards)):
        if card == cards[x]:
            print("river card = ", card)
            print("matched card = ", cards[x])
            del cards[x]
            print(len(cards))
            break

    print(river)


def assemble_gui():

    class Application(Frame):
        """ A GUI application that displays poker hands """

        def __init__(self, master):
            """ Initialize the Frame """
            Frame.__init__(self, master)
            self.grid()
            self.create_widgets()

        def create_widgets(self):
            """ Create labels & buttons that display cards """
            # Create button to deal cards
            self.button1 = Button(self, text="Deal me!")
            self.button1["command"] = self.deal_cards
            self.button1.grid()

            # Deal table cards
            self.button2 = Button(self, text="Flop")
            self.button2.grid()
            self.button2["command"] = self.show_flop

            self.button3 = Button(self, text="Turn")
            self.button3.grid()
            self.button3["command"] = self.show_turn

            self.button4 = Button(self, text="River")
            self.button4.grid()
            self.button4["command"] = self.show_river

            self.button5 = Button(self, text="RE-DEAL")
            self.button5.grid()
            self.button5["command"] = self.re_deal

            # Create labels to display cards
            self.player1_hand = Label(self)
            self.player1_hand.grid()

            self.player2_hand = Label(self)
            self.player2_hand.grid()

            self.flop = Label(self)
            self.flop.grid()

            self.turn = Label(self)
            self.turn.grid()

            self.river = Label(self)
            self.river.grid()

        def deal_cards(self):
            """ Deal cards to the player """
            self.player1_hand["text"] = player1_hand
            self.player2_hand["text"] = player2_hand

        def show_flop(self):
            """Reveal the flop """
            self.flop["text"] = flop

        def show_turn(self):
            """Reveal the turn """
            self.turn["text"] = turn

        def show_river(self):
            """Reveal the river """
            self.river["text"] = river

        def re_deal(self):
            """Re-deal the cards """
            # Initiate a new deck
            deck_of_cards()
            # Deal player1 cards
            assign_player1_hand()

            # Deal player2 cards
            assign_player2_hand()

            # Flop comes out
            the_flop()
            # turn
            the_turn()
            # river
            the_river()

            self.player1_hand["text"] = ""
            self.player2_hand["text"] = ""
            self.flop["text"] = ""
            self.turn["text"] = ""
            self.river["text"] = ""

    root = Tk()
    root.title("Texas Hold'em")
    root.geometry("600x400")

    app = Application(root)

    # Start the GUI
    root.mainloop()


main()
