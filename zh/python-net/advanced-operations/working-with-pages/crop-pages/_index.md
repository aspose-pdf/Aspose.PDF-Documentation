---
title: 使用 Python 编程裁剪 PDF 页面
linktitle: 裁剪页面
type: docs
weight: 70
url: zh/python-net/crop-pages/
description: 您可以通过 Aspose.PDF for Python via .NET 获取页面属性，例如宽度、高度、出血框、裁剪框和修剪框。
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "使用 Python 编程裁剪 PDF 页面",
    "alternativeHeadline": "如何在 Python 中裁剪 PDF 页面",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 文档生成",
    "keywords": "pdf, python, 裁剪 pdf 页面",
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
    "url": "/python-net/crop-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/crop-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "您可以通过 Aspose.PDF for Python via .NET 获取页面属性，例如宽度、高度、出血框、裁剪框和修剪框。"
}
</script>


## 获取页面属性

PDF 文件中的每个页面都有许多属性，例如宽度、高度、出血框、裁剪框和裁切框。Aspose.PDF for Python 允许您访问这些属性。

- **media_box**: 媒体框是最大的页面框。它对应于打印到 PostScript 或 PDF 时选择的页面大小（例如 A4、A5、US Letter 等）。换句话说，媒体框决定了显示或打印 PDF 文档的介质的物理大小。
- **bleed_box**: 如果文档有出血，PDF 也会有一个出血框。出血是超出页面边缘的颜色（或艺术品）的量。它用于确保当文档打印并裁切到尺寸（“裁切”）时，墨水会一直延伸到页面边缘。即使页面被错剪 - 稍微偏离裁切标记 - 页面上也不会出现白边。
- **trim_box**: 裁切框指示文档在打印和裁切后的最终尺寸。
- **art_box**: 艺术框是在文档中绘制在页面实际内容周围的框。
 此页面框用于在其他应用程序中导入PDF文档。  
- **crop_box**: 裁剪框是您的PDF文档在Adobe Acrobat中显示的“页面”大小。在正常视图中，Adobe Acrobat中只显示裁剪框的内容。有关这些属性的详细描述，请阅读Adobe.Pdf规格，特别是10.10.1页面边界。

下面的代码片段展示了如何裁剪页面：

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)

    # 创建新的Box矩形
    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_pdf)
```

在此示例中，我们使用了一个示例文件[这里](crop_page.pdf)。最初，我们的页面看起来如图1所示。  
![图1. 裁剪后的页面](crop_page.png)

更改后，页面将如图2所示。
![图2. 裁剪页面](crop_page2.png)

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
    "applicationCategory": "Python的PDF操作库",
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