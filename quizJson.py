import json

# jak działa json.load
# jak wygląda przykładowy plik json
# jaka roznica miedzy x.json() a json.load(x)


def init():
    print("Welcome in quiz")
    score = 0

    with open("questions.json", "r") as file:
        questionsArr = json.load(file)

    
    for index, question in enumerate(questionsArr):
        print(f"{index}: {question} ")
        print(question["question"])
        
        for index, alter in enumerate(question["alternatives"]):
            print(f"{index+1}: {alter}")

        user_answer = int(input("Put your answer: ")) - 1
        question["user_answer"] = user_answer
    

    for index, question in enumerate(questionsArr):
        if question["user_answer"] == question["correct_answer"]:
            score = score + 1
        
        print(f"Question {index}: user answer: {question["user_answer"]}, correct answer: {question["correct_answer"]}, score {score}/{index+1}")


    print(f"Final result: {score}/{len(questionsArr)}")


    

    

if __name__ == "__main__":
    init()
    

