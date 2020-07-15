import sys
def main(file) :
    lines = file.readlines()
    flt=[]
    for idx, line in enumerate(lines):
        flt.append(float(line.strip()))
    print(sum(flt))

if __name__ == "__main__":
    file = open(r"./t2.txt", "r")
    main(file)
    file.close()