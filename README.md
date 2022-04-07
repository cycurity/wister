# WISTER

```
 __          _______  _____ _______ ______ _____  
 \ \        / /_   _|/ ____|__   __|  ____|  __ \ 
  \ \  /\  / /  | | | (___    | |  | |__  | |__) |
   \ \/  \/ /   | |  \___ \   | |  |  __| |  _  / 
    \  /\  /   _| |_ ____) |  | |  | |____| | \ \ 
     \/  \/   |_____|_____/   |_|  |______|_|  \_\

                                     Cycurity       
```

## SUMMARY

> A unique wordlist generator with several types of combinations to choose from, or to mix them all. Capable of receiving words from various sources and outputing them to different encoding types.

## USAGE

![](./static/img/running.gif "Usage")

```
usage: wister.py [-h] [-c [1-5] [[1-5] ...]] [-d [2-5]] [-e FORMAT] [-i FILE] [-l] [-m [0-49]] [-M [1,50]] [-o FILE] [-N] [-v] [-V] [-w WORDS [WORDS ...]]

options:
  -h, --help            show this help message and exit
  -c [1-5] [[1-5] ...], --combination [1-5] [[1-5] ...]
                        Select which types of combinations to use.
  -d [2-5], --depth [2-5]
                        Select the depth of word mixing when using combination mode 1. Default: 3
  -e FORMAT, --encode FORMAT
                        Encode/Hash the generated wordlist with a given algorithm
  -i FILE, --input FILE
                        Select the input file containing the words.
  -l, --list            List the types of combination.
  -m [0-49], --min [0-49]
                        Select minimum characters for output. Default: 0
  -M [1,50], --max [1,50]
                        Select maximum characters for output. Default: 20
  -o FILE, --output FILE
                        Specify the output file. Default: output.lst
  -N, --noprogress      Disables progress bar (increses performance)
  -v, --version         Returns the version of the program.
  -V, --verbose         Verbose the output.
  -w WORDS [WORDS ...], --words WORDS [WORDS ...]
                        Words to generate the output with.
```

## INSTALLATION

The process to install Wister is as simple as cloning the repository to your local machine:

```
$ sudo apt-get install python3 python3-pip git
$ git clone -q https://github.com/cycurity/wister.git
$ cd wister
```

## MANUAL

&nbsp;&nbsp;&nbsp;&nbsp;To run the program, you need to pass at least a set of words, using an input file (`-i` or `--input`), or passing the words manually using the `-w` or `--words` tag. If no more options are passed, the program will just write the specified words to the default output file `output.lst`.

&nbsp;&nbsp;&nbsp;&nbsp;There are 5 types of combinations that can be used (with `-c` or `--combination`) simultaneously : `1. Word Mix`; `2. Case Alternate`; `3. Homograph`; `4. Reverser`; `5. Saltify`. To get more information about each type of combination, you should use the *list* argument (`-l` or `--list`). When using the first combination (Word Mix), you can also select the depth (`-d` / `--depth`) which will define the number of words being mixed together. By default, this value is set to 3. 

&nbsp;&nbsp;&nbsp;&nbsp;Addicionally, you can define the maximum generated word length (`-M` or `--max`) or the minimum number of characters required (`-m` or `--min`). By default, the minimum value is set to 0 and the max to 20.

&nbsp;&nbsp;&nbsp;&nbsp;To specify the desired output file, you must use `-o` or `--output`, followed by the filename.

&nbsp;&nbsp;&nbsp;&nbsp;The verbose option (`-V` / `--verbose`) will allow you to follow the generation of the wordlist, by printing the several steps of the program. When this option is enabled, the progress bar is disabled.

&nbsp;&nbsp;&nbsp;&nbsp;Optionally, the generated wordlist can be encoded or hashed, using `-e` or `--encode`, with specific types of algorithms: `MD5`; `Base64`; `Hexadecimal`; `URL Encode`; `SHA1`; `SHA2-256`; `SHA2-512`; `SHA3-256`; `SHA3-512`.

&nbsp;&nbsp;&nbsp;&nbsp;By default, the progress bar is enabled when verbose mode is not. You can also choose to disable it by using the `-N` or `--noprogress` flag. Disabling this feature will increase performance and decrease the overall execution time of the program.

&nbsp;&nbsp;&nbsp;&nbsp;To print the current program version, use `-v` or `--version`.

&nbsp;&nbsp;&nbsp;&nbsp;To get the usage and help page, use the `-h` flag or `--help`.

## CREDITS

Development team:
- [fssecur3](https://github.com/fssecur3 "fssecur3's Github Profile")
- [intMa1n](https://github.com/Bernardo15Sousa "intMa1n's Github Profile")

## LICENSE

Copyright (C) 2022, Cycurity

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

The software is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

Check out the GNU General Public License: [http://www.gnu.org/licenses/](http://www.gnu.org/licenses/)
