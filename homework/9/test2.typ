if $w in "pattern"[0..m-2]$ then

  shift[w] = len(pattern) - 1 - max {i < len(pattern) - 1 | pattern[i] = w }

else

  shift[w] = len(pattern)

