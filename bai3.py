def string():
    s = input()
    count_chu = 0
    count_so = 0
    for c in s:
        if c.isupper()==True or c.islower()==True:
            count_chu += 1
        elif c.isdigit()==True:
            count_so += 1
    print("Số chữ cái là:",count_chu)
    print("Số chữ số là:",count_so)

def main():
    string()

if __name__ == "__main__":
    main()            
