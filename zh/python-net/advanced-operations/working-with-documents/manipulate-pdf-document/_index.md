---
title: 使用 .NET 在 Python 中操作 PDF 文档
linktitle: 操作 PDF 文档
type: docs
weight: 20
url: /zh/python-net/manipulate-pdf-document/
description: 本文包含了使用 Python 验证符合 PDF A 标准的 PDF 文档、如何使用目录（TOC）、如何设置 PDF 过期日期等信息。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 操作 PDF 文档的指南
Abstract: 本文提供了使用 Python（特别是 Aspose.PDF 库）操作 PDF 文档的综合指南。它涵盖了多项功能，包括使用 `Document` 类的 `validate` 方法验证 PDF 文档是否符合 PDF/A-1a 和 PDF/A-1b 标准。文章还详细说明了如何在 PDF 文件中添加、定制和管理目录（TOC），例如设置不同的 TabLeaderTypes、隐藏页码以及使用前缀自定义页码。此外，文章解释了如何通过嵌入用于访问限制的 JavaScript 来设置 PDF 文档的过期日期，以及如何将 PDF 中的可填表单扁平化以使其不可编辑。每个章节均配有代码片段，演示如何使用 Aspose.PDF 在 Python 中实现这些功能。
---

## 使用 Python 操作 PDF 文档

## 验证 PDF 文档是否符合 PDF A 标准（A 1A 和 A 1B）

