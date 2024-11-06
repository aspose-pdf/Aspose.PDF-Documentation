---
title: 使用 Python 处理 PDF 中的作品集
linktitle: 作品集
type: docs
weight: 20
url: zh/python-net/portfolio/
description: 如何使用 Python 创建 PDF 作品集。您应该使用 Microsoft Excel 文件、Word 文档和图像文件来创建 PDF 作品集。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "使用 Python 处理 PDF 中的作品集",
    "alternativeHeadline": "在 PDF 文档中创建作品集",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 文档生成",
    "keywords": "pdf, python, 作品集",
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
    "url": "/python-net/portfolio/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/portfolio/"
    },
    "dateModified": "2023-02-04",
    "description": "如何使用 Python 创建 PDF 作品集。您应该使用 Microsoft Excel 文件、Word 文档和图像文件来创建 PDF 作品集。"
}
</script>


创建一个 PDF 组合文档可以将不同类型的文件合并和存档为一个一致的文档。这样的文档可以包括文本文件、图像、电子表格、演示文稿和其他材料，确保所有相关材料存储和组织在一个地方。

PDF 组合文档将有助于以高质量的方式展示您的演示，无论您在哪里使用它。一般来说，创建 PDF 组合文档是一个非常现代的任务。

## 如何创建 PDF 组合文档

Aspose.PDF for Python via .NET 允许使用 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类创建 PDF 组合文档。在通过 [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) 类获取后，将文件添加到 document.collection 对象中。当文件添加完成后，使用 Document 类的 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法保存组合文档。

以下示例使用 Microsoft Excel 文件、Word 文档和图像文件创建一个 PDF 组合文档。

以下代码生成了如下投资组合。

### 使用 Aspose.PDF for Python 创建的 PDF 投资组合

![使用 Aspose.PDF for Python 创建的 PDF 投资组合](working-with-pdf-portfolio_1.jpg)

```python

    import aspose.pdf as ap

    # 实例化 Document 对象
    document = ap.Document()

    # 实例化文档 Collection 对象
    document.collection = ap.Collection()

    # 获取要添加到投资组合的文件
    excel = ap.FileSpecification(input_excel)
    word = ap.FileSpecification(input_doc)
    image = ap.FileSpecification(input_jpg)

    # 提供文件描述
    excel.description = "Excel 文件"
    word.description = "Word 文件"
    image.description = "图像文件"

    # 将文件添加到文档集合
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # 保存投资组合文档
    document.save(output_pdf)
```

## 从 PDF 投资组合中移除文件

为了从 PDF 投资组合中删除/移除文件，尝试使用以下代码行。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)
    document.collection.delete()

    # 保存更新的文件
    document.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python Library",
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
    "applicationCategory": "PDF Manipulation Library for Python",
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