# we can read and write bytes
def makeBytes(values):
    '''make a byte string from values'''
    b = bytes(values)
    return b

def writeBytes(b):
    '''commit bytes to a persistent file'''
    try:
        fout = open('my_bytes', 'wb') # 'w' write 'b' bytes
        fout.write(b)
        fout.close()
    except Exception as err:
        print(err)

def readBytes():
    '''retreive bytes from a file'''
    try:
        fin = open('my_bytes', 'rb')
        retrieved_b = fin.read()
        fin.close()
        return retrieved_b
    except Exception as err:
        print(err)

if __name__ == '__main__':
    v = range(0,256)
    b = makeBytes(v) # convert the first 256 text characters into bytes
    writeBytes(b) # commit our data to a persistent byte file
    z = readBytes
    print(b) # this is still bytes