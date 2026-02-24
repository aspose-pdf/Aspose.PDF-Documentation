---
title: 使用 Python 格式化 PDF 文档
linktitle: 格式化 PDF 文档
type: docs
weight: 11
url: /zh/python-net/formatting-pdf-document/
description: 使用 Aspose.PDF for Python via .NET 创建并格式化 PDF 文档。使用下面的代码片段来完成您的任务。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 格式化 PDF 文档
Abstract: 本文提供了使用 Aspose.PDF 库在 Python 中操作和格式化 PDF 文档的完整指南。它涵盖了 PDF 定制的各个方面，包括设置文档窗口和页面显示属性，如居中窗口、阅读方向以及隐藏 UI 元素。文章解释了如何使用 `Document` 类以编程方式检索和设置这些属性。除此之外，还讨论了字体管理，详细说明了如何将标准 Type 1 字体和其他字体嵌入 PDF，确保文档的可移植性和跨系统的视觉一致性。文章还强调了设置默认字体名称、检索 PDF 中的所有字体以及使用 `FontSubsetStrategy` 增强字体嵌入的技术。此外，本文阐述了使用 `GoToAction` 类调整 PDF 文档的缩放比例，并配置打印对话框的预设属性，包括双面打印选项。每个章节均附有代码片段，提供了实现这些功能的实用示例。
---

## 使用 Python 格式化 PDF 文档

### 获取文档窗口和页面显示属性

本节帮助您了解如何获取文档窗口、查看器应用程序以及页面显示方式的属性。要设置这些属性：

使用 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类打开 PDF 文件。现在，您可以设置 Document 对象的属性，例如

- CenterWindow – 将文档窗口居中显示在屏幕上。默认值：false。
- Direction – 阅读顺序。这决定页面并排显示时的布局方式。默认值：从左到右。
- DisplayDocTitle – 在文档窗口标题栏中显示文档标题。默认值：false（显示标题）。
- HideMenuBar – 隐藏或显示文档窗口的菜单栏。默认值：false（显示菜单栏）。
- HideToolBar – 隐藏或显示文档窗口的工具栏。默认值：false（显示工具栏）。
- HideWindowUI – 隐藏或显示文档窗口元素，如滚动条。默认值：false（显示 UI 元素）。
- NonFullScreenPageMode – 文档在非全页模式下的显示方式。
- PageLayout – 页面布局。
- PageMode – 文档首次打开时的显示方式。选项包括显示缩略图、全屏显示、显示附件面板。

以下代码片段演示了如何使用 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类获取这些属性。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Get different document properties
    # Position of document's window - Default: false
    print("CenterWindow :", document.center_window)

    # Predominant reading order; determins the position of page
    # When displayed side by side - Default: L2R
    print("Direction :", document.direction)

    # Whether window's title bar should display document title
    # If false, title bar displays PDF file name - Default: false
    print("DisplayDocTitle :", document.display_doc_title)

    # Whether to resize the document's window to fit the size of
    # First displayed page - Default: false
    print("FitWindow :", document.fit_window)

    # Whether to hide menu bar of the viewer application - Default: false
    print("HideMenuBar :", document.hide_menubar)

    # Whether to hide tool bar of the viewer application - Default: false
    print("HideToolBar :", document.hide_tool_bar)

    # Whether to hide UI elements like scroll bars
    # And leaving only the page contents displayed - Default: false
    print("HideWindowUI :", document.hide_window_ui)

    # Document's page mode. How to display document on exiting full-screen mode.
    print("NonFullScreenPageMode :", document.non_full_screen_page_mode)

    # The page layout i.e. single page, one column
    print("PageLayout :", document.page_layout)

    # How the document should display when opened
    # I.e. show thumbnails, full-screen, show attachment panel
    print("pageMode :", document.page_mode)

```

### 设置文档窗口和页面显示属性

本节解释如何设置文档窗口、查看器应用程序以及页面显示的属性。要设置这些不同的属性：

1. 使用 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类打开 PDF 文件。
1. 设置 Document 对象的属性。
1. 使用 save 方法保存更新后的 PDF 文件。

可用的属性包括：

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

每个属性的使用方法及在下面代码中的说明如下。以下代码片段演示了如何使用 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类设置这些属性。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Set different document properties
    # Sepcify to position document's window - Default: false
    document.center_window = True

    # Predominant reading order; determins the position of page
    # When displayed side by side - Default: L2R
    document.direction = ap.Direction.R2L

    # Specify whether window's title bar should display document title
    # If false, title bar displays PDF file name - Default: false
    document.display_doc_title = True

    # Specify whether to resize the document's window to fit the size of
    # First displayed page - Default: false
    document.fit_window = True

    # Specify whether to hide menu bar of the viewer application - Default: false
    document.hide_menubar = True

    # Specify whether to hide tool bar of the viewer application - Default: false
    document.hide_tool_bar = True

    # Specify whether to hide UI elements like scroll bars
    # And leaving only the page contents displayed - Default: false
    document.hide_window_ui = True

    # Document's page mode. specify how to display document on exiting full-screen mode.
    document.non_full_screen_page_mode = ap.PageMode.USE_OC

    # Specify the page layout i.e. single page, one column
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT

    # Specify how the document should display when opened
    # I.e. show thumbnails, full-screen, show attachment panel
    document.page_mode = ap.PageMode.USE_THUMBS

    # Save updated PDF file
    document.save(output_pdf)
```

