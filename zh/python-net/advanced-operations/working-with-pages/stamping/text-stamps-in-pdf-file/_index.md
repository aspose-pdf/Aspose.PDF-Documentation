---
title: 在 PDF 中添加文字印章通过 Python
linktitle: PDF 文件中的文字印章
type: docs
weight: 20
url: zh/python-net/text-stamps-in-the-pdf-file/
description: 使用 Aspose.PDF for Python 库的 TextStamp 类向 PDF 文档添加文字印章。
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "在 PDF 中添加文字印章通过 Python",
    "alternativeHeadline": "在 PDF 中添加文字印章通过 Python",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, document generation",
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
    "url": "/python-net/text-stamps-in-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/text-stamps-in-the-pdf-file/"
    },
    "dateModified": "2023-04-04",
    "description": "使用 Aspose.PDF for Python 库的 TextStamp 类向 PDF 文档添加文字印章。"
}
</script>


## 使用 Python 添加文字印章

您可以使用 [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) 类在 PDF 文件中添加文字印章。[TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) 类提供了创建基于文本的印章所需的属性，例如字体大小、字体样式和字体颜色等。为了添加文字印章，您需要使用所需的属性创建一个 Document 对象和一个 TextStamp 对象。之后，您可以调用 Page 的 [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) 方法在 PDF 中添加印章。以下代码片段向您展示了如何在 PDF 文件中添加文字印章。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)

    # 创建文字印章
    text_stamp = ap.TextStamp("Sample Stamp")
    # 设置印章是否为背景
    text_stamp.background = True
    # 设置起始位置
    text_stamp.x_indent = 100
    text_stamp.y_indent = 100
    # 旋转印章
    text_stamp.rotate = ap.Rotation.ON90
    # 设置文本属性
    text_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_stamp.text_state.font_size = 14.0
    text_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    text_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    text_stamp.text_state.foreground_color = ap.Color.aqua
    # 将印章添加到特定页面
    document.pages[1].add_stamp(text_stamp)

    # 保存输出文档
    document.save(output_pdf)
```


## 为 TextStamp 对象定义对齐方式

在 PDF 文档中添加水印是经常需要的功能之一，Aspose.PDF for Python 完全能够添加图像和文本水印。我们有一个名为 [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) 的类，它提供了在 PDF 文件上添加文本印章的功能。最近有一个需求是支持在使用 TextStamp 对象时指定文本对齐方式的功能。因此，为了满足这一需求，我们在 [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) 类中引入了 [text_alignment](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) 属性。使用此属性，我们可以指定 [horizontal_alignment](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) 文本对齐方式。

以下代码片段展示了如何加载现有 PDF 文档并在其上添加 TextStamp 的示例。

```python

    import aspose.pdf as ap

    # 用输入文件实例化 Document 对象
    doc = ap.Document(input_pdf)
    # 用示例字符串实例化 FormattedText 对象
    text = ap.facades.FormattedText("This")
    # 向 FormattedText 添加新文本行
    text.add_new_line_text("is sample")
    text.add_new_line_text("Center Aligned")
    text.add_new_line_text("TextStamp")
    text.add_new_line_text("Object")
    # 使用 FormattedText 创建 TextStamp 对象
    stamp = ap.TextStamp(text)
    # 指定文本印章的水平对齐方式为居中对齐
    stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # 指定文本印章的垂直对齐方式为居中对齐
    stamp.vertical_alignment = ap.VerticalAlignment.CENTER
    # 指定 TextStamp 的文本水平对齐方式为居中对齐
    stamp.text_alignment = ap.HorizontalAlignment.CENTER
    # 设置印章对象的上边距
    stamp.top_margin = 20
    # 在文档的第一页上添加印章对象
    doc.pages[1].add_stamp(stamp)

    # 保存更新后的文档
    doc.save(output_pdf)
```


## 在 PDF 文件中填充描边文本作为印章

我们已经实现了在文本添加和编辑场景中设置渲染模式。要渲染描边文本，请创建 TextState 对象以传递高级属性。为描边设置颜色。之后，设置文本渲染模式，下一步是绑定 TextState，并添加印章。

以下代码片段演示了如何添加填充描边文本：

```python

    import aspose.pdf as ap

    # 创建 TextState 对象以传递高级属性
    ts = ap.text.TextState()
    # 为描边设置颜色
    ts.stroking_color = ap.Color.gray
    # 设置文本渲染模式
    ts.rendering_mode = ap.text.TextRenderingMode.STROKE_TEXT
    # 加载输入 PDF 文档
    file_stamp = ap.facades.PdfFileStamp(ap.Document(input_pdf))

    stamp = ap.facades.Stamp()
    stamp.bind_logo(
        ap.facades.FormattedText(
            "PAID IN FULL",
            ap.facades.FontColor(100, 100, 100),
            ap.facades.FontStyle.TIMES_ROMAN,
            ap.facades.EncodingType.WINANSI,
            True,
            78.0,
        )
    )

    # 绑定 TextState
    stamp.bind_text_state(ts)
    # 设置 X,Y 原点
    stamp.set_origin(100, 100)
    stamp.opacity = 5
    stamp.blending_space = ap.facades.BlendingColorSpace.DEVICE_RGB
    stamp.rotation = 45.0
    stamp.is_background = False
    # 添加印章
    file_stamp.add_stamp(stamp)
    file_stamp.save(output_pdf)
    file_stamp.close()
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
                "contactType": "销售",
                "areaServed": "美国",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "销售",
                "areaServed": "英国",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "销售",
                "areaServed": "澳大利亚",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Python 的 PDF 操作库",
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