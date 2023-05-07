users = {}
# with open('dummy_grades.txt', 'r') as file:
#     for line in file:
#         id, name, score, birthday, sex = line.strip().split(', ')
#         if score != 'N/A':
#             users[id] = {'name': name, 'score': int(score), 'birthday': int(birthday), 'sex': sex}

# # Answer to question a
# # There are no users with no registered score in the dictionary

# # Answer to question b
# oldest_id = min(users.keys(), key=lambda x: users[x]['birthday'])
# print("ID of the oldest user:", oldest_id)

# # Answer to question c
# average_score = sum(user['score'] for user in users.values()) / len(users)
# print("Average score:", average_score)

# # Answer to question d
# highest_score_user = max(users.values(), key=lambda x: x['score'])
# print("Sex of the user with the highest score:", highest_score_user['sex'])
