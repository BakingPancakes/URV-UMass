import json
import os
from pathlib import Path

# Collect average PAE from each file, and pair that in a Dataframe with 
#     the time it took for Alphafold to predict that protein 
#     (the number of recycles, iterations, strategy, etc on the colab)

def getAverage() -> dict[str:float]:
    means = {}
    for file in os.listdir("PAE Tables for 3 recycles 200 iterations and 2 seeds/"):
        with open("PAE Tables for 3 recycles 200 iterations and 2 seeds/"+file) as f:
            data = json.load(f)['predicted_aligned_error']
            count = 0
            sum = 0
            for list in data:
                for item in list:
                    count += 1
                    sum += item
            mean = sum / count
            means[Path(file).stem] = round(mean,3)

    return means
means = getAverage()
for key in means.keys():
    print(str(key) + ":" + str(means[key]))