---
title: 使用 Python 向 PDF 添加图像
linktitle: 添加图像
type: docs
weight: 10
url: /zh/python-net/add-image-to-existing-pdf-file/
description: 本节介绍如何使用 Python 库向现有 PDF 文件添加图像。
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "使用 Python 向 PDF 添加图像",
    "alternativeHeadline": "如何向 PDF 添加图像",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, 向 pdf 添加图像",
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
    "url": "/python-net/add-image-to-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-image-to-existing-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "本节介绍如何使用 Python 库向现有 PDF 文件添加图像。"
}
</script>


## 在现有 PDF 文件中添加图像

以下代码片段展示了如何在 PDF 文件中添加图像。

1. 加载输入 PDF 文件。
1. 指定将放置图片的页码。
1. 要在页面上定义图像的位置，请调用 [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 类的 [add_image](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) 方法。
1. 调用 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类的 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_file)

    document.pages[1].add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))

    document.save(output_pdf)
```

## 在现有 PDF 文件中添加图像（简化方式）

还有另一种替代的、更简单的方法来向 PDF 文件添加图像。
 你可以使用 [PdfFileMend](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/) 类的 [AddImage](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/methods/addimage/index) 方法。[add_image()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/#methods) 方法需要添加的图像、需要添加图像的页码和坐标信息。之后，保存更新后的 PDF 文件，并使用 [close()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/#methods) 方法关闭 PdfFileMend 对象。下面的代码片段展示了如何在现有的 PDF 文件中添加图像。

```python

    import aspose.pdf as ap

    # 打开文档
    mender = ap.facades.PdfFileMend()

    # 创建 PdfFileMend 对象以添加文本
    mender.bind_pdf(input_file)

    # 在 PDF 文件中添加图像
    mender.add_image(image_file, 1, 100.0, 600.0, 200.0, 700.0)

    # 保存更改
    mender.save(output_pdf)

    # 关闭 PdfFileMend 对象
    mender.close()

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
    "applicationCategory": "用于 Python 的 PDF 操作库",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>