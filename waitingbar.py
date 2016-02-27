#!/usr/bin/env python3

import sys
import threading
import time

from itertools import cycle


class WaitingBar(object):
    '''
    This class prints a fancy waiting bar with Greek chars and spins.
    It uses a thread to keep printing the bar while the main program runs

    Usage:

    THE_BAR = WaitingBar('Your Message Here')
    # Do something slow here
    (...)
    THE_BAR.stop()
    
    copyright phoemur - 2016
    '''

    def __init__(self, message='[*] Wait until loading is complete...'):
        self.MESSAGE = ' ' + str(message)
        self.CYCLES = ['-', '-', '\\', '\\', '|', '|', '/', '/', '-', '-', '\\', '\\', '|', '|', '/', '/']
        self.intab = u'abcdefghijklmnopqrstuvwxyzáàãâéèẽêíìîĩóòôõúùũûçABCDEFGHIJKLMNOPQRSTUVWXYZÁÀÃÂÉÈẼÊÍÌÎĨÓÒÔÕÚÙŨÛÇ'
        self.outab = u'αβ¢ΔεϝγηιφκλμνΩπσϼΣτυϞωχψζααααεεεειιιιΩΩΩΩυυυυ¢αβ¢ΔεϝγηιφκλμνΩπσϼΣτυϞωχψζααααεεεειιιιΩΩΩΩυυυυ¢'
        self.TABLE = {x: y for x, y in zip(self.intab, self.outab)}

        self.event = threading.Event()
        self.waiting_bar = threading.Thread(target=self.start, args=(self.event,))
        self.waiting_bar.start()

    def start(self, e):
        for index in cycle(range(len(self.MESSAGE))):
            if e.is_set():
                break
            if not self.MESSAGE[index].isalpha():
                continue
            for c in self.CYCLES:
                buff = list(self.MESSAGE)
                buff.append(c)

                try:
                    if sys.stdout.encoding.upper() == 'UTF-8':
                        buff[index] = self.TABLE[buff[index]]
                    else:
                        buff[index] = buff[index].swapcase()
                except KeyError:
                    pass

                sys.stdout.write(''.join(buff))
                time.sleep(0.05)
                sys.stdout.write('\r')
                sys.stdout.flush()

    def stop(self):
        self.event.set()
        self.waiting_bar.join()
        sys.stdout.write(self.MESSAGE + ' \n')


if __name__ == '__main__':
    '''
    A simple example to demonstrate the class in action
    '''

    # Start the bar
    THE_BAR = WaitingBar('[*] Calculating useless stuff...')

    # Do something slow
    import math
    from pprint import pprint

    a_list = {a: b for a, b in zip(range(1, 41), map(math.factorial, range(1, 41)))}
    time.sleep(20)

    # Stop the bar and print result
    THE_BAR.stop()
    pprint(a_list)
