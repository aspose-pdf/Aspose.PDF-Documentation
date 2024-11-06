---
title: 使用 Python 更改 PDF 页面大小
linktitle: 更改 PDF 页面大小
type: docs
weight: 60
url: zh/python-net/change-page-size/
description: 使用 Aspose.PDF for Python via .NET 库更改 PDF 文档的页面大小。
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "使用 Python 更改 PDF 页面大小",
    "alternativeHeadline": "使用 Python 调整 PDF 页面大小",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 文档生成",
    "keywords": "pdf, python, 更改 pdf 大小, 调整 pdf 大小",
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
    "url": "/python-net/change-page-size/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/change-page-size/"
    },
    "dateModified": "2023-04-04",
    "description": "使用 Aspose.PDF for Python via .NET 库更改 PDF 文档的页面大小。"
}
</script>


## 更改 PDF 页面大小

通过 .NET 的 Aspose.PDF for Python 允许您在 Python 应用程序中使用简单的代码行更改 PDF 页面大小。本主题解释如何更新/更改现有 PDF 文件的页面尺寸（大小）。

[Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 类包含 [set_page_size()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) 方法，允许您设置页面大小。下面的代码片段通过几个简单的步骤更新页面尺寸：

1. 加载源 PDF 文件。
1. 将页面获取到 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 对象中。
1. 获取指定页面。
1. 调用 set_page_size() 方法更新其尺寸。
1. 调用 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类的 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法以生成更新页面尺寸的 PDF 文件。

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)

    # 获取特定页面
    page = document.pages[1]

    # 设置页面大小为 A4 (11.7 x 8.3 英寸)，在 Aspose.Pdf 中，1 英寸 = 72 点
    # 因此 A4 尺寸为 (842.4, 597.6) 点
    page.set_page_size(597.6, 842.4)

    # 保存更新的文档
    document.save(output_pdf)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET 库",
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
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>