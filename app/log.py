import csv
import os

# log save 
def log_saving(chk, **kwargs):
    header = []
    data = []
    
    for k,v in kwargs.items():
        header.append(k)
        data.append(v)
        
    path = './error.csv' if chk == 'error' else './save.csv'

    if not os.path.isfile(path):
        with open(path, 'w', newline='') as f:
            write = csv.writer(f)
            write.writerow(header)
            write.writerow(data)
    else:
        with open(path, 'a', newline='') as f:
            write = csv.writer(f)
            write.writerow(data)