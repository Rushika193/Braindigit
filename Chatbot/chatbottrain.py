from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import logging

def set():
    chatbot=ChatBot('Kiki',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            trainer='chatterbot.trainers.ListTrainer',)
    logging.basicConfig(filename='example.log',level=logging.DEBUG)
   
    trainer=ListTrainer(chatbot)
    for files in os.listdir('C:/Users/Dell/AppData/Local/Programs/Python/Python38-32/Scripts/env/Scripts/chatbot/data/'):
        data=open('C:/Users/Dell/AppData/Local/Programs/Python/Python38-32/Scripts/env/Scripts/chatbot/data/' + files,encoding='latin-1').readlines()   
        trainer.train(data) 

                 

set()       


