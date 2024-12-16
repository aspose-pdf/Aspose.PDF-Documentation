---
title: 从 PDF 文件中删除图像使用 Python
linktitle: 删除图像
type: docs
weight: 20
url: /zh/python-net/delete-images-from-pdf-file/
description: 本节解释如何使用 Aspose.PDF for Python via .NET 从 PDF 文件中删除图像。
lastmod: "2023-04-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "从 PDF 文件中删除图像使用 Python",
    "alternativeHeadline": "如何从 PDF 中删除图像",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 文件生成",
    "keywords": "pdf, python, 删除, 从 pdf 中删除图像",
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
    "url": "/python-net/delete-images-from-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/delete-images-from-pdf-file/"
    },
    "dateModified": "2023-02-04",
    "description": "本节解释如何使用 Aspose.PDF for Python via .NET 从 PDF 文件中删除图像。"
}
</script>


有很多理由需要从 PDF 中删除所有或特定的图像。

有时，PDF 文件可能包含需要删除的重要图像，以保护隐私或防止未经授权访问某些信息。

删除不需要或冗余的图像可以帮助减少文件大小，从而更容易共享或存储 PDF。

如有必要，您可以通过删除文档中的所有图像来减少页数。此外，从文档中删除图像将有助于为 PDF 的压缩或提取文本信息做准备。

**Aspose.PDF for Python via .NET** 将帮助您完成此任务。

## 从 PDF 文件中删除图像

要从 PDF 文件中删除图像：

1. 打开现有的 PDF 文档。
2. 删除特定的图像。
3. 保存更新后的 PDF 文件。

以下代码片段展示了如何从 PDF 文件中删除图像。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_file)

    # 删除特定图像
    document.pages[2].resources.images.delete(1)

    # 保存更新后的 PDF 文件
    document.save(output_pdf)
```


## 从输入 PDF 中删除所有图像 

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_file)

    # 删除所有页面上的所有图像
    for i in range(len(document.pages)):
        while len(document.pages[i + 1].resources.images) != 0:
            document.pages[i + 1].resources.images.delete(1)

    # 保存更新后的 PDF 文件
    document.save(output_file)
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
    "applicationCategory": "PDF Manipulation Library for Python via .NET",
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