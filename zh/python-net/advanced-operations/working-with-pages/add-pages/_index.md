---
title: 在 PDF 中添加页面与 Python
linktitle: 添加页面
type: docs
weight: 10
url: zh/python-net/add-pages/
description: 本文介绍如何在 PDF 文件的所需位置插入（添加）页面。了解如何使用 C# 移动、删除（删除）PDF 文件中的页面。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "在 PDF 中添加页面与 Python",
    "alternativeHeadline": "如何在 PDF 文档中添加页面",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 文档生成",
    "keywords": "pdf, python, 添加 pdf 页面, 插入 pdf 页面",
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
    "url": "/python-net/add-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "本文介绍如何在 PDF 文件的所需位置插入（添加）页面。了解如何使用 Python 移动、删除（删除）PDF 文件中的页面。"
}
</script>


Aspose.PDF for Python via .NET API 提供了使用 Python 操作 PDF 文档页面的完全灵活性。它将 PDF 文档的所有页面保存在 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 中，可以用于处理 PDF 页面。  
Aspose.PDF for Python via .NET 允许您在文件中的任何位置插入页面到 PDF 文档中，也可以在 PDF 文件的末尾添加页面。  
本节展示了如何使用 Python 向 PDF 添加页面。

## 在 PDF 文件中添加或插入页面

Aspose.PDF for Python via .NET 允许您在文件中的任何位置插入页面到 PDF 文档中，也可以在 PDF 文件的末尾添加页面。

### 在 PDF 文件的指定位置插入空白页面

要在 PDF 文件中插入空白页面：

1. 使用输入 PDF 文件创建一个 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类对象。  

1. 使用指定索引调用[PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)集合的[insert](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection/methods/insert)方法。
1. 使用[save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)方法保存输出PDF。

以下代码片段向您展示了如何在PDF文件中插入页面。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)
    # 在PDF中插入一个空页面
    document.pages.insert(2)
    # 保存输出文件
    document.save(output_pdf)
```

### 在PDF文件末尾添加一个空页面

有时，您希望确保文档以空页面结尾。本主题解释了如何在PDF文档末尾插入一个空页面。

要在PDF文件末尾插入一个空页面：

1. 使用输入PDF文件创建一个[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)类对象。

1. 调用 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 集合的 [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) 方法，不带任何参数。
1. 使用 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法保存输出 PDF。

以下代码片段向您展示如何在 PDF 文件的末尾插入一个空页面。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)

    # 在 PDF 文件的末尾插入一个空页面
    document.pages.add()

    # 保存输出文件
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
    "applicationCategory": "PDF Manipulation Library for Python",
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