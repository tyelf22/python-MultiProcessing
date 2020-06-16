import requests as rq 
import time

start = time.perf_counter()

with open('flags.txt') as f:
    allFlags = [line.strip() for line in f]

byteSize = 0
def flagFunc():
    for flag in allFlags:
        r = rq.get(f'https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/{flag}-lgflag.gif')
        with open(f'./flags/{flag}.png', 'wb') as f:
            f.write(r.content)
        global byteSize
        byteSize += len(r.content)

flagFunc()

finish = time.perf_counter()

with open("cia_a_results.pdf", 'a') as f: #open text file for appending
            print(f'Elapsed Time: {round(finish-start, 2)} \n{byteSize} bytes downloaded', file=f) #print to text file












