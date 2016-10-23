def memoize(f):
  memo = {}
  print "ist memo:",memo
  def helper(x):
    print "x is:",x
    if x not in memo:
      memo[x] = f(x)
      print "id of memo f:",id(f)
    print "Memo: ",memo
    return memo[x]
  return helper

def kib(n):
  print "Old state"
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    print "N is:",n
    return kib(n-1) + kib(n-2)

print "id of old kib:",id(kib)
kib = memoize(kib)
print "id of new kib:",id(kib)
print kib(4)
print "id of memoize:",id(memoize)