"""
"Contestant who earns a score equal to or greater than the k-th place finisher's score will advance to the next round, as long as the contestant earns a positive score..." — an excerpt from contest rules.

A total of n participants took part in the contest (n ≥ k), and you already know their scores. Calculate how many participants will advance to the next round.

Input
The first line of the input contains two integers n and k (1 ≤ k ≤ n ≤ 50) separated by a single space.

The second line contains n space-separated integers a1, a2, ..., an (0 ≤ ai ≤ 100), where ai is the score earned by the participant who got the i-th place. The given sequence is non-increasing (that is, for all i from 1 to n - 1 the following condition is fulfilled: ai ≥ ai + 1).

Output
Output the number of participants who advance to the next round.
"""


def main():
    n, k = input().split(" ")
    n, k = int(n), int(k)
    scores = input().split(" ")
    for idx, score in enumerate(scores):
        scores[idx] = int(score)

    count = 0
    for idx, score in enumerate(scores):
        if score > 0 and score >= scores[k-1]:
            count += 1
    print(count)


if __name__ == "__main__":
    main()