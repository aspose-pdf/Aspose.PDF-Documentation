---
title: 使用Python通过.NET操作PDF文档
linktitle: 操作PDF文档
type: docs
weight: 20
url: zh/python-net/manipulate-pdf-document/
description: 本文包含有关如何使用Python验证PDF A标准的PDF文档，如何处理目录，如何设置PDF到期日期等信息。
keywords: "操作pdf python"
lastmod: "2023-04-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "通过Python操作PDF文档",
    "alternativeHeadline": "如何使用Python操作PDF文件",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf文档生成",
    "keywords": "pdf, dotnet, python, 操作pdf文件",
    "wordcount": "302",
    "proficiencyLevel":"初学者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/python-net/manipulate-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/manipulate-pdf-document/"
    },
    "dateModified": "2023-04-13",
    "description": "本文包含有关如何使用Python验证PDF A标准的PDF文档，如何处理目录，如何设置PDF到期日期等信息。"
}
</script>


## 在 Python 中操作 PDF 文档

## 验证 PDF 文档是否符合 PDF A 标准 (A 1A 和 A 1B)

要验证 PDF 文档是否兼容 PDF/A-1a 或 PDF/A-1b，请使用 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类的 [validate](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法。此方法允许您指定保存结果的文件名称以及所需的验证类型 PdfFormat 枚举：PDF_A_1A 或 PDF_A_1B。

以下代码片段向您展示如何验证 PDF 文档是否符合 PDF/A-1A。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)

    # 验证 PDF 是否符合 PDF/A-1a
    document.validate(output_xml, ap.PdfFormat.PDF_A_1A)
```

以下代码片段向您展示如何验证 PDF 文档是否符合 PDF/A-1b。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)

    # 验证 PDF 是否符合 PDF/A-1b
    document.validate(output_xml, ap.PdfFormat.PDF_A_1B)
```


## 使用目录

### 向现有 PDF 添加目录

PDF 中的目录（TOC）代表“目录”。它是一项功能，通过提供文档各个部分和标题的概览，允许用户快速浏览文档。

要向现有的 PDF 文件添加目录，请使用 [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) 命名空间中的 Heading 类。[aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) 命名空间可以创建新 PDF 文件，也可以操作现有 PDF 文件。要向现有的 PDF 添加目录，请使用 Aspose.Pdf 命名空间。以下代码片段展示了如何使用 Python 通过 .NET 在现有 PDF 文件中创建目录。

```python

    import aspose.pdf as ap

    # 加载现有的 PDF 文件
    doc = ap.Document(input_pdf)

    # 访问 PDF 文件的第一页
    tocPage = doc.pages.insert(1)

    # 创建对象以表示目录信息
    tocInfo = ap.TocInfo()
    title = ap.text.TextFragment("目录")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD

    # 设置目录的标题
    tocInfo.title = title
    tocPage.toc_info = tocInfo

    # 创建将用作目录元素的字符串对象
    titles = ["第一页", "第二页", "第三页", "第四页"]
    for i in range(0, 2):
        # 创建 Heading 对象
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = tocPage
        heading2.segments.append(segment2)

        # 指定标题对象的目标页面
        heading2.destination_page = doc.pages[i + 2]

        # 目标页面
        heading2.top = doc.pages[i + 2].rect.height

        # 目标坐标
        segment2.text = titles[i]

        # 将标题添加到包含目录的页面
        tocPage.paragraphs.add(heading2)

    # 保存更新后的文档
    doc.save(output_pdf)
```


### 为不同的目录级别设置不同的TabLeaderType

Aspose.PDF for Python还允许为不同的目录级别设置不同的TabLeaderType。您需要设置[TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/)的[line_dash](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties)属性。

