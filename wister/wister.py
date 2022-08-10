import wister.control as control
import wister.utils as utils
from wister.version import __version__

def main():
    argv = utils.args(__version__)
    print(f"""
 __          _______  _____ _______ ______ _____  
 \ \        / /_   _|/ ____|__   __|  ____|  __ \ 
  \ \  /\  / /  | | | (___    | |  | |__  | |__) |
   \ \/  \/ /   | |  \___ \   | |  |  __| |  _  / 
    \  /\  /   _| |_ ____) |  | |  | |____| | \ \ 
     \/  \/   |_____|_____/   |_|  |______|_|  \_\\

        \x1B[3mVersion {__version__}                Cycurity\x1B[23m
    """)
    time_elapsed = 0
    try:
        time_elapsed = control.control(argv)
        print(f"\nFinished in {time_elapsed:.3f}s.\n")
    except KeyboardInterrupt:
        print("\nAborting...")

if __name__ == "__main__":
    main()