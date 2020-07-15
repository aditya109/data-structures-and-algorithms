def main(fp):
    s = 1000
    flag = False
    for a in range(1, s//3):
        for b in range(1, s//2):
            c = s - a - b
            if (a*a)+(b*b) == (c*c):
                print(f"{a}+{b}+{c} == {a+b+c} Condition Satisfied ✔")
                fp.writelines(f"{a}+{b}+{c} == {a+b+c} Condition Satisfied\n")
                flag = True
                break
            else:
                print(f"{a}+{b}+{c} == {a+b+c} Condition NOT Satisfied ✘")
                fp.writelines(f"{a}+{b}+{c} == {a+b+c} Condition NOT Satisfied\n")
        if flag :
            break

if __name__ == "__main__":
    fp = open("t2.txt", "w+")
    main(fp)
    fp.close()    