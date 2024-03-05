

# writing to a text file can be done using print
def printToFile(t):
    '''write the text 't' into a persistent file'''
    fout = open('printlog.txt', 'a') # 'a' will append
    # print(t, file=fout, end=', ') # every time we use print the default is to add a new line
    print(t, file=fout) # every time we use print the default is to add a new line
    fout.close() # always good to close the file acces object

def writeTofile(t):
    '''use a file access object to commit text to a file'''
    try:    
        fout = open('my_log.txt', 'a')
        # fout.write(f'{t}\n') # may choose to append lew line character
        size   = len(t) # easy way to determine how many characters in the text
        offset = 0
        chunk  = 12 # choose how many characters to write at a time
        while True:
            if offset > size:
                fout.write('\n')
                break # this breaks out of the while loop
            else:
                part = t[offset: offset+chunk] # [start: stop-before]
                fout.write(part)
                offset += chunk
        fout.close() # close at the earliest opportunity
    except FileExistsError as fe:
        print(f'the file already exists {fe}')
    except Exception as err:
        print(err)


if __name__ == '__main__':
    printToFile('this is simple')
    writeTofile(''' Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
                Proin tincidunt aliquet nisl nec tristique. Quisque ac lobortis turpis. 
                Etiam dapibus rutrum augue sed congue. Duis in finibus augue. Cras vel 
                dapibus nulla. Vestibulum posuere odio eu tellus varius mattis. Integer 
                quis molestie eros. Donec molestie diam diam, vitae tincidunt erat 
                elementum blandit. Vivamus congue est vel ipsum commodo euismod. Etiam 
                odio tortor, ultricies ut tincidunt vel, ullamcorper vel urna.
                Ut id diam vitae risus elementum hendrerit. Curabitur at tincidunt ipsum. 
                Donec efficitur eros mollis nunc mattis, vel consectetur ipsum semper. 
                Donec consequat ex ligula, ac malesuada nunc pharetra et. 
                Fusce aliquam suscipit tempus. Sed luctus arcu id orci ornare gravida. 
                Sed in turpis non quam porttitor viverra ut non augue. Morbi eu ipsum 
                vitae mauris porttitor accumsan. Donec suscipit metus nunc, 
                in gravida mauris commodo vitae. Aenean at massa et risus consectetur 
                gravida. Etiam lobortis viverra dapibus. Fusce congue, erat sed interdum 
                efficitur, mi lacus laoreet libero, eu scelerisque nisl neque vitae sem. ''')