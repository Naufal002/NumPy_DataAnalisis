import os
os.system('cls')

import numpy as np
from numpy2tfrecord import Numpy2TFRecordConverter

with Numpy2TFRecordConverter("test.tfrecord") as converter:
    x = np.arange(100).reshape(10, 10).astype(np.float32)  # float array
    y = np.arange(100).reshape(10, 10).astype(np.int64)  # int array
    a = 5  # int
    b = 0.3  # float
    sample = {"x": x, "y": y, "a": a, "b": b}
    converter.convert_sample(sample)  # convert data sample