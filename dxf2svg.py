# Minh Nguyen 2022

import os
import subprocess
import sys
from keyboard import press
import time
from threading import Thread


def press_enter():
    time.sleep(5)
    press('enter')


def convert_dir(indir, outdir):
    for filename in os.listdir(indir):
        infile = os.path.join(indir, filename)
        outfile = os.path.join(outdir, os.path.splitext(filename)[0] + ".svg")
        command = ["inkscape", "--export-filename={}".format(outfile), "-l", ".\{}".format(infile)]
        t1 = Thread(target=press_enter)
        t2 = Thread(target=lambda: subprocess.run(command, shell=True))
        t1.start()
        t2.start()
        t1.join()
        t2.join()


convert_dir(sys.argv[1], sys.argv[2])
