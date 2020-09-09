from multiprocessing import Process
import os

num_processes = os.cpu_count()
print(f'you have {num_processes} cpu\'s')
