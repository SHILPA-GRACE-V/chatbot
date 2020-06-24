#Import packages
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#Import data to train the chatbot
bot=ChatBot('CHOTTU')                   #define chatbot
bot.set_trainer(ChatterBotCorpusTrainer)#define trainer - set algorithm
bot.train('chatterbot.corpus.english')  #Train the chatbot

#write code for interacting with chatbot

while(True):
    message=input('You: ')
    if(message=='Bye' or message=='bye'):
        #print('ChatBot: Bye. See you soon.')
        #print(bot.name,': Bye. See you soon')
        print('{}: Bye. See you soon.'.format(bot.name))
        break
    if(message!='Bye' or message!='bye'):
        #print('ChatBot: ',bot.get_response(message))
        print('{}: {}'.format(bot.name, bot.get_response(message)))
