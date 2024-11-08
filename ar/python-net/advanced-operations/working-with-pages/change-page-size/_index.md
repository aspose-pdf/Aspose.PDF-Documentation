---
title: تغيير حجم صفحة PDF باستخدام Python
linktitle: تغيير حجم صفحة PDF
type: docs
weight: 60
url: /ar/python-net/change-page-size/
description: تغيير حجم الصفحة من مستند PDF الخاص بك باستخدام مكتبة Aspose.PDF لـ Python عبر .NET.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "تغيير حجم صفحة PDF باستخدام Python",
    "alternativeHeadline": "تغيير حجم صفحة PDF باستخدام Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستند PDF",
    "keywords": "pdf, python, تغيير حجم pdf, تغيير حجم pdf",
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
    "url": "/python-net/change-page-size/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/change-page-size/"
    },
    "dateModified": "2023-04-04",
    "description": "تغيير حجم الصفحة من مستند PDF الخاص بك باستخدام مكتبة Aspose.PDF لـ Python عبر .NET."
}
</script>


## تغيير حجم صفحة PDF

تتيح لك Aspose.PDF لـ Python عبر .NET تغيير حجم صفحة PDF بأسطر بسيطة من التعليمات البرمجية في تطبيقات Python الخاصة بك. يشرح هذا الموضوع كيفية تحديث/تغيير أبعاد الصفحة (الحجم) لملف PDF موجود.

تحتوي فئة [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) على طريقة [set_page_size()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) التي تتيح لك تعيين حجم الصفحة. يقوم مقتطف الكود أدناه بتحديث أبعاد الصفحة في بضع خطوات سهلة:

1. تحميل ملف PDF المصدر.
2. الحصول على الصفحات في كائن [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
3. الحصول على صفحة معينة.
4. استدعاء طريقة set_page_size() لتحديث أبعادها.
5. استدعاء طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) لفئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) لإنشاء ملف PDF بالأبعاد المحدثة للصفحة.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)

    # الحصول على صفحة معينة
    page = document.pages[1]

    # تعيين حجم الصفحة كـ A4 (11.7 × 8.3 بوصة) وفي Aspose.Pdf، 1 بوصة = 72 نقطة
    # لذلك أبعاد A4 بالنقاط ستكون (842.4, 597.6)
    page.set_page_size(597.6, 842.4)

    # حفظ المستند المحدث
    document.save(output_pdf)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "مكتبة معالجة PDF لـ Python",
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