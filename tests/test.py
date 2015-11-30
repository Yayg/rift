import os
for _, dirs, _ in os.walk('.'):
    for directory in dirs:
        os.system('make -C ' + directory + ' all tests')
