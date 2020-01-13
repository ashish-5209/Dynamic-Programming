def edit(str1, str2, m, n):

    if m == 0:
        return n
    if n == 0:
        return m

    if str1[m-1] != str2[n-1]:

        return 1 + min(edit(str1, str2, m-1, n),
                edit(str1, str2, m, n-1),
                edit(str1, str2, m-1, n-1))
    return edit(str1, str2, m-1, n-1)

str1 = "sunday"
str2 = "saturday"
print(edit(str1, str2, len(str1), len(str2)))
