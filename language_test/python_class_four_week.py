
def average():
    sum_l = 0.0
    count = 0
    more_data = "yes"
    while more_data[0] == 'y':
        x = eval(input("Enter a number >>"))
        sum_l = sum_l + x
        count += 1
        more_data = input("Do you have more data(yes or no)>")
    print("the average of numbers is ",sum_l/count)

def average_flag():
    sum_l = 0.0
    count = 0
    xStr = input("Enter a number (<ENTER> to exit):")
    while xStr != "":
        x = eval(xStr)
        sum_l = sum_l + x
        count += 1
        xStr = input("Enter a number (<ENTER> to exit):")
    print("the average of numbers is ",sum_l/count)


if __name__ == "__main__":
    # average()
    average_flag()