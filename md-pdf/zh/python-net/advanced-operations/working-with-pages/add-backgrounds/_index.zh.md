---
title: 使用 Python 添加背景到 PDF
linktitle: 添加背景
type: docs
weight: 20
url: /python-net/add-backgrounds/
description: 使用 Python 向您的 PDF 文件添加背景图像。使用 BackgroundArtifact 类。
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "使用 Python 添加背景到 PDF",
    "alternativeHeadline": "在 PDF 中处理背景",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 文档生成",
    "keywords": "pdf, python, pdf 中的背景",
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
    "url": "/python-net/add-backgrounds/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-backgrounds/"
    },
    "dateModified": "2022-02-04",
    "description": "使用 Python 向您的 PDF 文件添加背景图像。使用 BackgroundArtifact 对象。"
}
</script>


背景图像可以用于为文档添加水印或其他细微设计。在通过 .NET 的 Aspose.PDF for Python 中，每个 PDF 文档是一个页面集合，每个页面包含一个工件集合。[BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/) 类可以用于向页面对象添加背景图像。

以下代码片段展示了如何使用 BackgroundArtifact 对象通过 Python 向 PDF 页面添加背景图像。

```python

    import aspose.pdf as ap

    # 创建一个新的 Document 对象
    document = ap.Document()

    # 向 document 对象添加新页面
    page = document.pages.add()

    # 创建 Background Artifact 对象
    background = ap.BackgroundArtifact()

    # 为 backgroundartifact 对象指定图像
    background.background_image = io.FileIO(input_image_file)

    # 将 backgroundartifact 添加到页面的工件集合中
    page.artifacts.append(background)

    # 保存文档
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
    "applicationCategory": "Python 的PDF操作库",
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