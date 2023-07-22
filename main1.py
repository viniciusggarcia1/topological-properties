import numpy as np
import qsh
from tqdm import tqdm
import time

print("========================TOPOLOGICAL PROPERTIES========================")

with tqdm(total=150) as prog:
    for i in range(10):
        time.sleep(1)
        prog.update(10)

    for i in range(5):
        time.sleep(1)
        prog.update(20)