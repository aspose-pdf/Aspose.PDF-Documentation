---
title: 如何使用 Python 创建 PDF
linktitle: 创建 PDF 文档
type: docs
weight: 10
url: zh/python-net/create-pdf-document/
description: 使用 Aspose.PDF for Python via .NET 创建和格式化 PDF 文档。
lastmod: "2023-04-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "如何使用 Python 创建 PDF",
    "alternativeHeadline": "通过 Python 从头创建 PDF 文档",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 文档生成",
    "keywords": "pdf, python, dotnet, 创建 pdf 文档",
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
    "url": "/python-net/create-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/create-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "使用 Aspose.PDF for Python via .NET 创建和格式化 PDF 文档。"
}
</script>


**Aspose.PDF for Python via .NET** 是一个 PDF 操作 API，允许开发人员通过 .NET 应用程序使用 Python 直接创建、加载、修改和转换 PDF 文件，只需几行代码。

## 如何创建简单的 PDF 文件

要使用 Aspose.PDF 通过 .NET 使用 Python 创建 PDF，可以按照以下步骤操作：

1. 创建 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类的对象
1. 向 Document 对象的 [pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 集合中添加一个 [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 对象
1. 向页面的 [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 集合中添加 [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)
1. 保存生成的 PDF 文档

```python

    import aspose.pdf as ap

    # 初始化文档对象
    document = ap.Document()
    # 添加页面
    page = document.pages.add()
    # 向新页面添加文本
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    # 保存更新后的 PDF
    document.save(output_pdf)
```