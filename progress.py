import os
import sys
import time

class Bar():
    def __init__(self, bar_len=50, title='Please wait'):
        self.startTime = time.time()
        self.bar_len = bar_len
        self.title = title

    def print_percent_done(self, index, total):
        '''
        index is expected to be 0 based index. 
        0 <= index < total
        '''
        percent_done = (index+1)/total*100
        percent_done = round(percent_done, 1)

        done = round(percent_done/(100/self.bar_len))
        togo = self.bar_len-done

        done_str = '█'*int(done)
        togo_str = '░'*int(togo)

        print(f'{self.title}: [{done_str}{togo_str}] {percent_done}%', end='\r')

        if percent_done > 99.9:
            clearConsole()
            print(f"Work has done in {time.time() - self.startTime} seconds\a")

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)