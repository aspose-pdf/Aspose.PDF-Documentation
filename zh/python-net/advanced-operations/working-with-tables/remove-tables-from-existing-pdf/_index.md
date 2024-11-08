---
title: 从现有 PDF 中移除表格
linktitle: 移除表格
type: docs
weight: 50
url: /zh/python-net/remove-tables-from-existing-pdf/
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "从现有 PDF 中移除表格",
    "alternativeHeadline": "如何从 PDF 中删除表格",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 文档生成",
    "keywords": "pdf, python, 移除表格, 删除表格",
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
                "contactType": "销售",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "销售",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "销售",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/remove-tables-from-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/remove-tables-from-existing-pdf/"
    },
    "dateModified": "2023-02-04",
    "description": ""
}
</script>


{{% alert color="primary" %}}

Aspose.PDF for Python via .NET 提供在生成 PDF 文档时插入/创建表格的功能，您也可以在任何现有的 PDF 文档中添加表格对象。然而，您可能需要[操作现有 PDF 中的表格](https://docs.aspose.com/pdf/python-net/manipulate-tables-in-existing-pdf/)，在这里您可以更新现有表格单元格中的内容。然而，您可能会遇到需要从现有 PDF 文档中移除表格对象的需求。

{{% /alert %}}

为了移除表格，我们需要使用 [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) 类来获取现有 PDF 中的表格，然后调用 [remove()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods)。

## 从 PDF 文档中移除表格

我们添加了新功能，即。
 [remove()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods) 到现有的 [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) 类，以便从 PDF 文档中删除表格。一旦吸收器成功地在页面上找到表格，它就能够删除它们。请查看以下代码片段，了解如何从 PDF 文档中删除表格：

```python

    import aspose.pdf as ap

    # 加载现有的 PDF 文档
    pdf_document = ap.Document(input_file)
    # 创建 TableAbsorber 对象以查找表格
    absorber = ap.text.TableAbsorber()
    # 用吸收器访问第一页
    absorber.visit(pdf_document.pages[1])
    # 获取页面上的第一个表格
    table = absorber.table_list[0]
    # 删除表格
    absorber.remove(table)
    # 保存 PDF
    pdf_document.save(output_file)
```

## 从 PDF 文档中删除多个表格

有时，PDF 文档可能包含多个表格，您可能需要从中删除多个表格。 为了从PDF文档中删除多个表格，请使用以下代码片段：

```python

    import aspose.pdf as ap

    # 加载现有的PDF文档
    pdf_document = ap.Document(input_file)
    # 创建TableAbsorber对象以查找表格
    absorber = ap.text.TableAbsorber()
    # 使用吸收器访问第二页
    absorber.visit(pdf_document.pages[1])
    # 获取表格集合的副本
    tables = absorber.table_list
    # 遍历集合的副本并删除表格
    for table in tables:
        absorber.remove(table)
    # 保存文档
    pdf_document.save(output_file)
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
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>