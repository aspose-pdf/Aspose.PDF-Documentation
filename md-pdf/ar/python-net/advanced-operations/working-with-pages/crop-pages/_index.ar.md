---
title: قص صفحات PDF برمجياً باستخدام Python
linktitle: قص الصفحات
type: docs
weight: 70
url: /python-net/crop-pages/
description: يمكنك الحصول على خصائص الصفحة، مثل العرض، الارتفاع، صندوق النزف، القص والتشذيب باستخدام Aspose.PDF لـ Python عبر .NET.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "قص صفحات PDF برمجياً باستخدام Python",
    "alternativeHeadline": "كيفية قص صفحات PDF في Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستندات PDF",
    "keywords": "pdf, python, قص صفحات pdf",
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
    "url": "/python-net/crop-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/crop-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "يمكنك الحصول على خصائص الصفحة، مثل العرض، الارتفاع، صندوق النزف، القص والتشذيب باستخدام Aspose.PDF لـ Python عبر .NET."
}
</script>


## الحصول على خصائص الصفحة

كل صفحة في ملف PDF تحتوي على عدد من الخصائص، مثل العرض، الارتفاع، صندوق النزيف، صندوق القص وصندوق القطع. يتيح لك Aspose.PDF for Python الوصول إلى هذه الخصائص.

- **media_box**: صندوق الوسائط هو أكبر صندوق صفحة. يتوافق مع حجم الصفحة (مثل A4، A5، US Letter، إلخ) المختار عند طباعة المستند إلى PostScript أو PDF. بعبارة أخرى، يحدد صندوق الوسائط الحجم الفعلي للوسيط الذي يتم عرض أو طباعة مستند PDF عليه.
- **bleed_box**: إذا كان المستند يحتوي على نزيف، فسيكون لـ PDF أيضًا صندوق نزيف. النزيف هو مقدار اللون (أو العمل الفني) الذي يمتد إلى ما بعد حافة الصفحة. يُستخدم للتأكد من أنه عند طباعة المستند وقطعه إلى الحجم ("مُقَطَّع")، فإن الحبر سيصل إلى حافة الصفحة. حتى في حالة قص الصفحة بشكل خاطئ - قُصّت بشكل غير دقيق عن علامات القطع - لن تظهر حواف بيضاء على الصفحة.
- **trim_box**: يشير صندوق القطع إلى الحجم النهائي للمستند بعد الطباعة والقطع.
- **art_box**: صندوق الفن هو الصندوق المرسوم حول المحتويات الفعلية للصفحات في مستنداتك.
 هذه الصفحة تُستخدم عند استيراد مستندات PDF في تطبيقات أخرى. 
- **crop_box**: صندوق الاقتصاص هو حجم "الصفحة" الذي يتم عنده عرض مستند PDF الخاص بك في Adobe Acrobat. في العرض العادي، يتم عرض محتويات صندوق الاقتصاص فقط في Adobe Acrobat. للحصول على وصف تفصيلي لهذه الخصائص، يمكنك قراءة مواصفات Adobe.Pdf، لا سيما 10.10.1 حدود الصفحة.

يظهر الجزء البرمجي أدناه كيفية اقتصاص الصفحة:

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)

    # إنشاء مستطيل صندوق جديد
    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_pdf)
```

في هذا المثال، استخدمنا ملفًا نموذجيًا [هنا](crop_page.pdf). في البداية، تبدو صفحتنا كما هو موضح في الشكل 1.
![الشكل 1. الصفحة المقتصة](crop_page.png)

بعد التغيير، ستبدو الصفحة كما هو موضح في الشكل 2.
![الشكل 2. الصفحة المقتصرة](crop_page2.png)

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF لـ Python عبر مكتبة .NET",
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
                "contactType": "المبيعات",
                "areaServed": "الولايات المتحدة",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "المبيعات",
                "areaServed": "بريطانيا",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "المبيعات",
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