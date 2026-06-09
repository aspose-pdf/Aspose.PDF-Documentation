---
title: 在 Python 中格式化 PDF 文档
linktitle: 格式化 PDF 文档
type: docs
weight: 11
url: /zh/python-net/formatting-pdf-document/
description: 了解如何在 Python 中格式化 PDF 文档、嵌入字体、控制查看器设置以及调整显示选项。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 格式化 PDF 文档
Abstract: 本文提供了使用 Aspose.PDF 库在 Python 中操作和格式化 PDF 文档的全面指南。它涵盖了 PDF 定制的各个方面，包括设置文档窗口和页面显示属性，如居中窗口、阅读方向以及隐藏 UI 元素。文章解释了如何使用 `Document` 类以编程方式获取和设置这些属性。此外，文章还涉及字体管理，详细说明了如何将 Standard Type 1 字体和其他字体嵌入 PDF，确保文档的可移植性和跨系统的视觉一致性。它还重点介绍了设置默认字体名称、从 PDF 中检索所有字体以及使用 `FontSubsetStrategy` 增强字体嵌入的技术。进一步地，本文阐述了使用 `GoToAction` 类调整 PDF 文档的缩放比例，以及配置打印对话框预设属性，包括双面打印选项。每个章节均附有代码片段，提供实现这些功能的实用示例。
---

当您需要在 Python 生成的文档中控制 PDF 查看器行为、字体嵌入、默认显示设置或打印首选项时，此指南很有用。

## 格式化 PDF 文档

### 获取文档窗口和页面显示属性

本主题帮助您了解如何获取文档窗口、查看器应用程序的属性以及页面的显示方式。要设置这些属性：

使用以下方式打开 PDF 文件 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类。现在，您可以设置 Document 对象的属性，例如

- CenterWindow – 将文档窗口居中显示在屏幕上。默认值：false。
- 方向 – 阅读顺序。这决定了页面在并排显示时的布局方式。默认：从左到右。
- DisplayDocTitle – 在文档窗口标题栏中显示文档标题。默认值：false（显示标题）。
- HideMenuBar – 隐藏或显示文档窗口的菜单栏。默认：false（菜单栏已显示）。
- HideToolBar – 隐藏或显示文档窗口的工具栏。默认：false（工具栏已显示）。
- HideWindowUI – 隐藏或显示文档窗口元素，例如滚动条。默认：false（显示 UI 元素）。
- NonFullScreenPageMode – 文档在非全页模式下的显示方式。
- PageLayout – 页面布局。
- PageMode – 文档首次打开时的显示方式。选项包括显示缩略图、全屏、显示附件面板。

以下代码片段展示了如何使用获取属性 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类。

```python
import aspose.pdf as ap


def get_document_window(input_pdf, output_pdf):
    """Print document window metadata for inspection."""
    document = ap.Document(input_pdf)

    print("CenterWindow:", document.center_window)
    print("Direction:", document.direction)
    print("DisplayDocTitle:", document.display_doc_title)
    print("FitWindow:", document.fit_window)
    print("HideMenuBar:", document.hide_menubar)
    print("HideToolBar:", document.hide_tool_bar)
    print("HideWindowUI:", document.hide_window_ui)
    print("NonFullScreenPageMode:", document.non_full_screen_page_mode)
    print("PageLayout:", document.page_layout)
    print("PageMode:", document.page_mode)
```

### 设置文档窗口和页面显示属性

本主题说明如何设置文档窗口、查看器应用程序和页面显示的属性。要设置这些不同的属性：

1. 使用以下方式打开 PDF 文件 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类。
1. 设置 Document 对象的属性。
1. 使用 save 方法保存已更新的 PDF 文件。

可用的属性有：

- 居中窗口
- 方向
- 显示文档标题
- 适应窗口
- 隐藏菜单栏
- 隐藏工具栏
- 隐藏窗口UI
- 非全屏页面模式
- 页面布局
- 页面模式

每个都在下面的代码中使用并描述。以下 - 代码片段向您展示如何使用它设置属性。 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类。

```python
import aspose.pdf as ap


def set_document_window(input_pdf, output_pdf):
    """Set document window properties and save the result."""
    document = ap.Document(input_pdf)

    document.center_window = True
    document.direction = ap.Direction.R2L
    document.display_doc_title = True
    document.fit_window = True
    document.hide_menubar = True
    document.hide_tool_bar = True
    document.hide_window_ui = True
    document.non_full_screen_page_mode = ap.PageMode.USE_OC
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT
    document.page_mode = ap.PageMode.USE_THUMBS

    document.save(output_pdf)
```

### 嵌入标准 Type 1 字体

某些 PDF 文档使用来自特殊 Adobe 字体集的字体。该集合中的字体称为 “Standard Type 1 Fonts”。此集合包含 14 种字体，嵌入此类字体需要使用特殊标志，即 [嵌入标准字体](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties). 以下代码片段可用于获取一个将所有字体（包括标准 Type 1 字体）嵌入的文档：

