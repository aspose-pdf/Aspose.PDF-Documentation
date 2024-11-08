---
title: تقسيم ملفات PDF برمجياً باستخدام Python
linktitle: تقسيم ملفات PDF
type: docs
weight: 60
url: /ar/python-net/split-pdf-document/
keywords: تقسيم pdf إلى ملفات متعددة, تقسيم pdf إلى ملفات منفصلة, تقسيم pdf باستخدام بايثون
description: يوضح هذا الموضوع كيفية تقسيم صفحات PDF إلى ملفات PDF فردية في تطبيقات Python الخاصة بك.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "تقسيم PDF برمجياً",
    "alternativeHeadline": "كيفية تقسيم PDF باستخدام Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستندات pdf",
    "keywords": "pdf, python, تقسيم pdf",
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
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/split-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/split-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "يوضح هذا الموضوع كيفية تقسيم صفحات PDF إلى ملفات PDF فردية في تطبيقات Python الخاصة بك."
}
</script>


تقسيم صفحات PDF يمكن أن يكون ميزة مفيدة لأولئك الذين يرغبون في تقسيم ملف كبير إلى صفحات منفصلة أو مجموعات من الصفحات.

## مثال حي

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) هو تطبيق ويب مجاني عبر الإنترنت يتيح لك استكشاف كيفية عمل وظيفة تقسيم العروض التقديمية.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

يوضح هذا الموضوع كيفية تقسيم صفحات PDF إلى ملفات PDF فردية في تطبيقات Python الخاصة بك. لتقسيم صفحات PDF إلى ملفات PDF ذات صفحة واحدة باستخدام Python، يمكن اتباع الخطوات التالية:

1. حلقة عبر صفحات مستند PDF من خلال مجموعة [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) الخاصة بكائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. لكل تكرار، قم بإنشاء كائن مستند جديد وقم بإضافة الكائن [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) الفردي إلى المستند الفارغ

1. احفظ ملف PDF الجديد باستخدام [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) الطريقة

## تقسيم ملف PDF إلى ملفات متعددة أو ملفات PDF منفصلة في بايثون

يوضح لك مقتطف الكود التالي في بايثون كيفية تقسيم صفحات PDF إلى ملفات PDF فردية.

```python

    import aspose.pdf as ap

    # فتح المستند
    document = ap.Document(input_pdf)

    page_count = 1

    # تكرار خلال جميع الصفحات
    for pdfPage in document.pages:
        new_document = ap.Document()
        new_document.pages.add(pdfPage)
        new_document.save(output_path + "_page_" + str(page_count) + ".pdf")
        page_count = page_count + 1
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