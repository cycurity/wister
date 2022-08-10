import wister.utils as utils
import wister.modes as modes
import sys
import time

def control (argv):
    v = argv.verbose
    min = 0
    max = 50
    words = []
    final = []

    if (argv.list):
        utils.list()
        sys.exit(0)

    if (not argv.words and not argv.input):
        sys.stderr.write("Error: No input file or words provided.\n")
        sys.exit(1)

    if (v):
        print("----------------------")

    if (argv.min >= 0 and argv.min < 50):
        min = argv.min
    else:
        sys.stderr.write("Error: Minimum limit cannot be less than 0 or higher than 49.\n")
        sys.exit(1)

    if (argv.max > min and argv.max <= 50):
        max = argv.max
    else:
        sys.stderr.write("Error: Maximum limit cannot be less than 1, higher than 50 or less than the minimum limit.\n")
        sys.exit(1)
    
    if (argv.types and v):
        print("Combinations: ", end="")
        for i in argv.types:
            if (i == argv.types[-1]):
                print(i)
            else:
                print(i, end=", ")
    
    if (argv.words):
        words = argv.words
        if (v):
            print("Words: ", end="")
            for i in words:
                if (i == words[-1]):
                    print(i)
                else:
                    print(i, end=", ")
    
    if (argv.input):
        words = utils.wordfile(argv.input)
        if (v):
            print(f"Input file: {argv.input.name}")
    
    if (argv.output != "output.lst" and v):
        print(f"Output file: {argv.output.name}")
    
    if (v):
        print("-----------\n")

    print("Generating wordlist...")
    start = time.time()
    final = words.copy()
        
    if (argv.types):
        if (not v and not argv.noprog):
            utils.progress(0)
        total = len(argv.types) * len(words)
        c = 0
        for i in argv.types:
            if (i == 1):
                final = modes.type1(min, max, words, final, v, argv.depth, [c, total], not argv.noprog)
            elif (i == 2):
                final = modes.type2(words, final, v,[c, total], not argv.noprog)
            elif (i == 3):
                final = modes.type3(words, final, v, [c, total], not argv.noprog)
            elif (i == 4):
                final = modes.type4(words, final, v, [c, total], not argv.noprog)
            elif (i == 5):
                final = modes.type5(min, max, words, final, v, argv.depth, [c, total], not argv.noprog)
            c += len(words)

        final = set(final)
    
    if (argv.encode):
        if (v):
            print("Encoding wordlist...")
        final = utils.encode(final, argv.encode)
    
    bts = utils.output(argv.output, final, v)
    bts = utils.convert(bts)
    print(f"\nGenerated {len(final)} lines. ({bts})")

    stop = time.time()
    elapsed = stop-start

    return elapsed