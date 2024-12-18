---
title: كيفية إنشاء ملف PDF باستخدام بايثون
linktitle: إنشاء مستند PDF
type: docs
weight: 10
url: /ar/python-net/create-pdf-document/
description: إنشاء وتنسيق مستند PDF باستخدام Aspose.PDF لبايثون عبر .NET.
lastmod: "2023-04-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "كيفية إنشاء ملف PDF باستخدام بايثون",
    "alternativeHeadline": "إنشاء مستند PDF من الصفر عبر بايثون",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "pdf, python, dotnet, إنشاء مستند pdf",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق مستندات Aspose.PDF",
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
                "contactType": "مبيعات",
                "areaServed": "الولايات المتحدة",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "المملكة المتحدة",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
                "areaServed": "أستراليا",
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
    "description": "إنشاء وتنسيق مستند PDF باستخدام Aspose.PDF لبايثون عبر .NET."
}
</script>


**Aspose.PDF for Python عبر .NET** هو API لمعالجة ملفات PDF يسمح للمطورين بإنشاء وتحميل وتعديل وتحويل ملفات PDF مباشرة من Python لتطبيقات .NET ببضع سطور من الكود.

## كيفية إنشاء ملف PDF بسيط

لإنشاء ملف PDF باستخدام Python عبر .NET مع Aspose.PDF، يمكنك اتباع الخطوات التالية:

1. إنشاء كائن من فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. إضافة كائن [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) إلى مجموعة [pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) لكائن Document
1. إضافة [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) إلى مجموعة [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) للصفحة
1. حفظ مستند PDF الناتج

```python

    import aspose.pdf as ap

    # تهيئة كائن المستند
    document = ap.Document()
    # إضافة صفحة
    page = document.pages.add()
    # إضافة نص إلى الصفحة الجديدة
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    # حفظ ملف PDF المحدث
    document.save(output_pdf)
```