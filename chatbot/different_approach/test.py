from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
bot = ChatBot('Carbo')

trainer = ListTrainer(bot)


for knowledeg in os.listdir('base'):
	BotMemory = open('base/'+ knowledeg, 'r').readlines()
	trainer.train(BotMemory)



app = Flask(__name__)

@app.route('/home')
def index():
	return render_template('index.html')

@app.route('/process',methods=['POST'])
def process():
	user_input=request.form['user_input']

	bot_response=bot.get_response(user_input)
	bot_response=str(bot_response)
	print("Carbo: "+bot_response)
	return render_template('index.html',user_input=user_input,
		bot_response=bot_response
		)


if __name__=='__main__':
	app.run(debug=True,port=2021)