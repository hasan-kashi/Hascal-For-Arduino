# Hascal Arduino Compiler

from os import execv
from os import system
from sys import argv
import sys
from hascal.h_parser import Parser
from hascal.h_lexer import Lexer

# Main 
if __name__ == '__main__':
    arduino_path = ""
    path_file = open('path.dat','r')
    
    lexer = Lexer()
    parser = Parser()
    version = "1.2.4"
    if len(argv) == 1 :
        print("Hascal : No such file or directory")
        print("usage : hascal <inputfile.has>")
    elif argv[1] == "help" :
        print("Hascal Compiler v1.2\nCopyright (c) 2019-2020 Hascal Development Team.\nAll rights reserved.\n")
        print("Enter following command in terminal to build a hascal file :\nhascal <filename>")
    elif argv[1] == "version":
        print(f"Hascal version : hascal v1.2.4 {sys.platform}")
    else :       
        try:
            with open(argv[1], "r") as fin:           
                parser.parse(lexer.tokenize(fin.read()))
                
            with open("tmp.ino","w") as fout:
                fout.write(parser.src_top +parser.src_main)
            output_file = argv[1]
            output_file_name =  ""
            #if sys.platform.startswith('linux'):
            #    output_file_name = output_file[:-3]
            #    system(f"tcc tmp.c -o {output_file_name}")
            #elif sys.platform.startswith('win32'):
            #    output_file_name = output_file[:-3] + "exe"
            #    system(f"tcc tmp.c -o {output_file_name}")
        except FileNotFoundError :
            print("Hascal : File not found ")

            
        
