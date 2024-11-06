---
title: حذف صفحات PDF برمجيًا باستخدام Python
linktitle: حذف صفحات PDF
type: docs
weight: 80
url: ar/python-net/delete-pages/
description: يمكنك حذف الصفحات من ملف PDF الخاص بك باستخدام مكتبة Aspose.PDF لـ Python عبر .NET.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "حذف صفحات PDF برمجيًا باستخدام Python",
    "alternativeHeadline": "كيفية إزالة صفحات PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستندات PDF",
    "keywords": "pdf, python, حذف صفحات pdf, إزالة صفحات pdf",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق وثائق Aspose.PDF",
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
    "description": "يمكنك حذف الصفحات من ملف PDF الخاص بك باستخدام مكتبة Aspose.PDF لـ Python عبر .NET."
}
</script>


يمكنك حذف الصفحات من ملف PDF باستخدام Aspose.PDF for Python عبر .NET. لحذف صفحة معينة من مجموعة [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).

## حذف صفحة من ملف PDF

1. قم باستدعاء طريقة [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) وحدد مؤشر الصفحة
2. قم باستدعاء طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) لحفظ ملف PDF المحدث
يوضح مقتطف الشيفرة التالي كيفية حذف صفحة معينة من ملف PDF باستخدام Python.

```python

    import aspose.pdf as ap

    # فتح المستند
    document = ap.Document(input_pdf)

    # حذف صفحة معينة
    document.pages.delete(2)

    # حفظ ملف PDF المحدث
    document.save(output_pdf)