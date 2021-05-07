"""
Naman Dave (Edit Aakash Panchal)
Aim: Different function testing in recombyte.py
Format: Function name followed by tests

Functions in recombyte.py ----- Testing_done
1. hash-build        ----- DONE      
2. inv_hash_build       ---- YES
3. save_hash        ---- YES
4. save_data        ---- YES
5. load_data        ---- YES
6. autocorrect_word  ----- DONE
7. lcs  ----- DONE
8. recombyte_q  ----- DONE
"""
import os
import src.va as va
import recombyte as rb
import pytest
import numpy as np

def test_inv_hash_build():
    rb.HASH_DUMP_FILE_NAME = "test.txt"
    query_list2 = ["Lorem", "Ipsum"]
    total_words = rb.hash_build(query_list2)
    ivh = rb.inv_hash_build(query_list2, total_words)
    
    assert set(ivh.keys()) == set({'lorem', 'ipsum'})
    assert ivh['lorem'][0][0] == 0 or ivh['lorem'][0][0] == 1
    assert ivh['lorem'][1][0] == 0 or ivh['lorem'][1][0] == 1
    assert ivh['lorem'][1][1] == 0 or ivh['lorem'][1][1] == 1
    assert ivh['ipsum'][0][0] == 1 ^ bool(ivh['lorem'][0][0])
    assert ivh['ipsum'][1][0] == 1 ^ bool(ivh['lorem'][1][0])
    assert ivh['ipsum'][1][1] == 1 ^ bool(ivh['lorem'][1][1])
    
def test_save_hash():
    rb.HASH_DUMP_FILE_NAME = "test2.txt"
    if os.path.exists(rb.HASH_DUMP_FILE_NAME):
        os.remove(rb.HASH_DUMP_FILE_NAME)

    query_list = ["lorem ipsum", "pikachu zap"]
    total_words = rb.hash_build(query_list)
    rb.save_hash(total_words)
    assert os.path.exists(rb.HASH_DUMP_FILE_NAME)
    os.remove(rb.HASH_DUMP_FILE_NAME)
    
    
def test_save_data():
    rb.DATA_STORAGE_FILENAME = "test_data_storage.p"
    if os.path.exists(rb.DATA_STORAGE_FILENAME):
        os.remove(rb.DATA_STORAGE_FILENAME)
    query_list = ["lorem ipsum", "pikachu zap"]
    rb.save_data(query_list)
    assert os.path.exists(rb.DATA_STORAGE_FILENAME)
    os.remove(rb.DATA_STORAGE_FILENAME)


def test_load_data():
    rb.DATA_STORAGE_FILENAME = "test_data_storage.p"
    if os.path.exists(rb.DATA_STORAGE_FILENAME):
        os.remove(rb.DATA_STORAGE_FILENAME)
    query_list = ["lorem ipsum", "pikachu zap"]
    rb.save_data(query_list)
    query_list, total_words, ivh, tot_words_dict = rb.load_data()
    
    assert os.path.exists(rb.DATA_STORAGE_FILENAME)
    assert set(query_list) == set({'lorem ipsum', 'pikachu zap'})
    assert set(total_words) == set({'ipsum', 'zap', 'pikachu', 'lorem'})
    assert str(type(tot_words_dict)) == "<class 'enchant.pypwl.PyPWL'>"
    assert ivh['lorem'][0][0] == ivh['ipsum'][0][0]
    assert np.all(ivh['lorem'][1] == ivh['ipsum'][1])
    assert ivh['pikachu'][0][0] == ivh['zap'][0][0]
    assert np.all(ivh['pikachu'][1] == ivh['zap'][1])
    assert ivh['zap'][0][0] == 0 or ivh['zap'][0][0] == 1
    assert ivh['lorem'][0][0] == 1 ^ bool(ivh['zap'][0][0])
    assert ivh['lorem'][1][0] == 1 ^ bool(ivh['zap'][1][0])
    assert ivh['lorem'][1][1] == 1 ^ bool(ivh['zap'][1][1])
    os.remove(rb.DATA_STORAGE_FILENAME)

