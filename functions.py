import pywhatkit


def playing(command,talk):
 song = command.replace('play', '')
 talk('playing ' + song)
 pywhatkit.playonyt(song)

def va_change_lang(text):
    langs = [{"name":"french","code":"FR-FR",'num':0},{"name":"english","code":"EN-US",'num':1},{"name":"spanish","code":"es-ES"}]
    query = text
    for  lang in langs:
       print(lang['name'] + text)
       if lang["name"] in text:
          print("oui")
          result = [lang["code"],lang["num"],lang["name"]]
          return result
        

