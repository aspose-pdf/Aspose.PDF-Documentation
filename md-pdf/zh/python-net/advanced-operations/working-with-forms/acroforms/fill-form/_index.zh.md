---
title: 填写 AcroForm - 使用 Python 填写 PDF 表单
linktitle: 填写 AcroForm
type: docs
weight: 20
url: /python-net/fill-form/
keywords: 使用 Python 填写 PDF 表单
description: 您可以使用 Aspose.PDF for Python 库在 PDF 文档中填写表单。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "填写 AcroForm",
    "alternativeHeadline": "如何在 PDF 中填写 AcroForm",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 文档生成",
    "keywords": "pdf, python, 填写 acroform",
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
    "url": "/python-net/fill-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/fill-form/"
    },
    "dateModified": "2023-02-04",
    "description": "您可以使用 Aspose.PDF for Python 库在 PDF 文档中填写表单。"
}
</script>


## 在 PDF 文档中填写表单字段

要填写表单字段，从文档对象的 [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) 集合中获取字段。然后使用字段的 [value](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/#properties) 属性设置字段值。

此示例选择一个 [TextBoxField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/)，并使用 Value 属性设置其值。

```python

    import aspose.pdf as ap

    # 打开文档
    pdfDocument = ap.Document(input_file)
    for formField in pdfDocument.form.fields:
        if formField.partial_name == "Field 1":
            # 修改字段值
            formField.value = "777"

    # 保存更新后的文档
    pdfDocument.save(output_pdf)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python Library",
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
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>