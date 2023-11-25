// figure自定义函数，caption的默认参数，numbering的默认参数，body
#let subfigure(body, caption: "", numbering: "(a)") = {
  let figurecount = counter(figure) // 图片计数
  let subfigurecount = counter("subfigure") // 子图计数
  let subfigurecounterdisplay = counter("subfigurecounter") // 显示子图计数，展示过子图计数的统计
  let number = locate(
    loc => { // loc表示位置的对象，
      let fc = figurecount.at(loc)
      let sc = subfigurecount.at(loc)
      if fc == sc.slice(0, -1) {
        subfigurecount.update(fc + (sc.last() + 1,))
        subfigurecounterdisplay.update((sc.last() + 1,))
      } else {
        subfigurecount.update(fc + (1,))
        subfigurecounterdisplay.update((1,))
      }
      subfigurecounterdisplay.display(numbering)
    },
  )
  body // 放文章主体
  v(-.65em)
  if not caption == none {
    align(center)[#number #caption] // 显示标题
  }
}

#figure( // 先设置了一排
  grid(
    columns: 3,
    gutter: 2em,
    subfigure(image("1.png", width: 50%)),
    subfigure(image("1.png", width: 50%)),
    subfigure(
      image("1.png", width: 50%),
      caption: "Test Caption",
    ), // 第三张图片标题
  ),
  caption: "Test caption", // 这三张图片的大标题
)
#v(2em)
#figure(
  grid(
    columns: (1fr, 1fr, 1fr), // 1fr，1fr，1fr这里总数是3fr，然后每份都是1/3
    rows: (auto, auto),
    gutter: 1pt, // 单元格之间的间距
    image("1.png", width: 50%),
    image("1.png", width: 50%),
    image("1.png", width: 50%),
    image("1.png", width: 50%),
    image("1.png", width: 50%),
    image("2.png", width: 50%),
  ),
  numbering: "1", // 从1开始计数
  caption: [
    SubFigures.// 标题
  ],
)

#[
  #show heading: set text(navy)
  // 这个navy是一个rgb的别名
  === This is navy-blue
  but this stays black
]

#[
  #set heading(numbering: "(I)", outlined: false) // 设置标题格式
  #show heading: it => block[
    // it是传入的参数
    #set align(center)
    #set text(font: "Inria Serif")
    \~ #emph(it.body)
    #counter(heading).display()~\
    // 这个\~~\是强调块的意思
  ]
  = Dragon
  with a base health of 15, the dragon is the most
  powerful creature. = Manticore
  while less powerful than the dragon, the manticore
  gets extra style points.
]

#[
  we started project in 2019 and are still working
  on it. Project is progressing badly. #parbreak() // 段落分隔
  #show "Project": smallcaps // 将project设置为 小的大写
  #show "badly": "great" // 将badly替换为great
  we started project in 2019 and are still working
  on it. Project is progressing badly.
]

#emph[hello] \
#emoji.face \
#"hello".len()

#{
  let a = [from]
  let b = [*world*]
  [hello]
  a + [ the ] + b
}

#let n = 2
#while n < 10 {
  n = (n * 2) - 1
  (n,)
}

#emoji.face

#rotate(10deg)[stick your finger in my ass]

#set align(center)
#scale(x: 150%)[
  Scaled apart
]

#let x = [lover fucker]

#sym.arrow.r

$gt.eq.not$

#emoji.face.halo

#"fuck you" // 这个是字符串

#set align(left)

"\#set"和"\#let"的区别:

"\#set"是设置的全局变量

而"\#let"是设置的局部变量

#list[A][B]

#enum(start: 2)[A][B]

#let alert(body, fill: red) = {
  set text(white)
  set align(center)
  rect(
    fill: fill,
    inset: 8pt,
    radius: 4pt,
    [*FBI WARNING: \ #body*],
  )
}

#alert[
  time to kick ass
]

#alert(
  fill: blue,
)[
    i hear of you are the best mom in the world
  ]

#show "once?": it => [#it, #it]
once?

#let format(title, ..authors) = [
  *#title* \
  _Written by #(authors
  .pos()
  .join(", ", last: " and "));._
]

#format("ArtosFlow", "Jane", "Joe")

#set text(fill: olive)
#overline(
  stroke: green.darken(20%),
  offset: -12pt,
)[
    你知道这是为什么吗？
  ]

#overline(offset: -1.2em)[
  The Tale Of A Faraway Line II \
  这是一个好东西
]

Take #underline(
  stroke: 1.5pt + red, // 粗的下滑红线
  offset: 2pt,
  [care],
)

`感觉这个不错#`

#set text(fill: black) // 设置为黑色
下面是代码块

#show raw.where(lang: "mydsl") : it => {
  let sum = 0
  for part in it.text.split("+"){
    sum += int(part.trim())
  }
  sum
}

// 可以自动计算的
```mydsl
1 + 2 + 3 + 4 + 5
```

```rs
fn main(){
    println!("Hello World!");
}
```

// 这个没有代码块包装
#show raw.where(block: false) : box.with(
    fill: luma(240),
    inset: (x: 3pt, y: 0pt),
    outset: (y: 3pt),
    radius: 2pt,
)

// 这个是有代码块包装的，源代码
#show raw.where(block: true): block.with(
    fill: luma(240),  // 设置填充
    inset: 10pt,
    radius: 4pt,
)

```sh
rg "hello world"
```

#set par(justify: true)
#set heading(numbering: "I.")

#show heading: it =>{
    set block(below: 10pt)
    set text(weight: "regular")
    align(center, smallcaps(it))
}

= Introduction
#lorem(40)

#set text(lang: "cn")
如果有时间，你会来看一看我吧

// 设置下标
test#sub[test]

$x < y => x gt.eq.not y$

$x < y arrow.r x gt.eq.not y$

$sum_(k=0)^n k
&= 1 + ... + n
&= (n(n+1))$

$frac(a^2, 2)$
$vec(1, 2, delim: "[")$
$mat(1, 2; 3, 4)$
$lim_x = op("lim", limits: #true)_x$

// 这个scripts(sum)就是：求和
$scripts(sum)_1^2 != sum_1^2$