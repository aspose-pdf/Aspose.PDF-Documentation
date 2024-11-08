---
title: كيفية دمج ملفات PDF باستخدام بايثون
linktitle: دمج ملفات PDF
type: docs
weight: 50
url: /ar/python-net/merge-pdf-documents/
keywords: "دمج ملفات pdf متعددة في ملف pdf واحد باستخدام بايثون، جمع ملفات pdf متعددة في ملف واحد بايثون، دمج ملفات pdf متعددة في واحد بايثون"
description: تشرح هذه الصفحة كيفية دمج مستندات PDF في ملف PDF واحد باستخدام بايثون.
lastmod: "2023-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "كيفية دمج ملفات PDF باستخدام بايثون",
    "alternativeHeadline": "جمع مستندات PDF عبر بايثون",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "التلاعب في مستندات pdf",
    "keywords": "pdf, python, دمج pdf, concatenate, جمع pdf",
    "wordcount": "212",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق Aspose.PDF Doc",
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
                "contactType": "المبيعات",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "المبيعات",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "المبيعات",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "https://docs.aspose.com/pdf/python-net/merge-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://docs.aspose.com/pdf/python-net/merge-pdf-documents/"
    },
    "dateModified": "2023-04-14",
    "description": "تشرح هذه الصفحة كيفية دمج مستندات PDF في ملف PDF واحد باستخدام بايثون عبر .NET."
}
</script>


## دمج أو تجميع ملفات PDF متعددة في ملف PDF واحد باستخدام Python

دمج ملفات PDF هو استفسار شائع جدًا بين المستخدمين. يمكن أن يكون ذلك مفيدًا عندما يكون لديك عدة ملفات PDF تريد مشاركتها أو تخزينها معًا كوثيقة واحدة.

يمكن أن يساعدك دمج ملفات PDF في تنظيم مستنداتك، وتوفير مساحة للتخزين على جهاز الكمبيوتر الخاص بك، ومشاركة عدة ملفات PDF مع الآخرين عن طريق دمجها في وثيقة واحدة.

دمج PDF في Python عبر .NET ليس مهمة بسيطة بدون استخدام مكتبة طرف ثالث. 
توضح هذه المقالة كيفية دمج ملفات PDF متعددة في وثيقة PDF واحدة باستخدام Aspose.PDF لـ Python عبر .NET.

## دمج ملفات PDF باستخدام Python وDOM

لدمج ملفين PDF:

1. قم بإنشاء كائنين [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) ، يحتوي كل منهما على واحد من ملفات PDF المدخلة.

1. ثم قم باستدعاء طريقة [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) لمجموعة [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) لكائن Document الذي تريد إضافة ملف PDF الآخر إليه.
1. مرر مجموعة PageCollection لكائن Document الثاني إلى طريقة [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) لمجموعة PageCollection الأولى.
1. أخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

يظهر مقطع الشيفرة التالي كيفية دمج ملفات PDF.

```python

    import aspose.pdf as ap

    # افتح المستند الأول
    document1 = ap.Document(input_pdf_1)
    # افتح المستند الثاني
    document2 = ap.Document(input_pdf_2)

    # أضف صفحات المستند الثاني إلى الأول
    document1.pages.add(document2.pages)

    # احفظ ملف الإخراج المدموج
    document1.save(output_pdf)
```


## مثال حي

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) هو تطبيق ويب مجاني على الإنترنت يتيح لك التحقيق في كيفية عمل وظيفة دمج العروض التقديمية.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

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