#outline() // 目录

#set heading(numbering: "1.")
#set math.equation(numbering: "(1)")

#show ref: it => {
  let eq = math.equation
  let el = it.element
  if el != none and el.func() == eq {
    numbering(
      el.numbering,
      ..counter(eq).at(el.location()),
    )
  } else {
    it
  }
}

= Beginnings <beginning>
In @beginning we prove @pythagoras.

$a^2 + b^2 = c^2$ <pythagoras>

#set heading(numbering: "1.a.")

= A section

== A subsection

=== A sub-subsection

#heading[Normal]

#heading(outlined: false)[Hidden] // 这个heading不会出现在目录中

#numbering("1.1)", 1, 2, 3) // 这个是设置了三个等级

#numbering("1.a.i", 1, 2, 4) // 也是设置三个等级

#numbering("I - 1", 12, 2)
你知道这是为什么吗？

#numbering((..nums) => nums
.pos()
.map(str) // 这个是映射成了string?
.join(".") + ")", 1, 2, 3)

#show link: underline

#link("https://www.google.com")

#link("https://www.google.com")[看看这个网站]

#locate(loc => [
  My locatation: \
  #loc.position()!// 展示位置
])

#set page(numbering: "(i)")

= Preface
The preface is numbered with roman roman numerals.

#set page(numbering: "1/1")
#counter(page).update(1)

= Main text

#let mine = counter("mycounter")

= value
#locate(
  loc => {
    let start-val = mine.at(loc) // 在输入中获取一个数组
    let elements = query(<intro>, loc)
    let intro-val = mine.at(elements.first().location()) // 也是返回一个数组
    let final-val = mine.final(loc) // 返回一个数组
    [
      Starts as #start-val \
      Value at intro is: #intro-val \
      Final value is: #final-val \
    ]
  },
)

#mine.update(n => n + 3)

= Introduction <intro>
#lorem(10)

#mine.step()

#mine.step()

#set page(
  header: locate(
    loc => {
      let elems = query(selector(heading).before(loc), loc)
      let academy = smallcaps[
        Typst Academy
      ]
      if elems == () {
        align(right, academy)
      } else {
        let body = elems.last().body
        academy + h(1fr) + emph(body)
      }
    },
  ),
)

= Introduce