---
title: 在 Python 中搜索并提取 PDF 文本
linktitle: 搜索并获取文本
type: docs
weight: 60
url: /zh/python-net/search-and-get-text-from-pdf/
description: 了解如何在 Python 中搜索、检查和提取 PDF 文档中的文本。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中搜索 PDF 文本并检查提取的片段
Abstract: 本文说明了如何使用 Aspose.PDF for Python via .NET 对 PDF 文档进行搜索和提取文本。它涵盖了 `TextAbsorber` 和 `TextFragmentAbsorber`，包括基于区域的提取、特定页面的搜索、短语匹配，以及对文本位置和字体属性的检查。
---

## 从 PDF 中搜索文本

使用 … 在 PDF 文档中搜索并提取定义的矩形区域的文本 `TextAbsorber` 类。它使用纯文本格式模式，以获得干净、未格式化的输出，这对于从结构化区域（如页眉、页脚或表格区域）提取内容非常有用。通过组合 `TextExtractionOptions` 和 `TextSearchOptions` 使用矩形约束，您可以控制文本的提取位置和方式。

当您需要审计 PDF 文本内容、提取用于分析的文本，或检查匹配文本片段的位置和格式时，请使用此页面。

1. 使用 'ap.Document' 加载 PDF 文件。
1. 配置文本提取选项。
1. 使用矩形约束定义搜索区域。
1. 创建并配置 TextAbsorber。
1. 处理文档中的所有页面。
1. 检索并显示提取的文本。

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_absorber_search(input_file_path):
    # Open PDF document
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Process all pages
    document.pages.accept(absorber)

    print(f"Text fragments found: {absorber.text}")
```

## 从特定 PDF 页面搜索文本

使用 Aspose.PDF 的 TextAbsorber 在 PDF 中搜索并提取特定页面和区域的文本。它针对文档的第 2 页，只提取在定义的矩形区域内找到的文本。
通过结合 TextExtractionOptions（用于格式控制）和 TextSearchOptions（用于区域限制），您可以高效地执行精确的、针对特定页面的文本提取。

1. 加载 PDF 文档。
1. 设置文本提取选项。
1. 将文本提取限制在页面的特定矩形区域。
1. 创建并配置 TextAbsorber。
1. 处理特定页面。
1. 检索并显示提取的文本。

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_absorber_search_page(input_file_path):
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Only page 2
    document.pages[2].accept(absorber)

    print(f"Text fragments found: {absorber.text}")
```

## 分析并提取 PDF 中的详细文本片段属性

与提取原始文本的 TextAbsorber 不同，TextFragmentAbsorber 提供关于每个文本片段的详细低层信息——例如其位置、字体属性、颜色以及嵌入细节。

1. 加载 PDF 文档。
1. 初始化 TextFragmentAbsorber。
1. 处理文档中的所有页面。
1. 遍历提取的文本片段。
1. 打印基本文本信息。
1. 打印字体和格式详情。

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    document.pages.accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
        print("XIndent:", fragment.position.x_indent)
        print("YIndent:", fragment.position.y_indent)
        print("Font - Name:", fragment.text_state.font.font_name)
        print("Font - IsAccessible:", fragment.text_state.font.is_accessible)
        print("Font - IsEmbedded:", fragment.text_state.font.is_embedded)
        print("Font - IsSubset:", fragment.text_state.font.is_subset)
        print("Font Size:", fragment.text_state.font_size)
        print("Foreground Color:", fragment.text_state.foreground_color)
