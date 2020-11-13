import random
import json
import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

import train
import translation
import last_language

def recheck(mode):
    check = input(f"{mode} is ok? [Y] or [N]")
    if check == "Y":
        pass
    else:
        set_mode()


def set_mode():
    mode = input(
    """
    [''] 안에 있는 단어를 입력해주세요.
    친한 정도를 설정해주세요.
    1. 너랑 완전 친함! [절친]   
    2. 너랑 그냥 친함. [친구] 
    3. 그냥 그럼.      [사람]
    4. 끝말잇기!       [끝말잇기]
    you : 
    """
    )
    if mode == "절친":
        recheck(mode)
        return 2
    if mode == "친구":
        recheck(mode)
        return 1
    if mode == "사람":
        recheck(mode)
        return 0
    if mode == "끝말잇기":
        recheck(mode)
        return -1
    else:
        return set_mode()


def check_exist(json_name, pth_name):
    base_json_dir = "resource/jsonFile/" + json_name
    base_pth_dir = "resource/pthFile/" + pth_name
    try:
        with open(base_pth_dir, "r"): # 열리면,
            pass
    except:
        #안 열리면
        print("training file")
        train.main(json_name, pth_name) # make data file


mode = set_mode()

#import from Grapic User Interface
if mode == 0:
    original_data_name = 'low.json'
    train_data_name = "low.pth"
    print("training file")
    train.main(original_data_name, train_data_name)
elif mode == 1:
    original_data_name = 'middle.json'
    train_data_name = "middle.pth"
    print("training file")
    train.main(original_data_name, train_data_name)
elif mode == 2:
    original_data_name = 'high.json'
    train_data_name = "high.pth"
    print("training file")
    train.main(original_data_name, train_data_name)
elif mode == -1:
    last_language.main()
    set_mode()



device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("resource/jsonFile/" + original_data_name, 'r', encoding="UTF8") as json_data:
    intents = json.load(json_data)

data = torch.load("resource/pthFile/" + train_data_name)
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]
model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()



bot_name = "세미"

print(f"""'그만하자'를 입력하면 끌 수 있습니다.

        안녕! 난 {bot_name}야.
        난 영어를 더 잘해! 한국어도 알아듣긴 해!
        한 문장씩, 질문해 주면 좋겠어!""")
while True:
    sentence = input("You: ")
    
    if sentence == "그만하자" or mode == -1:
        print("담에 또봐")
        break
    
    sentence = translation.main(sentence)

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(
        device)

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
        # 모를 때, 대답
        if mode == 2:
            print(f"{bot_name}: 무슨 말 하는지 모르겠다. ㅜㅜ")
        elif mode == 1:
            print(f"{bot_name}: 뭐라고?")
        elif mode == 0:
            print(f"{bot_name}: ?")