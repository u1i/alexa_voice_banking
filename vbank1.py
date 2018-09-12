# -*- coding: utf-8 -*-

# speechcons: https://developer.amazon.com/docs/custom-skills/speechcon-reference-interjections-english-us.html

import logging
import os
import random

from flask import Flask
from flask_ask import Ask, request, session, question, statement

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)


@ask.launch
def launch():
    speech_output = "<speak>Welcome to Yoisho Bank!</speak>"
    #speech_output = "<speak><say-as interpret-as='cardinal'>12345</say-as><say-as interpret-as='digits'>12345</say-as></speak>"
    #speech_output = "<speak><audio src='https://s3.amazonaws.com/xwaay/irasshaimase2.mp3'/></speak>"

    reprompt_text = speech_output
    return question(speech_output).reprompt(reprompt_text)

@ask.intent('GetBalance')
def get_balance():

	try:
		file = open("/tmp/balance.db","r")
		amount = str(int(file.read()))
		file.close()
	except:
		amount = "0"

	if amount == "0":
		return statement("<speak><say-as interpret-as='interjection'>Well well</say-as>. You have zero dollars. <prosody pitch='x-high'>Nothing at all.</prosody> Nada. <say-as interpret-as='interjection'>aw man</say-as>.</speak>")
	else:
		return statement("<speak>Your account currently has a balance of <say-as interpret-as='cardinal'>" + amount + "</say-as> dollars. <say-as interpret-as='interjection'>yay</say-as>.</speak>")

@ask.intent('AMAZON.StopIntent')
def stop():
    return statement("Thank you for banking with us!")

@ask.intent('AMAZON.FallbackIntent')
def stop():
    outp = "Sorry I didn't get that. Try again?"
    return question(outp).reprompt(outp)

@ask.intent('AMAZON.CancelIntent')
def cancel():
    return statement("Thank you for banking with us!")


@ask.session_ended
def session_ended():
    return "{}", 200

if __name__ == '__main__':
    app.run(debug=True)
