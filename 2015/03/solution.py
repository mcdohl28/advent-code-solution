# Solution
from collections import Counter
part_one_answer = 0
part_two_answer = 0

class Santa:
    def __init__(self):
        self.loc = [0, 0]
        self.num_of_move=1

    def get_current_location(self):
        return self.loc

    def get_total_moves(self):
        return self.num_of_move

    def move_north(self):
        self.loc = [self.loc[0] + 1, self.loc[1]]
        self.num_of_move = self.num_of_move + 1

    def move_south(self):
        self.loc = [self.loc[0] - 1, self.loc[1]]
        self.num_of_move = self.num_of_move + 1

    def move_east(self):
        self.loc = [self.loc[0] , self.loc[1] + 1]
        self.num_of_move = self.num_of_move + 1

    def move_west(self):
        self.loc = [self.loc[0] , self.loc[1] - 1]
        self.num_of_move = self.num_of_move + 1

## Function
def get_data(file):
    with open(file) as f:
        data = f.readlines()
    #print(len(data))
    return data

def print_answers(part_one, part_two):
    print("######################################")
    print("Part 1 Answer: " + str(part_one))
    print("Part 2 Answer: " + str(part_two))
    print("######################################")


def execute_part_one(data):
    answer = 0
    house_location = []
    location = Santa()
    house_location.append(location.get_current_location())
    for element in data:
        movement_chart = element

    #print(movement_chart)

    for direction in movement_chart:
        if direction == '^':
            location.move_north()
        if direction == 'v':
            location.move_south()
        if direction == '>':
            location.move_east()
        if direction == '<':
            location.move_west()

        #print("Current Location: " + str(location.get_current_location()))
        if location.get_current_location() not in house_location:
            house_location.append(location.get_current_location())

    #print("Total Number of Movement: " + str(location.get_total_moves()))
    #print("List of House Location: " + str(house_location))
    answer = len(house_location)
    return answer


def execute_part_two(data):
    answer = 0
    santa_visit_location = []
    robot_visit_location = []
    common_location = []

    santa_location = Santa()
    robot_location = Santa()

    santa_visit_location.append(santa_location.get_current_location())
    robot_visit_location.append(robot_location.get_current_location())
    common_location.append(santa_location.get_current_location())

    for element in data:
        movement_chart = element

    movement_number = 0

    for direction in movement_chart:
        movement_number = movement_number+1
        #print("movement Number: " + str(movement_number))

        if movement_number % 2 != 0:
            if direction == '^':
                santa_location.move_north()
            if direction == 'v':
                santa_location.move_south()
            if direction == '>':
                santa_location.move_east()
            if direction == '<':
                santa_location.move_west()

            santa_visit_location.append(santa_location.get_current_location())
           # common_location.append(santa_location.get_current_location())
        else:
            if direction == '^':
                robot_location.move_north()
            if direction == 'v':
                robot_location.move_south()
            if direction == '>':
                robot_location.move_east()
            if direction == '<':
                robot_location.move_west()

            robot_visit_location.append(robot_location.get_current_location())
            #common_location.append(santa_location.get_current_location())

    #print("Santa visited location: " + str(santa_visit_location))
    #print("Robot visited location: " + str(robot_visit_location))
    #print("Common Visited location: " + str(common_location))
    answer = get_duplicate_location(santa_visit_location, robot_visit_location, common_location)
    return answer

def get_duplicate_location(santa_location, robot_location, common_location):

    for santa in santa_location:
        if santa not in common_location:
            common_location.append(santa)

    for robot in robot_location:
        if robot not in common_location:
            common_location.append(robot)

    #print(common_location)
    return len(common_location)

## Execution
actual = "data.txt"
sample = "sample.txt"

data = get_data(actual)

## processing...
part_one_answer = execute_part_one(data)
part_two_answer = execute_part_two(data)

# Display
print_answers(part_one_answer, part_two_answer)