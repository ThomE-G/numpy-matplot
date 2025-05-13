rows = int(input("number of rows:"))
columns = int(input("number of chairs per row:"))

import numpy as np
from numpy import random
seating = []
names = ["Nick", "Ina", "Mimi", "Jim", "Edie", "Len", "Frank", "Gigi", "Dan", "Cindy-Lou-Who", "Olivia", "Kim", "Thomas"]
np.random.shuffle(names)

for i in range(rows * columns):
        seating.append(names[i])

print(seating.reshape(row, column))
