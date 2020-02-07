from scipy.stats import vonmises
import matplotlib.pyplot as plt
import numpy as np
import csv
from math import pi

SAMPLE_SIZE = 1000

if __name__ == "__main__":
    bucketed_data = np.zeros([SAMPLE_SIZE, 37])
    for kappa in range(1, 6):
        for i in range(1000):
            vm_dist = vonmises.rvs(kappa, size=SAMPLE_SIZE)
            positives = [x+pi for x in vm_dist]
            bucket_number = [int((x * 180 / pi) // 10) for x in positives]
            for num in bucket_number:
                bucketed_data[i][num] += 1
            # label the data
            bucketed_data[i][36] = -2-kappa
        np.savetxt('vonmesis_{}.csv'.format(kappa), bucketed_data, delimiter=",")
