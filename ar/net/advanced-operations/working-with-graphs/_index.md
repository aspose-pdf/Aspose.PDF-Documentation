---
title: العمل مع الرسوم البيانية في ملف PDF
linktitle: العمل مع الرسوم البيانية
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ar/net/working-with-graphs/
description: تشرح هذه المقالة ما هو الرسم البياني، كيفية إنشاء كائن مستطيل مملوء، ووظائف أخرى
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-graphs/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Graphs in PDF file",
    "alternativeHeadline": "Create and Manipulate Graphs in PDF Files",
    "abstract": "اكتشف الميزة الجديدة القوية لإنشاء ومعالجة الرسوم البيانية داخل مستندات PDF باستخدام Aspose.PDF for .NET. تتيح هذه الوظيفة للمطورين إنشاء مجموعة متنوعة من أشكال الرسوم البيانية، بما في ذلك الأقواس، والدوائر، والخطوط، والمستطيلات، مما يعزز العرض المرئي للبيانات في تطبيقاتهم. قم بتحسين عملية إنشاء PDF الخاصة بك وقدم تصورات بيانات ديناميكية بسهولة",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Graph, PDF documents, Aspose.PDF for .NET, Graph class, Shapes, Arc, Circle, Line graph, Rectangle, PDF manipulation",
    "wordcount": "329",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "dateModified": "2024-11-25",
    "description": "تشرح هذه المقالة ما هو الرسم البياني، كيفية إنشاء كائن مستطيل مملوء، ووظائف أخرى"
}
</script>

## ما هو الرسم البياني

إضافة الرسوم البيانية إلى مستندات PDF هي مهمة شائعة جدًا للمطورين أثناء العمل مع Adobe Acrobat Writer أو تطبيقات معالجة PDF الأخرى. هناك العديد من أنواع الرسوم البيانية التي يمكن استخدامها في تطبيقات PDF.
يدعم [Aspose.PDF for .NET](/pdf/net/) أيضًا إضافة الرسوم البيانية إلى مستندات PDF. لهذا الغرض، يتم توفير فئة الرسم البياني. الرسم البياني هو عنصر على مستوى الفقرة ويمكن إضافته إلى مجموعة الفقرات في مثيل الصفحة. يحتوي مثيل الرسم البياني على مجموعة من الأشكال.

الأنواع التالية من الأشكال مدعومة من قبل فئة [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph):

- [قوس](/pdf/net/add-arc/) - يُطلق عليه أحيانًا أيضًا علم وهو زوج مرتب من الرؤوس المجاورة، ولكن يُطلق عليه أحيانًا أيضًا خط موجه.
- [دائرة](/pdf/net/add-circle/) - تعرض البيانات باستخدام دائرة مقسمة إلى قطاعات. نستخدم الرسم البياني الدائري (المعروف أيضًا باسم مخطط دائري) لإظهار كيف تمثل البيانات أجزاء من كل واحد أو مجموعة واحدة.
- [منحنى](/pdf/net/add-curve/) - هو اتحاد متصل من الخطوط الإسقاطية، حيث يلتقي كل خط بثلاثة خطوط أخرى في نقاط مزدوجة عادية.
- [خط](/pdf/net/add-line) - تُستخدم الرسوم البيانية الخطية لعرض البيانات المستمرة ويمكن أن تكون مفيدة في التنبؤ بالأحداث المستقبلية عندما تظهر الاتجاهات على مر الزمن.
- [مستطيل](/pdf/net/add-rectangle/) - هو واحد من العديد من الأشكال الأساسية التي ستراها في الرسوم البيانية، ويمكن أن يكون مفيدًا جدًا في مساعدتك على حل مشكلة.
- [بيضاوي](/pdf/net/add-ellipse/) - هو مجموعة من النقاط على مستوى، مما يخلق شكلًا بيضاويًا منحنيًا.

التفاصيل أعلاه موضحة أيضًا في الأشكال أدناه:

![الأشكال في الرسوم البيانية](graphs.png)


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