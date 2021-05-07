"""
Developer   : Naman Dave
College ID  : 201801439
About       : CLI based implementation(beta)
"""
def merge_dict(a, b):
    return {**a, **b}
import os
import sys
import src.va as va
import recombyte as rb
import webbrowser
from src.nmn import dict1
from sys import platform
from src.Jay_201801141 import hash_dict as h10
from src.nishit import hash_dict as h1
from src.jeet201801232 import hash_dict as h2
from src.kbg_201801147 import hash_dict as h3
from src.aakash import hash_dict as h4
from src.createfile_118 import hash_dict as h5
from src.deletefile_118 import hash_dict as h6
from src.hash_201801012 import hash_201801012 as h7
from src.parthav import hash_dict as h8
from src.sid_201801470 import hash_dict as h9
dict1 = merge_dict(dict1, h10)
dict1 = merge_dict(dict1,h1)
dict1 = merge_dict(dict1,h2)
dict1 = merge_dict(dict1,h3)
dict1 = merge_dict(dict1,h4)
dict1 = merge_dict(dict1,h5)
dict1 = merge_dict(dict1,h6)
dict1 = merge_dict(dict1,h7)
dict1 = merge_dict(dict1,h8)
dict1 = merge_dict(dict1,h9)



my_list = [ ]

my_list += list(dict1.keys())
query_list = list(my_list)

rm = True
#print(rb.recombyte_q.__docs__())
if rm or not os.path.exists(rb.DATA_STORAGE_FILENAME):
     #os.remove("F:\\temp\Grp-28-Intelligent_Systems_of_Voice_Recognition\Project\ISVR\data_storage.p")
     rb.save_data(query_list)

query_list, total_words, words_dict, tot_words_dict = rb.load_data()
command = None
while True:

    command = va.ask().lower()
    if(command==""):
        continue
    if "search" in command and "online" in command:
        webbrowser.open("https://www.google.com/search?q=" +command.split("online")[1])
        continue
    if "stop" in command or "shut down" in command or "shutdown" in command: 
        break
    answer = rb.recombyte_q(command, query_list, words_dict, tot_words_dict)

    #print(answer)
    if answer != []:
        answer[0][0] = answer[0][0].lower()
        #va.speak(answer[0][0])
        if answer[0][0] in dict1:
            dict1[answer[0][0]](command)

