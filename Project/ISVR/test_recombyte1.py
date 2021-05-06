"""
Aakash Panchal (Edit Naman)
Aim: Different function testing in recombyte.py
Format: Function name followed by tests

Functions in recombyte.py ----- Testing_done
1. hash-build        ----- YES      
2. inv_hash_build
3. save_hash
4. save_data
5. load_data
6. autocorrect_word  ----- YES
7. lcs  ----- YES
8. recombyte_q  ----- YES
"""

import os
import src.va as va
import recombyte as rb
import pytest

my_list = [
    "Open Chrome",
    "Open text editor",
    "Open Mozila firefox",
    "Evaluate string",
    "Search Online",
    "Search File",
    "Play music",
    "Play Song ",
    "Open Youtube",
]

# Changed, the test mustn't disrupt the original hash storage (Naman)
rb.HASH_DUMP_FILE_NAME = "test.txt"
query_list = list(my_list)
total_words = rb.hash_build(query_list)
words_dict = rb.inv_hash_build(query_list, total_words)
rb.save_hash(total_words)
tot_words_dict = rb.load_hash()


# hash_build ---------------------------------------------------------------------------------------
# function returns a set containing all unique words in the query_list (case in-sensitive)
# All words are begin converted into lower-case

def test_hash_build1():
    #1 Basic Test
    assert rb.hash_build(list(["Open Chrome"])) == set({'open', 'chrome'})

def test_hash_build2():
    #2 Empty input
    assert rb.hash_build(list([])) == set({})

# Inv_hash_build -------------------------TBD-------------------------------------------------------

# Function returns 
assert(True)

# autocorrect_word() -------------------------------------------------------------------------------


#1 firefox
def test_autocorrect_word1():
    assert rb.autocorrect_word("mozfirefox", tot_words_dict)[0] == "firefox"


#2 music
def test_autocorrect_word2():
    assert rb.autocorrect_word("mosicss", tot_words_dict)[0] == "music"


#3 youtube
def test_autocorrect_word3():
    assert rb.autocorrect_word("yotbe", tot_words_dict)[0] == "youtube"


#4 Online
def test_autocorrect_word4():
    assert rb.autocorrect_word("on lion", tot_words_dict)[0] == "online"


#5 text
#assert(rb.autocorrect_word("texxxxxxxxxxxxxxxxxxxxxt", tot_words_dict)[0] == "text")
def test_autocorrect_word5():
    assert rb.autocorrect_word("texxxxt", tot_words_dict)[0] == "text"


#6 Evaluate
def test_autocorrect_word6():
    assert rb.autocorrect_word("evalueate", tot_words_dict)[0] == "evaluate"


# lcs : Returns the length of longest common subsequence----------------------------------------------------


#1 Basic test
def test_lcs1():
    assert rb.lcs("One", "Once up") == 3


#2 Case differentiate (Output 3 not 4 : "ame")
def test_lcs2():
    assert rb.lcs("same", "Same") == 3


#3 Empty input
def test_lcs3():
    assert rb.lcs(" ", "") == 0

    
#4 zero as ouptut
def test_lcs4():
    assert rb.lcs("a", "b") == 0


#recombyte_q ----------------------------------------------------
#1 mozilla firefox test
def test_recombyte_q1():
    assert rb.recombyte_q(
                "Hey badman, don go upa n dan jass open mozillla firefoxy",
                query_list,
                words_dict,
                tot_words_dict,
                take_best=True,
            )[0][0] == "Open Mozila firefox"

    
#2a Just to check how system responds when there is no matching functionality
def test_recombyte_q2():
    assert len(rb.recombyte_q(
                "N",
                query_list,
                words_dict,
                tot_words_dict,
                take_best=True,
            )) == 0


#2b Just to check how system responds when there is no matching functionality
def test_recombyte_q3():
    assert len(rb.recombyte_q(
                "Nothing to say",
                query_list,
                words_dict,
                tot_words_dict,
                take_best=False,  # Change Naman
                t1=1.0,
                t4=1.0,
            )) == 0


#3 Play music test
def test_recombyte_q4():
    assert rb.recombyte_q(
                "ply msc",
                query_list,
                words_dict,
                tot_words_dict,
                take_best=True,
            )[0][0] == "Play music"


#4 search online testing
def test_recombyte_q5():
    assert rb.recombyte_q(
                "I want to Search online",
                query_list,
                words_dict,
                tot_words_dict,
                take_best=False,
                t1 = 0.7,
                t2 = 0.69,
                t4 = 0
            )[0][0] == "Search Online"


#5 Mention of two types queries together
def test_recombyte_q6():
    assert rb.recombyte_q(
                "Wnna open a file",
                query_list,
                words_dict,
                tot_words_dict,
                take_best=True,
            )[0][0] == "Search File"

    
#6 Weired type of input : checks how system responds!
def test_recombyte_q7():
    assert len(rb.recombyte_q(
                "No ha ha ha ha ha",
                query_list,
                words_dict,
                tot_words_dict,
                take_best=True,
            )) == 0


