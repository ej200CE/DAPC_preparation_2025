from math import ceil


def time(pixels, fps):
    return ceil(pixels * fps / 1000) / fps

def total_time(levels, fps):
    res = 0
    for l in levels:
        res += time(l, fps)
    return res


if __name__ == "__main__":

    n, fps = map(int, input().split())
    levels = list(map(int, input().split()))

    print("Original time: ", total_time(levels, fps))

    for i in range(1, fps):
        print("Time with fps = ", i, "| ", total_time(levels, i))

