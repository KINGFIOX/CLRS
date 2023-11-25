$"dp[i][j]" = cases(min_{i <= r <= j}("dp[i][r-1] + dp[r+1][j]") + w(i,j) "if j - i = 1", q_(i-1) "if j - i = 1")$

其中$w(i,j)=sum_(k=i)^j p_k + sum_(k=i-1)^j q_k$