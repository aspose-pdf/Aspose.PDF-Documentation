---
title: 使用 Python 向 PDF 添加文本
linktitle: 向 PDF 添加文本
type: docs
weight: 10
url: zh/python-net/add-text-to-pdf-file/
description: 本文描述了在 Aspose.PDF 中处理文本的各个方面。了解如何向 PDF 添加文本、添加 HTML 片段或使用自定义 OTF 字体。
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "使用 Python 向 PDF 添加文本",
    "alternativeHeadline": "如何向 PDF 添加文本",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 文件生成",
    "keywords": "pdf, python, 向 pdf 添加文本",
    "wordcount": "302",
    "proficiencyLevel":"初级",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF 文档团队",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/add-text-to-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-text-to-pdf-file/"
    },
    "dateModified": "2024-02-04",
    "description": "本文描述了在 Aspose.PDF for Python 中处理文本的各个方面。了解如何向 PDF 添加文本、添加 HTML 片段或使用自定义 OTF 字体。"
}
</script>


## 添加文本

1. 使用 Aspose.PDF 打开输入的 PDF 文档。
1. 选择要添加文本的特定页面。
1. 创建一个 TextFragment 对象。文本片段是用内容 'main text' 创建的。该片段定位在页面的坐标 (100, 600)。
1. 设置文本属性。设置文本的各种属性，如字体大小、字体类型（Times New Roman）、背景颜色（浅灰色）和前景颜色（红色）。
1. 创建 TextBuilder 对象。用所选页面实例化一个 TextBuilder 对象。
1. 附加文本片段。使用 TextBuilder 对象将先前创建的文本片段附加到 PDF 页面。
1. 调用 [document.save](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法并保存输出的 PDF 文件。

以下代码片段展示了如何在现有 PDF 文件中添加文本：

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)

    # 获取特定页面
    page = document.pages[1]

    # 创建文本片段
    text_fragment = ap.text.TextFragment("main text")
    text_fragment.position = ap.text.Position(100, 600)

    # 设置文本属性
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red

    # 创建 TextBuilder 对象
    builder = ap.text.TextBuilder(page)

    # 将文本片段附加到 PDF 页面
    builder.append_text(text_fragment)

    # 保存生成的 PDF 文档。
    document.save(output_pdf)             
```


## 从流加载字体

以下代码片段显示了如何在向 PDF 文档添加文本时从流对象加载字体。

```python

    import aspose.pdf as ap

    # 加载输入 PDF 文件
    document = ap.Document()
    document.pages.add()
    # 为文档的第一页创建文本构建器对象
    text_builder = ap.text.TextBuilder(document.pages[1])
    # 创建带示例字符串的文本片段
    text_fragment = ap.text.TextFragment("Hello world")

    if input_ttf != "":
        # 将 TrueType 字体加载到流对象中
        font_stream = open(input_ttf, "rb")
        # 设置文本字符串的字体名称
        text_fragment.text_state.font = ap.text.FontRepository.open_font(
            font_stream, ap.text.FontTypes.TTF
        )
        # 指定文本片段的位置
        text_fragment.position = ap.text.Position(10, 10)
        # 将文本添加到 TextBuilder，以便可以将其放置在 PDF 文件上
        text_builder.append_text(text_fragment)
        # 保存生成的 PDF 文档。
        document.save(output_pdf)
```


## 使用 TextParagraph 添加文本

以下代码片段演示了如何使用 [TextParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) 类在 PDF 文档中添加文本。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document()
    # 向文档对象的页面集合中添加页面
    page = document.pages.add()
    builder = ap.text.TextBuilder(page)
    # 创建文本段落
    paragraph = ap.text.TextParagraph()
    # 设置后续行缩进
    paragraph.subsequent_lines_indent = 20
    # 指定添加 TextParagraph 的位置
    paragraph.rectangle = ap.Rectangle(100, 300, 200, 700, False)
    # 指定自动换行模式
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )
    # 创建文本片段
    fragment1 = ap.text.TextFragment("the quick brown fox jumps over the lazy dog")
    fragment1.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment1.text_state.font_size = 12
    # 将片段添加到段落
    paragraph.append_line(fragment1)
    # 添加段落
    builder.append_paragraph(paragraph)

    # 保存生成的 PDF 文档。
    document.save(output_pdf)
```


