import logging
import os
import re
import random
from six.moves.urllib.request import urlopen


from flask import Flask
from flask_ask import Ask, request, session, question, statement


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)


@ask.launch
def launch():
    speech_output = "Would you like to hear a pun? I promise it's funny."
    reprompt_text = speech_output
    return question(speech_output).reprompt(reprompt_text)


@ask.intent('GetPun')
def get_pun():
	sj = [ "Don't trust the atoms - they make up everything", "It's hard to explain puns to kleptomaniacs because they always take things literally.", "Nostalgia ain't what it used to be.", "Is there another word for 'pseudonym'?", "I used to think the brain was the most important organ. Then I thought, look what's telling me that.", "A magician was walking down the street and turned into a grocery store.", "A blind man walks into a bar. And a table. And a chair.", "What's the best part about living in Switzerland? Not sure, but the flag is a big plus.", "Two fish are in a tank. One turns to the other and asks 'How do you drive this thing?'", "Pampered cows produce spoiled milk.", "Learn sign language, it's very handy.", "I started a band called ninehundredninetynine Megabytes - we haven't gotten a gig yet.", "What is the difference between ignorance and apathy? I don't know, and I don't care.", "Dwarfs and midgets have very little in common.", "How do you make Holy Water - you boil hell out of it.", "I wondered why the frisbee was getting bigger, and then it hit me.", "At first I didn't know how to fasten the seatbelt. Then it clicked.", "I totally understand how batteries feel because I'm rarely ever included in things either.", "I invented a new word: Plagiarism" ]

	joke = sj[random.randint(0,len(sj)-1)]
	return statement(joke)

@ask.intent('Axway')
def get_axway():
	return statement("Axway? It's the coolest company on the planet!")

@ask.intent('AMAZON.StopIntent')
def stop():
    return statement("This was fun. Cheers!")

@ask.intent('AMAZON.FallbackIntent')
def stop():
    outp = "Sorry I didn't get that. Try again?"
    return question(outp).reprompt(outp)

@ask.intent('ConfusedIntent')
def stop():
    outp = "Oh come on. Play along, will you?"
    return question(outp).reprompt(outp)


@ask.intent('AMAZON.CancelIntent')
def cancel():
    return statement("Goodbye")

@ask.intent('CanFulfillIntentRequest')
def cancel():
    return statement("Yo!")


@ask.session_ended
def session_ended():
    return "{}", 200

if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)

