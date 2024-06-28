#coding=utf-8
import os, sys, platform
try:
    if sys.argv[1]=='update':
        os.system('rm -rf lava.so')
except:
    pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('lava.so'):
        os.system('curl -L https://github.com/ALEXANDERKIEINURLUV/lava/blob/main/lava.cpython-311.so?raw=true -o lava.so')
        from tyrontest import main_menu
        main_menu()
    else:
        from tyrontest import main_menu
        main_menu()
else:
    print ('Your device is not supported ')
    exit()
