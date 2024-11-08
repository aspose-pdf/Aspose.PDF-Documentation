---
title: 使用 Python 程序化拆分 PDF
linktitle: 拆分 PDF 文件
type: docs
weight: 60
url: /zh/python-net/split-pdf-document/
keywords: 拆分 pdf 为多个文件, 拆分 pdf 为独立的 pdf, 拆分 pdf python
description: 本主题展示如何在您的 Python 应用程序中将 PDF 页面拆分为单个 PDF 文件。
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "程序化拆分 PDF",
    "alternativeHeadline": "如何使用 Python 拆分 PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 文档生成",
    "keywords": "pdf, python, 拆分 pdf",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
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
    "url": "/python-net/split-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/split-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "本主题展示如何在您的 Python 应用程序中将 PDF 页面拆分为单个 PDF 文件。"
}
</script>


将 PDF 页面拆分对于想要将大型文件拆分为单独页面或页面组的人来说是一个有用的功能。

## 实时示例

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) 是一个免费的在线网络应用程序，可以让你研究演示拆分功能的工作原理。

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

本主题介绍如何在 Python 应用程序中将 PDF 页面拆分为单个 PDF 文件。要使用 Python 将 PDF 页面拆分为单页 PDF 文件，可以按照以下步骤进行：

1. 通过 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象的 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 集合循环遍历 PDF 文档的页面
1. 对于每次迭代，创建一个新的 Document 对象，并将单个 [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 对象添加到空文档中

1. 使用 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法保存新的 PDF

## 在 Python 中将 PDF 拆分为多个文件或独立的 PDF

以下 Python 代码片段向您展示了如何将 PDF 页面拆分为单个 PDF 文件。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)

    page_count = 1

    # 遍历所有页面
    for pdfPage in document.pages:
        new_document = ap.Document()
        new_document.pages.add(pdfPage)
        new_document.save(output_path + "_page_" + str(page_count) + ".pdf")
        page_count = page_count + 1