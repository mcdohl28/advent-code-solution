# Solution
part_one_answer = 0
part_two_answer = 0

up_action = "up"
down_action = "down"
forward_action = "forward"

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

    horizontal = 0
    depth = 0
    list_of_instructions = process_data(data)

    for instruction in list_of_instructions:
        #print(instruction)
        action = instruction[0]
        value = int(instruction[1])
        print (action,value)

        if action == forward_action:
            horizontal = horizontal + value
        elif action == up_action:
            depth = depth - value
        elif action == down_action:
            depth = depth + value

    return horizontal * depth


def execute_part_two(data):
    horizontal = 0
    depth = 0
    aim = 0
    list_of_instructions = process_data(data)

    for instruction in list_of_instructions:
        # print(instruction)
        action = instruction[0]
        value = int(instruction[1])

        if action == forward_action:
            horizontal = horizontal + value
            depth = depth + aim * value
        elif action == up_action:
            #depth = depth - value
            aim = aim - value
        elif action == down_action:
            #depth = depth + value
            aim = aim + value

        print(action, value, horizontal, depth, aim)
    return horizontal * depth

def initialise_data():
    grid = []

    for row in range(1000):
        horizontal_grid = []
        for col in range(1000):
            horizontal_grid.append(0)
        grid.append(horizontal_grid)

    #print("Number of rows = " + str(len(grid)))
    #print("Test = " + str(grid[1][1]))
    return grid

def process_data(data):
    list_of_instructions = []
    for line in data:
        line_trimmed = line.strip("\n")
        instruction = line_trimmed.split()
        #print (instruction)
        list_of_instructions.append(instruction)

    return list_of_instructions
## Execution
actual = "data.txt"
sample = "sample.txt"
sample2 = "sample2.txt"

data1 = get_data(actual)
data2 = get_data(actual)

## processing...
part_one_answer = execute_part_one(data1)
part_two_answer = execute_part_two(data2)

# Display
print_answers(part_one_answer, part_two_answer)