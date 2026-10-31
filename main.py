import numpy as np

values = np.array([-10, 50, 65, 80, 95, 110])

selected = values[(values >= 60) & (values <= 90)]
print(selected)

values[values < 0] = 0
print(values)

result = np.where(values >= 60, "합격", "불합격")
print(result)