```python
import aspose.pdf as ap


def embedded_fonts(input_pdf, output_pdf):
    """Ensure fonts in an existing PDF are embedded."""
    document = ap.Document(input_pdf)
    document.embed_standard_fonts = True

    for page in document.pages:
        if page.resources.fonts:
            for page_font in page.resources.fonts:
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### 在创建 PDF 时嵌入字体

如果您需要使用除 Adobe Reader 支持的 14 种核心字体之外的任何字体，则必须在生成 PDF 文件时嵌入字体描述。如果未嵌入字体信息，Adobe Reader 将从操作系统中获取（前提是系统已安装该字体），否则将根据 PDF 中的字体描述符构建替代字体。

>请注意，嵌入的字体必须安装在主机上，即在以下代码的情况下，‘Univers Condensed’ 字体已安装到系统中。

我们使用属性 'is_embedded' 将字体信息嵌入 PDF 文件。将此属性的值设为 'True' 将把完整的字体文件嵌入 PDF，尽管这会增加 PDF 文件的大小。以下是可用于将字体信息嵌入 PDF 的代码片段。

```python
import aspose.pdf as ap


def embedded_fonts_in_new_document(input_pdf, output_pdf):
    """Embed fonts while generating a document from scratch."""
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" This is a sample text using Custom font.")
    text_state = ap.text.TextState()
    text_state.font = ap.text.FontRepository.find_font("Arial")
    text_state.font.is_embedded = True
    segment.text_state = text_state
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    document.save(output_pdf)
```

### 在保存 PDF 时设置默认字体名称

当 PDF 文档包含的字体在文档本身和设备上都不可用时，API 会将这些字体替换为默认字体。如果字体是可用的（已安装在设备上或已嵌入文档中），则输出的 PDF 应该保持相同的字体（不应被替换为默认字体）。默认字体的值应包含字体名称（而不是字体文件的路径）。我们已经实现了在将文档保存为 PDF 时设置默认字体名称的功能。以下代码片段可用于设置默认字体：

```python
import aspose.pdf as ap


def set_default_font(input_pdf, output_pdf):
    """Assign a fallback font when saving a PDF."""
    document = ap.Document(input_pdf)

    save_options = ap.PdfSaveOptions()
    save_options.default_font_name = "Arial"
    document.save(output_pdf, save_options)
```

### 获取 PDF 文档中的所有字体

如果您想获取 PDF 文档中的所有字体，您可以使用 [字体实用工具](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 提供的方法在 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类。请检查以下代码片段，以获取现有 PDF 文档中的所有字体：

```python
import aspose.pdf as ap


def get_all_fonts(input_pdf, output_pdf):
    """Print all fonts referenced by a document."""
    document = ap.Document(input_pdf)
    for font in document.font_utilities.get_all_fonts():
        print(font.font_name)
```

### 使用 FontSubsetStrategy 改进字体嵌入

以下代码片段展示了如何设置 [字体子集策略](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/) 已使用 [字体实用工具](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 属性:

```python
import aspose.pdf as ap


def improve_fonts_embedding(input_pdf, output_pdf):
    """Apply different font subset strategies to reduce file size."""
    document = ap.Document(input_pdf)

    document.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    document.font_utilities.subset_fonts(
        ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY
    )

    document.save(output_pdf)
```

### 获取/设置 PDF 文件的缩放因子

有时，您想确定 PDF 文档的当前缩放比例是多少。使用 Aspose.Pdf，您可以查找当前值，也可以设置它。

这 [转到动作](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) 类 Destination 属性允许您获取与 PDF 文件关联的缩放值。同样，它可以用于设置文件的缩放因子。

#### 设置缩放因子

以下代码片段展示了如何设置 PDF 文件的缩放因子。

```python
import aspose.pdf as ap


def set_zoom_factor(input_pdf, output_pdf):
    """Set an initial zoom level via document open action."""
    document = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(
        ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5)
    )
    document.open_action = action
    document.save(output_pdf)
```

#### 获取缩放因子

下面的代码片段展示了如何获取 PDF 文件的缩放因子。

```python
import aspose.pdf as ap


def get_zoom_factor(input_pdf, output_pdf):
    """Print the zoom level configured in the document open action."""
    document = ap.Document(input_pdf)

    action = document.open_action
    if action and action.destination:
        print("Zoom:", action.destination.zoom)
    else:
        print("Zoom: not set")
```

## 相关文档主题

- [使用 Python 处理 PDF 文档](/pdf/zh/python-net/working-with-documents/)
- [在 Python 中创建 PDF 文件](/pdf/zh/python-net/create-pdf-document/)
- [在 Python 中操作 PDF 文档](/pdf/zh/python-net/manipulate-pdf-document/)
- [在 Python 中优化 PDF 文件](/pdf/zh/python-net/optimize-pdf/)
