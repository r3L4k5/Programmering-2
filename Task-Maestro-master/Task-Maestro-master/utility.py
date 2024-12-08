
import os

split_seg = lambda lines: print("-" * 136, "\n" * lines)  #Seperates segments in terminal, dynamic length and line breaks

clear_screen = lambda: (os.system("cls"), print("\n")) #Clears the terminal and adds an empty line

bold = lambda bold_txt: f"\033[1m{bold_txt}\033[0m" #Turns input text bold



