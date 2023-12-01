# Family name: Samarventhan Surendran
# Student number:  300376981
# Course: IT1 1120 
# Assignment Number 4
# year 2023


####
#2
####

# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     other=[]

     for i in range(len(deck)):
         if i %2==0:
             dealer.append(deck[i])
         else:
             other.append(deck[i])

     return (dealer, other)
 


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs = []

    for ch in l:
        num_card = ch[0]
        pair = False

        new_pair = []
        for card in no_pairs:
            if card[0] == num_card and not pair:
                pair = True
            else:
                new_pair.append(card)
        no_pairs = new_pair

        if not pair:
            no_pairs.append(ch)

    random.shuffle(no_pairs)

    return no_pairs


def print_deck(deck):
    
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    for ch in deck:
        print(ch)
    
def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''

     ask_input=0
     while ask_input<1 or ask_input > n:
         ask_input= int(input("Give me an integer between 1 and "+str(n)+": "))
         if ask_input<1 or ask_input>n:
             print("Invalid number. Please enter integer between 1 and "+str(n))
     return ask_input

def play_game():
     '''()->None
     This function plays the game'''
    
     deck = make_deck()
     shuffle_deck(deck)
     tmp = deal_cards(deck)

     dealer = tmp[0]
     human = tmp[1]

     print("Hello. My name is Robot, and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:\n")
     print_deck(human)
     print("\nDo not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     dealer = remove_pairs(dealer)
     human = remove_pairs(human)

     player_turn = True

     while len(human) > 0 and len(dealer) > 0:
         print("***********************************************************")
         if player_turn:
             print("Your turn.")
             print("\nYour current deck of cards is:\n")
             print_deck(human)
             print("\nI have", len(dealer), "cards. If 1 stands for my first card and")
             print(len(dealer), "for my last card, which of my cards would you like?")
             selected_card = get_valid_input(len(dealer))
             selected_card_pos = selected_card - 1
             selected_dealer_card = dealer[selected_card_pos]
         
             if selected_card == 1:
                 selected_card = "1st"
                 print("You asked for my", selected_card, "card.")
             elif selected_card == 2:
                 selected_card = "2nd"
                 print("You asked for my", selected_card, "card.")
             elif selected_card == 3:
                 selected_card = "3rd"
                 print("You asked for my", selected_card, "card.")
             elif 3 < selected_card < 20:
                 selected_card = str(selected_card) + "th"
                 print("You asked for my", selected_card, "card.")
         
             print("Here it is. It is", selected_dealer_card)
         
             human.append(selected_dealer_card)
             dealer.pop(selected_card_pos)
         
           
             print("\nWith", selected_dealer_card, "added, your current deck of cards is:\n")
             print_deck(human)
         
             dealer = remove_pairs(dealer)
             human = remove_pairs(human)
         
            
             print("\nAnd after discarding pairs and shuffling, your deck is:\n")
             print_deck(human)
             wait_for_player()
         else:
             print("My turn.\n")
             if len(human) > 0:
                 took_card = random.randint(0, len(human) - 1)
                 dealer_card = human[took_card]
                 num_took_card = took_card + 1
                 if num_took_card == 1:
                     num_took_card = "1st"
                     print("I took your", num_took_card, "card.")
                 elif num_took_card == 2:
                     num_took_card = "2nd"
                     print("I took your", num_took_card, "card.")
                 elif num_took_card == 3:
                     num_took_card = "3rd"
                     print("I took your", num_took_card, "card.")
                 elif 3 < num_took_card < 20:
                     num_took_card = str(num_took_card) + "th"
                     print("I took your", num_took_card, "card.")
                 
                 dealer.append(dealer_card)
                 human.pop(took_card)
    
             dealer = remove_pairs(dealer)
             human = remove_pairs(human)

             wait_for_player()
        
         player_turn = not player_turn

     if "Q" in human:
         print("***********************************************************")
         print("Ups. You do not have any more cards")
         print("You lost! I, Robot, win") 

     elif len(human) == 0:
         print("***********************************************************")
         print("Ups. You do not have any more cards")
         print("Congratulations! You, Human, win")

     if "Q" in dealer:
         print("***********************************************************")
         print("Ups. You do not have any more cards")
         print("Congratulations! You, Human, win")

     elif len(dealer) ==0:
         print("***********************************************************")
         print("Ups. I do not have any more cards")
         print("You lost! I, Robot, win")
             
    
	
	 

# main
play_game()
