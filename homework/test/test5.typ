#let cell = rect.with(
    inset: 8pt,
    fill: rgb("e4e5ea"),
    width: 100%,
    radius: 6pt
)

#grid(
    columns: (60pt, 1fr, 60pt),
    rows: (60pt, auto),
    gutter: 3pt,
    cell(height: 100%)[easy to learn],
    cell(height: 100%)[great output],
    cell(height: 100%)[Intuitive],
    cell[our best typst yet],
    cell[
        responsive \ design in \ print
        for everyone
    ],
    cell[one more thing...],
)

#let thing(body) = style(styles => {
    let size = measure(body, styles)
    [Width of "#body" is #size.width]
    // 这个size是成员属性
})

#thing[Hey] \
#thing[Welcome]

#for i in range(16){
    let amount = i * 4pt
    place(center, dx: amount - 32pt, dy: amount / 8)[A]
}

v表示垂直对齐方式，8pt表示字体大小，weak: true表示文本的强度1。

h表示水平对齐方式

路径：用来绘制图像

#path(
    fill: blue.lighten(80%),
    stroke: blue,
    closed: true,
    (0pt, 50pt),
    (100%, 50pt),
    ((50%, 0pt), (40pt, 0pt)),
)
