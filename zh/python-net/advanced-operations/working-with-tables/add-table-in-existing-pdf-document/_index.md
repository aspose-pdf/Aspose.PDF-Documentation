---
title: 在 PDF 中创建或添加表格使用 Python
linktitle: 创建或添加表格
type: docs
weight: 10
url: /zh/python-net/add-table-in-existing-pdf-document/
description: Aspose.PDF for Python via .NET 是一个用于创建、读取和编辑 PDF 表格的库。在此主题中查看其他高级功能。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "在 PDF 中创建或添加表格使用 Python",
    "alternativeHeadline": "如何使用 Python via .NET 向 PDF 添加表格",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 文档生成",
    "keywords": "pdf, python, 在 pdf 中创建表格, 添加表格",
    "wordcount": "302",
    "proficiencyLevel":"初学者",
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
    "url": "/python-net/add-table-in-existing-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-table-in-existing-pdf-document/"
    },
    "dateModified": "2023-02-04",
    "description": "Aspose.PDF for Python via .NET 是一个用于创建、读取和编辑 PDF 表格的库。在此主题中查看其他高级功能。"
}
</script>


## 使用 Python 创建表格

在处理 PDF 文档时，表格非常重要。它们为系统化显示信息提供了极好的功能。Aspose.PDF 命名空间包含名为 [Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/)、[Cell](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/) 和 [Row](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/) 的类，这些类提供了从头创建 PDF 文档时创建表格的功能。

可以通过创建 Table 类的对象来创建表格。

```python

    table = ap.Table()
```

### 在现有 PDF 文档中添加表格

要通过 .NET 使用 Aspose.PDF for Python 将表格添加到现有的 PDF 文件，请执行以下步骤：

1. 加载源文件。
1. 初始化表格并设置其列和行。
1. 设置表格设置（我们已设置边框）。
1. 填充表格。
1. 将表格添加到页面。
1. 保存文件。

以下代码片段显示了如何在现有 PDF 文件中添加文本。

```python

    import aspose.pdf as ap

    # 加载源PDF文档
    doc = ap.Document(input_file)
    # 初始化一个新的表实例
    table = ap.Table()
    # 将表格边框颜色设置为浅灰色
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.from_rgb(apd.Color.light_gray))
    # 设置表格单元格的边框
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.from_rgb(apd.Color.light_gray))
    # 创建一个循环以添加10行
    for row_count in range(0, 10):
        # 向表中添加行
        row = table.rows.add()
        # 添加表格单元格
        row.cells.add("列 (" + str(row_count) + ", 1)")
        row.cells.add("列 (" + str(row_count) + ", 2)")
        row.cells.add("列 (" + str(row_count) + ", 3)")
    # 将表对象添加到输入文档的第一页
    doc.pages[1].paragraphs.add(table)
    # 保存包含表对象的更新文档
    doc.save(output_file)
```

### 表格中的ColSpan和RowSpan