```python

    import aspose.pdf as ap

    doc = ap.Document()
    tocPage = doc.pages.add()
    toc_info = ap.TocInfo()

    # 设置LeaderType
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("目录")
    title.text_state.font_size = 30
    toc_info.title = title

    # 将列表部分添加到Pdf文档的部分集合中
    tocPage.toc_info = toc_info
    # 通过设置左边距和
    # 每个级别的文本格式设置来定义四级列表的格式

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

    # 在Pdf文档中创建一个部分
    page = doc.pages.add()

    # 在部分中添加四个标题
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        heading2.toc_page = tocPage
        segment2.text = "示例标题" + str(Level)
        heading2.text_state.font = ap.text.FontRepository.find_font("Arial")

        # 将标题添加到目录中。
        heading2.is_in_list = True
        page.paragraphs.add(heading2)

    # 保存Pdf
    doc.save(output_pdf)
```


### 隐藏目录中的页码

如果您不想在目录中显示页码，可以将[TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/)类的[is_show_page_numbers](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties)属性设置为false。请查看以下代码片段以隐藏目录中的页码：

```python

    import aspose.pdf as ap

    doc = ap.Document()
    toc_page = doc.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("目录")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    # 将列表部分添加到PDF文档的部分集合中
    toc_page.toc_info = toc_info
    # 通过设置左边距和各级文本格式设置来定义四级列表的格式

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
    # 在部分中添加四个标题
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        segment2.text = "这是第 " + str(Level) + " 级的标题"
        heading2.is_in_list = True
        page.paragraphs.add(heading2)
    doc.save(output_pdf)

```


### 自定义页码同时添加目录

在 PDF 文档中添加目录时，自定义目录中的页码是很常见的。例如，我们可能需要在页码前添加一些前缀，如 P1、P2、P3 等。在这种情况下，Aspose.PDF for Python 提供了 [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) 类的 [page_numbers_prefix](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) 属性，可以用来自定义页码，如以下代码示例所示。

```python

    import aspose.pdf as ap

    # 加载现有的 PDF 文件
    doc = ap.Document(input_pdf)
    # 获取 PDF 文件的第一页
    toc_page = doc.pages.insert(1)
    # 创建对象以表示目录信息
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    # 设置目录的标题
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info
    for i in range(len(doc.pages)):
        # 创建标题对象
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        # 指定标题对象的目标页
        heading2.destination_page = doc.pages[i + 1]
        # 目标页
        heading2.top = doc.pages[i + 1].rect.height
        # 目标坐标
        segment2.text = "Page " + str(i)
        # 将标题添加到包含目录的页面
        toc_page.paragraphs.add(heading2)

    # 保存更新后的文档
    doc.save(output_pdf)

```


## 如何设置PDF到期日期

我们对PDF文件应用访问权限，以便某些用户组可以访问PDF文档的特定功能/对象。为了限制PDF文件的访问，我们通常应用加密，并且可能需要设置PDF文件的到期日期，以便访问/查看文档的用户可以获得有关PDF文件到期的有效提示。

```python

    import aspose.pdf as ap

    # 实例化Document对象
    doc = ap.Document()
    # 向PDF文件的页面集合添加页面
    doc.pages.add()
    # 向页面对象的段落集合中添加文本片段
    doc.pages[1].paragraphs.add(ap.text.TextFragment("Hello World..."))
    # 创建JavaScript对象以设置PDF到期日期
    javaScript = ap.annotations.JavascriptAction(
        "var year=2017;"
        + "var month=5;"
        + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        + "expiry = new Date(year, month);"
        + "if (today.getTime() > expiry.getTime())"
        + "app.alert('The file is expired. You need a new one.');"
    )
    # 设置JavaScript为PDF打开动作
    doc.open_action = javaScript

    # 保存PDF文档
    doc.save(output_pdf)
```


## 在 Python 中将可填写的 PDF 扁平化

PDF 文档通常包含带有交互式可填写控件的表单，例如单选按钮、复选框、文本框、列表等。为了使其在各种应用程序中不可编辑，我们需要将 PDF 文件扁平化。  
Aspose.PDF 提供了在 Python 中只需几行代码即可扁平化 PDF 的功能：

```python

    import aspose.pdf as ap

    # 加载源 PDF 表单
    doc = ap.Document(input_pdf)

    # 扁平化可填写的 PDF
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # 保存更新后的文档
    doc.save(output_pdf)