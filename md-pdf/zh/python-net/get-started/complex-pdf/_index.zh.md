---

title: 创建一个复杂的PDF  
linktitle: 创建一个复杂的PDF  
type: docs  
weight: 30  
url: /python-net/complex-pdf-example/  
description: Aspose.PDF for Python via .NET 允许您创建包含图像、文本片段和表格的更复杂的文档。  
lastmod: "2022-12-22"  
sitemap:  
    changefreq: "weekly"  
    priority: 0.7  

---

[Hello, World](/pdf/python-net/hello-world-example/) 示例展示了使用 Python 和 Aspose.PDF 创建 PDF 文档的简单步骤。在本文中，我们将看看如何使用 Aspose.PDF for Python 创建一个更复杂的文档。作为一个例子，我们将从一家运营客运渡轮服务的虚构公司获取一份文档。我们的文档将包含一张图片、两个文本片段（标题和段落）和一个表格。

如果我们从头开始创建一个文档，我们需要遵循一定的步骤：

1. 实例化一个 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象。在这一步中，我们将创建一个包含一些元数据但没有页面的空PDF文档。
1. 向文档对象添加一个 [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)。现在我们的文档将有一页。
1. 向页面添加一个 [Image](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/)。
1. 为页眉创建一个 [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/)。对于页眉，我们将使用Arial字体，字体大小为24pt，并居中对齐。
1. 将页眉添加到页面的 [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties)。
1. 为描述创建一个 [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/)。对于描述，我们将使用Arial字体，字体大小为24pt，并居中对齐。
1. 将（描述）添加到页面段落。
1. 创建一个表格，添加表格属性。

1. 添加 (表格) 到页面 [段落](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties)。
1. 保存文档 "Complex.pdf"。

```python

    import aspose.pdf as ap

    # 初始化文档对象
    document = ap.Document()
    # 添加页面
    page = document.pages.add()

    # 添加图像
    page.add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))

    # 添加标题
    header = ap.text.TextFragment("2020年秋季新的渡轮路线")
    header.text_state.font = ap.text.FontRepository.find_font("Arial")
    header.text_state.font_size = 24
    header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    header.position = ap.text.Position(130, 720)
    page.paragraphs.add(header)

    # 添加描述
    descriptionText = "游客必须在线购买门票，每天限量5000张。 \
    渡轮服务正在半负荷运行，并且时间表减少。请预期排队。"
    description = ap.text.TextFragment(descriptionText)
    description.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    description.text_state.font_size = 14
    description.horizontal_alignment = ap.HorizontalAlignment.LEFT
    page.paragraphs.add(description)

    # 添加表格
    table = ap.Table()

    table.column_widths = "200"
    table.border = ap.BorderInfo(ap.BorderSide.BOX, 1.0, ap.Color.dark_slate_gray)
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.BOX, 0.5, ap.Color.black)
    table.default_cell_padding = ap.MarginInfo(4.5, 4.5, 4.5, 4.5)
    table.margin.bottom = 10
    table.default_cell_text_state.font = ap.text.FontRepository.find_font("Helvetica")

    headerRow = table.rows.add()
    headerRow.cells.add("出发城市")
    headerRow.cells.add("出发岛屿")

    i = 0
    while i < headerRow.cells.count:
        headerRow.cells[i].background_color = ap.Color.gray
        headerRow.cells[i].default_cell_text_state.foreground_color = ap.Color.white_smoke
        i += 1

    time = timedelta(hours=6, minutes=0)
    incTime = timedelta(hours=0, minutes=30)

    i = 0
    while i < 10:
        dataRow = table.rows.add()
        dataRow.cells.add(str(time))
        time = time.__add__(incTime)
        dataRow.cells.add(str(time))
        i += 1

    page.paragraphs.add(table)

    document.save(output_pdf)
```