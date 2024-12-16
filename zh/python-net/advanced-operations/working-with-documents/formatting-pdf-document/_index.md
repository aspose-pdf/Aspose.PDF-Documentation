---
title: 使用Python格式化PDF文档
linktitle: 格式化PDF文档
type: docs
weight: 11
url: /zh/python-net/formatting-pdf-document/
description: 使用Aspose.PDF for Python via .NET创建和格式化PDF文档。使用下面的代码片段来解决您的任务。
lastmod: "2023-04-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "使用Python格式化PDF文档",
    "alternativeHeadline": "如何通过.NET在Python中格式化PDF文档",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, dotnet, python, 格式化PDF文档",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
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
    "url": "/python-net/formatting-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/formatting-pdf-document/"
    },
    "dateModified": "2023-04-13",
    "description": "使用Aspose.PDF for Python via .NET创建和格式化PDF文档。使用下面的代码片段来解决您的任务。"
}
</script>


## 格式化 PDF 文档

### 获取文档窗口和页面显示属性

本主题帮助您了解如何获取文档窗口、查看器应用程序的属性，以及页面如何显示。要设置这些属性：

使用 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类打开 PDF 文件。现在，您可以设置 Document 对象的属性，例如

- CenterWindow – 将文档窗口置于屏幕中央。默认值：false。
- Direction – 阅读顺序。这决定了页面并排显示时的布局方式。默认值：从左到右。
- DisplayDocTitle – 在文档窗口标题栏中显示文档标题。默认值：false（显示标题）。
- HideMenuBar – 隐藏或显示文档窗口的菜单栏。默认值：false（显示菜单栏）。
- HideToolBar – 隐藏或显示文档窗口的工具栏。默认值：false（显示工具栏）。
- HideWindowUI – 隐藏或显示文档窗口元素，如滚动条。
 默认值：false（显示UI元素）。
- NonFullScreenPageMode – 文档在非全屏模式下的显示方式。
- PageLayout – 页面布局。
- PageMode – 文档首次打开时的显示方式。选项包括显示缩略图、全屏、显示附件面板。

下面的代码片段展示了如何使用 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类获取属性。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)

    # 获取不同的文档属性
    # 文档窗口的位置 - 默认值：false
    print("CenterWindow :", document.center_window)

    # 主要阅读顺序；决定页面的位置
    # 并排显示时 - 默认值：L2R
    print("Direction :", document.direction)

    # 窗口的标题栏是否应显示文档标题
    # 如果为false，则标题栏显示PDF文件名 - 默认值：false
    print("DisplayDocTitle :", document.display_doc_title)

    # 是否调整文档窗口的大小以适应
    # 首次显示的页面 - 默认值：false
    print("FitWindow :", document.fit_window)

    # 是否隐藏查看器应用程序的菜单栏 - 默认值：false
    print("HideMenuBar :", document.hide_menubar)

    # 是否隐藏查看器应用程序的工具栏 - 默认值：false
    print("HideToolBar :", document.hide_tool_bar)

    # 是否隐藏UI元素，如滚动条
    # 仅显示页面内容 - 默认值：false
    print("HideWindowUI :", document.hide_window_ui)

    # 文档的页面模式。退出全屏模式时如何显示文档。
    print("NonFullScreenPageMode :", document.non_full_screen_page_mode)

    # 页面布局，即单页，一列
    print("PageLayout :", document.page_layout)

    # 文档打开时的显示方式
    # 即显示缩略图、全屏、显示附件面板
    print("pageMode :", document.page_mode)

```

### 设置文档窗口和页面显示属性

本主题说明如何设置文档窗口、查看器应用程序和页面显示的属性。要设置这些不同的属性：

1. 使用 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类打开 PDF 文件。
1. 设置 Document 对象的属性。
1. 使用保存方法保存更新的 PDF 文件。

可用的属性有：

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

每个属性的使用和描述如下代码所示。以下代码片段演示了如何使用 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类设置属性。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)

    # 设置不同的文档属性
    # 指定将文档窗口居中显示 - 默认: false
    document.center_window = True

    # 主要阅读顺序; 确定页面的位置
    # 当并排显示时 - 默认: L2R
    document.direction = ap.Direction.R2L

    # 指定窗口的标题栏是否应显示文档标题
    # 如果为 false，标题栏显示 PDF 文件名 - 默认: false
    document.display_doc_title = True

    # 指定是否调整文档窗口的大小以适应
    # 首次显示的页面 - 默认: false
    document.fit_window = True

    # 指定是否隐藏查看器应用程序的菜单栏 - 默认: false
    document.hide_menubar = True

    # 指定是否隐藏查看器应用程序的工具栏 - 默认: false
    document.hide_tool_bar = True

    # 指定是否隐藏 UI 元素，如滚动条
    # 仅显示页面内容 - 默认: false
    document.hide_window_ui = True

    # 文档的页面模式。指定在退出全屏模式时如何显示文档。
    document.non_full_screen_page_mode = ap.PageMode.USE_OC

    # 指定页面布局，即单页，一列
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT

    # 指定打开文档时的显示方式
    # 即显示缩略图，全屏，显示附件面板
    document.page_mode = ap.PageMode.USE_THUMBS

    # 保存更新的 PDF 文件
    document.save(output_pdf)
```


### 嵌入标准Type 1字体

