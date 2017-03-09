import json
import re
import random
# import pymorphy2
import subprocess
# morph = None

# def morph_init():
#     global morph
#     morph = pymorphy2.MorphAnalyzer()

def is_correct(word):
    if len(word)<15 and re.match('[а-яА-ЯЁё]+',word):
        return True
    return False

# def normal_form(word):
#     return morph.parse(word)[0].normal_form

# def same_form(origin_word,word_to_change):
#     origin_parsed = morph.parse(origin_word)[0]
#     change_parsed = morph.parse(word_to_change)[0]
#     params = set()
#     for i in str(change_parsed.tag).split(","):
#         if i:
#             try:
#                 inflected = origin_parsed.inflect({i})
#             except Exception:
#                 pass
#     return inflected.word

def split_into_words(string):
    return re.sub("[^\w]", " ",  string).split()

def json_read(filename):
    with open(filename) as f:
        return json.load(f)

def json_write(filename,data):
    with open(filename,'w') as f:
        return json.dump(data,f)

def sublist_exists(l1, l2):
    return l1.issubset(l2)

def choice(iterable):
    return random.choice(iterable)

def command_output(command):
    df = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE)
    return df.communicate()[0].decode().strip()
