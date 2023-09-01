                      #DAY 15

import json

with open("quetions.json", "r") as file:
  content = file.read()

data = json.loads(content)  #print(type(content)) & print(type(data))

for quetion in data:
  print(quetion["quetion_test"])
  for index, alternatives in enumerate(quetion["alternatives"]):
    print(index + 1, "-", alternatives)
  user_choice = int(input("Enter your answer"))
  quetion["user_choice"] = user_choice

  print("\n")

score = 0
for index, quetion in enumerate(data):
  if quetion["user_choice"] == quetion["correct_answer"]:
    score += 1
    result = "Correct"
  else:
    result = "Wrong"
  msg = f"Your Answer is {result} for quetion {index+1} - \
  Your answer :{quetion['user_choice']},\
  correct answer :{quetion['correct_answer']}"

  print(msg)
  print("\n")

print("your score :", score, "/", len(data))
