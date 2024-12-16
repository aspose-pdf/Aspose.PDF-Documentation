---
title: 使用 Python 在 PDF 中添加图像印章
linktitle: PDF 文件中的图像印章
type: docs
weight: 10
url: /zh/python-net/image-stamps-in-pdf-page/
description: 使用 Aspose.PDF for Python 库的 ImageStamp 类在 PDF 文档中添加图像印章。
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "使用 Python 在 PDF 中添加图像印章",
    "alternativeHeadline": "使用 Python 在 PDF 中添加图像印章",
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
    "url": "/python-net/image-stamps-in-pdf-page/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/image-stamps-in-pdf-page/"
    },
    "dateModified": "2023-04-04",
    "description": "使用 Aspose.PDF for Python 库的 ImageStamp 类在 PDF 文档中添加图像印章。"
}
</script>


## 在 PDF 文件中添加图像印章

您可以使用 [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) 类向 PDF 文件添加图像印章。[ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) 类提供了创建基于图像的印章所需的属性，如高度、宽度、不透明度等。

要添加图像印章：

1. 使用所需属性创建一个 Document 对象和一个 ImageStamp 对象。
1. 调用 [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 类的 [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) 方法将印章添加到 PDF 中。

以下代码片段展示了如何在 PDF 文件中添加图像印章。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)

    # 创建图像印章
    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.background = True
    image_stamp.x_indent = 100
    image_stamp.y_indent = 100
    image_stamp.height = 300
    image_stamp.width = 300
    image_stamp.rotate = ap.Rotation.ON270
    image_stamp.opacity = 0.5
    # 将印章添加到特定页面
    document.pages[1].add_stamp(image_stamp)

    # 保存输出文档
    document.save(output_pdf)
```


## 控制添加图章时的图像质量

在将图像作为图章对象添加时，您可以控制图像的质量。[ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) 类的 [quality](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) 属性用于此目的。它表示图像的质量百分比（有效值为 0..100）。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)

    # 创建图像图章
    image_stamp = ap.ImageStamp(input_jpg)
    image_stamp.quality = 10
    # 将图章添加到特定页面
    document.pages[1].add_stamp(image_stamp)

    # 保存输出文档
    document.save(output_pdf)
```

## 浮动框中的背景图像图章

Aspose.PDF for Python API 允许您在浮动框中添加图像图章作为背景。
 [FloatingBox](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) 类的 [background](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) 属性可以用于为浮动框设置背景图像印章，如以下代码示例所示。

```python

    import aspose.pdf as ap

    # 实例化 Document 对象
    document = ap.Document()
    # 向 PDF 文档添加页面
    page = document.pages.add()
    # 创建 FloatingBox 对象
    box = ap.FloatingBox(200.0, 100.0)
    # 设置 FloatingBox 的左侧位置
    box.left = 40
    # 设置 FloatingBox 的顶部位置
    box.top = 80
    # 设置 FloatingBox 的水平对齐方式
    box.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # 向 FloatingBox 的段落集合中添加文本片段
    box.paragraphs.add(ap.text.TextFragment("main text"))
    # 设置 FloatingBox 的边框
    box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    img = ap.Image()
    img.file = input_image_file
    # 添加背景图像
    box.background_image = img
    # 设置 FloatingBox 的背景颜色
    box.background_color = ap.Color.yellow
    # 将 FloatingBox 添加到页面对象的段落集合中
    page.paragraphs.add(box)
    # 保存 PDF 文档
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