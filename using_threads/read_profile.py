import pstats
def main():
    '''access and reveal the cProfile report'''
    p = pstats.Stats('prof_out')
    p.print_stats()

if __name__ == '__main__':
    main()