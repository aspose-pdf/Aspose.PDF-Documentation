---
title: العمل مع الرسوم البيانية في ملف PDF
linktitle: العمل مع الرسوم البيانية
type: docs
weight: 70
url: /ar/net/graphs/
description: يشرح هذا المقال ما هو الرسم البياني، كيفية إنشاء كائن مستطيل مملوء، ووظائف أخرى
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "العمل مع الرسوم البيانية في ملف PDF",
    "alternativeHeadline": "كيفية إنشاء الرسوم البيانية في PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستند PDF",
    "keywords": "pdf, c#, الرسوم البيانية في pdf",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
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
    "url": "/net/graphs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/graphs/"
    },
    "dateModified": "2022-02-04",
    "description": "يشرح هذا المقال ما هو الرسم البياني، كيفية إنشاء كائن مستطيل مملوء، ووظائف أخرى"
}
</script>
## ما هو الرسم البياني

إضافة الرسوم البيانية إلى مستندات PDF هي مهمة شائعة جدًا للمطورين أثناء العمل مع Adobe Acrobat Writer أو تطبيقات معالجة PDF الأخرى. هناك العديد من أنواع الرسوم البيانية التي يمكن استخدامها في تطبيقات PDF.
يدعم [Aspose.PDF for .NET](/pdf/ar/net/) أيضًا إضافة الرسوم البيانية إلى مستندات PDF. لهذا الغرض، يتم توفير فئة الرسم البياني. الرسم البياني هو عنصر على مستوى الفقرة ويمكن إضافته إلى مجموعة الفقرات في نموذج الصفحة. يحتوي نموذج الرسم البياني على مجموعة من الأشكال.

أنواع الأشكال التالية مدعومة من قبل فئة [الرسم البياني](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph):

- [Arc](/pdf/ar/net/add-arc/) - يُسمى أحيانًا أيضًا بالعلم وهو زوج مرتب من الرؤوس المتجاورة، ولكن يُطلق عليه أحيانًا خط موجه.
- [Circle](/pdf/ar/net/add-circle/) - يعرض البيانات باستخدام دائرة مقسمة إلى قطاعات. نستخدم رسم بياني دائري (يُسمى أيضًا مخطط دائري) لإظهار كيف تمثل البيانات أجزاء من كل واحد أو مجموعة واحدة.
- [Curve](/pdf/ar/net/add-curve/) - هو اتحاد متصل من الخطوط التصويرية، حيث يلتقي كل خط بثلاثة خطوط أخرى في نقاط مزدوجة عادية.
- [Curve](/pdf/ar/net/add-curve/) - هو اتحاد متصل لخطوط متقاطعة، حيث يلتقي كل خط بثلاثة خطوط أخرى في نقاط مزدوجة عادية.
- [Line](/pdf/ar/net/add-line) - تُستخدم الرسوم البيانية للخطوط لعرض البيانات المستمرة ويمكن أن تكون مفيدة في التنبؤ بالأحداث المستقبلية عندما تظهر اتجاهات على مر الزمن.
- [Rectangle](/pdf/ar/net/add-rectangle/) - هي واحدة من الأشكال الأساسية العديدة التي ستراها في الرسوم البيانية، ويمكن أن تكون مفيدة جدًا في مساعدتك على حل مشكلة.
- [Ellipse](/pdf/ar/net/add-ellipse/) - هو مجموعة من النقاط على مستوى، تكوين شكل بيضاوي منحني.

تُظهر التفاصيل أعلاه أيضًا في الأشكال أدناه:

![Figures in Graphs](graphs.png)

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

