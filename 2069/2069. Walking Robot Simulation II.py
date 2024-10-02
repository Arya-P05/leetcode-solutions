from typing import List

class Robot:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.x, self.y = 0, 0
        self.dirLabels = ["East", "North", "West", "South"]
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.direction = 0

    def step(self, num: int) -> None:
        displacement = num % ((self.width + self.height - 2) * 2)
        if displacement == 0 and (self.x, self.y) == (0, 0) and self.direction == 0:
            self.direction = 3
        
        for step_forward in range(displacement):
            nextX, nextY = self.x + self.directions[self.direction][0], self.y + self.directions[self.direction][1]

            while not (0 <= nextX < self.width and 0 <= nextY < self.height):
                self.direction = ((self.direction + 1) % 4)
                nextX, nextY = self.x + self.directions[self.direction][0], self.y + self.directions[self.direction][1]
            
            self.x = nextX
            self.y = nextY

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.dirLabels[self.direction]

def testCase1():
    rob = Robot(6, 4)
    rob.step(6)
    assert rob.getDir() == "North"
    assert rob.getPos() == [5, 1]
    
def main():
    robot = None

    while True:
        user_input = input("Type Robot, step, getPos, getDir, or quit: ").strip()
        
        if user_input == "quit":
            print("Exiting the program.")
            break

        command = user_input.split()[0]

        if command == "Robot":
            width = int(input("Enter the grid width: "))
            height = int(input("Enter the grid height: "))
            robot = Robot(width, height)
            print(f"Initialized Robot with grid {width}x{height}")
        
        elif command == "step" and robot is not None:
            num_steps = int(input("Enter the number of steps: "))
            robot.step(num_steps)
            print(f"Robot moved {num_steps} steps. Current Position: {robot.getPos()}, Facing: {robot.getDir()}")
        
        elif command == "getPos" and robot is not None:
            pos = robot.getPos()
            print(f"Robot Position: {pos}")
        
        elif command == "getDir" and robot is not None:
            direction = robot.getDir()
            print(f"Robot Direction: {direction}")
        
        else:
            print("Invalid command or robot not initialized. Please try again.")

if __name__ == "__main__":
    testCase1()
    main()