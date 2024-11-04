---
title: 操作现有PDF中的表格
linktitle: 操作表格
type: docs
weight: 40
url: /python-net/manipulate-tables-in-existing-pdf/
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "操作现有PDF中的表格",
    "alternativeHeadline": "如何更新现有PDF中的表格内容",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 文档生成",
    "keywords": "pdf, python, 操作表格",
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
    "url": "/python-net/manipulate-tables-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/manipulate-tables-in-existing-pdf/"
    },
    "dateModified": "2023-02-04",
    "description": ""
}
</script>


## 操作现有 PDF 中的表格

Aspose.PDF for Python via .NET 支持的最早功能之一是其处理表格的能力，并且它为从头生成或已有的 PDF 文件中添加表格提供了极大的支持。在这个新版本中，我们实现了搜索和解析已经存在于 PDF 文档页面上的简单表格的新功能。一个名为 [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) 的新类提供了这些能力。TableAbsorber 的用法与现有的 [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) 类非常相似。以下代码片段展示了更新特定表格单元格内容的步骤。

```python

    import aspose.pdf as ap

    # 加载现有 PDF 文件
    pdf_document = ap.Document(input_file)
    # 创建 TableAbsorber 对象以查找表格
    absorber = ap.text.TableAbsorber()
    # 使用吸收器访问第一页
    absorber.visit(pdf_document.pages[1])
    # 获取页面上第一个表格的访问权限，第一个单元格及其中的文本片段
    fragment = absorber.table_list[0].row_list[0].cell_list[0].text_fragments[1]
    # 更改单元格中第一个文本片段的文本
    fragment.text = "hi world"
    pdf_document.save(output_file)
```


## 在 PDF 文档中用新表替换旧表

如果您需要查找特定表并用所需表替换它，可以使用 [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) 类的 [replace()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods) 方法来实现。以下示例演示了在 PDF 文档中替换表的功能：

```python

    import aspose.pdf as ap

    # 加载现有的 PDF 文档
    pdf_document = ap.Document(input_file)
    # 创建 TableAbsorber 对象以查找表
    absorber = ap.text.TableAbsorber()
    # 使用吸收器访问第一页
    absorber.visit(pdf_document.pages[1])
    # 获取页面上的第一个表
    table = absorber.table_list[0]
    # 创建新表
    new_table = ap.Table()
    new_table.column_widths = "100 100 100"
    new_table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 1)

    row = new_table.rows.add()
    row.cells.add("列 1")
    row.cells.add("列 2")
    row.cells.add("列 3")

    # 用新表替换表
    absorber.replace(pdf_document.pages[1], table, new_table)
    # 保存文档
    pdf_document.save(output_file)
```


## 如何确定表格是否会在当前页面中断

此代码生成一个包含表格的PDF文档，计算页面上的可用空间，并检查向表格添加更多行是否会因空间限制而导致分页符。结果将保存到输出文件中。

```python

    import aspose.pdf as ap

    # 实例化一个PDF类对象
    pdf = ap.Document()
    # 添加一个部分到PDF文档的部分集合中
    page = pdf.pages.add()
    # 实例化一个表格对象
    table1 = ap.Table()
    table1.margin.top = 300
    # 在所需部分的段落集合中添加表格
    page.paragraphs.add(table1)
    # 设置表格的列宽
    table1.column_widths = "100 100 100"
    # 使用BorderInfo对象设置默认单元格边框
    table1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # 使用另一个自定义的BorderInfo对象设置表格边框
    table1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # 创建MarginInfo对象并设置其左、下、右和上边距
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # 将默认单元格内边距设置为MarginInfo对象
    table1.default_cell_padding = margin
    # 如果将计数器增加到17，表格将会中断
    # 因为它不能再容纳于这个页面上
    for row_counter in range(0, 17):
        # 在表格中创建行，然后在行中创建单元格
        row1 = table1.rows.add()
        row1.cells.add("col " + str(row_counter) + ", 1")
        row1.cells.add("col " + str(row_counter) + ", 2")
        row1.cells.add("col " + str(row_counter) + ", 3")
    # 获取页面高度信息
    page_height = pdf.page_info.height
    # 获取页面顶部和底部边距、表格顶部边距和表格高度的总高度信息
    total_objects_height = page.page_info.margin.top + page.page_info.margin.bottom + table1.margin.top + \
                           table1.get_height(None)
    # 显示页面高度、表格高度、表格顶部边距以及页面顶部和底部边距信息
    print("PDF文档高度 = " + str(pdf.page_info.height) + "\n顶部边距信息 = " + str(page.page_info.margin.top)
          + "\n底部边距信息 = " + str(page.page_info.margin.bottom) + "\n\n表格顶部边距信息 = "
          + str(table1.margin.top) + "\n平均行高 = " + str(table1.rows[0].min_row_height) + " \n表格高度 "
          + str(table1.get_height(None)) + "\n ----------------------------------------" + "\n总页面高度 ="
          + str(page_height) + "\n包括表格的累计高度 =" + str(total_objects_height))
    # 检查我们是否从页面高度中扣除页面顶部边距+页面底部边距
    # + 表格顶部边距和表格高度，且小于10（平均行高可以大于10）
    if (page_height - total_objects_height) <= 10:
        # 如果值小于10，则显示消息。
        # 这表明不能再放置另一行，如果我们添加新行，表格将会中断。
        # 这取决于行高值。
        print("页面高度 - 对象高度 < 10，因此表格将会中断")
    # 保存pdf文档
    pdf.save(output_file)
```


