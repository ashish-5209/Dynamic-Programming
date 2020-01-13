def palindrom(s, i, j):
    if i == j:
        return 1
    if s[i] == s[j] and i+1 == j:
        return 2
    if s[i] == s[j]:
        return palindrom(s, i+1, j-1) + 2
    return max(palindrom(s, i, j-1), palindrom(s, i+1, j))

if __name__ == '__main__':
    s = "GEEKSFORGEEKS"
    n = len(s)
    print("The length of the LPS is",
                  palindrom(s, 0, n - 1))
