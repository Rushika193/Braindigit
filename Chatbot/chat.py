from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatbot=ChatBot('Kiki')
trainer=ListTrainer(chatbot)

trainer.train(['Hi, how are you?',
                'I am good,What about you?',
                    'Good too',
                    'What would you prefer to do in free time?',
                    'listening music,dance,cooking and reading,'])


while True:
    request=input('user: ')
    response=chatbot.get_response(request)
    print('Kiki: ',response)