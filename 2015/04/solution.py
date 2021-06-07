# Solution
import hashlib

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
    secret_key = data
    for salt in range(1050000):
        hash_value = secret_key + str(salt)
        hashed_value = hash_it(hash_value)
        if hashed_value[0:5] == "00000":
            #print(hash_value)
            answer = salt
            break

    print(answer)
    return answer


def execute_part_two(data):
    answer = 0
    secret_key = data
    for salt in range(3000001, 4000000):
        hash_value = secret_key + str(salt)
        hashed_value = hash_it(hash_value)
        if hashed_value[0:6] == "000000":
            # print(hash_value)
            answer = salt
            break

    print(answer)
    return answer


def hash_it(data):
    return hashlib.md5(data.encode()).hexdigest()

## Execution
actual = "data.txt"
sample = "sample.txt"

#data = get_data(sample)

data="ckczppom"

## processing...
part_one_answer = execute_part_one(data)
part_two_answer = execute_part_two(data)

# Display
print_answers(part_one_answer, part_two_answer)