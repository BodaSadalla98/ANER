from numpy import string_
from franco import franco_trans
import re
from helpers.constants import class_to_color







wiki_base_url = "https://ar.wikipedia.org/wiki/"

def prepare_output(sentence, labels):
    res = ""
    for i in range(len(sentence)):
        res += sentence[i] + ": " + labels[i]+ "\n"
    return res


def final_result(l):
    s = ''
    print('l is :')
    print (l)
    for t in l:
        print(t)
    return s


def is_english(s):
    for l in s:
        if (65 <= ord(l) <= 90) or (97 <= ord(l) <= 122):
            return True
    return False


def is_ar(s):
    for ch in s:
        if ('\u0600' <= ch <= '\u06FF' or
                '\u0750' <= ch <= '\u077F' or
                '\u08A0' <= ch <= '\u08FF' or
                '\uFB50' <= ch <= '\uFDFF' or
                '\uFE70' <= ch <= '\uFEFF' or
                '\U00010E60' <= ch <= '\U00010E7F' or
                '\U0001EE00' <= ch <= '\U0001EEFF'):
            return True
    return False


def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')


def remove_r(s):
    l = s.split('\r')
    res = " ".join(l)
    return res


def remove_n(s):
    l = s.split('\n')
    res = " ".join(l)
    return res


def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)


def prepare_sentence(s):
    temp = remove_n(s)
    temp = remove_r(temp)
    temp = remove_emoji(temp)
    l = temp.split(' ')
    for i in range(0, len(l)):
        w = l[i]
        if(not is_ar(w)  and w!= ','):
            l[i] = franco_trans(w)
    res = " ".join(l)
    return res
 

##### Start here

# def get_separate_entities(labels, tokens):
#     """
#         takes labels and token , return full name entity (mohamed, salah --> "mohamed salah")
#         this will be used to search in wikipedia
#     """

#     print(labels, tokens)

#     res = []                                          
#     b_before = False
#     temp = ""
#     key_value = ()
#     for i in range(len(labels)):
#         print(res)
#         curr = labels[i]
        
#         if("B-" in curr):
#             curr_class = curr.split('-')[1]
#             if(b_before):
#                 key_value = (temp[:-1], 1, class_to_color[curr_class])
#                 res.append(key_value)
#                 temp = tokens[i] + ' '
#             else:
#                 b_before = True
#                 temp += tokens[i] + ' '
#                 if(i == len(labels)-1):
#                     key_value = (temp[:-1], 1, class_to_color[curr_class])
#                     res.append(key_value)
#                 # print("temp is:" + str(temp))

#         elif("I-" in curr):
#             curr_class = curr.split('-')[1]

#             temp += tokens[i] + ' '
#             if(i == len(labels)-1):
#                 key_value = (temp[:-1], 1, class_to_color[curr_class])
#                 res.append(key_value)

#         else:
#             if(temp == ""):
#                 key_value = (tokens[i], 0)
#                 res.append(key_value) 
#             else:
#                 key_value = (temp[:-1], 1)
#                 res.append(key_value)
#                 key_value = (tokens[i], 0)
#                 res.append(key_value) 
#                 temp = ""
#                 b_before = False
    
   

#     print(res)
#     return res 

def get_separate_entities(labels, tokens):

    outputs = []

    last_cls = ''

    for i, x in enumerate(labels):
        label = labels[i]

        if  label == 'O':
            outputs.append([tokens[i],0,''])
            last_cls = ''
        
        elif 'B-' in label:
            cls = label[2:]
            outputs.append([tokens[i],1,class_to_color[cls]])
            last_cls = cls
        else:
            cls = label[2:]
            if cls == last_cls:
                t,_,clr = outputs[-1]
                t = t + ' ' + tokens[i]
                outputs[-1] = [t,1,clr]
            else:
                outputs.append([tokens[i],1,class_to_color[cls]])
                last_cls = cls

    print(outputs)
    return outputs





def get_wiki_urls(names):
    """
        gets the correct url of wikepedia for a certain search entity
    """
    res = []
    
    for e in names:
        if(e[1] == 0):
            res.append('#')
            continue

        temp = ""
        name = e[0]
        
        for c in name:
            if(c == ' '):
                temp += '_'
            else:
                temp += c
        res.append(wiki_base_url + temp)

    return res








