from scipy.stats import vonmises
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
from math import pi

SAMPLE_SIZE = 1000
NUM_BUCKETS = 36

def gen_bucketed_vonmesis():
    bucketed_data = np.zeros([SAMPLE_SIZE, NUM_BUCKETS+1])
    for kappa in range(1, 6):
        for i in range(1000):
            vm_dist = vonmises.rvs(kappa, size=SAMPLE_SIZE)
            positives = [x+pi for x in vm_dist]
            bucket_number = [int((x * 180 / pi) // 10) for x in positives]
            for num in bucket_number:
                bucketed_data[i][num] += 1
            # label the data
            bucketed_data[i][NUM_BUCKETS] = -2-kappa
        np.savetxt('vonmesis_{}.csv'.format(kappa), bucketed_data, delimiter=",")

# Pass in path of file to be read to output
# Assuming file was saved with np.savetxt.
# Also assuming data was saved in format a[sample_num][bucket_num]
def visualise_von_mesis(fname):
    array = pd.read_csv(fname)
    bucketed_data = array.values
    # output the first set of buckets.
    bucket_num = [x for x in range(NUM_BUCKETS)]
    freq = bucketed_data[0][:-1]
    plt.plot(bucket_num, freq)
    plt.ylim(bottom=0)
    plt.show()

if __name__ == "__main__":
    visualise_von_mesis("vonmesis_1.csv")
    visualise_von_mesis("vonmesis_5.csv")
    visualise_von_mesis("uniformtest1.csv")
