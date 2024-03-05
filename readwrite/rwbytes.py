# we can read and write bytes
def makeBytes(values):
    '''make a byte string from values'''
    b = bytes(values)
    return b

def writeBytes(b):
    '''commit bytes to a persistent file'''
    try:
        fout = open('my_bytes', 'rb') # 'w' write 'b' bytes
        fout.write(b)
    except Exception as err:
        print(err)
    finally:
        try:
            fout.close() # always close - butr be careful, fout might not exist here
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

def decodeBytes(my_b):
    # decoded_string = byte_string.decode(encoding)
    txt = my_b.decode() # there is also an encode()
    return txt

if __name__ == '__main__':
    v = range(0,256)
    my_b = makeBytes(v) # convert the first 256 text characters into bytes
    writeBytes(my_b) # commit our data to a persistent byte file
    z = readBytes()
    print(z) # this is still bytes
    # can we decode the bytes
    t = decodeBytes(my_b[0:60])
    print(type(t), t)