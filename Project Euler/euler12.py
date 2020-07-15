def main():
    t_no = 0
    i = 1
    while True:
        t_no += i

        factors = 2
        for f in range(2, t_no-1):
            if t_no % f == 0:
                factors+=1
        if factors > 500:
            print(f"{i}: {factors} Condition Satisfied ✔")
            break
        else:
            print(f"{i}: {factors} Condition NOT Satisfied ✘")
        i+=1

if __name__ == "__main__":
    main()