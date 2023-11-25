#set text(
    font: "Microsoft Sans Serif",
    size:10pt,
)

#set page(
    paper: "a4",
    margin: (x: 1.8cm, y: 1.5cm),
    header: align(right)[
      标题，右对齐
    ],
    numbering: "1",
)

这是一个好东西


#align(bottom + center)[
    内容竖直居中，并且水平对齐
    #image("./image/test_img.png", width: 70%)
    *加粗文字*
]

#lorem(15) 随机生成15个字符，用来占位

= 你知道这是为什么吗？

+ 数字序号1
  - 无序1
+ 数字序号2
  - 无序2

@glaciers 会显示图片的标号

当所有人都替你开心

我才傻傻清醒


原来早已有人为你定做了嫁衣

感谢你特别邀请

#par(justify: true)[
  = background
  justify是文本左右对齐

  长亭外，古道边，芳草碧连天
]

$vec(x_1, x_2, x_3)$

@glaciers

@glaciers

$7.32 beta + sum_(i=0)^nabla Q_i / 2$

$epsilon$

$v := vec(x_1, x_2, x_3)$

$a arrow.squiggly b$

你是不是一个大傻逼

$Q = rho A v + c "time offset"$

#figure(
  image("./image/test_img.png", width: 70%),
  caption: [
    _Glaciers_ from an important part
  ],
) <glaciers>