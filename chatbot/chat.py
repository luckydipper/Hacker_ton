import random
import json

import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

import train
def main(read_dir = "intents.json", write_dir = "data.pth"):
    pass


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r', encoding="UTF8") as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Sam"



def recheck(mode):
    check = input(f"{mode} is ok? [Y] or [N]")
    if check == "Y":
        pass
    else:
        set_mode()


def set_mode():
    mode = input(
    """
    write in CAPITAL!
    plz set the mode
    1. hard mode [H]   
    2. middle mode [M] 
    3. easy mode [E]  
    you : """
    )
    if mode == "H":
        recheck(mode)
        return 0
    if mode == "M":
        recheck(mode)
        return 1
    if mode == "E":
        recheck(mode)
        return 2
    else:
        return None

mode = set_mode()


print("Let's chat! (type 'quit' to exit)")
while True:
    # sentence = "do you use credit cards?"
    
    
    sentence = input("You: ")
    
    if sentence == "quit":
        break

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                result = random.choice(intent['responses'])
                print(f"{bot_name}: {result}")
    else:
        print(f"{bot_name}: I do not understand...")