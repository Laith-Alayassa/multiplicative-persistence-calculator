
def sequence_till_one(number, initial_total, times_run):
    if len(str(number)) == 1:
        print("We reached the number")
        return times_run

    times_run += 1
    string_number = str(number)
    total = initial_total
    for character in string_number:
        total *= int(character)
    print("new Total = ", total)
    return sequence_till_one(total, 1, times_run)


def till_one_finder(num):
    return sequence_till_one(num, 1, 0)


def ask_for_number():
    num = input("what is the number that you'd like to check: ")
    print("num of times ran was : \n ", till_one_finder(num))


if __name__ == '__main__':
    ask_for_number()
