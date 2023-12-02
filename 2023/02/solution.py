'''
Requirements:
In game 1, three sets of cubes are revealed from the bag (and then put back again). 
The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. 
However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; 
similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. 
If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. 
What is the sum of the IDs of those games?

'''

#importing the module 
import logging

#now we will Create and configure logger 
logging.basicConfig(filename="std.log", 
					format='[%(asctime)s] - %(message)s', 
					filemode='w') 

#Let us Create an object 
logger=logging.getLogger() 

#Now we are going to Set the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 


## Function
def read_from_file(file):
    with open(file) as f:
        data = f.readlines()
    ##print(len(data))
    return data


def execute_script():
    part_one_sample = 0
    part_two_sample = 0
    part_one_answer = 0
    part_two_answer = 0
    sample = "sample.txt"
    actual = "input.txt"
    sample2 = "sample2.txt"
    actual2 = "input.txt"
    
    #sample_data1 = read_from_file(sample)
    #actual_data1 = read_from_file(actual)

    sample_data2 = read_from_file(sample2)
    actual_data2 = read_from_file(actual2)

    ## processing...
    #part_one_sample = process_part_one_data(sample_data1)
    #part_one_answer = process_part_one_data(actual_data1)
    #part_two_sample = process_part_two_data(sample_data2)
    part_two_answer = process_part_two_data(actual_data2)

    # Display
    print_answers(part_one_sample, part_two_sample, part_one_answer, part_two_answer)


def print_answers(sample_one, sample_two, actual_one, actual_two):
    print("######################################")
    print("Sample 1 Answer: " + str(sample_one))
    print("Part 1 Answer: " + str(actual_one))
    print("\n")
    print("Sample 2 Answer: " + str(sample_two))
    print("Part 2 Answer: " + str(actual_two))
    print("######################################")


def process_part_one_data(input):
    output=0
    temp = input
    configuration_dict= {
        'red': 12,
        'green': 13,
        'blue': 14
     } 
    
    ##print('Total records to process:' , temp)

    ## Process the input into list.
    for i in temp:
        logger.debug("=====-Start record-=====")
        value = i.strip() ## strip away newline
        logger.debug("Input value:"+ value)
        
        # split delimiter the game number and the result set.
        input_list = value.split(': ')
        game=input_list[0].split(' ')
        game_pass_condition=True
        game_number=game[1]  # used for calculation output.
        set_result=input_list[1].split('; ')
        #per_set_result = set_result.split(', ')
        for j in set_result:
            ##logger.debug("Per Set Result:"+ j)
            if j.find(",") >=0:
                per_set_result=j.split(', ')
                ##logger.debug("a:"+ str(per_set_result))
                for k in per_set_result:
                    per_set_result=k.split(' ')
                    logger.debug("b:"+ str(per_set_result))
                    if per_set_result[1] == "red":
                        if (configuration_dict["red"] < int(per_set_result[0])):
                            logger.debug("Data contain more count than red value.")
                            game_pass_condition=False
                            break
                    if per_set_result[1] == "green":
                        if (configuration_dict["green"] < int(per_set_result[0])):
                            logger.debug("Data contain more count than green value.")
                            game_pass_condition=False
                            break
                    if per_set_result[1] == "blue":
                        if (configuration_dict["blue"] < int(per_set_result[0])):
                            logger.debug("Data contain more count than blue value.")
                            game_pass_condition=False
                            break
            else:
                per_set_result=j.split(' ')
                logger.debug("b:"+ str(per_set_result))
                if per_set_result[1] == "red":
                    if (configuration_dict["red"] < int(per_set_result[0])):
                        logger.debug("Data contain more count than red value.")
                        game_pass_condition=False
                        break
                if per_set_result[1] == "green":
                    if (configuration_dict["green"] < int(per_set_result[0])):
                        logger.debug("Data contain more count than green value.")
                        game_pass_condition=False
                        break
                if per_set_result[1] == "blue":
                    if (configuration_dict["blue"] < int(per_set_result[0])):
                        logger.debug("Data contain more count than blue value.")
                        game_pass_condition=False
                        break
            ##logger.debug("After splitting:"+ str(per_set_result))
        if game_pass_condition == True:
            output+=int(game_number)   

        logger.debug("Game Number:"+ game_number)
        logger.debug("Output:"+ str(output))
        logger.debug("=====-End record-=====")


    return output

def process_part_two_data(input):
    output=0
    temp = input

    ## Process the input into list.
    for i in temp:
        logger.debug("=====-Start record-=====")
        value = i.strip() ## strip away newline
        logger.debug("Input value:"+ value)
        
        number_of_red=0
        number_of_blue=0
        number_of_green=0
        power_per_round=0

        # split delimiter the game number and the result set.
        input_list = value.split(': ')
        game=input_list[0].split(' ')
        game_number=game[1]  # used for calculation output.
        set_result=input_list[1].split('; ')
        logger.debug("Game Number:"+ game_number)

        for j in set_result:
            ##logger.debug("Per Set Result:"+ j)
            if j.find(",") >=0:
                per_set_result=j.split(', ')
                ##logger.debug("a:"+ str(per_set_result))
                for k in per_set_result:
                    per_set_result=k.split(' ')
                    logger.debug("if:"+ str(per_set_result))
                    if per_set_result[1] == "red":
                        if int(per_set_result[0]) >= number_of_red:
                            number_of_red = int(per_set_result[0])
                    if per_set_result[1] == "green":
                        if int(per_set_result[0]) >= number_of_green:
                            number_of_green = int(per_set_result[0])
                    if per_set_result[1] == "blue":
                        if int(per_set_result[0]) >= number_of_blue:
                            number_of_blue = int(per_set_result[0])
            else:
                per_set_result=j.split(' ')
                logger.debug("else:"+ str(per_set_result))
                if per_set_result[1] == "red":
                    if int(per_set_result[0]) >= number_of_red:
                        number_of_red = int(per_set_result[0])
                if per_set_result[1] == "green":
                    if int(per_set_result[0]) >= number_of_green:
                        number_of_green = int(per_set_result[0])
                if per_set_result[1] == "blue":
                    if int(per_set_result[0]) >= number_of_blue:
                        number_of_blue = int(per_set_result[0])
            ##logger.debug("After splitting:"+ str(per_set_result))
            logger.debug("number of red="+str(number_of_red))
            logger.debug("number of green="+str(number_of_green))
            logger.debug("number of blue="+str(number_of_blue))
        power_per_round = int(number_of_red) * int(number_of_green) * int(number_of_blue)
        logger.debug("Power per round="+str(power_per_round))
        output += power_per_round
        logger.debug("Output:"+ str(output))
        logger.debug("=====-End record-=====")
    
    return output

## Execution starts below
print('Advent 2023 - 02')

execute_script()