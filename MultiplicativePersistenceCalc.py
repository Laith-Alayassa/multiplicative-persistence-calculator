
def sequence_till_one(number, initial_total, times_run, nums_reached):
    nums_reached += [number]
    # print(f"list of numbers until now {nums_reached}")
    if len(str(number)) == 1:
        return (times_run, nums_reached)

    times_run += 1
    string_number = str(number)
    total = initial_total
    for character in string_number:
        total *= int(character)
    return sequence_till_one(total, 1, times_run, nums_reached)


def till_one_finder(num):
    return sequence_till_one(num, 1, 0, [])


def ask_for_number():
    num = input("what is the number that you'd like to check: ")
    result = till_one_finder(num)
    print(f"======================num of times ran is: {result[0]} \nand the numbers it went through were {result[1]}========")




if __name__ == '__main__':
    ask_for_number()
