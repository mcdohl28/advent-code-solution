# Solution for Q1
floor = 0
position = 0
part_two_answer=0

sample_str = "((("

## Function
def up_one_floor():
    return floor + 1

def down_one_floor():
    return floor - 1

## Execution

# get input...
with open('data.txt') as f:
    data = f.read()

#print(len(data))

## processing...
for element in data:
    position = position+1
    if element == '(':
        floor = up_one_floor()
    elif element == ')':
        floor = down_one_floor()
        if part_two_answer==0 and floor == -1:
            part_two_answer = position

# Display
print("Part 1 Answer: " + str(floor))
print("Part 2 Answer: " + str(part_two_answer))

