# Problem 1

numbers = [5,7,7,8,8,8,10]
fun = lambda x: x % 2 == 0
even = filter(fun, numbers)
li = list(even)
count = len(li)
print(count)

###################################################################
# Problem 2

def search_index(lst, target):
    try:
        index = lst.index(target)
        return index
    except ValueError:
        from bisect import bisect_left
        index = bisect_left(lst, target)
        return index
print(search_index([4,2,3,1,7], 3))
print(search_index([4,2,3,1,7], 5))

###################################################################
# Problem 3

import itertools

def find_closest_sum(nums, target):
    closest_sum = float('inf')
    closest_combination = None
    
    for combination in itertools.combinations(nums, 4):
        current_sum = sum(combination)
        if abs(current_sum - target) < abs(closest_sum - target):
            closest_sum = current_sum
            closest_combination = combination
            
    return closest_combination
nums = [4,2,3,1,7,12]
target = 28
print(find_closest_sum(nums, target))

###################################################################
# Problem 4

users = {}
with open('dummy_grades.txt', 'r') as file:
    for line in file:
        id, name, score, birthday, sex = line.strip().split(', ')
        if score != 'N/A':
            users[id] = {'name': name, 'score': int(score), 'birthday': int(birthday), 'sex': sex}

# a. Do no store a user with no registered score ?
# No users with no registered score in the dictionary

# b. What is the ID of the oldest user ?
oldest_id = min(users.keys(), key=lambda x: users[x]['birthday'])
print("ID of the oldest user:", oldest_id)

# c. What is the average score ?
average_score = sum(user['score'] for user in users.values()) / len(users)
print("Average score:", average_score)

# d. What is the sex of the user with the highest score ?
highest_score_user = max(users.values(), key=lambda x: x['score'])
print("Sex of the user with the highest score:", highest_score_user['sex'])

###################################################################
# Problem 5

from users_data import users_data

def save_data_to_file():
    with open('busted.txt', 'w') as file:
        for user_id, user_data in users_data.items():
            name = user_data['name']
            birthday = user_data['birthday']
            file.write(f"{user_id} {name} - {birthday}\n")

save_data_to_file()