## 向 TextSegment 添加超链接

此代码演示了如何在 PDF 文档中创建动态和交互式内容，包括指向外部资源的超链接。

PDF 页面可能由一个或多个 TextFragment 对象组成，其中每个 TextFragment 对象可以包含一个或多个 [TextSegment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textsegment/) 实例。

请尝试使用以下代码片段来完成此需求：

```python

    import aspose.pdf as ap

    # 创建文档实例
    document = ap.Document()
    # 向 PDF 文件的页面集合中添加页面
    page1 = document.pages.add()
    # 创建 TextFragment 实例
    tf = ap.text.TextFragment("Sample Text Fragment")
    # 设置 TextFragment 的水平对齐方式
    tf.horizontal_alignment = ap.HorizontalAlignment.RIGHT
    # 使用示例文本创建一个 textsegment
    segment = ap.text.TextSegment(" ... Text Segment 1...")
    # 将 segment 添加到 TextFragment 的 segments 集合中
    tf.segments.append(segment)
    # 创建一个新的 TextSegment
    segment = ap.text.TextSegment("Link to Google")
    # 将 segment 添加到 TextFragment 的 segments 集合中
    tf.segments.append(segment)
    # 为 TextSegment 设置超链接
    segment.hyperlink = ap.WebHyperlink("www.google.com")
    # 设置文本段的前景色
    segment.text_state.foreground_color = ap.Color.blue
    # 将文本格式设置为斜体
    segment.text_state.font_style = ap.text.FontStyles.ITALIC
    # 创建另一个 TextSegment 对象
    segment = ap.text.TextSegment("TextSegment without hyperlink")
    # 将 segment 添加到 TextFragment 的 segments 集合中
    tf.segments.append(segment)
    # 将 TextFragment 添加到页面对象的段落集合中
    page1.paragraphs.add(tf)
    # 保存生成的 PDF 文档。
    document.save(output_pdf)
```


## 使用 OTF 字体

Aspose.PDF for Python via .NET 提供了在创建/操作 PDF 文件内容时使用自定义/TrueType 字体的功能，以便文件内容可以使用非默认系统字体显示。

```python

    import aspose.pdf as ap

    # 创建新的文档实例
    document = ap.Document()
    # 向 PDF 文件的页面集合添加页面
    page = document.pages.add()
    # 使用示例文本创建 TextFragment 实例
    fragment = ap.text.TextFragment("OTF 字体中的示例文本")
    # 您甚至可以在系统目录中指定 OTF 字体的路径
    fragment.text_state.font = ap.text.FontRepository.open_font(input_otf)
    # 指定在 PDF 文件中嵌入字体，以便其正确显示，
    # 即使目标计算机上未安装/存在特定字体
    fragment.text_state.font.is_embedded = True
    # 将 TextFragment 添加到 Page 实例的段落集合
    page.paragraphs.add(fragment)
    # 保存生成的 PDF 文档。
    document.save(output_pdf)
```


## 使用 DOM 添加 HTML 字符串

下面的 Python 代码利用 Aspose.PDF 库创建一个包含 HTML 片段的 PDF 文档。

1. 实例化 Document。创建 Document 类的一个实例，代表 PDF 文档。
2. 向 PDF 文档添加页面。
3. 用 HTML 内容实例化一个 HtmlFragment 对象。
4. 设置 HTML 片段的边距。在本例中，底部边距设置为 10 点，顶部边距设置为 200 点。
5. 将 HTML 片段添加到页面。
6. 保存 PDF 文件。

```python

    import aspose.pdf as ap

    # 实例化 Document 对象
    doc = ap.Document()
    # 向 PDF 文件的页面集合中添加页面
    page = doc.pages.add()
    # 用 HTML 内容实例化 HtmlFragment
    title = ap.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>")
    # 设置底部边距信息
    title.margin.bottom = 10
    # 设置顶部边距信息
    title.margin.top = 200
    # 将 HTML 片段添加到页面的段落集合
    page.paragraphs.add(title)
    # 保存 PDF 文件
    doc.save(output_pdf)
```


### FootNote的自定义线样式

以下示例演示了如何将脚注添加到Pdf页面的底部并定义自定义线样式。

