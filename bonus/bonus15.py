import json

filepath = "/Users/charanjeetsingh/Documents/PythonProjects/Python_ Experiments/bonus/questions.json"
with open(filepath, 'r') as file:
    content = file.read()

data = json.loads(content)
print(type(data))

for question in data:
    print(question["question_text"])
    for index, alternatives in enumerate(question["alternatives"]):
        print(index + 1, "-", alternatives)
    user_choice = int(input("Please select your answer: "))
    question["user_choice"] = user_choice

score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct answer"]:
        score = score + 1
        result = "Correct answer"
    else:
        result = "Wrong Answer"
    message = (f"{index + 1} {result}- Your answer {question['user_choice']}, "
               f"Correct answer: {question['correct answer']}")
    print(message)


print("Score is: ", score)
print(f"You have answered {score} out of {len(data)} questions correctly")
