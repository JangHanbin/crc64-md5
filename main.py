import hashlib
import fastcrc
import time

start = time.time()

for i in range(0, 1000000):
    fastcrc.crc64.ecma_182('Hello May {0}'.format(i).encode('utf8'))
print("time :", time.time() - start)

start = time.time()
for i in range(0, 1000000):
    hashlib.md5('Hello May {0}'.format(i).encode('utf8')).hexdigest()
print("time :", time.time() - start)