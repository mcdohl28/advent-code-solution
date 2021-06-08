# Solution
part_one_answer = 0
part_two_answer = 0

toggle_action = "toggle"
turn_on_action = "turn on"
turn_off_action = "turn off"

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

    result = initialise_data()

    #print(len(data))
    for line in data:
        #print(line.strip("\n"))
        line_stripped = line.strip("\n")
        if toggle_action in line_stripped:
            action = line_stripped[:6]
            destination = line_stripped[7:].split(" through ")

            start_location = destination[0]
            end_location = destination[1]

            start = start_location.split(',')
            end = end_location.split(',')

            for row in range(int(start[0]), int(end[0]) + 1):
                for col in range(int(start[1]), int(end[1]) + 1):
                    if result[row][col] == 1:
                        result[row][col] = 0
                    elif result[row][col] == 0:
                        result[row][col] = 1
                    else:
                        pass

            print("[+] Action = [" + action + "], destination=[" + str(destination) + "]. Done.")
        elif turn_on_action in line_stripped:
            action = line_stripped[:7]
            destination = line_stripped[8:].split(" through ")

            start_location = destination[0]
            end_location = destination[1]

            start = start_location.split(',')
            end = end_location.split(',')

            #for x in result:
            #    print(x)

            for row in range(int(start[0]), int(end[0]) + 1):
                for col in range(int(start[1]), int(end[1]) + 1):
                    result[row][col] = 1
            print("[+] Action = [" + action + "], destination=[" + str(destination) + "]. Done.")
        elif turn_off_action in line_stripped:
            action = line_stripped[:8]
            destination = line_stripped[9:].split(" through ")

            start_location = destination[0]
            end_location = destination[1]

            start = start_location.split(',')
            end = end_location.split(',')

            for row in range(int(start[0]), int(end[0]) + 1):
                for col in range(int(start[1]), int(end[1]) + 1):
                    result[row][col] = 0
            print("[+] Action = [" + action + "], destination=[" + str(destination) + "]. Done.")
        else:
            pass

    for line in result:
        for bulb in line:
            if bulb > 0:
                answer = answer + 1

    return answer

def execute_part_two(data):
    answer = 0

    result = initialise_data()

    #print(len(data))
    for line in data:
        #print(line.strip("\n"))
        line_stripped = line.strip("\n")
        if toggle_action in line_stripped:
            action = line_stripped[:6]
            destination = line_stripped[7:].split(" through ")

            start_location = destination[0]
            end_location = destination[1]

            start = start_location.split(',')
            end = end_location.split(',')

            for row in range(int(start[0]), int(end[0]) + 1):
                for col in range(int(start[1]), int(end[1]) + 1):
                    result[row][col] = result[row][col] + 2

            print("[+] Action = [" + action + "], destination=[" + str(destination) + "]. Done.")
        elif turn_on_action in line_stripped:
            action = line_stripped[:7]
            destination = line_stripped[8:].split(" through ")

            start_location = destination[0]
            end_location = destination[1]

            start = start_location.split(',')
            end = end_location.split(',')

            #for x in result:
            #    print(x)

            for row in range(int(start[0]), int(end[0]) + 1):
                for col in range(int(start[1]), int(end[1]) + 1):
                    result[row][col] = result[row][col] + 1
            print("[+] Action = [" + action + "], destination=[" + str(destination) + "]. Done.")
        elif turn_off_action in line_stripped:
            action = line_stripped[:8]
            destination = line_stripped[9:].split(" through ")

            start_location = destination[0]
            end_location = destination[1]

            start = start_location.split(',')
            end = end_location.split(',')

            for row in range(int(start[0]), int(end[0]) + 1):
                for col in range(int(start[1]), int(end[1]) + 1):
                    result[row][col] = result[row][col] -1
                    if result[row][col] < 0 :
                        result[row][col] = 0

            print("[+] Action = [" + action + "], destination=[" + str(destination) + "]. Done.")
        else:
            pass

    for line in result:
        for bulb in line:
            #print(str(bulb))
            if bulb > 0:
                answer = answer + bulb

    return answer


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