def Fibonacci():
    n = int(input())
    if n<2:
        print("Nhập lại n lớn hơn 2")
        n = int(input())
    lst = []
    for i in range(n):
        if i == 0:
            lst.append(i)
        elif i == 1:
            lst.append(i)
        else:
            lst.append(lst[i-1]+lst[i-2])      
    return lst
def main():
    print(Fibonacci())

if __name__=="__main__":
    main()    