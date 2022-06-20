# demo of apply function
import time
import pandas as pd
import numpy as np

# initializing the dataframe
df = pd.DataFrame(np.random.randint(0, 11, size=(1000000, 5)), columns=('a', 'b', 'c', 'd', 'e'))

# printing the dataframe
print(df)


# defining the function to calculate the new column
def func(a, b, c, d, e):
    if e == 10:
        return c * d
    elif (e < 10) and (e >= 5):
        return c + d
    elif e < 5:
        return a + b


# print the start time
start_time = time.time()
print('The start_time is: ' + str(start_time))

#  use of apply function to create the new column 'f'
df['f'] = df.apply(lambda x: func(x['a'], x['b'], x['c'], x['d'], x['e']), axis=1)

# print the end time
end_time = time.time()
print('The end_time is: ' + str(end_time))
print('Time take is: ' + str(end_time - start_time))

# def func1(r):
#     print(r)
# df.apply(lambda x: func1(x), axis=1)

# print the new dataframe
print(df)
