# Amber Harding
# CSCI 261 Assignment 4
from random import randrange


def max2(x, y):                 # Find Max of 2 numbers
    z = x - y                   # Find difference between x and y
    i = (z >> 31) & 0x1         # If (x - y) is negative, then set i = 1; otherwise set i = 0.
    max = x - i * z
    return max


def fSelect(xs, index):
    for i in range(len(xs) - 1):
        minIndx = i
        minVal = xs[i]
        j = i+1
        while j < len(xs):
            if minVal > xs[j]:
                minIndx = j
                minVal = xs[j]
            j += 1
        if minIndx != i:
            temp = xs[i]
            xs[i] = xs[minIndx]
            xs[minIndx] = temp
    print(xs)
    return xs[index]


def iSelect(xs, index):
    l = 0
    h = len(xs) - 1
    return iSelectHelper(xs, index, l, h)


def iSelectHelper(xs, index, l, r):
    # If the list contains only one element, return that element
    if l == r:
        return xs[l]

    # select `pIndex` between left and right
    pIndex = randrange(l, r)

    pIndex = partition(xs, index, l, r)

    # The pivot is in its sorted position
    if index == pIndex:
        return xs[index]

    # if `index` is less than the pivot index
    elif index < pIndex:
        return iSelectHelper(xs, index, l, pIndex - 1)

    # if `index` is more than the pivot index
    else:
        return iSelectHelper(xs, index, pIndex + 1, r)


def swap(xs, i, j):
    temp = xs[i]
    xs[i] = xs[j]
    xs[j] = temp


def partition(xs, index, l, r):
    # Pick `pIndex` as a pivot from the list
    pivot = xs[index]

    # Move pivot to end
    swap(xs, index, r)

    # elements less than the pivot will be pushed to the left of `pIndex`;
    # elements more than the pivot will be pushed to the right of `pIndex`;
    # equal elements can go either way
    pIndex = l

    # each time we find an element less than or equal to the pivot, `pIndex`
    # is incremented, and that element would be placed before the pivot.
    for i in range(l, r):
        if xs[i] <= pivot:
            swap(xs, i, pIndex)
            pIndex = pIndex + 1

    # Move pivot to its place
    swap(xs, pIndex, r)

    # return `pIndex` (index of the pivot element)
    return pIndex


if __name__ == '__main__':
    xs = [1, 0, 5, 6, 3, 7, 2, 1, 8]
    print(fSelect(xs, 7))
    print(iSelect(xs, 2))
