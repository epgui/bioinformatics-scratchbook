# http://www.cs.jhu.edu/~langmea/resources/lecture_notes/

def naive(p, t):
  occurences = []
  for i in xrange(len(t) - len(p) + 1):
    match = True
    for j in xrange(len(p)):
      if t[i+j] != p[j]:
        match = False
        break
      if match:
        occurences.append(i)
  return occurences
