# Solution
part_one_answer = 0
part_two_answer = 0

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
    previous_number = 0
    number_of_increase=0
    number_of_decrease=0

    result = initialise_data()

    #print(len(data))
    for index, item in enumerate(data):

        if index > 0:
            previous_number = current_number

        current_number = int(item.strip("\n"))

        if index > 0:
            if current_number > previous_number:
                number_of_increase = number_of_increase + 1
            elif current_number < previous_number:
                number_of_decrease = number_of_decrease - 1

        print(index, previous_number, current_number, number_of_increase, number_of_decrease)

    return number_of_increase

def execute_part_two(data):
    number_of_increase = 0
    number_of_decrease = 0

    list_of_value = []
    list_of_sum = []
    temp_sum = 0

    # print(len(data))
    for index, item in enumerate(data):
        #print(index, item.strip("\n"))
        current_number = int(item.strip("\n"))
        list_of_value.append(current_number)

    print(list_of_value)

    i = 0
    while i < len(list_of_value):
        #print (list_of_value[i])
        small_list = list_of_value[0:3]
        print (small_list)

        if len(small_list) == 3:
            for value in small_list:
                temp_sum = temp_sum + value
            list_of_sum.append(temp_sum)
            temp_sum = 0

        list_of_value.pop(0)
    print(small_list, list_of_sum, len(list_of_sum))

    previous_number = 0
    current_number = 0

    for index, item in enumerate(list_of_sum):

        if index > 0:
            previous_number = current_number
        current_number = item

        if index > 0:
            if current_number > previous_number:
                number_of_increase = number_of_increase + 1
            elif current_number < previous_number:
                number_of_decrease = number_of_decrease - 1
        print(previous_number, current_number, number_of_increase, number_of_decrease)

    return number_of_increase

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

data1 = get_data(sample)
data2 = get_data(actual)

## processing...
##part_one_answer = execute_part_one(data1)
part_two_answer = execute_part_two(data2)

# Display
print_answers(part_one_answer, part_two_answer)