---
title: 提取 AcroForm - 在 Python 中从 PDF 提取表单数据
linktitle: 提取 AcroForm
type: docs
weight: 30
url: /python-net/extract-form/
keywords: 从 pdf 提取表单数据 python
description: 使用 Aspose.PDF for Python 库从您的 PDF 文档中提取表单。获取 PDF 文件中单个字段的值。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "提取 AcroForm",
    "alternativeHeadline": "如何在 Python 中从 PDF 提取 AcroForm",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 文档生成",
    "keywords": "pdf, python, 提取 acroform",
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
            "https://www.youtube.com/@AsposePDF",
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
    "url": "/python-net/extract-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/extract-form/"
    },
    "dateModified": "2023-02-04",
    "description": "使用 Aspose.PDF for Python 库从您的 PDF 文档中提取表单。获取 PDF 文件中单个字段的值。"
}
</script>


## 从表单中提取数据

### 获取 PDF 文档中所有字段的值

要从 PDF 文档中获取所有字段的值，需要遍历所有表单字段，然后使用 Value 属性获取值。从基础字段类型 [Field](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/) 的 Form 集合中获取每个字段，并访问其 [value](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/#properties) 属性。

以下 Python 代码片段展示了如何获取 PDF 文档中所有字段的值。

```python

    import aspose.pdf as ap

    # 打开文档
    pdfDocument = ap.Document(input_file)

    # 从所有字段获取值
    for formField in pdfDocument.form.fields:
        # 如果需要，分析名称和值
        print("字段名称 : " + formField.partial_name)
        print("值 : " + str(formField.value))