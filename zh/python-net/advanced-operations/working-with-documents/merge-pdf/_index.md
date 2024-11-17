---
title: 如何使用 Python 合并 PDF
linktitle: 合并 PDF 文件
type: docs
weight: 50
url: /zh/python-net/merge-pdf-documents/
description: 本页面说明如何使用 Python 将 PDF 文档合并为一个单一的 PDF 文件。
lastmod: "2023-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "如何使用 Python 合并 PDF",
    "alternativeHeadline": "通过 Python 组合 PDF 文档",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 文档操作",
    "keywords": "pdf, python, 合并 pdf, 连接, 组合 pdf",
    "wordcount": "212",
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
    "url": "https://docs.aspose.com/pdf/python-net/merge-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://docs.aspose.com/pdf/python-net/merge-pdf-documents/"
    },
    "dateModified": "2023-04-14",
    "description": "本页面说明如何通过 .NET 使用 Python 将 PDF 文档合并为一个单一的 PDF 文件。"
}
</script>


## 合并或组合多个PDF为单个PDF在Python中

合并PDF文件是用户中非常流行的查询。当您有多个PDF文件想要作为一个文档共享或存储在一起时，这会很有用。

合并PDF文件可以帮助您整理文件，在您的电脑上腾出存储空间，并通过将多个PDF文件组合成一个文档来与他人分享。

在不使用第三方库的情况下，通过.NET在Python中合并PDF文件并不是一项简单的任务。
本文展示了如何使用Aspose.PDF for Python via .NET将多个PDF文件合并为一个PDF文档。

## 使用Python和DOM合并PDF文件

要连接两个PDF文件：

1. 创建两个[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)对象，每个对象包含一个输入的PDF文件。

1. 然后为您想要添加其他 PDF 文件的 Document 对象调用 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 集合的 [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) 方法。
1. 将第二个 Document 对象的 PageCollection 集合传递给第一个 PageCollection 集合的 [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) 方法。
1. 最后，使用 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法保存输出 PDF 文件。

以下代码片段展示了如何连接 PDF 文件。

```python

    import aspose.pdf as ap

    # 打开第一个文档
    document1 = ap.Document(input_pdf_1)
    # 打开第二个文档
    document2 = ap.Document(input_pdf_2)

    # 将第二个文档的页面添加到第一个文档
    document1.pages.add(document2.pages)

    # 保存连接后的输出文件
    document1.save(output_pdf)
```


## 实例演示

[Aspose.PDF 合并工具](https://products.aspose.app/pdf/merger) 是一个免费的在线网络应用程序，允许您研究演示合并功能的工作原理。

[![Aspose.PDF 合并工具](merger.png)](https://products.aspose.app/pdf/merger)

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