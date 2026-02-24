---
title: 在 Python 中将 PDF 转换为 HTML
linktitle: 将 PDF 转换为 HTML 格式
type: docs
weight: 50
url: /zh/python-net/convert-pdf-to-html/
lastmod: "2025-09-27"
description: 本主题向您展示如何使用 Aspose.PDF for Python via .NET 库将 PDF 文件转换为 HTML 格式。
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: 如何在 Python 中将 PDF 转换为 HTML
Abstract: 本文提供了使用 Python 将 PDF 文件转换为 HTML 的全面指南，特别是通过 Aspose.PDF for Python via .NET 库。它概述了以编程方式实现此转换的必要步骤，重点介绍了从源 PDF 创建 `Document` 对象以及使用 `HtmlSaveOptions` 将文档保存为 HTML 格式。文章包含了一个简洁的 Python 代码片段，演示转换过程。此外，文章还介绍了在线工具 Aspose.PDF 的 "PDF to HTML" 应用程序，供用户探索其功能和转换质量。本文结构涵盖了多个相关主题，确保对使用 Python 进行 PDF 到 HTML 转换有深入的了解。
---

## 将 PDF 转换为 HTML

**Aspose.PDF for Python via .NET** 提供了许多将各种文件格式转换为 PDF 文档以及将 PDF 文件转换为多种输出格式的功能。本文讨论如何将 PDF 文件转换为 <abbr title="HyperText Markup Language">HTML</abbr>。您只需几行 Python 代码即可将 PDF 转换为 HTML。如果您想创建网站或向在线论坛添加内容，可能需要将 PDF 转换为 HTML。使用 Python 以编程方式转换 PDF 为 HTML 是一种方法。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 HTML**

Aspose.PDF for Python 为您提供在线免费应用程序 ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)，您可以尝试了解其功能和效果。

[![Aspose.PDF Convertion PDF to HTML with Free App](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

步骤：在 Python 中将 PDF 转换为 HTML

1. 使用源 PDF 文档创建 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象的实例。
1. 通过调用 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法，将其保存为 [HtmlSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/)。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### 将 PDF 转换为 HTML 并将图像保存到指定文件夹

此函数使用 Aspose.PDF for Python via .NET 将 PDF 文件转换为 HTML 格式。所有提取的图像均存储在指定文件夹中，而不是嵌入到 HTML 文件中。

1. 配置 HTML 保存选项。
1. 将 HTML 保存为带有外部图像的文件。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.special_folder_for_all_images = self.data_dir
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### 将 PDF 转换为多页 HTML

此函数将 PDF 文件转换为多页 HTML，每个 PDF 页面导出为单独的 HTML 文件。这样可以更容易地浏览输出，并减少大型 PDF 的加载时间。

1. 使用 'ap.Document' 加载源 PDF。
1. 创建 'HtmlSaveOptions' 并设置 'split_into_pages'。
1. 将文档保存为 HTML，并将页面拆分为独立的文件。
1. 打印确认信息。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.split_into_pages = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### 将 PDF 转换为 HTML 并将 SVG 图像保存到指定文件夹

此函数将 PDF 转换为 HTML 格式，同时将所有图像以 SVG 文件形式存储在指定文件夹中，而不是直接嵌入到 HTML 中。

1. 使用 'ap.Document' 加载源 PDF。
1. 创建 'HtmlSaveOptions' 并将 'special_folder_for_svg_images' 设置为目标文件夹。
1. 将文档保存为带有外部 SVG 图像的 HTML。
1. 打印确认信息。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.special_folder_for_svg_images = self.data_dir
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### 将 PDF 转换为 HTML 并保存压缩的 SVG 图像

此代码段将 PDF 转换为 HTML 格式，将所有图像以 SVG 文件存储在指定文件夹中，并进行压缩以减小文件大小。

1. 使用 'ap.Document' 加载 PDF 文档。
1. 创建 'HtmlSaveOptions' 并：
- 设置 'special_folder_for_svg_images' 以在外部存储 SVG 图像。
- 启用 'compress_svg_graphics_if_any' 以压缩 SVG 图像。
1. 将文档保存为带有压缩外部 SVG 图像的 HTML。
1. 打印确认信息。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.special_folder_for_svg_images = self.data_dir
    save_options.compress_svg_graphics_if_any = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### 将 PDF 转换为 HTML 并控制嵌入的光栅图像

此代码段将 PDF 转换为 HTML 格式，将光栅图像嵌入为 PNG 页面背景。这种方法保持了图像质量和 HTML 中的页面布局。

1. 使用 'ap.Document' 加载 PDF 文档。
1. 创建 'HtmlSaveOptions' 并将 'raster_images_saving_mode' 设置为 'AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND'。
1. 将文档保存为嵌入栅格图像的 HTML。
1. 打印确认信息。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.raster_images_saving_mode = apdf.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### 将 PDF 转换为仅正文内容的 HTML 页面

此函数将 PDF 转换为 HTML 格式，生成仅包含 'body' 内容的页面，不包含额外的 'html' 或 'head' 标签，并将输出拆分为多个页面。

1. 使用 'ap.Document' 加载 PDF 文档。
1. 创建 'HtmlSaveOptions' 并进行配置：
- 将 'html_markup_generation_mode = WRITE_ONLY_BODY_CONTENT' 设置为仅生成 'body' 内容。
- 设置 'split_into_pages' 以为每个 PDF 页面创建单独的 HTML 文件。
1. 使用指定选项将文档保存为 HTML。
1. 打印确认信息。

```python

from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.html_markup_generation_mode = apdf.HtmlSaveOptions.HtmlMarkupGenerationModes.WRITE_ONLY_BODY_CONTENT
    save_options.split_into_pages = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### 将 PDF 转换为带透明文本渲染的 HTML

此函数将 PDF 转换为 HTML 格式，将所有文本（包括带阴影的文本）渲染为透明，从而在保持视觉真实感的同时，允许在输出 HTML 中进行灵活的样式设置。

1. 使用 'ap.Document' 加载 PDF 文档。
1. 创建 'HtmlSaveOptions' 并进行配置：
- 将 'save_transparent_texts' 设置为将普通文本渲染为透明。
- 将 'save_shadowed_texts_as_transparent_texts' 设置为将带阴影的文本渲染为透明。
1. 使用透明文本渲染将文档保存为 HTML。
1. 打印确认信息。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.save_transparent_texts = True
    save_options.save_shadowed_texts_as_transparent_texts = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### 将 PDF 转换为带文档层渲染的 HTML

此函数将 PDF 转换为 HTML 格式，通过将标记内容转换为输出 HTML 中的独立层来保留文档层。这样可以准确渲染层叠元素（如注释、背景和叠加层）。

1. 使用 'ap.Document' 加载 PDF 文档。
1. 创建 'HtmlSaveOptions' 并启用 'convert_marked_content_to_layers' 以保留层。
1. 将文档保存为带层内容的 HTML。
1. 打印确认信息。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.convert_marked_content_to_layers  = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```


