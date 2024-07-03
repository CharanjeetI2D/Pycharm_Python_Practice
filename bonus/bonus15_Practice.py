import json

filepath = "/Users/charanjeetsingh/Documents/PythonProjects/Python_ Experiments/bonus/Questions2.json"

with open(filepath, 'r') as file:
    content = file.read()
    data = json.loads(content)

score = 0

for question in data:
    print(question['question_text'])
    for index, alternatives in enumerate(question['alternatives']):
        print(index + 1, '-', alternatives)
    user_input = int(input("Please select answer: "))
    question["user_input"] = user_input
    if user_input == question["correct answer"]:
        score = score + 1
    print(f"Correct answer: {question['correct answer']}" + "\n"
          f"Your answer: {user_input}")

print(f"Total score {score} out of {len(data)}")