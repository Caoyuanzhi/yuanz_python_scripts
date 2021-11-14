import re
import time
import sys
import argparse
import os, os.path




parser = argparse.ArgumentParser(description="input to this script")
parser.add_argument('--dir',type=str,default=None)
parser.add_argument('--date',type=str,default=time.strftime("%m-%d_%H:%M",time.localtime()))

args = parser.parse_args()
#print(args.dir)
#print(args.date)

print(os.getcwd())

match_pattern='log'

def search_dir(dir_path):
    print(dir_path)
    for filename in os.listdir(dir_path):
        match_file = re.match('.*'+match_pattern+'.*',filename)
        if(match_file):
            print(filename)
            with open(dir_path+'/'+filename,'r') as curr_file:
                for line in curr_file:
                    match_str = re.match('IPC'+'\s*(\d+)',line)
                    if(match_str):
                        IPC = match_str.group(1)
                        print(IPC)

search_dir(os.getcwd() + '/' + args.dir)    

