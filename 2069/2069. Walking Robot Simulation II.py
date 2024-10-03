from typing import List, Tuple, Set

class RobotGridSystem():
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.occupiedPos = set()
        self.robot_positions = {} # id: position
    
    def add_robot(self, id: int, position: Tuple[int, int]):
        if position not in self.occupiedPos:
            self.occupiedPos.add(position)
            self.robot_positions[id] = position
    
    def is_occupied(self, position: Tuple[int, int]) -> bool:
        return position in self.occupiedPos
    
    def update_position(self, id: int, new_position: Tuple[int, int]) -> None:
        current_position = self.robot_positions[id]
        self.occupiedPos.remove(current_position)
        self.occupiedPos.add(new_position)
        self.robot_positions[id] = new_position


class Robot:
    def __init__(self, width: int, height: int, grid_manager: RobotGridSystem, robot_id: int):
        self.width = width
        self.height = height
        self.x, self.y = 0, 0
        self.dirLabels = ["East", "North", "West", "South"]
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.direction = 0
        self.grid_manager = grid_manager
        self.robot_id = robot_id
        self.grid_manager.add_robot(self.robot_id, (self.x, self.y))

    def step(self, num: int) -> None:
        displacement = num % ((self.width + self.height - 2) * 2)
        if displacement == 0 and (self.x, self.y) == (0, 0) and self.direction == 0:
            self.direction = 3
        
        for step_forward in range(displacement):
            nextX, nextY = self.x + self.directions[self.direction][0], self.y + self.directions[self.direction][1]

            while not ((0 <= nextX < self.width and 0 <= nextY < self.height)) or self.grid_manager.is_occupied(nextX, nextY):
                self.direction = ((self.direction + 1) % 4)
                nextX, nextY = self.x + self.directions[self.direction][0], self.y + self.directions[self.direction][1]
            
            self.grid_manager.update_position(self.robot_id, (nextX, nextY))
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
    grid = RobotGridSystem(5, 5)
    rob = Robot(5, 5, grid, 1)
    max = Robot(5, 5, grid, 2)

    rob.step(4)
    max.step(8)

    print(f"Rob's current position is: {rob.getPos()} and is facing: {rob.getDir()}")
    print(f"Max's current position is: {max.getPos()} and is facing: {max.getDir()}")

if __name__ == "__main__":
    main()
    
# def main():
#     robot = None

#     while True:
#         user_input = input("Type Robot, step, getPos, getDir, or quit: ").strip()
        
#         if user_input == "quit":
#             print("Exiting the program.")
#             break

#         command = user_input.split()[0]

#         if command == "Robot":
#             width = int(input("Enter the grid width: "))
#             height = int(input("Enter the grid height: "))
#             robot = Robot(width, height)
#             print(f"Initialized Robot with grid {width}x{height}")
        
#         elif command == "step" and robot is not None:
#             num_steps = int(input("Enter the number of steps: "))
#             robot.step(num_steps)
#             print(f"Robot moved {num_steps} steps. Current Position: {robot.getPos()}, Facing: {robot.getDir()}")
        
#         elif command == "getPos" and robot is not None:
#             pos = robot.getPos()
#             print(f"Robot Position: {pos}")
        
#         elif command == "getDir" and robot is not None:
#             direction = robot.getDir()
#             print(f"Robot Direction: {direction}")
        
#         else:
#             print("Invalid command or robot not initialized. Please try again.")