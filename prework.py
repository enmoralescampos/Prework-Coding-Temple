# Question 1
def hello_name(user_name):
    print("Hello_" + user_name + "!")


# Question 2
def first_odds():
    for i in range(1, 100, 2):
        print(i)


# Question 3
def max_num_in_list(a_list):
    maxNum = a_list[0]
    for num in a_list:
        if num > maxNum:
            maxNum = num
    return maxNum


# Question 4
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# Question 5
def is_consecutive(a_list):
    for i in range(1, len(a_list)):
        if a_list[i] != a_list[i-1] + 1:
            return False
    return True

