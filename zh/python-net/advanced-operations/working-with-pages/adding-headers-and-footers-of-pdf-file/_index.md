---
title: 向 PDF 添加页眉和页脚使用 Python
linktitle: 向 PDF 添加页眉和页脚
type: docs
weight: 50
url: /zh/python-net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for Python via .NET 允许您使用 TextStamp 类向 PDF 文件添加页眉和页脚。
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "向 PDF 添加页眉和页脚使用 Python",
    "alternativeHeadline": "如何向 PDF 文件添加页眉和页脚",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 文档生成",
    "keywords": "pdf, python, 添加页眉, 添加页脚到 pdf",
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
    "url": "/python-net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for Python via .NET 允许您使用 TextStamp 类向 PDF 文件添加页眉和页脚。"
}
</script>


**Aspose.PDF for Python via .NET** 允许您在现有的 PDF 文件中添加页眉和页脚。您可以向 PDF 文档添加图像或文本。此外，还可以尝试在一个 PDF 文件中使用 Python 添加不同的页眉。

## 在 PDF 文件的页眉中添加文本

您可以使用 [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) 类在 PDF 文件的页眉中添加文本。TextStamp 类提供了创建基于文本的印章所需的属性，例如字体大小、字体样式和字体颜色等。为了在页眉中添加文本，您需要使用所需属性创建一个 Document 对象和一个 TextStamp 对象。之后，您可以调用 Page 的 'add_stamp' 方法将文本添加到 PDF 的页眉中。

您需要设置 [top_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) 属性，以便调整 PDF 页眉区域中的文本。您还需要将 'horizontal_alignment' 设置为 Center 并将 'vertical_alignment' 设置为 Top。

以下代码片段向您展示了如何使用 Python 在 PDF 文件的页眉中添加文本：

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)

    # 创建页眉
    textStamp = ap.TextStamp("Header Text")
    # 设置印章的属性
    textStamp.top_margin = 10
    textStamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    textStamp.vertical_alignment = ap.VerticalAlignment.TOP
    # 在所有页面上添加页眉
    for page in document.pages:
        page.add_stamp(textStamp)

    # 保存更新的文档
    document.save(output_pdf)
```

## 在 PDF 文件的页脚中添加文本

您可以使用 [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) 类在 PDF 文件的页脚中添加文本。
 TextStamp 类提供了创建基于文本的印章所需的属性，如字体大小、字体样式和字体颜色等。为了在页脚中添加文本，您需要使用所需属性创建一个 Document 对象和一个 TextStamp 对象。之后，您可以调用 Page 的 'add_stamp' 方法在 PDF 的页脚中添加文本。

以下代码片段展示了如何使用 Python 在 PDF 文件的页脚中添加文本：

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)
    # 创建页脚
    textStamp = ap.TextStamp("Footer Text")
    # 设置印章的属性
    textStamp.bottom_margin = 10
    textStamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    textStamp.vertical_alignment = ap.VerticalAlignment.BOTTOM
    # 在所有页面上添加页脚
    for page in document.pages:
        page.add_stamp(textStamp)

    # 保存更新的 PDF 文件
    document.save(output_pdf)
```

## 在 PDF 文件的页眉中添加图像

您可以使用 [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) 类在 PDF 文件的页眉中添加图像。 Image Stamp 类提供了创建基于图像的印章所需的属性，如字体大小、字体样式和字体颜色等。为了在页眉中添加图像，您需要创建一个 Document 对象和一个使用所需属性的 Image Stamp 对象。之后，您可以调用 Page 的 'add_stamp' 方法在 PDF 的页眉中添加图像。

下面的代码片段展示了如何使用 Python 在 PDF 文件的页眉中添加图像：

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)

    # 创建页眉
    image_stamp = ap.ImageStamp(input_image)
    # 设置印章的属性
    image_stamp.top_margin = 10
    image_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    image_stamp.vertical_alignment = ap.VerticalAlignment.TOP
    # 在所有页面上添加页眉
    for page in document.pages:
        page.add_stamp(image_stamp)

    # 保存更新后的文档
    document.save(output_pdf)
