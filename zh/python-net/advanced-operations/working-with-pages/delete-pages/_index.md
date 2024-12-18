---
title: 使用Python编程删除PDF页面
linktitle: 删除PDF页面
type: docs
weight: 80
url: /zh/python-net/delete-pages/
description: 您可以使用Aspose.PDF for Python通过.NET库从PDF文件中删除页面。
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "使用Python编程删除PDF页面",
    "alternativeHeadline": "如何删除PDF页面",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf文档生成",
    "keywords": "pdf, python, 删除pdf页面, 去除pdf页面",
    "wordcount": "302",
    "proficiencyLevel":"初学者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF文档团队",
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
    "url": "/python-net/delete-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/delete-pages/"
    },
    "dateModified": "2023-04-04",
    "description": "您可以使用Aspose.PDF for Python通过.NET库从PDF文件中删除页面。"
}
</script>


您可以使用 Aspose.PDF for Python via .NET 从 PDF 文件中删除页面。要从 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 集合中删除特定页面。

## 从 PDF 文件中删除页面

1. 调用 [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) 方法并指定页面的索引
2. 调用 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法以保存更新的 PDF 文件
下面的代码片段展示了如何使用 Python 从 PDF 文件中删除特定页面。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)

    # 删除特定页面
    document.pages.delete(2)

    # 保存更新后的 PDF
    document.save(output_pdf)