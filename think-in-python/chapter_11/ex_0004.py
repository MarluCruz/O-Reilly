def ack(m, n):
  known
  if m == 0:
    return n + 1
  if m > 0 and n == 0:
    if n in known:
        known[n] = n
        return n + 1
    return ack(m -1, 1)
  if m > 0 and n > 0:
    if m in known:
        return m + 2
    known[n] = n
    known[m] = m
    return ack(m-1, ack(m,n-1))
    

known = {0:0}
print(ack(3, 4))


