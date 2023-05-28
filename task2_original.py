# Insert your Student Registration Number (SRN) between the
# quotation marks in the assignment statement below:

SRN = "21008521"

# For example, if your SRN is 01234567 the assignment statement
# should read  SRN = "01234567"

# ----------------------------------------------------------------------------------------------------------------------------
# TASK 2 (10 marks)
# WHAT YOU HAVE TO DO
#
# Modify this script to provide correct implementations of each
# method below that currently contains a code stub
#
# When you have finished, submit the modified version of this script
#
# DO NOT CHANGE the names or parameters of any of these methods
# DO NOT CHANGE the names of the four fields
# Make sure you read the method descriptions carefully
#
# You are not allowed to use any external modules
# in the solution of these problems (no imports)
# ----------------------------------------------------------------------------------------------------------------------------
#
# The script contains a class definition and a program that can
# be used to test its behaviour
#
# To run the program type  play()  at the command line in the
# Python shell
#
# ----------------------------------------------------------------------------------------------------------------------------

class coin_game () :
    # A class of objects that capture the state of a game
    # that involves adding coins to a stack until a target
    # number of coins has been reached
    # The winner is the person who adds the coins to
    # the stack that bring it up to the target number
    # Each coin_game, C, has four fields:
    #  C.target   the target number of coins on the stack
    #             C.target is a positive int
    #  C.coins    the current number of coins on the stack
    #             C.coins is a non-negative int
    #  C.limit    the maximum number of coins that can be
    #             added to the stack in each move
    #             C.limit is a positive int
    #  C.player   the identity of the next player to play
    #             C.player is either 0 or 1

    def __init__ (self,target,limit) :
        # Creates a new coin_game object, using the parameters
        # target and limit, and initialises the identity of the
        # player whose turn it is to play next to 0
        # This method already works correctly
        self.target = target
        self.coins  = 0
        self.limit  = limit
        self.player = 0


# Method 1: 2 marks
    def game_over (self) :
        # Returns True if the target number of coins
        # has been reached (or exceeded)
        # returns False otherwise
        if self.coins >= self.target :
            return True
        
        return False   # code stub


# Method 2: 1 mark   
    def whose_turn_next (self) :
        # Returns the identity of the player whose turn
        # it is to play next
        
        return self.player   # code stub


# Method 3: 2 marks
    def who_played_last (self) :
        # Returns the identity of the player who played
        # the last turn
        if self.player == 0 :
            ID_player = 1
        else :
            ID_player = 0
        return ID_player   # code stub


# Method 4: 1 mark
    def coin_limit (self) :
        # Returns the limit on the number of coins that
        # can be added on each turn
        return self.limit   # code stub




# Method 5: 1 mark
    def stack_target (self) :
        # Returns the target number of coins for the stack
        # When this number is reached (or exceeded) the game
        # is over
        
        return self.target  # code stub


# Method 6: 3 marks
    def play (self,coins_to_add) :
        # Adds the number of coins specified by the parameter
        # coins_to_add and switches to the next player
        self.coins = self.coins + coins_to_add  # code stub
        if self.player != 0:
            self.player = 0
        else :
            self.player = 1

    def __str__ (self) :
        # Returns a string-based representation of the stack of coins
        # in a coin_game object so that it can be displayed using Python's
        # built-in print function
        # This method already works correctly
        stack_as_string = "Target = " + str(self.target) + " coins\n"
        stack_as_string += "Current = " + str(self.coins) + " coins:\n" + ("O" * self.coins)
        return stack_as_string


# ----------------------------------------------------------------------------------------------------------------------------
# DO NOT CHANGE any part of this script between here and
# the end of the file
# ----------------------------------------------------------------------------------------------------------------------------
# GAME PLAY


def play() :
    # Sets up and runs a coin stacking game
    # Once you have got the coin_game class working you should
    # test it by setting up a game with a different target
    # and a different number of coins that can be added on each turn
    # for example    game = coin_game(10,3)
    game = coin_game(10,3)
    print ("Welcome to the coin game")
    print ("Players take it in turns to add coins to a stack")
    print ("until the stack contains " + str(game.stack_target()) + " coins\n")
    print ("You may add between 1 and " + str(game.coin_limit()) + " coins")
    print ("The player who adds the last coin is the winner\n")
    playing = True
    while playing :
        print (game,"\n")
        current_player = game.whose_turn_next()
        print ("It's player",current_player,"to play next")
        while True :
            prompt = "How many coins to add? Maximum " + str(game.coin_limit()) + ": "
            n = int(input(prompt))
            if n >= 1 and n <= game.coin_limit() :
                print ()
                break
        game.play(n)
        if game.game_over() :
            print ("Congratulations player",game.who_played_last(),"you win")
            playing = False
    print ("Thank you for playing")