### 嵌入标准 Type 1 字体

某些 PDF 文档使用来自 Adobe 特殊字体集的字体。该集合中的字体称为“标准 Type 1 字体”。此集合包含 14 种字体，嵌入此类字体需要使用特殊标志，例如 [embed_standard_fonts](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties)。以下代码片段可用于获取一个所有字体（包括标准 Type 1 字体）均已嵌入的文档：

```python

    import aspose.pdf as ap

    # Load an existing PDF Document
    document = ap.Document(input_pdf)
    # Set EmbedStandardFonts property of document
    document.embed_standard_fonts = True
    for page in document.pages:
        if page.resources.fonts != None:
            for page_font in page.resources.fonts:
                # Check if font is already embedded
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### 在创建 PDF 时嵌入字体

如果您需要使用除 Adobe Reader 支持的 14 种核心字体之外的任何字体，则必须在生成 PDF 文件时嵌入字体描述。如果未嵌入字体信息，Adobe Reader 将从操作系统中获取已安装的字体，或根据 PDF 中的字体描述符构造替代字体。

>请注意，嵌入的字体必须已安装在宿主机器上，例如以下代码中的 ‘Univers Condensed’ 字体已在系统中安装。

我们使用属性 'is_embedded' 将字体信息嵌入 PDF 文件。将此属性的值设为 'True' 将把完整的字体文件嵌入 PDF，尽管这会增加 PDF 文件的大小。以下代码片段可用于将字体信息嵌入 PDF。

```python

    import aspose.pdf as ap

    # Instantiate Pdf object by calling its empty constructor
    doc = ap.Document()

    # Create a section in the Pdf object
    page = doc.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" This is a sample text using Custom font.")
    ts = ap.text.TextState()
    ts.font = ap.text.FontRepository.find_font("Arial")
    ts.font.is_embedded = True
    segment.text_state = ts
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    # Save PDF Document
    doc.save(output_pdf)
```

### 保存 PDF 时设置默认字体名称

当 PDF 文档包含的字体在文档本身和设备上都不可用时，API 会将这些字体替换为默认字体。如果字体可用（已安装在设备上或嵌入文档中），输出的 PDF 应保持相同的字体（不应被默认字体替换）。默认字体的值应包含字体名称（而不是字体文件的路径）。我们已经实现了在将文档保存为 PDF 时设置默认字体名称的功能。以下代码片段可用于设置默认字体：

```python

    import aspose.pdf as ap

    # Load an existing PDF document with missing font
    document = ap.Document(input_pdf)

    pdfSaveOptions = ap.PdfSaveOptions()
    # Specify Default Font Name
    newName = "Arial"
    pdfSaveOptions.default_font_name = newName
    document.save(output_pdf, pdfSaveOptions)
```

### 获取 PDF 文档中的所有字体

如果您想获取 PDF 文档中的所有字体，可以使用由 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类提供的 [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 方法。请查看以下代码片段，以获取现有 PDF 文档中的所有字体：

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    fonts = doc.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```

### 使用 FontSubsetStrategy 改进字体嵌入

以下代码片段展示了如何设置用于 [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 属性的 [FontSubsetStrategy](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/)：

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    # All fonts will be embedded as subset into document in case of SubsetAllFonts.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    # Font subset will be embedded for fully embedded fonts but fonts which are not embedded into document will not be affected.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY)
    doc.save(output_pdf)
```

### 获取/设置 PDF 文件的缩放因子

有时，您想确定 PDF 文档当前的缩放因子。使用 Aspose.Pdf，您既可以查到当前值，也可以进行设置。

[GoToAction](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) 类的 Destination 属性允许您获取与 PDF 文件相关的缩放值。同样，它也可用于设置文件的缩放因子。

#### 设置缩放因子

以下代码片段展示了如何设置 PDF 文件的缩放因子。

```python

    import aspose.pdf as ap

    # Instantiate new Document object
    doc = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5))
    doc.open_action = action
    # Save the document
    doc.save(output_pdf)
```

#### 获取缩放因子

以下代码片段展示了如何获取 PDF 文件的缩放因子。

```python

    import aspose.pdf as ap

    # Instantiate new Document object
    doc = ap.Document(input_pdf)

    # Create GoToAction object
    action = doc.open_action

    # Get the Zoom factor of PDF file
    print(action.destination.zoom)
```

### 设置打印对话框预设属性

Aspoose.PDF 允许设置 PDF 文档的 [DUPLEX_FLIP_LONG_EDGE](https://reference.aspose.com/pdf/python-net/aspose.pdf/printduplex/#members) 成员。它使您能够更改默认设置为单面的 DuplexMode 属性。以下展示了两种实现此功能的不同方法。

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
        print("The file has duplex flip short edge")

    ed.change_viewer_preference(ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE)
    ed.save(output_pdf)
```


