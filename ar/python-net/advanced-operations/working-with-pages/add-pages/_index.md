---
title: إضافة صفحات في PDF باستخدام بايثون
linktitle: إضافة صفحات
type: docs
weight: 10
url: ar/python-net/add-pages/
description: تعلمك هذه المقالة كيفية إدراج (إضافة) صفحة في الموقع المطلوب في ملف PDF. تعرف على كيفية نقل، إزالة (حذف) الصفحات من ملف PDF باستخدام C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة صفحات في PDF باستخدام بايثون",
    "alternativeHeadline": "كيفية إضافة صفحات في مستند PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستندات pdf",
    "keywords": "pdf, python, إضافة صفحة pdf, إدراج صفحة pdf",
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
    "url": "/python-net/add-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "تعلمك هذه المقالة كيفية إدراج (إضافة) صفحة في الموقع المطلوب في ملف PDF. تعرف على كيفية نقل، إزالة (حذف) الصفحات من ملف PDF باستخدام بايثون."
}
</script>


Aspose.PDF لـ Python عبر .NET API يوفر مرونة كاملة للعمل مع الصفحات في مستند PDF باستخدام Python. يحتفظ بجميع صفحات مستند PDF في [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) التي يمكن استخدامها للعمل مع صفحات PDF. 
Aspose.PDF لـ Python عبر .NET يتيح لك إدراج صفحة في مستند PDF في أي موقع في الملف بالإضافة إلى إضافة صفحات إلى نهاية ملف PDF. 
يوضح هذا القسم كيفية إضافة صفحات إلى PDF باستخدام Python.

## إضافة أو إدراج صفحة في ملف PDF

Aspose.PDF لـ Python عبر .NET يتيح لك إدراج صفحة في مستند PDF في أي موقع في الملف بالإضافة إلى إضافة صفحات إلى نهاية ملف PDF.

### إدراج صفحة فارغة في ملف PDF في الموقع المطلوب

لإدراج صفحة فارغة في ملف PDF:

1. قم بإنشاء كائن فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) مع ملف PDF المدخل.

1. استدعاء طريقة [insert](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection/methods/insert) لمجموعة [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) مع الفهرس المحدد.
1. احفظ ملف PDF الناتج باستخدام طريقة [save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

يوضح لك مقطع الشيفرة البرمجية التالي كيفية إدراج صفحة في ملف PDF.

```python

    import aspose.pdf as ap

    # فتح المستند
    document = ap.Document(input_pdf)
    # إدراج صفحة فارغة في PDF
    document.pages.insert(2)
    # حفظ الملف الناتج
    document.save(output_pdf)
```

### إضافة صفحة فارغة في نهاية ملف PDF

أحيانًا، تريد التأكد من أن المستند ينتهي بصفحة فارغة. يشرح هذا الموضوع كيفية إدراج صفحة فارغة في نهاية مستند PDF.

لإدراج صفحة فارغة في نهاية ملف PDF:

1. أنشئ كائن فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) مع ملف PDF المدخل.

1. قم باستدعاء طريقة [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) الخاصة بمجموعة [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) بدون أي معلمات.
1. قم بحفظ ملف PDF الناتج باستخدام طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

يظهر لك مقطع الشيفرة التالي كيفية إدراج صفحة فارغة في نهاية ملف PDF.

```python

    import aspose.pdf as ap

    # فتح المستند
    document = ap.Document(input_pdf)

    # إدراج صفحة فارغة في نهاية ملف PDF
    document.pages.add()

    # حفظ ملف الإخراج
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
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>