```python

    import aspose.pdf as ap

    # 创建Document实例
    doc = ap.Document()
    # 向PDF的pages集合添加页面
    page = doc.pages.add()
    # 创建GraphInfo对象
    graph = ap.GraphInfo()
    # 设置线宽为2
    graph.line_width = 2
    # 设置graph对象的颜色
    graph.color = ap.Color.red
    # 设置虚线数组值为3
    graph.dash_array = [3]
    # 设置虚线相位值为1
    graph.dash_phase = 1
    # 为页面设置脚注线样式为graph
    page.note_line_style = graph
    # 创建TextFragment实例
    text = ap.text.TextFragment("Hello World")
    # 为TextFragment设置FootNote值
    text.foot_note = ap.Note("测试文本1的脚注")
    # 将TextFragment添加到文档第一页的段落集合中
    page.paragraphs.add(text)
    # 创建第二个TextFragment
    text = ap.text.TextFragment("Aspose.Pdf for .NET")
    # 为第二个文本片段设置FootNote
    text.foot_note = ap.Note("测试文本2的脚注")
    # 将第二个文本片段添加到PDF文件的段落集合中
    page.paragraphs.add(text)
    # 保存生成的PDF文档。
    doc.save(output_pdf)
```


### 自定义脚注标签

下面的代码片段展示了如何创建一个包含脚注的文本片段的 PDF 文档。

默认情况下，脚注编号从 1 开始递增。然而，我们可能需要设置一个自定义的脚注标签。为了实现这一需求，请尝试使用以下代码片段

```python

    import aspose.pdf as ap

    # 创建 Document 实例
    document = ap.Document()
    # 向 PDF 的页面集合中添加页面
    page = document.pages.add()
    # 创建 GraphInfo 对象
    graph = ap.GraphInfo()
    # 设置线宽为 2
    graph.line_width = 2
    # 设置图形对象的颜色
    graph.color = ap.Color.red
    # 设置虚线数组值为 3
    graph.dash_array = [3]
    # 设置虚线相位值为 1
    graph.dash_phase = 1
    # 为页面设置脚注线样式为图形
    page.note_line_style = graph
    # 创建 TextFragment 实例
    text = ap.text.TextFragment("Hello World")
    # 为 TextFragment 设置脚注值
    text.foot_note = ap.Note("测试文本 1 的脚注")
    # 指定脚注的自定义标签
    text.foot_note.text = " Aspose"
    # 将 TextFragment 添加到文档第一页的段落集合中
    page.paragraphs.add(text)
    # 保存生成的 PDF 文档
    document.save(output_pdf)
```


## 添加图像和表格到脚注

此代码演示了如何使用 Aspose.PDF for Python 创建一个包含复杂脚注的 PDF 文档，该脚注包括图像、文本和表格。

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()
    text = ap.text.TextFragment("some text")
    page.paragraphs.add(text)

    text.foot_note = ap.Note()
    image = ap.Image()
    image.file = input_jpg
    image.fix_height = 20
    text.foot_note.paragraphs.add(image)
    foot_note = ap.text.TextFragment("footnote text")
    foot_note.text_state.font_size = 20
    foot_note.is_in_line_paragraph = True
    text.foot_note.paragraphs.add(foot_note)
    table = ap.Table()
    table.rows.add().cells.add().paragraphs.add(ap.text.TextFragment("Row 1 Cell 1"))
    text.foot_note.paragraphs.add(table)

    # 保存生成的 PDF 文档。
    document.save(output_pdf)
```

## 如何创建尾注

尾注是一个引用来源，指引读者到文章末尾的一个特定位置，在那里他们可以找到文章中引用或提到的信息或文字的来源。
 当使用尾注时，你引用或改写的句子或总结的材料后面会跟着一个上标数字。

此代码演示了如何使用 Aspose.PDF for Python 将一个带有尾注的文本片段添加到 PDF 文档中：

```python

    import aspose.pdf as ap

    # 创建 Document 实例
    document = ap.Document()
    # 添加页面到 PDF 的页面集合中
    page = document.pages.add()
    # 创建 TextFragment 实例
    text = ap.text.TextFragment("Hello World")
    # 为 TextFragment 设置尾注值
    text.end_note = ap.Note("sample End note")
    # 为 FootNote 指定自定义标签
    text.end_note.text = " Aspose"
    # 将 TextFragment 添加到文档第一页的段落集合中
    page.paragraphs.add(text)
    # 保存生成的 PDF 文档。
    document.save(output_pdf)