一些PDF文档具有来自特殊Adobe字体集的字体。来自此集合的字体称为“标准Type 1字体”。此集合包括14种字体，嵌入这种类型的字体需要使用特殊的标志，即[embed_standard_fonts](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties)。以下是可以用于获取嵌入所有字体（包括标准Type 1字体）的文档的代码片段：

```python

    import aspose.pdf as ap

    # 加载一个现有的PDF文档
    document = ap.Document(input_pdf)
    # 设置文档的EmbedStandardFonts属性
    document.embed_standard_fonts = True
    for page in document.pages:
        if page.resources.fonts != None:
            for page_font in page.resources.fonts:
                # 检查字体是否已经嵌入
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```


### 在创建PDF时嵌入字体

如果您需要使用 Adobe Reader 支持的 14 种核心字体以外的任何字体，则必须在生成 PDF 文件时嵌入字体描述。如果字体信息没有嵌入，Adobe Reader 将从操作系统中获取（如果已经安装在系统上），或者根据 PDF 中的字体描述构建替代字体。

>请注意，嵌入的字体必须安装在主机上，即在以下代码中，'Univers Condensed' 字体安装在系统上。

我们使用属性 'is_embedded' 将字体信息嵌入到 PDF 文件中。将此属性的值设置为 'True' 将把完整的字体文件嵌入到 PDF 中，虽然这会增加 PDF 文件的大小。以下是用于将字体信息嵌入 PDF 的代码片段。

```python

    import aspose.pdf as ap

    # 通过调用其空构造函数实例化 Pdf 对象
    doc = ap.Document()

    # 在 Pdf 对象中创建一个部分
    page = doc.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" 这是使用自定义字体的示例文本。")
    ts = ap.text.TextState()
    ts.font = ap.text.FontRepository.find_font("Arial")
    ts.font.is_embedded = True
    segment.text_state = ts
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    # 保存 PDF 文档
    doc.save(output_pdf)
```


### 保存 PDF 时设置默认字体名称

当 PDF 文档包含的字体在文档本身和设备上都不可用时，API 会将这些字体替换为默认字体。如果字体可用（安装在设备上或嵌入到文档中），输出的 PDF 应该具有相同的字体（不应被默认字体替换）。默认字体的值应包含字体的名称（而不是字体文件的路径）。我们实现了一个功能，可以在将文档保存为 PDF 时设置默认字体名称。以下代码片段可用于设置默认字体：

```python

    import aspose.pdf as ap

    # 加载一个现有的缺少字体的 PDF 文档
    document = ap.Document(input_pdf)

    pdfSaveOptions = ap.PdfSaveOptions()
    # 指定默认字体名称
    newName = "Arial"
    pdfSaveOptions.default_font_name = newName
    document.save(output_pdf, pdfSaveOptions)
```

### 从 PDF 文档中获取所有字体

如果您想从 PDF 文档中获取所有字体，可以使用 [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 方法，该方法在 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类中提供。
 请查看以下代码片段以从现有的 PDF 文档中获取所有字体：

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    fonts = doc.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```

### 使用 FontSubsetStrategy 改进字体嵌入

以下代码片段显示了如何设置使用 [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 属性的 [FontSubsetStrategy](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/)：

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    # 在 SubsetAllFonts 的情况下，所有字体将作为子集嵌入到文档中。
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    # 字体子集将嵌入完全嵌入的字体，但未嵌入到文档中的字体将不受影响。
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY)
    doc.save(output_pdf)
```

### 获取和设置 PDF 文件的缩放因子

有时，你可能想要确定 PDF 文档当前的缩放因子是多少。使用 Aspose.Pdf，你可以找出当前值并设置一个新的值。

[GoToAction](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) 类的 Destination 属性允许你获取与 PDF 文件关联的缩放值。同样，它也可以用于设置文件的缩放因子。

#### 设置缩放因子

以下代码片段展示了如何设置 PDF 文件的缩放因子。

```python

    import aspose.pdf as ap

    # 实例化新的 Document 对象
    doc = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5))
    doc.open_action = action
    # 保存文档
    doc.save(output_pdf)
```

#### 获取缩放因子

以下代码片段展示了如何获取 PDF 文件的缩放因子。

```python

    import aspose.pdf as ap

    # 实例化新的 Document 对象
    doc = ap.Document(input_pdf)

    # 创建 GoToAction 对象
    action = doc.open_action

    # 获取 PDF 文件的缩放因子
    print(action.destination.zoom)
```


### 设置打印对话框预设属性

Aspose.PDF 允许设置 PDF 文档的 [DUPLEX_FLIP_LONG_EDGE](https://reference.aspose.com/pdf/python-net/aspose.pdf/printduplex/#members) 成员。它允许您更改 PDF 文档的 DuplexMode 属性，该属性默认设置为 simplex。这可以通过以下两种不同的方法实现。

```python

    import aspose.pdf as ap

    doc = ap.Document()
    doc.pages.add()
    doc.duplex = ap.PrintDuplex.DUPLEX_FLIP_LONG_EDGE
    doc.save(output_pdf)
```

### 使用 PDF 内容编辑器设置打印对话框预设属性

```python

    import aspose.pdf as ap

    ed = ap.facades.PdfContentEditor()
    ed.bind_pdf(input_pdf)
    if (ed.get_viewer_preference() & ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE) > 0:
        print("该文件具有双面翻转短边")

    ed.change_viewer_preference(ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE)
    ed.save(output_pdf)
```