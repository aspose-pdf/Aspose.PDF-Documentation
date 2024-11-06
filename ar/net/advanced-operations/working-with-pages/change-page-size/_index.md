---
title: تغيير حجم صفحة PDF باستخدام C#
linktitle: تغيير حجم صفحة PDF
type: docs
weight: 40
url: ar/net/change-page-size/
description: قم بتغيير حجم صفحة مستند PDF الخاص بك باستخدام مكتبة Aspose.PDF لـ .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "تغيير حجم صفحة PDF باستخدام C#",
    "alternativeHeadline": "تغيير حجم صفحة PDF باستخدام .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستند PDF",
    "keywords": "pdf, c#, تغيير حجم pdf, تغيير حجم pdf",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق وثائق Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "url": "/net/change-page-size/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/change-page-size/"
    },
    "dateModified": "2022-02-04",
    "description": "قم بتغيير حجم صفحة مستند PDF الخاص بك باستخدام مكتبة Aspose.PDF لـ .NET."
}
</script>
## تغيير حجم صفحة PDF

يتيح لك Aspose.PDF لـ .NET تغيير حجم صفحة PDF بأسطر بسيطة من الكود في تطبيقات .NET الخاصة بك. يشرح هذا الموضوع كيفية تحديث/تغيير أبعاد الصفحة (الحجم) لملف PDF موجود.

يعمل الكود التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

تحتوي فئة [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) على طريقة SetPageSize(...) التي تتيح لك تعيين حجم الصفحة. يقوم الكود أدناه بتحديث أبعاد الصفحة في بضع خطوات سهلة:

1. تحميل ملف PDF المصدر.
1. الحصول على الصفحات في كائن [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. الحصول على صفحة معينة.
1. استدعاء طريقة SetPageSize(..) لتحديث أبعادها.
1. استدعاء طريقة Save(..) لفئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) لإنشاء ملف PDF بأبعاد صفحة محدثة.

{{% alert color="primary" %}}

يرجى ملاحظة أن خصائص الارتفاع والعرض تستخدم النقاط كوحدة أساسية، حيث 1 بوصة = 72 نقطة و1 سم = 1/2.54 بوصة = 0.3937 بوصة = 28.3 نقطة.
يرجى ملاحظة أن خصائص الارتفاع والعرض تستخدم النقاط كوحدة أساسية، حيث 1 بوصة = 72 نقطة و1 سم = 1/2.54 بوصة = 0.3937 بوصة = 28.3 نقطة.

{{% /alert %}}

الشفرة التالية توضح كيفية تغيير أبعاد صفحة PDF إلى حجم A4.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-UpdateDimensions-UpdateDimensions.cs" >}}

## الحصول على حجم صفحة PDF

يمكنك قراءة حجم صفحة PDF لملف PDF موجود باستخدام Aspose.PDF لـ.NET. العينة البرمجية التالية تظهر كيفية قراءة أبعاد صفحة PDF باستخدام C#.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetDimensions-GetDimensions.cs" >}}

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>