```

## 文本和图像作为行内段落

PDF 文件的默认布局是流式布局（从左上到右下）。 因此，每个新元素添加到 PDF 文件时，都是添加到右下方的流程中。然而，我们可能需要在同一水平线（一个接一个）显示各种页面元素，即图像和文本。一种方法是创建一个表格实例，并将两个元素添加到单独的单元格对象中。然而，另一种方法可以是使用内联段落。通过将图像和文本的 IsInLineParagraph 属性设置为 true，这些段落会显示为其他页面元素的内联段落。

以下代码片段展示了如何在 PDF 文件中将文本和图像作为内联段落添加。

```python

    import aspose.pdf as ap

    # 实例化 Document 实例
    document = ap.Document()
    # 向 Document 实例的 pages 集合中添加页面
    page = document.pages.add()
    # 创建 TextFragment
    text = ap.text.TextFragment("Hello World.. ")
    # 将文本片段添加到 Page 对象的段落集合中
    page.paragraphs.add(text)
    # 创建一个图像实例
    image = ap.Image()
    # 设置图像为内联段落，使其显示在
    # 上一个段落对象（TextFragment）之后
    image.is_in_line_paragraph = True
    # 指定图像文件路径
    image.file = input_jpg
    # 设置图像高度（可选）
    image.fix_height = 30
    # 设置图像宽度（可选）
    image.fix_width = 100
    # 将图像添加到 page 对象的段落集合中
    page.paragraphs.add(image)
    # 使用不同的内容重新初始化 TextFragment 对象
    text = ap.text.TextFragment(" Hello Again..")
    # 设置 TextFragment 为内联段落
    text.is_in_line_paragraph = True
    # 将新创建的 TextFragment 添加到页面的段落集合中
    page.paragraphs.add(text)
    # 保存生成的 PDF 文档
    document.save(output_pdf)
```

## 指定添加文本时的字符间距

下面的代码片段展示了如何生成一个包含增加字符间距的文本片段的 PDF 文档。

可以使用 TextFragment 实例在 PDF 文件的段落集合中添加文本，也可以使用 TextParagraph 对象，甚至可以使用 TextStamp 类在 PDF 内盖上文本。

### 使用 TextBuilder 和 TextFragment

```python

    import aspose.pdf as ap

    # 创建 Document 实例
    document = ap.Document()
    # 向 Document 的页面集合添加页面
    document.pages.add()
    # 创建 TextBuilder 实例
    builder = ap.text.TextBuilder(document.pages[1])
    # 创建包含示例内容的文本片段实例
    wide_fragment = ap.text.TextFragment("Text with increased character spacing")
    wide_fragment.text_state.apply_changes_from(ap.text.TextState("Arial", 12))
    # 为 TextFragment 指定字符间距
    wide_fragment.text_state.character_spacing = 2.0
    # 指定 TextFragment 的位置
    wide_fragment.position = ap.text.Position(100, 650)
    # 将 TextFragment 附加到 TextBuilder 实例
    builder.append_text(wide_fragment)
    # 保存生成的 PDF 文档。
    document.save(output_pdf)
```


### 使用 TextParagraph

```python

    import aspose.pdf as ap

    # 创建 Document 实例
    document = ap.Document()
    # 将页面添加到 Document 的页面集合中
    document.pages.add()
    # 创建 TextBuilder 实例
    builder = ap.text.TextBuilder(document.pages[1])
    # 实例化 TextParagraph 实例
    paragraph = ap.text.TextParagraph()
    # 创建 TextState 实例以指定字体名称和大小
    state = ap.text.TextState(12.0)
    state.font = ap.text.FontRepository.find_font("Arial")
    # 指定字符间距
    state.character_spacing = 1.5
    # 将文本追加到 TextParagraph 对象
    tt = "这是具有字符间距的段落"
    paragraph.append_line(tt, state)
    # 指定 TextParagraph 的位置
    paragraph.position = ap.text.Position(100, 550)
    # 将 TextParagraph 追加到 TextBuilder 实例
    builder.append_paragraph(paragraph)
    # 保存生成的 PDF 文档。
    document.save(output_pdf)