## 在表中添加重复列

在 [Aspose.Pdf.Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) 类中，你可以设置 [repeating_rows_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties)，如果表格在垂直方向上太长而溢出到下一页，它将重复行。然而，在某些情况下，表格太宽而无法适应单个页面，需要在下一页继续。为了实现这个目的，我们在 [Aspose.Pdf.Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) 类中实现了 [repeating_columns_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) 属性。设置此属性将导致表格按列方式分隔至下一页，并在下一页的开头重复给定的列数。以下代码片段展示了 [repeating_columns_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) 属性的用法：

```python

    import aspose.pdf as ap

    # 创建一个新文档
    doc = ap.Document()
    page = doc.pages.add()
    # 实例化一个占据整个页面的外部表
    outer_table = ap.Table()
    outer_table.column_widths = "100%"
    outer_table.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # 实例化一个将嵌套在 outerTable 内的表对象，该对象将在同一页面内拆分
    my_table = ap.Table()
    my_table.broken = ap.TableBroken.VERTICAL_IN_SAME_PAGE
    my_table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_CONTENT
    # 将 outerTable 添加到页面段落
    # 将我的表格添加到 outerTable
    page.paragraphs.add(outer_table)
    body_row = outer_table.rows.add()
    body_cell = body_row.cells.add()
    body_cell.paragraphs.add(my_table)
    my_table.repeating_columns_count = 5
    page.paragraphs.add(my_table)
    # 添加标题行
    row = my_table.rows.add()
    row.cells.add("header 1")
    row.cells.add("header 2")
    row.cells.add("header 3")
    row.cells.add("header 4")
    row.cells.add("header 5")
    row.cells.add("header 6")
    row.cells.add("header 7")
    row.cells.add("header 11")
    row.cells.add("header 12")
    row.cells.add("header 13")
    row.cells.add("header 14")
    row.cells.add("header 15")
    row.cells.add("header 16")
    row.cells.add("header 17")
    for row_counter in range(0, 6):
        # 在表中创建行，然后在行中创建单元格
        row1 = my_table.rows.add()
        row1.cells.add("col " + str(row_counter) + ", 1")
        row1.cells.add("col " + str(row_counter) + ", 2")
        row1.cells.add("col " + str(row_counter) + ", 3")
        row1.cells.add("col " + str(row_counter) + ", 4")
        row1.cells.add("col " + str(row_counter) + ", 5")
        row1.cells.add("col " + str(row_counter) + ", 6")
        row1.cells.add("col " + str(row_counter) + ", 7")
        row1.cells.add("col " + str(row_counter) + ", 11")
        row1.cells.add("col " + str(row_counter) + ", 12")
        row1.cells.add("col " + str(row_counter) + ", 13")
        row1.cells.add("col " + str(row_counter) + ", 14")
        row1.cells.add("col " + str(row_counter) + ", 15")
        row1.cells.add("col " + str(row_counter) + ", 16")
        row1.cells.add("col " + str(row_counter) + ", 17")
    doc.save(output_file)
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
    "applicationCategory": "PDF 操作库适用于 Python via .NET",
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