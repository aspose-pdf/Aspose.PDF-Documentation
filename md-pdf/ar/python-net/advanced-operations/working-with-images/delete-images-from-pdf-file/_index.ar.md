---
title: حذف الصور من ملف PDF باستخدام Python
linktitle: حذف الصور
type: docs
weight: 20
url: /python-net/delete-images-from-pdf-file/
description: يشرح هذا القسم كيفية حذف الصور من ملف PDF باستخدام Aspose.PDF لـ Python عبر .NET.
lastmod: "2023-04-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "حذف الصور من ملف PDF باستخدام Python",
    "alternativeHeadline": "كيفية إزالة الصور من PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, delete, remove image from pdf",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/python-net/delete-images-from-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/delete-images-from-pdf-file/"
    },
    "dateModified": "2023-02-04",
    "description": "يشرح هذا القسم كيفية حذف الصور من ملف PDF باستخدام Aspose.PDF لـ Python عبر .NET."
}
</script>


هناك العديد من الأسباب لإزالة جميع الصور أو صور محددة من ملفات PDF.

أحيانًا قد يحتوي ملف PDF على صور مهمة تحتاج إلى إزالتها لحماية الخصوصية أو لمنع الوصول غير المصرح به إلى معلومات معينة.

يمكن أن يساعد إزالة الصور غير المرغوب فيها أو الزائدة في تقليل حجم الملف، مما يسهل مشاركة أو تخزين ملفات PDF.

إذا لزم الأمر، يمكنك تقليل عدد الصفحات عن طريق إزالة جميع الصور من المستند. 
كما أن حذف الصور من المستند سيساعد في تحضير ملف PDF للضغط أو استخراج معلومات النصوص.

**Aspose.PDF for Python عبر .NET** سيساعدك في هذه المهمة.

## حذف الصور من ملف PDF

لحذف صورة من ملف PDF:

1. افتح مستند PDF موجود.
2. احذف صورة معينة.
3. احفظ ملف PDF المحدث.

يعرض مقطع الكود التالي كيفية حذف صورة من ملف PDF.

```python

    import aspose.pdf as ap

    # افتح المستند
    document = ap.Document(input_file)

    # احذف صورة معينة
    document.pages[2].resources.images.delete(1)

    # احفظ ملف PDF المحدث
    document.save(output_pdf)
```


## حذف جميع الصور من ملف PDF المدخل

```python

    import aspose.pdf as ap

    # فتح المستند
    document = ap.Document(input_file)

    # حذف جميع الصور في جميع الصفحات
    for i in range(len(document.pages)):
        while len(document.pages[i + 1].resources.images) != 0:
            document.pages[i + 1].resources.images.delete(1)

    # حفظ ملف PDF المحدث
    document.save(output_file)
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
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>