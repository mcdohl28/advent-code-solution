'''
Requirements:
The newly-improved calibration document consists of lines of text; 
each line originally contained a specific calibration value that the Elves now need to recover. 
On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

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
    actual = "data.txt"
    actual2 = "data2.txt"
    sample = "input.txt"
    sample2 = "input.txt"

    sample_data1 = read_from_file(sample)
    sample_data2 = read_from_file(sample2)

    #actual_data1 = read_from_file(actual)
    #actual_data2 = read_from_file(actual2)

    ## processing...
    part_one_sample = process_part_one_data(sample_data1)
    part_two_sample = process_part_two_data(sample_data2)
    #part_one_answer = execute_part_one(actual_data1)
    #part_two_answer = execute_part_two(actual_data2)

    # Display
    print_answers(part_one_sample, part_two_sample, part_one_answer, part_two_answer)


def print_answers(sample_one, sample_two, actual_one, actual_two):
    print("######################################")
    print("Sample 1 Answer: " + str(sample_one))
    print("Sample 2 Answer: " + str(sample_two))
    print("Part 1 Answer: " + str(actual_one))
    print("Part 2 Answer: " + str(actual_two))
    print("######################################")


def process_part_one_data(input):
    output=0
    temp = input
    sanitize_list=[]
    number_list=[]
    ##print('Total records to process:' , temp)

    ## Process and sanitize the list.
    for i in temp:
        value = i.strip() ## strip away newline
        ##print(value)
        for j in value:
            ## check each character for digit, if yes, append into a list
            if j.isdigit():
                ##print(j)
                number_list.append(j) 

        ## do the sum here when processing. each line; if more than 2 numbers, take first and last number for sum.
        if len(number_list) >1:
            ##print ("First Number: ", number_list[0] )
            ##print ("Last Number Number: ", number_list[-1] )
            output += int(number_list[0] + number_list[-1]) 
            ##print ("SUM Output Number: ", output )
        else:
            ## Special Handling of single digit. to consider last number as same as first number. Use multiply by 11 to get the answer.
            ##print ("Else Number: ", number_list[0] )
            special_number=int(number_list[0])*11
            ##print ("special Number: ", special_number )
            output += special_number
            ##print ("Output Number: ", output )

        sanitize_list.append(number_list) ## add to the sanitize list for further verification.
        number_list=[] ## reset the number_list.

    ##print("Santize List = ", sanitize_list) ## enable to check your answers.
    
    return output


def process_part_two_data(input):
    output=0
    temp = input
    sanitize_list=[]
    number_list=[]
    
    ## Dictionary to refer.
    digit_dict = {
        "eightwo": "eighttwo",
        "twone": "twoone",
        "oneight": "oneeight",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    ##logger.debug('Total records to process:' , temp)

    ## Process and sanitize the list.
    for i in temp:
        value = i.strip() ## strip away newline
        logger.debug("original_data:" + str(value))
        
        ## Loop the dictionary to convert all the valid words to digit.
        for x in digit_dict:
            ##print(x, digit_dict[x])
            value = value.replace(x,digit_dict[x])
        
        logger.debug("replaced value: "+ str(value))
        
        for j in value:
            ## check each character for digit, if yes, append into a list
            if j.isdigit():
                ##print(j)
                number_list.append(j) 

        ## do the sum here when processing. each line; if more than 2 numbers, take first and last number for sum.
        if len(number_list) >1:
            logger.debug ("First Number: " + str(number_list[0]) )
            logger.debug ("Last Number Number: "+ str(number_list[-1]) )
            output += int(number_list[0] + number_list[-1]) 
            ##logger.debug ("SUM Output Number: "+ str(output) )
        else:
            ## Special Handling of single digit. to consider last number as same as first number. Use multiply by 11 to get the answer.
            logger.debug ("Else Number: "+ str(number_list[0]) )
            special_number=int(number_list[0])*11
            ##print ("special Number: ", special_number )
            output += special_number
            logger.debug ("Output Number: "+str(output) )
        
        logger.debug("Output accumulated Value:" + str(output))
        sanitize_list.append(number_list) ## add to the sanitize list for further verification.
        number_list=[] ## reset the number_list.

    ##print("Santize List = ", sanitize_list) ## enable to check your answers.
    
    return output



## Execution starts below
print('Advent 2023 - 01')

execute_script()