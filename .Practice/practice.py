"""
key feautres:
- 

constraints:
- 

parking system class:
    init (b m s):
        making our 3 vairables (arrays of [car type, num of spots aval, num of spots taken])

    add_car (carType):
        adding a car to parking lot

    remove_car (carType):
        removing a car from parking lot

    check_availability (carType):
        check if car spots full if not return true, otherwise false
"""

import sys

class ParkingSystem:
    def __init__(self, big, medium, small):
        self.big_space = ["Big", big, 0] #o of n space
        #seperate vars is o1, tradeoff
        self.med_space = ["Medium", medium, 0]

        self.small_space = ["Small", small, 0]

        self.num_of_big_spaces = big
        self.num_of_medium_spaces = medium
        self.num_of_small_spaces = small

    def add_car(self, carType):
        if carType == self.big_space[0] and self.num_of_big_spaces < self.big_space[1]:
            self.big_space[2] += 1
            return True
        elif carType == self.med_space[0] and self.med_space[2] < self.med_space[1]:
            self.med_space[2] += 1
            return True
        elif carType == self.small_space[0] and self.small_space[2] < self.small_space[1]:
            self.small_space[2] += 1
            return True
        else:
            return False
    
    def __str__(self):
        print(f"big: {self.big_space}, medium: {self.med_space}, small: {self.small_space}")
        

n = len(sys.argv)
park = ParkingSystem(sys.argv[0], sys.argv[1], sys.argv[2])

print(park.add_car("Big"))

'''
Feedback:
    - loop command line args until q prompt
        - read from OS for testing, constant input
    - key features
    - clarify constraints
        - shows thinking about edge cases
        - keep in mind PAIR PROGRAMMING - need their input too
        - ask questions
        - dont make too many assumptions
            - this is what im thinking...is it correct to assume...
        - dont assume infinite plane for example - need to ask
    - edge cases
        - can we move 0 steps
        - on mars, is there a number of steps to loop around the planet? or is it an infinite plane
        - invalid input? error handling
    - follow blueprint
        - write in sudo code
    - efficiency vs readability
        - using the list vs seperate variables
    - MENTION TRADE OFFS WHY YOU DO WHAT YOURE DOING
        - data structure
        - number of classes
        - precedence to readability - for cooperation purposes
        - scalable
            - sutrcutred like this for modularity
            - can easily implement new features without affecting current ones
        - maintainable
        - potential improvements for the future
            - encapsulation?
    - calm in searching things up
        - admit it, ask to search up syntax
        - i know what i want to do, the syntax is the only issue
        - problem solving is still fine
    - continuous input
        - sys
    - good var names
        - ask them if they think its clear enough
    - since we're pair programming, feel free to nudge me or give feedback
    

- follow ups (5 mins)
    - multi layered? how would you do it (for car parking lot)
    - multiple robots on the same plane?
        - collision?
        - affects movement?
    - what would happen if you turn it off
        - how would struct change if you needed to turn it off
        - constraints:
            - quitting program != turning off
            - turn off = remember where it's at so you can continue after
            - is turn off permanent? no?
                - msut also have a turn on method with the turn on
            - change it so that youre still storing final position in seperate var
            - take blueprint and change it
    - ask constraints again

shopify has a huge pairing culture
from farhan the cto?? he advises it a lot interview by tuple
- how has pairing made you a better programmer (collab opportunities)
- real world impacts on you

shopify values

testing
- after each method
TEST TEST WE LOVE IT WHEN PEOPLE TEST

robot
    init
        bool state (if off, can't move or turn)

    move fwd

    move bwd

    turn right

    turn left

    turn 180

    turn off
        # add bool to init
        # power button from robot?
            # can we still get pos/dir, is it just for movement
            # or is it total off

    turn on

    getpos

    getdir

    getstate (on or off)

main
    printing to terminal (everything has one responsibility)
        input and output, do separately for clarity
'''
