def func(s):
    s = s.split(" ")
    left = 0
    right = len(s) - 1
    while left <= right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    res = " ".join(s)
    return res

def func1(s):
    words = s.split()
    res = []
    for word in words:
        res.insert(0, word)
    final_s = " ".join(res)
    return final_s



print(func("Welc0e to my world"))


print(func1("Welc0e to my world"))