要验证 PDF 文档是否兼容 PDF/A-1a 或 PDF/A-1b，请使用 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类的 [validate](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法。该方法允许您指定保存结果的文件名以及所需的验证类型 PdfFormat 枚举：PDF_A_1A 或 PDF_A_1B。

以下代码片段展示了如何验证 PDF 文档以符合 PDF/A-1A。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Validate PDF for PDF/A-1a
    document.validate(output_xml, ap.PdfFormat.PDF_A_1A)
```

以下代码片段展示了如何验证 PDF 文档以符合 PDF/A-1b。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Validate PDF for PDF/A-1a
    document.validate(output_xml, ap.PdfFormat.PDF_A_1B)
```

## 使用目录（TOC）

### 向现有 PDF 添加目录

PDF 中的 TOC 代表“目录”（Table of Contents）。它是一项功能，允许用户通过提供文档各章节和标题的概览，快速导航文档。

要向现有 PDF 文件添加目录，请使用 [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) 命名空间中的 Heading 类。[aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) 命名空间既可以创建新 PDF，也可以操作现有的 PDF。要向现有 PDF 添加目录，请使用 Aspose.Pdf 命名空间。以下代码片段展示了如何使用 Python via .NET 在现有 PDF 文件中创建目录。

```python

    import aspose.pdf as ap

    # Load an existing PDF files
    doc = ap.Document(input_pdf)

    # Get access to first page of PDF file
    tocPage = doc.pages.insert(1)

    # Create object to represent TOC information
    tocInfo = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD

    # Set the title for TOC
    tocInfo.title = title
    tocPage.toc_info = tocInfo

    # Create string objects which will be used as TOC elements
    titles = ["First page", "Second page", "Third page", "Fourth page"]
    for i in range(0, 2):
        # Create Heading object
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = tocPage
        heading2.segments.append(segment2)

        # Specify the destination page for heading object
        heading2.destination_page = doc.pages[i + 2]

        # Destination page
        heading2.top = doc.pages[i + 2].rect.height

        # Destination coordinate
        segment2.text = titles[i]

        # Add heading to page containing TOC
        tocPage.paragraphs.add(heading2)

    # Save the updated document
    doc.save(output_pdf)
```

### 为不同的目录层级设置不同的 TabLeaderType

Aspose.PDF for Python 还允许为不同的目录层级设置不同的 TabLeaderType。您需要设置 [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) 的 [line_dash](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) 属性。

```python

    import aspose.pdf as ap

    doc = ap.Document()
    tocPage = doc.pages.add()
    toc_info = ap.TocInfo()

    # set LeaderType
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 30
    toc_info.title = title

    # Add the list section to the sections collection of the Pdf document
    tocPage.toc_info = toc_info
    # Define the format of the four levels list by setting the left margins
    # and
    # text format settings of each level

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.left = 0
    toc_info.format_array[0].margin.right = 30
    toc_info.format_array[0].line_dash = ap.text.TabLeaderType.DOT
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 10
    toc_info.format_array[1].margin.right = 30
    toc_info.format_array[1].line_dash = 3
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].margin.left = 20
    toc_info.format_array[2].margin.right = 30
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].line_dash = ap.text.TabLeaderType.SOLID
    toc_info.format_array[3].margin.left = 30
    toc_info.format_array[3].margin.right = 30
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    # Create a section in the Pdf document
    page = doc.pages.add()

    # Add four headings in the section
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        heading2.toc_page = tocPage
        segment2.text = "Sample Heading" + str(Level)
        heading2.text_state.font = ap.text.FontRepository.find_font("Arial")

        # Add the heading into Table Of Contents.
        heading2.is_in_list = True
        page.paragraphs.add(heading2)

    # save the Pdf
    doc.save(output_pdf)
```

### 在目录中隐藏页码

如果您不想在目录中显示页码（以及标题），可以将 [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) 类的 [is_show_page_numbers](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) 属性设为 false。请查看以下代码片段以在目录中隐藏页码：

```python

    import aspose.pdf as ap

    doc = ap.Document()
    toc_page = doc.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    # Add the list section to the sections collection of the Pdf document
    toc_page.toc_info = toc_info
    # Define the format of the four levels list by setting the left margins and
    # text format settings of each level

    toc_info.is_show_page_numbers = False
    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.right = 0
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 30
    toc_info.format_array[1].text_state.underline = True
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD
    page = doc.pages.add()
    # Add four headings in the section
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        segment2.text = "this is heading of level " + str(Level)
        heading2.is_in_list = True
        page.paragraphs.add(heading2)
    doc.save(output_pdf)

```

### 添加目录时自定义页码

在 PDF 文档中添加目录时，自定义目录的页码是常见需求。例如，我们可能需要在页码前添加前缀，如 P1、P2、P3 等。在这种情况下，Aspose.PDF for Python 提供了 [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) 类的 [page_numbers_prefix](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) 属性，可用于实现此功能。

```python

    import aspose.pdf as ap

    # Load an existing PDF files
    doc = ap.Document(input_pdf)
    # Get access to first page of PDF file
    toc_page = doc.pages.insert(1)
    # Create object to represent TOC information
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    # Set the title for TOC
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info
    for i in range(len(doc.pages)):
        # Create Heading object
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        # Specify the destination page for heading object
        heading2.destination_page = doc.pages[i + 1]
        # Destination page
        heading2.top = doc.pages[i + 1].rect.height
        # Destination coordinate
        segment2.text = "Page " + str(i)
        # Add heading to page containing TOC
        toc_page.paragraphs.add(heading2)

    # Save the updated document
    doc.save(output_pdf)

```

## 如何设置 PDF 过期日期

我们在 PDF 文件上应用访问权限，以便特定用户组能够访问 PDF 文档的某些功能/对象。为了限制 PDF 文件的访问，我们通常会使用加密，并可能需要设置 PDF 文件的过期时间，以便在用户访问/查看文档时收到有关 PDF 文件过期的有效提示。

```python

    import aspose.pdf as ap

    # Instantiate Document object
    doc = ap.Document()
    # Add page to pages collection of PDF file
    doc.pages.add()
    # Add text fragment to paragraphs collection of page object
    doc.pages[1].paragraphs.add(ap.text.TextFragment("Hello World..."))
    # Create JavaScript object to set PDF expiry date
    javaScript = ap.annotations.JavascriptAction(
        "var year=2017;"
        + "var month=5;"
        + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        + "expiry = new Date(year, month);"
        + "if (today.getTime() > expiry.getTime())"
        + "app.alert('The file is expired. You need a new one.');"
    )
    # Set JavaScript as PDF open action
    doc.open_action = javaScript

    # Save PDF Document
    doc.save(output_pdf)
```

## 在 Python 中扁平化可填表单 PDF

PDF 文档通常包含带有交互式可填充控件的表单，如单选按钮、复选框、文本框、列表等。为了在各种应用场景中使其不可编辑，需要对 PDF 文件进行扁平化处理。
Aspose.PDF 提供了在 Python 中仅使用几行代码即可扁平化 PDF 的功能：

```python

    import aspose.pdf as ap

    # Load source PDF form
    doc = ap.Document(input_pdf)

    # Flatten Flatten Fillable PDF
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(output_pdf)
```


