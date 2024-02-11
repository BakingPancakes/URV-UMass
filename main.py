import json
import os
from pathlib import Path

# Collect average PAE from each file, and pair that in a Dataframe with 
#     the time it took for Alphafold to predict that protein 
#     (the number of recycles, iterations, strategy, etc on the colab)

def getAverage() -> dict[str:float]:
    means = {}
    for file in os.listdir("PAE_files"):
        with open("PAE_files/"+file) as f:
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

print(getAverage())