Aspose.PDF for Python via .NET 提供了 [col_span](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/#properties) 属性用于合并表中的列，以及 [row_span](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/#properties) 属性用于合并行。


我们在创建表格单元格的 `Cell` 对象上使用 `col_span` 或 `row_span` 属性。应用所需属性后，创建的单元格可以添加到表格中。

```python

    import aspose.pdf as ap

    # 通过调用空构造函数初始化 Document 对象
    pdf_document = ap.Document()
    pdf_document.pages.add()
    # 初始化一个新的 Table 实例
    table = ap.Table()
    # 设置表格边框颜色为浅灰色
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # 设置表格单元格的边框
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # 向表格添加第一行
    row1 = table.rows.add()
    for cellCount in range(1, 5):
        # 添加表格单元格
        row1.cells.add("测试 1" + str(cellCount))

    # 向表格添加第二行
    row2 = table.rows.add()
    row2.cells.add("测试 2 1")
    cell = row2.cells.add("测试 2 2")
    cell.col_span = 2
    row2.cells.add("测试 2 4")

    # 向表格添加第三行
    row3 = table.rows.add()
    row3.cells.add("测试 3 1")
    row3.cells.add("测试 3 2")
    row3.cells.add("测试 3 3")
    row3.cells.add("测试 3 4")

    # 向表格添加第四行
    row4 = table.rows.add()
    row4.cells.add("测试 4 1")
    cell = row4.cells.add("测试 4 2")
    cell.row_span = 2
    row4.cells.add("测试 4 3")
    row4.cells.add("测试 4 4")

    # 向表格添加第五行
    row5 = table.rows.add()
    row5.cells.add("测试 5 1")
    row5.cells.add("测试 5 3")
    row5.cells.add("测试 5 4")

    # 将表格对象添加到输入文档的第一页
    pdf_document.pages[1].paragraphs.add(table)
    # 保存更新后的包含表格对象的文档
    pdf_document.save(output_file)
```


执行代码的结果如下图所示的表格：

![ColSpan 和 RowSpan 演示](colspan_rowspan.png)

## 处理边框、边距和填充

请注意，它还支持为表格设置边框样式、边距和单元格填充的功能。在深入技术细节之前，理解下面示意图中展示的边框、边距和填充的概念非常重要：

![边框、边距和填充](set-border-style-margins-and-padding-of-table_1.png)

在上图中，您可以看到表格、行和单元格的边框重叠。使用 Aspose.PDF，表格可以有边距，单元格可以有填充。要设置单元格边距，我们必须设置单元格填充。

### 边框

要设置 [Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/)、[Row](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/) 和 [Cell](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/) 对象的边框，请使用 Table.border、Row.border 和 Cell.border 属性。
 单元格边框也可以使用 [Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) 或 Row 类的 [default_cell_border](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) 属性来设置。上面讨论的所有与边框相关的属性都被分配给 Row 类的一个实例，该实例是通过调用其构造函数创建的。Row 类有许多重载，可以接受几乎所有定制边框所需的参数。

### 边距或填充

可以使用 Table 类的 [default_cell_padding](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/#properties) 属性来管理单元格填充。所有与填充相关的属性都被分配给 [MarginInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) 类的一个实例，该类接受关于 `left`、`right`、`top` 和 `bottom` 参数的信息来创建自定义边距。
在以下示例中，单元格边框的宽度设置为0.1点，表格边框的宽度设置为1点，单元格内边距设置为5点。

![PDF表格中的边距和边框](margin-border.png)

```python

    import aspose.pdf as ap

    # 通过调用其空构造函数实例化Document对象
    doc = ap.Document()
    page = doc.pages.add()
    # 实例化一个表对象
    tab1 = ap.Table()
    # 在所需部分的段落集合中添加表格
    page.paragraphs.add(tab1)
    # 设置表格的列宽
    tab1.column_widths = "50 50 50"
    # 使用BorderInfo对象设置默认单元格边框
    tab1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # 使用另一个自定义的BorderInfo对象设置表格边框
    tab1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # 创建MarginInfo对象并设置其左、下、右和上边距
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # 将默认单元格内边距设置为MarginInfo对象
    tab1.default_cell_padding = margin
    # 创建表格中的行，然后在行中创建单元格
    row1 = tab1.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add()
    my_text = ap.text.TextFragment("col3 with large text string")
    # Row1.Cells.Add("col3 with large text string to be placed inside cell")
    row1.cells[2].paragraphs.add(my_text)
    row1.cells[2].is_word_wrapped = False
    row2 = tab1.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")
    # 保存Pdf
    doc.save(output_file)
```


要创建圆角表格，请使用 [BorderInfo 类](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) [rounded_border_radius](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/#properties) 值，并将表格角样式设置为圆形。

```python

    import aspose.pdf as ap
    
    tab1 = ap.Table()
    graph = ap.GraphInfo()
    graph.color = ap.Color.red
    # 创建一个空白的 BorderInfo 对象
    b_info = ap.BorderInfo(ap.BorderSide.ALL, graph)
    # 设置圆角边框，圆角半径为 15
    b_info.rounded_border_radius = 15
    # 将表格角样式设置为圆形
    tab1.corner_style = ap.BorderCornerStyle.ROUND
    # 设置表格边框信息
    tab1.border = b_info
```

## 应用不同的自动调整设置到表格

在使用像 Microsoft Word 这样的可视化工具设计表格时，您通常会使用自动调整功能之一来方便地将表格调整到所需的宽度。
 例如，您可以使用 "AUTO_FIT_TO_WINDOW" 选项将表格的宽度与页面匹配，或使用 AUTO_FIT_TO_CONTENT。默认情况下，使用 Aspose.Pdf 创建新表格时，它使用 [column_adjustment](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) 的 "Customized" 值。在以下代码片段中，我们在表格中设置对象参数 [MarginInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) 和 [BorderInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) 对象。测试示例并评估结果。

```python

    import aspose.pdf as ap

    # 通过调用空构造函数实例化 Pdf 对象
    doc = ap.Document()
    # 在 Pdf 对象中创建章节
    sec1 = doc.pages.add()
    # 实例化一个表格对象
    tab1 = ap.Table()
    # 在所需章节的段落集合中添加表格
    sec1.paragraphs.add(tab1)
    # 设置表格的列宽
    tab1.column_widths = "50 50 50"
    tab1.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_WINDOW
    # 使用 BorderInfo 对象设置默认单元格边框
    tab1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # 使用另一个自定义 BorderInfo 对象设置表格边框
    tab1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # 创建 MarginInfo 对象并设置其左、下、右和上边距
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # 将默认单元格填充设置为 MarginInfo 对象
    tab1.default_cell_padding = margin
    # 在表格中创建行，然后在行中创建单元格
    row1 = tab1.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add("col3")
    row2 = tab1.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")
    # 保存更新后的包含表格对象的文档
    doc.save(output_file)
```

### 获取表格宽度

有时需要动态获取表格宽度。Aspose.PDF.Table 类有一个方法 [get_width()](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#methods) 用于此目的。例如，您没有明确设置表格列宽并将 [column_adjustment](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) 设置为 'AUTO_FIT_TO_CONTENT'。在这种情况下，您可以按如下方式获取表格宽度。

```python

    import aspose.pdf as ap

    # 创建一个新文档
    doc = ap.Document()
    # 在文档中添加页面
    page = doc.pages.add()
    # 初始化新表格
    table = ap.Table()
    table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_CONTENT
    # 在表格中添加行
    row = table.rows.add()
    # 在表格中添加单元格
    cell = row.cells.add("单元格 1 文本")
    cell = row.cells.add("单元格 2 文本")
    # 获取表格宽度
    print(table.get_width())
```

## 向表格单元格添加 SVG 图像

Aspose.PDF for Python via .NET 提供了将表格单元格插入 PDF 文件的功能。
 在构建表格时，您可以在这些单元格中包含文本和图像。此外，API 提供了将 SVG 文件转换为 PDF 格式的功能。通过将这些功能结合使用，您可以加载 SVG 图像并将其放置在表格单元格内。

以下代码摘录演示了创建表对象并在其一个单元格内嵌入 SVG 图像的过程。

```python

    import aspose.pdf as ap

    # 实例化 Document 对象
    doc = ap.Document()
    # 创建图像实例
    img = ap.Image()
    # 将图像类型设置为 SVG
    img.file_type = ap.ImageFileType.SVG
    # 源文件路径
    img.file = DIR_INPUT_TABLE + "SVGToPDF.svg"
    # 设置图像实例的宽度
    img.fix_width = 50
    # 设置图像实例的高度
    img.fix_height = 50
    # 创建表实例
    table = ap.Table()
    # 设置表格单元格的宽度
    table.column_widths = "100 100"
    # 创建行对象并将其添加到表实例中
    row = table.rows.add()
    # 创建单元格对象并将其添加到行实例中
    cell = row.cells.add()
    # 向单元格对象的段落集合中添加文本片段
    cell.paragraphs.add(ap.text.TextFragment("First cell"))
    # 向行对象中添加另一个单元格
    cell = row.cells.add()
    # 向最近添加的单元格实例的段落集合中添加 SVG 图像
    cell.paragraphs.add(img)
    # 创建页面对象并将其添加到文档实例的页面集合中
    page = doc.pages.add()
    # 将表格添加到页面对象的段落集合中
    page.paragraphs.add(table)
    # 保存 PDF 文件
    doc.save(output_file)
```

## 在表格行之间插入分页符

默认情况下，当您在 PDF 文件中创建表格时，如果表格超出其底部边距，表格将跨多个页面显示。然而，有时我们需要在表格中添加特定数量的行后强制进行分页。以下代码片段描述了在表格中包含 10 行时插入分页符的过程。

```python

    import aspose.pdf as ap

    # 实例化 Document 对象
    doc = ap.Document()
    # 向 PDF 文件的页面集合中添加页面
    doc.pages.add()
    # 创建表格实例
    tab = ap.Table()
    # 设置表格的边框样式
    tab.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)
    # 设置表格的默认边框样式，边框颜色为红色
    tab.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)
    # 指定表格列宽
    tab.column_widths = "100 100"
    # 创建循环以添加 200 行到表格
    for counter in range(0, 201):
        row = ap.Row()
        tab.rows.add(row)
        cell1 = ap.Cell()
        cell1.paragraphs.add(ap.text.TextFragment("Cell " + str(counter) + ", 0"))
        row.cells.add(cell1)
        cell2 = ap.Cell()
        cell2.paragraphs.add(ap.text.TextFragment("Cell " + str(counter) + ", 1"))
        row.cells.add(cell2)
        # 当添加 10 行时，将新行渲染到新页面中
        if counter % 10 == 0 and counter != 0:
            row.is_in_new_page = True
    # 将表格添加到 PDF 文件的段落集合中
    doc.pages[1].paragraphs.add(tab)
    # 保存 PDF 文档
    doc.save(output_file)
```


## 在新页面上渲染表格

默认情况下，段落被添加到页面对象的段落集合中。然而，可以在新页面上渲染表格，而不是直接在页面上添加之前的段落级对象之后。

### 示例：如何使用 Python 在新页面上渲染表格

要在新页面上渲染表格，请使用 [BaseParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf/baseparagraph/) 类中的 [is_in_new_page](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) 属性。以下代码片段展示了如何实现。

```python

    import aspose.pdf as ap

    doc = ap.Document()
    page_info = doc.page_info
    margin_info = page_info.margin

    margin_info.left = 37
    margin_info.right = 37
    margin_info.top = 37
    margin_info.bottom = 37

    page_info.is_landscape = True

    table = ap.Table()
    table.column_widths = "50 100"
    # 添加页面。
    cur_page = doc.pages.add()
    for i in range(1, 121):
        row = table.rows.add()
        row.fixed_row_height = 15
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("内容 1"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("HHHHH"))
    paragraphs = cur_page.paragraphs
    paragraphs.add(table)

    table1 = ap.Table()
    table1.column_widths = "100 100"
    for i in range(1, 11):
        row = table1.rows.add()
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("LAAAAAAA"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("LAAGGGGGG"))
    table1.is_in_new_page = True
    # 我想把表格 1 保持在下一页...
    paragraphs.add(table1)
    doc.save(output_file)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "applicationCategory": "PDF 操作库用于 Python via .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>