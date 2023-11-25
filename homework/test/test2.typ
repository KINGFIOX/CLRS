#set page(paper: "a4", header: align(right)[
  原来我们之间已没有任何关系
], numbering: "1")
#set text(
  font: ("Linux Libertine", "Microsoft YaHei"),
  size: 11pt,
)
#align(center, text(17pt)[
  *那是我日夜思念深深爱的人那*
])

#set par(justify: true, first-line-indent: 2em)
两端对齐，段的开始的时候空两个字符 11pt是11个像素的意思
#lorem(600)

#align(center, text(17pt)[
  *感谢你特别邀请，观赏你要的爱情*
])

#grid(columns: (1fr, 1fr),
    align(center)[
        王靳 \
        吴语诗 \
        #link("mailto:wangfiox@gmail.com")
    ],
    align(center)[
        王之原 \
        程思远 \
        #link("mailto:wys2004@gmail.com")
    ]
)

#align(center)[
    #set par(justify: false)
    *摘要* \
    #lorem(80)
]

设置变量
#let title = [
    晚风吹起你鬓间的白发
]

新开一页，设置头
#set page(
    header: align(
        right + horizon,
        title
    ),
)

#align(center, text(17pt)[
    *#title*
])

#show: rest => columns(2, rest)
= 介绍
#lorem(300)

= 相关的工作
#lorem(300)

#show heading: it => [
    #set align(center)
    #set text(12pt, weight: "regular")
    #block(smallcap(it.body))  转化为小型大写
]

一级标题就是放到了一个block中

#show heading.where(
    level : 2
): it => text(
    size: 11pt,
    weight: "regular",
    style: "italic",
    it.body + [.],
)

二级标题几乎与正文放在差不多的位置


