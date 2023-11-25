$lim_(n->infinity)frac(sum_(i=1)^n i^2, n^3)$
$=lim_(n->infinity)frac(sum_(i=1)^n i^2 - sum_(i=1)^(n-1) i^2, n^3 - (n-1)^3)$
$=lim_(n->infinity)frac(n^2, n^3 - (n^3 - 3n^2 + 3n - 1))$
$=lim_(n->infinity)frac(n^3, 3n^2 - 3n + 1)=1/3$

故$f(n)=sum_(i=1)^(n)$是$Theta(n)$