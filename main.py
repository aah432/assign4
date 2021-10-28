from random import randrange


def max2(x, y):                 # Find Max of 2 numbers
    z = x - y                   # Find difference between x and y
    i = (z >> 31) & 0x1         # If (x - y) is negative, then set i = 1; otherwise set i = 0.
    max = x - i * z
    return max


def fSelect(xs, i):
    if xs:
        for x in xs:
            if x == xs[i]:
                return x
    else:
        return "Error Empty list"


def iSelect(xs, k):
    if len(xs) == 1:
        return xs[0]
    else:
        xpart = partition(xs, randrange(len(xs)))
        x = xpart[0]  # partitioned array
        j = xpart[1]  # pivot index
        if j == k:
            return x[j]
        elif j > k:
            return iSelect(x[:j], k)
        else:
            k = k - j - 1
            return iSelect(x[(j + 1):], k)


def partition(x, pivot_index):
    i = 0
    if pivot_index != 0: x[0], x[pivot_index] = x[pivot_index], x[0]
    for j in range(len(x) - 1):
        if x[j + 1] < x[0]:
            x[j + 1], x[i + 1] = x[i + 1], x[j + 1]
            i += 1
    x[0], x[i] = x[i], x[0]
    return x, i


if __name__ == '__main__':
    xs = [2, 8, 3, 1, 4, 0, 7, 3, 11]
    #print(str(fSelect(xs, 2)))
    print(iSelect(xs, 3))        # supposed to return 1
    print(xs[iSelect(xs, 3)])
    #print(max(90, 9))

