from scipy.stats import vonmises
import matplotlib.pyplot as plt
import numpy as np
import csv

SAMPLE_SIZE = 1000

if __name__ == "__main__":
    for kappa in range(1, 6):
        vm_dist = vonmises.rvs(kappa, size=SAMPLE_SIZE)
        with open('vonmises_{}.csv'.format(kappa), mode="w") as vonmises_file:
            dist_writer = csv.writer(vonmises_file, delimiter=',')
            #print(vm_dist.tolist())
            dist_writer.writerow(vm_dist.tolist())
