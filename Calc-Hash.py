#напишите программу на Python, которая будет вычислять хэш-значения.

import hashlib

obj = hashlib.sha256(b'hi, what is you name?')

hex_d = obj.hexdigest()

print(hex_d)
