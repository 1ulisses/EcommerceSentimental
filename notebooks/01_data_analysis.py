# %%
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

for dirname, _, filenames in os.walk("../data"):
    for filename in filenames:
        print(os.path.join(dirname, filename))
