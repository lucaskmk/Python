def eh_fibonacci(m):
    final = 0
    if len(m) < 3:
        return False
    for i in range(2, len(m)):     
        if m[i] == m[i-1] + m[i-2]:
            final += 1
        else:
            return False
    if final == len(m) - 2:
            return True