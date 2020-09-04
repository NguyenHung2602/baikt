def so_nguyen_to():
    lst = []
    count2 = 0
    count = 0
    for i in range(10000,100000):
        for k in range(2,int(i/2)):
            if i%k ==0:
                count = 1
                break
        if count == 0:
            lst.append(i)
            count2+=1
        count = 0
    return count2       

def main():
    print(so_nguyen_to())

if __name__=="__main__":
    main()