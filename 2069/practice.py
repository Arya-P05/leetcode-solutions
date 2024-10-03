'''
key features:
- create the grid
- store the robots position after each move
- store the robots direction after each move
- having a method to move/turn the robot depending on user input

contraints:
- min and max of width and height
- is 0 steps a thing

you provide tests or I make as I go, farhan made me realize the importance

class Robot():
    init:
        width
        height
        x
        y
        directions (all 4 directions) - array of tuples [(1, 0), (0, -1), (-1, 0), (0, 1)]
        direction_idx = 0
        directionLabels = ["East", "South", "West", "North"]
    
    moving_forward:
        move the robot forward (updating the x and y position of the robot)
        also turn if needed
    
    position:
        return x and y
    
    direction:
        return directionLabels[direction_idx]

Readable: The intent is clear—iterate a set number of times to simulate movement.
Maintainable: The logic of handling invalid moves is separated from counting steps, making it easier to read and understand.
Flexible: The structure can easily accommodate changes, such as adding new movement rules, without rewriting the fundamental logic.

Our design pattern: Iterator, as we defined our own method to iterate around the grid.
Composition over Inheritance: While inheritance can be useful, it can lead to overly complex hierarchies. Composition, on the other hand, promotes flexibility.
Could use Encapsulation in the future if we wanted to be more secure and hide the implementation details of our object. double underscore prefixes.

We want code that is efficient, reusable, and easy to maintain. Using these best practices allows me to write code that not only works, but is also clean and manageable. 

I'm extremely facinated by the learning culture promoted at Shopify. I realized how great it probably thorugh Tobi because during an interview he mentioned 
how he would pair program with one of the engineers and they would throw away all source code at the end of the day other than the unit tests until they
can develop the entire feature in one day and that was the best code he ever wrote.
- so what resources do you highly recommend i make use of if i get the chance to be there in a few monnths

How can i exceed your expectations of a shopify intern

'''

