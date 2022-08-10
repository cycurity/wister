import argparse
import sys
import hashlib
import urllib.parse
import base64

def args(version):
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("-c", "--combination", dest="types", metavar="[1-5]", choices=(1,2,3,4,5), nargs="+", type=int, help="Select which types of combinations to use.")
    parser.add_argument("-d", "--depth", metavar="[2-5]", choices=(2,3,4,5), type=int, default=3, help="Select the depth of word mixing when using combination mode 1. Default: 3")
    parser.add_argument("-e", "--encode", metavar="FORMAT", choices=("md5", "base64", "hex", "url", "sha1", "sha256" , "sha512", "sha3-256", "sha3-512"), help='Encode/Hash the generated wordlist with a given algorithm: "md5", "base64", "hex", "url", "sha1", "sha256" , "sha512", "sha3-256", "sha3-512"')
    parser.add_argument("-i", "--input", metavar="FILE", type=argparse.FileType('r'), dest="input", help="Select the input file containing the words.")
    parser.add_argument("-l", "--list", action="store_true", help="List the types of combination.")
    parser.add_argument("-m", "--min", metavar="[0-49]", default=0, type=int, help="Select minimum characters for output. Default: 0")
    parser.add_argument("-M", "--max", metavar="[1,50]", default=20, type=int, help="Select maximum characters for output. Default: 20")
    parser.add_argument("-o", "--output", default="output.lst", metavar="FILE", type=argparse.FileType('w'), dest="output", help="Specify the output file. Default: output.lst")
    parser.add_argument("-N", "--noprogress", dest="noprog", action="store_true", default=False, help="Disables progress bar (increases performance)")
    parser.add_argument("-v", "--version", action="version", version=f"{version}", help="Returns the version of the program.")
    parser.add_argument("-V", "--verbose", action="store_true", default=False, help="Verbose the output.")
    parser.add_argument("-w", "--words", nargs='+', type=str, help="Words to generate the output with.")
    
    # ADD argument for number of threads to execute
    # ADD argument to ask if the user wants the generated words to be echoed on stdout
    return parser.parse_args()

def list():
    print("""
    Types of Combinations

1.  Word Mix - The words are mixed between each other
        abc123
        admin123
        123abc
        123admin
        abcadmin
        admin123abc
        ...

2.  Case Alternate - The case is mixed for each word or combination
        Admin
        admiN
        AdmiN
        ADMIN

3.  Homograph - Change specific characters for others, commonly used, similar ones
        4dmin
        @dmin
        adm1n
        adm!n
        4dm1n
        @dm1n
        ...

4.  Reverser - Reverse the words
        admin
        123
        abc
        nimda
        321
        cba

5.  Saltify - Add some salt (like ponctuation or numbers)
        admin1
        admin.123
        abc_admin
        123-abc
        ...

You can add multiple types of combinations when executing.""")

def progress(progress):
    barLength = 40
    if isinstance(progress, int):
        progress = float(progress)
    if progress < 0:
        progress = 0
    if progress >= 1:
        progress = 1
    block = int(round(barLength * progress))
    text = "\r[{0}] {1:.0f}%".format( "#" * block + "-" * (barLength - block), progress * 100)
    sys.stdout.write(text)
    sys.stdout.flush()

def wordfile (file):
    words = []
    for word in file:
        word = word.strip()
        words.append(word)
    file.close()
    return words

def output (file, words: list, v):
    if (v):
        print("Saving to '" + file.name + "'...")
    for i in words:
        file.write(i + "\n")
    bts = file.tell()
    file.close()
    return bts

def encode(final, encoding):
    newfinal = []
    if (encoding == "md5"):
        for w in final:
            newfinal.append(hashlib.md5(w.encode()).hexdigest())
    elif (encoding == "url"):
        for w in final:
            newfinal.append(urllib.parse.quote_plus(w))
    elif (encoding == "base64"):
        for w in final:
            newfinal.append(str(base64.b64encode(w.encode("utf-8")), "utf-8"))
    elif (encoding == "hex"):
        for w in final:
            newfinal.append(w.encode("utf-8").hex())
    elif (encoding == "sha1"):
        for w in final:
            newfinal.append(hashlib.sha1(w.encode()).hexdigest())
    elif (encoding == "sha256"):
        for w in final:
            newfinal.append(hashlib.sha256(w.encode()).hexdigest())
    elif (encoding == "sha512"):
        for w in final:
            newfinal.append(hashlib.sha512(w.encode()).hexdigest())
    elif (encoding == "sha3-512"):
        for w in final:
            newfinal.append(hashlib.sha3_512(w.encode()).hexdigest())
    else:
        for w in final:
            newfinal.append(hashlib.sha3_256(w.encode()).hexdigest())
    return newfinal

def convert(b):
    b = int(b)
    if (b > 1000000000):
        return f"{b / 1000000000:.2f} Gb"
    elif (b > 1000000):
        return f"{b / 1000000:.2f} Mb"
    elif (b > 1000):
        return f"{b / 1000:.2f} Kb"
    else:
        return f"{b:.2f} B"