```

## 在 PDF 文件底部添加图像

您可以使用 [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) 类在 PDF 文件的页脚中添加图像。 [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) 类提供了创建基于图像的图章所需的属性，比如字体大小、字体样式和字体颜色等。为了在页脚中添加图像，你需要使用所需的属性创建一个 Document 对象和一个 Image Stamp 对象。之后，你可以调用 Page 的 'add_stamp' 方法在 PDF 的页脚中添加图像。

以下代码片段向你展示了如何使用 Python 在 PDF 文件的页脚中添加图像：

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)
    # 创建页脚
    image_stamp = ap.ImageStamp(input_image)
    # 设置图章的属性
    image_stamp.bottom_margin = 10
    image_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    image_stamp.vertical_alignment = ap.VerticalAlignment.BOTTOM
    # 在所有页面添加页脚
    for page in document.pages:
        page.add_stamp(image_stamp)

    # 保存更新后的 PDF 文件
    document.save(output_pdf)
```

## 在一个 PDF 文件中添加不同的页眉

我们知道可以通过使用 [top_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) 或 [bottom_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) 属性在文档的页眉/页脚部分添加 TextStamp，但有时我们可能需要在单个 PDF 文档中添加多个页眉/页脚。**通过 .NET 的 Aspose.PDF for Python** 解释了如何做到这一点。

为了实现此要求，我们将创建单独的 TextStamp 对象（对象的数量取决于所需的页眉/页脚数量），并将它们添加到 PDF 文档中。
 我们还可以为单个图章对象指定不同的格式信息。在以下示例中，我们创建了 Document 对象和三个 TextStamp 对象，然后使用 Page 的 'add_stamp' 方法在 PDF 的页眉部分添加文本。以下代码片段向您展示如何使用 Aspose.PDF for Python 在 PDF 文件的页脚中添加图像：

```python

    import aspose.pdf as ap

    # 创建三个图章
    stamp1 = ap.TextStamp("Header 1")
    stamp2 = ap.TextStamp("Header 2")
    stamp3 = ap.TextStamp("Header 3")

    # 设置图章对齐方式（将图章放在页面顶部，水平居中）
    stamp1.vertical_alignment = ap.VerticalAlignment.TOP
    stamp1.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # 指定字体样式为粗体
    stamp1.text_state.font_style = ap.text.FontStyles.BOLD
    # 设置文本前景色信息为红色
    stamp1.text_state.foreground_color = ap.Color.red
    # 指定字体大小为14
    stamp1.text_state.font_size = 14

    # 现在我们需要将第二个图章对象的垂直对齐方式设置为顶部
    stamp2.vertical_alignment = ap.VerticalAlignment.TOP
    # 设置图章的水平对齐信息为居中对齐
    stamp2.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # 设置图章对象的缩放因子
    stamp2.zoom = 10

    # 设置第三个图章对象的格式
    # 指定图章对象的垂直对齐信息为顶部
    stamp3.vertical_alignment = ap.VerticalAlignment.TOP
    # 设置图章对象的水平对齐信息为居中对齐
    stamp3.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # 设置图章对象的旋转角度
    stamp3.rotate_angle = 35
    # 设置图章的背景颜色为粉色
    stamp3.text_state.background_color = ap.Color.pink
    # 将图章的字体信息更改为 Verdana
    stamp3.text_state.font = ap.text.FontRepository.find_font("Verdana")
    # 第一个图章添加在第一页；
    document.pages[1].add_stamp(stamp1)
    # 第二个图章添加在第二页；
    document.pages[2].add_stamp(stamp2)
    # 第三个图章添加在第三页。
    document.pages[3].add_stamp(stamp3)

    # 保存更新的文档
    document.save(output_pdf)
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
    "applicationCategory": "PDF 操作库 for Python",
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