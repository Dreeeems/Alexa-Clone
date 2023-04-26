def playing(command,talk):
 song = command.replace('play', '')
 talk('playing ' + song)
 return song




fct=[playing]