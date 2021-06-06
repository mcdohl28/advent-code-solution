# Solution
part_one_answer = 0
part_two_answer = 0

class Present:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def get_surface_area(self):
        surface_area = (2 * self.length * self.width) + (2 * self.width * self.height) + (2 * self.height * self.length)
        return surface_area

    def get_min_area(self):
        params = [self.length, self.width, self.height]
        params.sort()
        area = params[0] * params[1]
        #print("Sorting sequence: " + str(params) + ", returning area=" + str(area))
        return area

    def get_feet_of_ribbon_to_wrap(self):
        params = [self.length, self.width, self.height]
        params.sort()
        perimeter = params[0] + params[0] + params[1] + params[1]
        return perimeter

    def get_feet_of_ribbon_for_bow(self):
        return self.length * self.width * self.height

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
    for element in data:
        line = element.strip('\n').split("x")
        box = Present(int(line[0]), int(line[1]), int(line[2]))
        total_area = box.get_surface_area() + box.get_min_area()
        line.append(total_area)
        # print(line)
        answer = answer + total_area
    return answer


def execute_part_two(data):
    answer = 0
    for element in data:
        line = element.strip('\n').split("x")
        box = Present(int(line[0]), int(line[1]), int(line[2]))
        total_feet = box.get_feet_of_ribbon_to_wrap() + box.get_feet_of_ribbon_for_bow()
        line.append(total_feet)
        print(line)
        answer = answer + total_feet
    return answer


## Execution
actual = "data.txt"
sample = "sample.txt"

data = get_data(actual)

## processing...
part_one_answer = execute_part_one(data)
part_two_answer = execute_part_two(data)

# Display
print_answers(part_one_answer, part_two_answer)