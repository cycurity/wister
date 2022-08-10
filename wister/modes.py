import wister.utils as utils
import sys
import os

# Word Mix
def type1 (min, max, words, final, v, depth, total, bar):
    if (v):
        print("Mixing words...")

    tmp = ""
    count = 1
    for a in words:
        if (not v and bar):
            utils.progress((count + total[0]) / total[1])
            count += 1
        tmp = a + a
        if (len(tmp) <= max and len(tmp) >= min):
            final.append(tmp)
        if (len(a) <= max and len(a) >= min):
            for b in words:
                if (not a == b):
                    tmp = a + b
                    if (len(tmp) <= max and len(tmp) >= min):
                        final.append(tmp)
                        if (depth >= 3):
                            for c in words:
                                if (not c == a and not c == b):
                                    tmp = a + b + c
                                    if (len(tmp) <= max and len(tmp) >= min):
                                        final.append(tmp)
                                        if (depth >= 4):
                                            for d in words:
                                                if (not d == a and not d == b and not d == c):
                                                    tmp = a + b + c + d
                                                    if (len(tmp) <= max and len(tmp) >= min):
                                                        final.append(tmp)
                                                        if (depth == 5):
                                                            for e in words:
                                                                if (not e == a and not e == b and not e == c and not e == d):
                                                                    tmp = a + b + c + d + e
                                                                    if (len(tmp) <= max and len(tmp) >= min):
                                                                        final.append(tmp)

    return final


# Case Alternate
def type2 (words, final, v, total, bar):
    if (v):
        print("Alternating letter case...")
    count = 1
    for word in words:
        if (not v and bar):
            utils.progress((count + total[0]) / total[1])
            count += 1
        if (len(word) == 1):
            if (word.islower()):
                final.append(word.upper())
            elif (word.isupper()):
                final.append(word.lower())
        else:
            if (word.islower()):
                final.append(word.upper())  
                final.append(word.capitalize())
                if (len(word) > 2):
                    final.append(str(word[0:1].upper() + word[1:len(word)-1] + word[len(word)-1:len(word)].upper()))
                final.append(str(word[0:len(word)-1] + word[len(word)-1:len(word)].upper()))
            elif (word.isupper()):
                final.append(word.lower())  
                final.append(word[:1].lower() + word[1:])
                if (len(word) > 2):
                    final.append(str(word[0:1].lower() + word[1:len(word)-1] + word[len(word)-1:len(word)].lower()))
                final.append(str(word[0:len(word)-1] + word[len(word)-1:len(word)].lower()))
            elif (not word.isalpha()):
                continue
            else:
                lowercase = word.lower()
                uppercase = word.upper()
     
                final.append(uppercase)
                final.append(lowercase)
                final.append(uppercase[:1].lower() + uppercase[1:])
                final.append(lowercase[:1].upper() + lowercase[1:])
                
                if (len(word) > 2):
                    final.append(str(uppercase[0:1].lower() + uppercase[1:len(uppercase)-1] + uppercase[len(uppercase)-1:len(uppercase)].lower()))
                final.append(str(uppercase[0:len(uppercase)-1] + uppercase[len(uppercase)-1:len(uppercase)].lower()))
                if (len(word) > 2):
                    final.append(str(lowercase[0:1].upper() + lowercase[1:len(lowercase)-1] + lowercase[len(lowercase)-1:len(lowercase)].upper()))
                final.append(str(lowercase[0:len(lowercase)-1] + lowercase[len(lowercase)-1:len(lowercase)].upper()))
                
    return final


# Homograph
def type3 (words, final, v, total, bar):
    if (v):
        print("Using homograph characters...")
    
    chars = {
        'A': ['4', '@'],
        'E': ['3', '€', '&', '£'],
        'T': ['7', '+'],
        'S': ['$', '§', '5', 'z', 'Z'],
        'I': ['1', '!', '|'],
        'O': ['0'],
        'B': ['8', '6'],
        'C': ['<', '(', '{'],
        'Q': ['9', '0', 'O'],
        'L': ['1'],
        'H': ['#']
    }
    sys.stdout.write("\r")
    tmp = words.copy()
    count = 1
    for word in tmp:
        if (not v and bar):
            utils.progress((total[0] / total[1]) + ((count + total[0]) / (len(tmp) * (total[1] / len(words)))))
            count += 1
        for letter in word:
            if letter.upper() in chars:
                for new_letter in chars[letter.upper()]:
                    new_word = word.replace(letter, new_letter)
                    tmp.append(new_word)

    return final + tmp


# Reverser
def type4 (words, final, v, total, bar):
    if (v):
        print("Reversing words...")

    count = 1
    for w in words:
        if (not v and bar):
            utils.progress((count + total[0]) / total[1])
            count += 1
        a = w[::-1]
        final.append(a)
    
    return final


# Salt
def type5 (min, max, words, final, v, depth, total, bar):
    if (v):
        print("Adding salt...")
    lines_stripped = []
    try:
        #with resources.open_binary("wister", "salt.dic") as fp:
        #    saltb = fp.read()
        #salt = BytesIO(saltb)
        with open(os.path.abspath(os.path.dirname(__file__)) + "/salt.dic") as file:
            count = 1
            lines = file.readlines()
            for l in lines:
                lines_stripped.append(l.strip())
            for w in words:
                if (not v and bar):
                    utils.progress((count + total[0]) / total[1])
                    count += 1
                final = final + __type5extra(min, max, [w] + [lines_stripped], final)
    finally:
        pass

    return final


def __type5extra(min, max, words, final):
    tmp = ""
    w = words[0]
    if (len(w) <= max and len(w) >= min and not w.isdigit()):
        for b in words[1]:
            if (not w == b):
                tmp = w + b
                if (len(tmp) <= max and len(tmp) >= min):
                    final.append(tmp)
                    for c in words[1]:
                        if (not c == w and not c == b and not (c.isdigit() and b.isdigit())):
                            tmp = w + b + c
                            if (len(tmp) <= max and len(tmp) >= min):
                                final.append(tmp)

    return final