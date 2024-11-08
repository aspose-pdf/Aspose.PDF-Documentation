---
title: إضافة مرفق إلى مستند PDF باستخدام Python
linktitle: إضافة مرفق إلى مستند PDF
type: docs
weight: 10
url: /ar/python-net/add-attachment-to-pdf-document/
description: تصف هذه الصفحة كيفية إضافة مرفق إلى ملف PDF باستخدام Aspose.PDF لـ Python عبر مكتبة .NET.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة مرفق إلى مستند PDF عبر Python",
    "alternativeHeadline": "كيفية إضافة مرفقات إلى PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستند PDF",
    "keywords": "pdf, python, المرفقات في pdf",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق توثيق Aspose.PDF",
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
    "url": "/python-net/add-attachment-to-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-attachment-to-pdf-document/"
    },
    "dateModified": "2023-02-04",
    "description": "تصف هذه الصفحة كيفية إضافة مرفق إلى ملف PDF باستخدام Aspose.PDF لـ Python عبر مكتبة .NET"
}
</script>


المرفقات يمكن أن تحتوي على مجموعة متنوعة من المعلومات ويمكن أن تكون من أنواع ملفات متنوعة. هذه المقالة تشرح كيفية إضافة مرفق إلى ملف PDF.

1. أنشئ مشروع بايثون جديد.
1. قم باستيراد حزمة Aspose.PDF
1. أنشئ كائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. أنشئ كائن [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) مع الملف الذي تقوم بإضافته، ووصف الملف.
1. أضف كائن [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) إلى مجموعة [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) الخاصة بكائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)، باستخدام طريقة [add](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods).

مجموعة [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) تحتوي على جميع المرفقات في ملف PDF.
 يظهر لك مقتطف الكود التالي كيفية إضافة مرفق في مستند PDF.

```python

    import aspose.pdf as ap

    # فتح المستند
    document = ap.Document(input_pdf)

    # إعداد ملف جديد ليتم إضافته كمرفق
    fileSpecification = ap.FileSpecification(attachment_file, "ملف نصي نموذجي")

    # إضافة المرفق إلى مجموعة مرفقات المستند
    document.embedded_files.append(fileSpecification)

    # حفظ المخرجات الجديدة
    document.save(output_pdf)
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