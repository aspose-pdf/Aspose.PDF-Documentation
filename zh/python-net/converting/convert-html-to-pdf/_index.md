---
title: 在 Python 中将 HTML 转换为 PDF
linktitle: 将 HTML 转换为 PDF 文件
type: docs
weight: 40
url: /zh/python-net/convert-html-to-pdf/
lastmod: "2025-09-27"
description: 学习如何使用 Aspose.PDF for Python via .NET 将 HTML 内容转换为 PDF 文档
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: 如何使用 Aspose.PDF for Python 将 HTML 转换为 PDF
Abstract: Aspose.PDF for Python via .NET 提供了一个强大的解决方案，可在应用程序中从网页和原始 HTML 代码创建 PDF 文件。本文章提供了使用 Python 将 HTML 转换为 PDF 的指南，概述了 Aspose.PDF for Python——一个 PDF 操作 API，能够实现 HTML 文档到 PDF 格式的无缝转换。转换过程可以根据需要进行自定义。文章包含了一个 Python 代码示例，演示了转换过程，包括创建 HtmlLoadOptions 类的实例、初始化 Document 对象，并使用 Document.Save() 方法保存输出的 PDF 文档。此外，Aspose 还提供了一个在线工具用于将 HTML 转换为 PDF，允许用户探索其功能和转换质量。
---

## Python HTML 转 PDF 转换

**Aspose.PDF for Python** 是一个 PDF 操作 API，可让您无缝将任何现有的 HTML 文档转换为 PDF。HTML 转 PDF 的过程可以灵活定制。

## 将 HTML 转换为 PDF

以下 Python 代码示例展示了如何将 HTML 文档转换为 PDF。

1. 创建 [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) 类的实例。
1. 初始化 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象。
1. 通过调用 **document.save()** 方法保存输出的 PDF 文档。

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.page_layout_option = ap.HtmlPageLayoutOption.SCALE_TO_PAGE_WIDTH
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**尝试在线将 HTML 转换为 PDF**

Aspose 为您提供在线免费应用程序 ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf)，您可以尝试了解其功能和质量。

[![Aspose.PDF 转换 HTML 到 PDF 使用免费应用](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## 使用媒体类型将 HTML 转换为 PDF

本例展示了如何使用 Aspose.PDF for Python via .NET 通过特定渲染选项将 HTML 文件转换为 PDF。

1. 创建 [HtmlLoadOptions()](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) 类的实例。'html_media_type' 应用针对屏幕显示的 CSS 规则。'html_media_type' 属性可以有多个值。您可以将其设置为 HtmlMediaType.SCREEN 或 HtmlMediaType.PRINT。
1. 使用加载选项将 HTML 加载到 ap.Document 中。
1. 将文档保存为 PDF。

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.html_media_type = ap.HtmlMediaType.SCREEN
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## 将 HTML 转换为 PDF 的优先级 CSS 页面规则

某些文档可能包含使用 [the Page rule](https://developer.mozilla.org/en-US/docs/Web/CSS/@page) 的布局设置，这在生成布局时可能导致歧义。您可以使用 'is_priority_css_page_rule' 属性来控制优先级。如果此属性设置为 'True'，则 CSS 规则会首先应用。

1. 创建 [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) 类的实例。
1. 将 'is_priority_css_page_rule = False' 设置为禁用对 @page CSS 规则的优先级，使其他样式占优。
1. 使用配置好的选项将 HTML 加载到 ap.Document 中。
1. 将文档保存为 PDF。

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    # load_options.is_priority_css_page_rule = False
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## 使用嵌入字体将 HTML 转换为 PDF

本例展示了在嵌入字体的情况下将 HTML 文件转换为 PDF。如果您需要带有嵌入字体的 PDF 文档，应该将 'is_embed_fonts' 设置为 True。

1. 创建 'HtmlLoadOptions()' 以配置 HTML 到 PDF 的转换。
1. 将 'is_embed_fonts = True' 设置为确保 HTML 中使用的所有字体直接嵌入 PDF，保持视觉保真度。
1. 使用这些选项将 HTML 加载到 ap.Document 中。
1. 将文档保存为 PDF。

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.is_embed_fonts = True
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## 在 HTML 转 PDF 转换期间将内容渲染在单页上

本例演示了如何使用 Aspose.PDF for Python 将 HTML 文件转换为单页 PDF。
您可以使用 'is_render_to_single_page' 属性将所有内容显示在一页上。

1. 创建 'HtmlLoadOptions()' 实例以配置转换过程。
1. 启用 'is_render_to_single_page' 将整个 HTML 内容渲染到单个连续的 PDF 页面上。
1. 使用配置好的选项将文档加载到 'ap.Document' 中。
1. 将结果保存为 PDF 文件。

```python
    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    options = ap.HtmlLoadOptions()
    options.is_render_to_single_page = True

    doc = ap.Document(path_infile, options)
    doc.save(path_outfile)
```

## 将 MHTML 转换为 PDF

此示例展示了如何使用 Aspose.PDF for Python 将 MHT (MHTML) 文件转换为 PDF 文档，并使用特定页面尺寸。

1. 创建 ap.MhtLoadOptions() 实例以配置 MHT 文件处理。
1. 设置各种参数，例如页面大小。
1. 使用输入文件和配置好的加载选项初始化文档。
1. 将生成的文档保存为 PDF。

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    load_options = ap.MhtLoadOptions()
    load_options.page_info.width = 842
    load_options.page_info.height= 1191
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```
