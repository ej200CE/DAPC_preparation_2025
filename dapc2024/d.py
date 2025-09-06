def word_to_num(word):
    res = ""
    for ch in word:
        if ch in {"a", "b", "c"}:
            res += "2"
        elif ch in {"d", "e", "f"}:
            res += "3"
        elif ch in {"g", "h", "i"}:
            res += "4"
        elif ch in {"j", "k", "l"}:
            res += "5"
        elif ch in {"m", "n", "o"}:
            res += "6"
        elif ch in {"p", "q", "r", "s"}:
            res += "7"
        elif ch in {"t", "u", "v"}:
            res += "8"
        elif ch in {"w", "x", "y", "z"}:
            res += "9"
    return int(res)

def main():
    n, m = map(int, input().split())
    words = [input() for _ in range(n)]
    nums = [int(input()) for _ in range(m)]

    dict = {} # num -> list of words
    for num in nums:
        dict[num] = []

    for word in words:
        converted_word = word_to_num(word)
        if converted_word in dict:
            dict[converted_word].append(word)

    for num in nums:
        all_words = dict[num]
        print(len(all_words), " ".join(all_words))

if __name__ == "__main__":
    main()