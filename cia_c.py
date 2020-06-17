''' Tyson Elfors
6/15/20
CS-1410
Project 7 - Concurrent Programming
'''

"""I declare that the following source code was written solely by me.
I understand that copying any source code, in whole or in part, constitues cheating,
and that I will receive a zero on this project if I am found in violation of this policy."""

import requests as rq #requests module
import time #time module
import concurrent.futures #multi-processing module

start = time.perf_counter() #start time

with open('flags.txt') as f: #open flags file 
    allFlags = [line.strip() for line in f] #read each line of flags file and add to list

byteSize = 0 #initialize byte size

def flagFunc(flag):
    '''Download country flag images using requests module'''
    r = rq.get(f'https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/{flag}-lgflag.gif') #get url based on flag
    with open(f'{flag}.png', 'wb') as f:  #put flag image in flags folder
        f.write(r.content) #write bytes to file
    global byteSize
    byteSize += len(r.content) #add to byteSize variable

with concurrent.futures.ThreadPoolExecutor() as executor: #use multi-threading
    executor.map(flagFunc, allFlags) #use multi-threading to map through flagFunc


finish = time.perf_counter() #end time

with open("cia_c_results.pdf", 'a') as f: #open text file for appending
            print(f'Elapsed Time: {round(finish-start, 2)} \n{byteSize} bytes downloaded', file=f) #print to text file