```

### 使用 TextStamp

```python

    import aspose.pdf as ap

    # 创建 Document 实例
    document = ap.Document()
    # 将页面添加到 Document 的页面集合中
    page = document.pages.add()
    # 使用示例文本实例化 TextStamp 实例
    stamp = ap.TextStamp("这是具有字符间距的文本印章")
    # 为 Stamp 对象指定字体名称
    stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    # 指定 TextStamp 的字体大小
    stamp.text_state.font_size = 12
    # 将字符间距指定为 1
    stamp.text_state.character_spacing = 1
    # 设置印章的 x_indent
    stamp.x_indent = 100
    # 设置印章的 y_indent
    stamp.y_indent = 500
    # 将文本印章添加到页面实例
    stamp.put(page)
    # 保存生成的 PDF 文档。
    document.save(output_pdf)
```


## 创建多列 PDF 文档

[Aspose.PDF for Python via .NET](https://docs.aspose.com/pdf/python-net/) 也提供了在 PDF 文档页面内创建多列的功能。为了创建多列 PDF 文件，我们可以使用 FloatingBox 类，因为它提供了 column_info 属性来指定 FloatingBox 内的列数，并且我们还可以使用 column_spacing 和 width 属性分别指定列间距和列宽。

列间距是指列之间的空隙，默认列间距为 1.25 厘米。如果未指定列宽，[Aspose.PDF for Python via .NET](https://docs.aspose.com/pdf/python-net/) 会根据页面大小和列间距自动计算每列的宽度。

下面给出了一个示例，以演示如何创建包含图形对象（Line）的两列，并将它们添加到 FloatingBox 的段落集合中，然后将其添加到 Page 实例的段落集合中。

```python

    import aspose.pdf as ap

    document = ap.Document()
    # 指定PDF文件的左边距信息
    document.page_info.margin.left = 40
    # 指定PDF文件的右边距信息
    document.page_info.margin.right = 40
    page = document.pages.add()

    graph1 = ap.drawing.Graph(500, 2)
    # 将线添加到段落集合的部分对象中
    page.paragraphs.add(graph1)

    # 指定线的坐标
    pos1 = [1.0, 2.0, 500.0, 2.0]
    l1 = ap.drawing.Line(pos1)
    graph1.shapes.append(l1)
    # 创建包含HTML标签的文本字符串变量
    s = (
        '<font face="Times New Roman" size=4>'
        + "<strong> 如何避免金钱骗局</<strong> "
        + "</font>"
    )
    # 创建包含HTML文本的文本段落
    heading_text = ap.HtmlFragment(s)
    page.paragraphs.add(heading_text)

    box = ap.FloatingBox()
    # 在部分中添加四列
    box.column_info.column_count = 2
    # 设置列之间的间距
    box.column_info.column_spacing = "5"

    box.column_info.column_widths = "105 105"
    text1 = ap.text.TextFragment("作者：一位谷歌员工（谷歌官方博客）")
    text1.text_state.font_size = 8
    text1.text_state.line_spacing = 2
    box.paragraphs.add(text1)
    text1.text_state.font_size = 10

    text1.text_state.font_style = ap.text.FontStyles.ITALIC
    # 创建一个图形对象来绘制一条线
    graph2 = ap.drawing.Graph(50, 10)
    # 指定线的坐标
    pos2 = [1.0, 10.0, 100.0, 10.0]
    l2 = ap.drawing.Line(pos2)
    graph2.shapes.append(l2)

    # 将线添加到段落集合的部分对象中
    box.paragraphs.add(graph2)

    text2 = ap.text.TextFragment(
        "Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue. Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales."
    )
    box.paragraphs.add(text2)
    page.paragraphs.add(box)
    # 保存PDF文件
    document.save(output_pdf)
