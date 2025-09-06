alphabet = "abcdefghijklm"

def convert(x, base):
    ans = []
    rest = x
    while rest >= 1:
        rst = rest % base
        if rst >= 10:
            ans.append(alphabet[rst-10])
        else:
            ans.append(rest % base)
        rest = rest // base
    return ''.join(map(str, reversed(ans)))

def check(n):
    for b in range(16, 1, -1):
        if n % b ** 2 == 0:
            converted = convert(n, b)
            print(b, converted)
            return
    print("impossible")


string = input().split()
n = int(string[0])
check(n)