```

## 在单个 PDF 页面上搜索特定文本短语

使用 TextFragmentAbsorber 在 PDF 文档的单页中搜索特定文本短语。不同于搜索整个文档，这种方法仅限制在单页内进行搜索，从而更高效地确认文本在诸如页眉、页脚或特定内容区域等目标区域中的存在和位置。

1. 加载 PDF 文档。
1. 使用搜索短语初始化 TextFragmentAbsorber。
1. 将 Absorber 应用于特定页面。
1. 遍历找到的片段。

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_page(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale")
    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## 逐页顺序文本搜索及累计结果

使用 Aspose.PDF 的 TextFragmentAbsorber 在 PDF 文档的多页中逐步搜索文本。
不同于单页或全文件搜索，这种方法允许您按顺序处理页面，逐步收集结果，并在页面特定的上下文中分析文本片段。此方法非常适合大型文档或渐进式处理工作流。

1. 加载 PDF 文档。
1. 初始化 TextFragmentAbsorber 并设置搜索短语。
1. 处理首页。仅搜索第 1 页。打印文本、页码和位置。提供单独的页面特定结果以确保清晰。
1. 顺序处理下一页。转到第2页，并可选择继续处理文档的其余部分。\u0027absorber.visit()\u0027 确保累积所有已访问页面的结果。打印累计的搜索结果，显示文本和位置。

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_sequential_search(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.phrase = "whale"

    # First page
    document.pages[1].accept(absorber)
    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)

    print("--")

    # Continue to next page
    document.pages[2].accept(absorber)
    absorber.visit(document)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)
```

## 在矩形区域内的目标短语搜索

在 PDF 中搜索特定短语，同时将搜索限制在单页的特定矩形区域内。
通过将短语搜索与空间约束相结合，您可以在指定区域精确定位内容，而无需扫描整页或整份文档。这对于表单、页眉、页脚或内容出现在可预测位置的结构化报告尤为有用。

