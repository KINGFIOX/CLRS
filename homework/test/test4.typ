$sans(A B C)$

$frak(P)$

$mono(x + y = z)$

$bb(b)$

#set align(center)
Centered text, a sight to see \
In perfect balance, visually \
Not left nor right, it stands alone \
A work of art, a visual throne

你知道这是为什么吗？

#table(
    columns: (auto, auto, auto),
    inset: 10pt,
    align: horizon,
    [], [*Area*], [*Parameters*],
    image("1.png", height: 5%),  // 第一列
    $pi h (D^2 - d^2) / 4$,  // 第二列
    [
        $h$: height \
        $D$: outer radius \
        $d$: inner radius
    ],
    image("1.png", height: 5%),
    $sqrt(2) / 12 a^3$,
    [$a$: edge length]
)

#table(
    // odd(col)奇数列是灰色
    fill: (col, _) => if calc.odd(col) { luma(240) } else {white},
    align: (col, row) =>
        if row == 0 {center}  // 第0行是中间
        else if col == 0 {left}  // 第一列是靠左
        else {right},  // 第一列是靠右
    columns: 4,  // 设置为4列
    [], [*Q1*], [*Q2*], [*Q3*],
    [Revenue: ], [1000 $euro$], [2000 $euro$], [3000 $euro$],
    [Expenses: ], [500 $euro$], [1000 $euro$], [1500 $euro$],
    [Profit: ], [500 $euro$], [1000 $euro$], [1500 $euro$]
)

#set align(left)

#set page(columns: 2)
Preliminary findings from our ongoing research project have revealed a hitherto unknown phenomenon of extraordinary significance.

#colbreak()
Through rigorous experimentation and analysis, we have discovered a hitherto uncharacterized process that defies our current understanding of the fundamental laws of nature.

#box(
    height: 68pt,
    columns(2, gutter: 11pt)[
        #lorem(400)
    ]
)
