import os, sys
def decode(fn):
    with open(fn, "rb") as f:
        data = f.read()
    i = 0
    while i < len(data):
        if data[i] == 0xAA:
            if data[i+2] == 1 and i + 6 < len(data):
                print(f"\n{data[i+3]}-{data[i+4]}{data[i+5]}{data[i+6]}:",end='')
                i+=7
            elif data[i+2] == 2 and i + 5 < len(data):
                print(f"{data[i+3]}-{int.from_bytes(data[i+4:i+6],byteorder='little',signed=True)},",end='')
                i+=6
        i+=1

files = [f for f in os.listdir(sys.argv[1]) if os.path.isfile(os.path.join(sys.argv[1], f))]
files.sort()
for file in files:
    decode(f"{sys.argv[1]}/{file}")