1. 加载 PDF 文档。
1. 使用 Phrase 和 Rectangular Constraints 初始化 TextFragmentAbsorber
1. 将吸收器应用于第2页。将处理限制在第2页，以减少不必要的计算。确保搜索针对特定页面。
1. 遍历找到的片段并打印

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_phrase(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        "elephant", ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## 使用正则表达式在 PDF 中进行文本模式搜索

使用正则表达式在 PDF 中搜索文本模式。通过在 TextFragmentAbsorber 中启用正则模式，您可以定位诸如数字、日期、价格、坐标或自定义文本格式等复杂模式。该函数将搜索限制在特定页面上，使针对结构化数据的提取更高效。

1. 加载 PDF 文档。
1. 使用正则表达式模式初始化 TextFragmentAbsorber。
1. 将吸收器应用于第2页。为提高效率和精确度，将搜索限制在第2页。仅分析此页上的文本。
1. 遍历已找到的片段。打印匹配的文本片段及其坐标。为提取的模式提供精确的位置信息。

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_regex(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        r"\d+\.\d+", ap.text.TextSearchOptions(is_regular_expression_used=True)
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## 使用 TextFragmentAbsorber 将文本匹配转换为 PDF 超链接

在 PDF 中搜索特定的文本短语并将其转换为可点击的超链接。使用带有正则表达式模式的 TextFragmentAbsorber，它定位目标词并应用视觉样式（颜色和下划线）以及交互式链接。

1. 加载 PDF 文档。
1. 使用正则表达式模式初始化 TextFragmentAbsorber。
1. 将 Absorber 应用于第 1 页。
1. 为匹配项设置样式并添加超链接。
1. 保存已修改的 PDF。

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_and_add_hyperlink(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale|elephant")
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        fragment.text_state.foreground_color = ap.Color.blue
        fragment.text_state.underline = True
        fragment.hyperlink = ap.WebHyperlink(
            f"https://en.wikipedia.org/wiki/{fragment.text}"
        )

    output = input_file_path.replace("in.pdf", "out.pdf")
    document.save(output)
```

## 使用 TextFragmentAbsorber 在 PDF 中搜索和识别样式化文本

在 PDF 中基于格式属性而不是内容搜索文本片段。使用 TextFragmentAbsorber，它可以识别具有特定样式的文本，例如粗体文本。

1. 加载 PDF 文档。
1. 初始化 TextFragmentAbsorber。
1. 将 Absorber 应用于第 1 页。
1. 根据格式检查文本片段。检查字体样式是否为粗体。

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_styled_text(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.font_style == ap.text.FontStyles.BOLD:
            print(f"Bold: {fragment.text}")
        if fragment.text_state.invisible:
            print(f"Invisible: {fragment.text}")
```

## PDF 页面中的可视文本高亮

此功能将文本识别与渲染合并为单一工作流程。它不仅提取文本，还通过在每页的 PNG 图像上用彩色矩形高亮显示片段、段落和字符来可视化它们。

我们的示例通过以下方式对 PDF 执行高级文本可视化：

- 使用正则表达式搜索所有可见的文本片段
- 将每个 PDF 页面渲染为高分辨率 PNG 图像
- 在文本片段、文本段以及单个字符周围绘制彩色矩形

1. 设置输出图像分辨率。每个 PDF 页面均转换为 150 DPI 的 PNG 图像。
1. 打开 PDF 并初始化 Text Absorber。
1. 处理每一页。将吸收器应用于每一页。收集所有检测到的文本片段及其几何位置。
1. 将页面转换为 PNG 流。
1. 为绘图准备图形对象。
1. 应用坐标变换。将 PDF 坐标转换为图像像素。
1. 为文本元素绘制矩形。
1. 保存结果。

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_and_highlight(infile):
    resolution = 150
    png_device = ap.devices.PngDevice(ap.devices.Resolution(resolution, resolution))

    # Open PDF document
    document = ap.Document(infile)
    absorber = ap.text.TextFragmentAbsorber(r"[\S]+")
    absorber.text_search_options.is_regular_expression_used = True

    for page in document.pages:
        page.accept(absorber)
        stream = io.BytesIO()
        png_device.process(page, stream)
        with drawing.Bitmap.from_stream(stream) as bmp:
            with drawing.Graphics.from_image(bmp) as gr:
                scale = resolution / 72
                gr.transform = drawing.drawing2d.Matrix(
                    float(scale),
                    float(0),
                    float(0),
                    float(-scale),
                    float(0),
                    float(bmp.height),
                )
                text_fragment_collection = absorber.text_fragments
                # Loop through the fragments
                for text_fragment in text_fragment_collection:
                    gr.draw_rectangle(
                        drawing.Pens.yellow,
                        float(text_fragment.position.x_indent),
                        float(text_fragment.position.y_indent),
                        float(text_fragment.rectangle.width),
                        float(text_fragment.rectangle.height),
                    )
                    for seg_num in range(1, len(text_fragment.segments) + 1):
                        segment = text_fragment.segments[seg_num]
                        for char_num in range(1, len(segment.characters) + 1):
                            character_info = segment.characters[char_num]
                            rect = page.get_page_rect(True)
                            print(
                                f"TextFragment = {text_fragment.text}"
                                + f" Page URY = {rect.ury}"
                                + f" TextFragment URY = {text_fragment.rectangle.ury}"
                            )
                            gr.draw_rectangle(
                                drawing.Pens.black,
                                float(character_info.rectangle.llx),
                                float(character_info.rectangle.lly),
                                float(character_info.rectangle.width),
                                float(character_info.rectangle.height),
                            )
                        gr.draw_rectangle(
                            drawing.Pens.green,
                            float(segment.rectangle.llx),
                            float(segment.rectangle.lly),
                            float(segment.rectangle.width),
                            float(segment.rectangle.height),
                        )

                # Save result
                bmp.save(
                    infile.replace("_in.pdf", str(page.number) + "_out.png"),
                    drawing.imaging.ImageFormat.png,
                )
```

## 相关文本主题

- [使用 Python 在 PDF 中处理文本](/pdf/zh/python-net/working-with-text/)
- [通过 Python 替换 PDF 中的文本](/pdf/zh/python-net/replace-text-in-pdf/)
- [在 Python 中为 PDF 文本添加工具提示](/pdf/zh/python-net/pdf-tooltip/)
- [向 PDF 添加文本](/pdf/zh/python-net/add-text-to-pdf-file/)