```


## 使用自定义制表位

这个Python代码片段展示了如何创建一个PDF文档，其中包含使用制表位排列的文本片段，以模拟表格结构。

以下是设置自定义制表位的示例。

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()

    ts = ap.text.TabStops()
    ts1 = ts.add(100.0)
    ts1.alignment_type = ap.text.TabAlignmentType.RIGHT
    ts1.leader_type = ap.text.TabLeaderType.SOLID
    ts2 = ts.add(200.0)
    ts2.alignment_type = ap.text.TabAlignmentType.CENTER
    ts2.leader_type = ap.text.TabLeaderType.DASH
    ts3 = ts.add(300.0)
    ts3.alignment_type = ap.text.TabAlignmentType.LEFT
    ts3.leader_type = ap.text.TabLeaderType.DOT

    header = ap.text.TextFragment(
        "这是一个使用制表位形成表格的示例", ts
    )
    text0 = ap.text.TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", ts)

    text1 = ap.text.TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", ts)
    text2 = ap.text.TextFragment("#$TABdata21 ", ts)
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data22 "))
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data23"))

    page.paragraphs.add(header)
    page.paragraphs.add(text0)
    page.paragraphs.add(text1)
    page.paragraphs.add(text2)

    document.save(output_pdf)
```


## 如何在 PDF 中添加透明文本

PDF 文件包含图像、文本、图形、附件、注释对象，在创建 TextFragment 时，您可以设置前景色、背景色信息以及文本格式。Aspose.PDF for Python via .NET 支持添加带有 Alpha 颜色通道的文本功能。

以下代码片段展示了如何添加带有透明颜色的文本。

```python

    import aspose.pdf as ap

    # 创建 Document 实例
    document = ap.Document()
    # 创建页面并添加到 PDF 文件的页面集合
    page = document.pages.add()

    # 使用示例值创建 TextFragment 实例
    text = ap.text.TextFragment(
        "transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text "
    )
    # 从 Alpha 通道创建颜色对象
    color = ap.Color.from_argb(30, 0, 255, 0)
    # 为文本实例设置颜色信息
    text.text_state.foreground_color = color
    # 将文本添加到页面实例的段落集合
    page.paragraphs.add(text)

    document.save(output_pdf)
```


## 为字体指定行间距

每种字体都有一个抽象的方块，其高度是相同字号的行之间的预期距离。这个方块称为 em 方块，它是定义字形轮廓的设计网格。许多输入字体的字母的某些点放置在字体的 em 方块边界之外，因此为了正确显示字体，需要使用特殊设置。

下面的代码片段加载一个 PDF，使用 TrueType 字体添加具有特定行间距的文本片段，并保存修改后的 PDF 文档：

```python

    import aspose.pdf as ap

    # 加载输入 PDF 文件
    document = ap.Document()
    # 创建包含 LineSpacingMode.FULL_SIZE 的 TextFormattingOptions
    options = ap.text.TextFormattingOptions()
    options.line_spacing = ap.text.TextFormattingOptions.LineSpacingMode.FULL_SIZE

    # 创建带有示例字符串的文本片段
    text_fragment = ap.text.TextFragment("Hello world")

    # 将 TrueType 字体加载到流对象中
    font_stream = open(input_ttf, "rb")
    # 设置文本字符串的字体名称
    text_fragment.text_state.font = ap.text.FontRepository.open_font(
        font_stream, ap.text.FontTypes.TTF
    )
    # 指定文本片段的位置
    text_fragment.position = ap.text.Position(100, 600)
    # 将当前片段的 TextFormattingOptions 设置为预定义的（指向 LineSpacingMode.FULL_SIZE）
    text_fragment.text_state.formatting_options = options
    page = document.pages.add()
    page.paragraphs.add(text_fragment)

    # 保存生成的 PDF 文档
    document.save(output_pdf)
```


## 动态获取文本宽度

此Python代码片段在Aspose.PDF中比较了从字体对象和文本状态对象获取的字符串测量值：

```python

    import math as ap

    font = ap.text.FontRepository.find_font("Arial")
    ts = ap.text.TextState()
    ts.font = font
    ts.font_size = 14

    if mt.fabs(font.measure_string("A", 14) - 9.337) > 0.001:
        print("意外的字体字符串测量！")

    if mt.fabs(ts.measure_string("z") - 7.0) > 0.001:
        print("意外的字体字符串测量！")

    c_code = ord("A")
    while c_code <= ord("z"):
        c = chr(c_code)

        fn_measure = font.measure_string(str(c), 14)
        ts_measure = ts.measure_string(str(c))

        print(str(c_code) + "-" + c + "-" + str(ts_measure))

        if mt.fabs(fn_measure - ts_measure) > 0.001:
            print("字体和状态字符串测量不匹配！")

        c_code += 1
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>