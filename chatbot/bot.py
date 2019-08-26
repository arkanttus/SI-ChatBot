from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Training Example')

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "../corpus"
)

while True:
    try:
        user = input("Voce: ")
        response = chatbot.get_response(user)
        print("bot: " + str(response))
        print("confidence: " + str(response.confidence))
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
