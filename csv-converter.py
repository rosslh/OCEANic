import json

def getEffect(data):
    effect = {
            "openness": 0,
            "conscientiousness": 0,
            "extraversion": 0,
            "agreeableness": 0,
            "neuroticism": 0
        };
    
    direction = 1 if data[3][0] == "+" else -1
    magnitude = int(data[3][2:])
    print(magnitude)
    print(direction)
    if(data[4][0] == "O"):
        effect["openness"] += magnitude * direction
    elif(data[4][0] == "C"):
        effect["conscientiousness"] += magnitude * direction
    elif(data[4][0] == "E"):
        effect["extraversion"] += magnitude * direction
    elif(data[4][0] == "A"):
        effect["agreeableness"] += magnitude * direction
    elif(data[4][0] == "N"):
        effect["neuroticism"] += magnitude * direction
    
    return effect

def main():
    questions = []

    traits = open('traits.csv', 'r') 
    lines = traits.readlines() 
    
    count = 0
    # Strips the newline character 
    for line in lines: 
        lineData = line.strip().split(",")
        question = lineData[6]
        effect = getEffect(lineData)
        questions.append({
            "question": question,
            "effect": effect
        })
    
    with open('questions.json', 'w') as outfile:
        json.dump(questions, outfile)

main()