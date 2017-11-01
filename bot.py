#bot.py

import json 
import requests
import time
import wikipedia
import sys

wikipedia.set_lang("pt")

TOKEN = "453230637:AAHOqkOTt9Kd1HP5xsH0xxiazdWVTsS2VZU"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)



#def wiki(chat_id):
  #   textq = 'Sobre o que voce quer saber?'
   #  url = URL + "sendMessage?text={}&chat_id={}".format(textq, chat_id)
    # get_url(url)
#
 #    text_a, chat = get_last_chat_id_and_text(get_updates())
  #   ans = wikipedia.summary(text_a, sentences=2)
   #  url = URL + "sendMessage?text={}&chat_id={}".format(ans, chat_id)
    # get_url(url)




def send_message(text, chat_id):
    if (text) == ('/acorde'):
         text1 = 'Bom Dia!'
         url = URL + "sendMessage?text={}&chat_id={}".format(text1, chat_id)
         get_url(url)
    else:
         url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
         get_url(url)

def main():
    last_textchat = (None, None)
    while True:
        text, chat = get_last_chat_id_and_text(get_updates())
        if (text, chat) != last_textchat:
            send_message(text, chat)
            last_textchat = (text, chat)
        time.sleep(0.5)
        print (text,chat)


if __name__ == '__main__':
    main()