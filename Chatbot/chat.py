from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.response_selection import get_first_response
from chatterbot.comparisons import levenshtein_distance

def get_response(message):

    chatbot = ChatBot('kiki',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
           {
            "import_path": "chatterbot.logic.BestMatch",
             'maximum_similarity_threshold': 0.90,
             "default_response": 'I am sorry, but I do not understand.',
            },
             ],
            trainer='chatterbot.trainers.ListTrainer')

    

    while True:
        if message.strip()!='bye':
            reply=chatbot.get_response(message)
            response=str(reply)
            return(response)

        if message.strip()=='bye':
            return("bye")
            break
