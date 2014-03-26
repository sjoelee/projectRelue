def main(num):
    total = 0
    for val in xrange(1,num):
        if val % 3 == 0 or val % 5 == 0:
            total += val
    print total
        
if __name__=="__main__":
    main(1000)
