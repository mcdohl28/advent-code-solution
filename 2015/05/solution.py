# Solution
import re
part_one_answer = 0
part_two_answer = 0

naughty = 0
nice = 1

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
    #print(len(data))
    for line in data:
        #print(line.strip("\n"))
        line_stripped = line.strip("\n")
        answer = answer + define_notti_or_nice(line_stripped)

    return answer

def execute_part_two(data):
    answer = 0
    for line in data:
        #print(line.strip("\n"))
        line_stripped = line.strip("\n")
        answer = answer + define_updated_notti_or_nice(line_stripped)
    return answer

def define_notti_or_nice(input):
    outcome = 0
    '''print("text=[" + input + "]")
    print("Requirement 1 - contains at least 3 vowels\t: "+str(contains_at_least_three_vowel(input)))
    print("Requirement 2 - appears twice in a row\t\t: " + str(appears_twice_in_a_row(input)))
    print("Requirement 3 - does not contain the strings\t: " + str(not_within_selected_string(input)))'''
    if not_within_selected_string(input):
        outcome = naughty
    else:
        if contains_at_least_three_vowel(input) and appears_twice_in_a_row(input):
            outcome = nice
        else:
            outcome = naughty

    '''print("text=[" + input + "], requirement1=[" + str(contains_at_least_three_vowel(input))
                                                       + "], requirement2=[" + str(appears_twice_in_a_row(input))
                                                       + "], requirement3=[" + str(not_within_selected_string(input))
                                                                                   + "], outcome=[" + str(outcome)+"]")'''
    return outcome

def define_updated_notti_or_nice(input):
    outcome = 0
    if contains_pair_of_letters_twice(input) and contains_letter_repeated_with_a_letter_between(input):
        outcome = nice
    else:
        outcome = naughty

    #print("Input=[" + input + "], Outcome1=[" + str(contains_pair_of_letters_twice(input)) +
    #      "], Outcome2=[" + str(contains_letter_repeated_with_a_letter_between(input)) + "], finalOutCome=[" + str(outcome) + "]")

    return outcome

def contains_at_least_three_vowel(text):
    result = re.findall(r'[aeiou]', text, re.IGNORECASE)
    #print(str(len(result)))
    return len(result) > 2

def appears_twice_in_a_row(text):
    result = []
    patterns = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj',
               'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt',
               'uu', 'vv', 'ww', 'xx', 'yy', 'zz']
    for pattern in patterns:
        for match in re.findall(pattern, text):
            result = match
    #print("Value that appear twice: "+ str(result))
    return len(result) > 0

def not_within_selected_string(text):
    result = []
    patterns = ['ab', 'cd', 'pq', 'xy']
    for pattern in patterns:
        for match in re.findall(pattern, text):
            result = match
    return len(result) > 0

def contains_pair_of_letters_twice(text):
    result = []
    result = re.findall(r'^.*?([a-z]{2}).*?(\1).*$', text, re.IGNORECASE)
    #print(str(len(result)))
    return len(result) > 0

def contains_letter_repeated_with_a_letter_between(text):
    result = []

    #print (text)
    indexes_of_match = []
    for letter in text:
        indexes_of_match.append(letter)
    #print(str(indexes_of_match))

    list_1 = indexes_of_match[:-2]
    list_2 = indexes_of_match[2:]
    #print(str(list_1))
    #print(str(list_2))

    for i in range(len(list_1)):
        if list_1[i] == list_2[i]:
            #print("Character=["+list_1[i]+"], compares=["+ list_2[i]+"]")
            result.append(list_1[i])
            break

    return len(result) > 0

## Execution
actual = "data.txt"
sample = "sample.txt"
sample2 = "sample2.txt"

data = get_data(actual)

## processing...
part_one_answer = execute_part_one(data)
part_two_answer = execute_part_two(data)

# Display
print_answers(part_one_answer, part_two_answer)