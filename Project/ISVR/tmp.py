"""
Developer   : Naman Dave
College ID  : 201801439
About       : Temporary file (for testing purpose)
"""
import os
import src.va as va
import recombyte as rb

my_list = [
        "Open Chrome",
        "Open text editor",
        "Open Mozila firefox",
        "Evaluate string",
        "Search Online",
        "search file online",
        "Search File",
        "Play music",
        "Play a Song",
        "Play songs",
        "youtube",
        "youtube music",
        "open youtube",
        "Play youtube",
        "Play songs youtube",
        "play song youtube",
        "open youtube and play songs",
        "open youtube and play a song",
        "open youtube and play music"
        ]
query_list = list(my_list)

rm = True

if rm or not os.path.exists(rb.DATA_STORAGE_FILENAME):
    os.remove("data_storage.p")
    rb.save_data(query_list)

query_list, total_words, words_dict, tot_words_dict = rb.load_data()
command = ""
while True:
    command = va.ask()
    if "stop" in command:
        break
    answer = rb.recombyte_q(command, query_list, words_dict, tot_words_dict)
    print(answer)
    if answer != []:
        va.speak(answer[0][0])