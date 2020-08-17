from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import logging
chatbot=ChatBot('Kiki',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            logic_adapters=[
         
            {
             "import_path": "chatterbot.logic.BestMatch",
             'maximum_similarity_threshold': 0.90,
             "default_response": 'I am sorry, but I do not understand.',
            },
             ],
            trainer='chatterbot.trainers.ListTrainer')

trainer=ListTrainer(chatbot)

for file in os.listdir('C:/Users/Dell/AppData/Local/Programs/Python/Python38-32/Scripts/env/Scripts/chatbot/data/'):
        data=open('C:/Users/Dell/AppData/Local/Programs/Python/Python38-32/Scripts/env/Scripts/chatbot/data/' + file,encoding='latin-1').readlines()   
        trainer.train(data)
logging.basicConfig(filename='example.log',level=logging.DEBUG)

while True:
    message=input("user:")
    if message.strip()!= 'bye':
        response=chatbot.get_response(message)
        print("kiki:",response)

    if message.strip() == 'bye':
            print('bye')     
            break       