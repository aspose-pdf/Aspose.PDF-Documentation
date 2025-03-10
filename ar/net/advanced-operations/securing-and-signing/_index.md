---
title: تأمين وتوقيع PDF في C#
linktitle: التأمين والتوقيع في PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 210
url: /ar/net/securing-and-signing/
description: يصف هذا القسم ميزات استخدام التوقيع وتأمين مستند PDF الخاص بك باستخدام C#
lastmod: "2024-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Securing and signing PDF in C#",
    "alternativeHeadline": "Securely Digitally Sign PDFs with C#",
    "abstract": "اكتشف القدرات المتقدمة لتأمين وتوقيع مستندات PDF رقميًا باستخدام C#. تتيح هذه الميزة للمستخدمين تطبيق توقيعات رقمية قوية مع خوارزميات وخيارات تجزئة متنوعة، مما يضمن سلامة المستند وموثوقيته. عزز أمان PDF الخاص بك مع وظائف التوقيع الشاملة من Aspose.PDF المصممة للتكامل السلس في تطبيقات .NET",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Securing PDF, signing PDF, digital signature, electronic signature, PKCS1, PKCS7, digest algorithms, Aspose.PDF, C# PDF manipulation, timestamp signature",
    "wordcount": "302",
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
    "url": "/net/securing-and-signing/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/securing-and-signing/"
    },
    "dateModified": "2024-02-07",
    "description": "يصف هذا القسم ميزات استخدام التوقيع وتأمين مستند PDF الخاص بك باستخدام C#"
}
</script>

يصف هذا القسم كيفية توقيع مستندات PDF رقميًا بشكل آمن باستخدام C#. يتم استخدام مصطلحي التوقيع الإلكتروني والتوقيع الرقمي بالتبادل، لكنهما في الأساس مختلفان. بشكل عام، يأتي التوقيع الرقمي مع ختم معتمد من [سلطة التصديق](https://en.wikipedia.org/wiki/Certificate_authority) ويستخدم لحماية المستند الموقع من التلاعب. بدلاً من ذلك، غالبًا ما يُستخدم التوقيع الإلكتروني لإظهار النية في توقيع مستند.

يدعم Aspose.PDF التوقيعات الرقمية:
- PKCS1 مع خوارزمية توقيع RSA وتجزيء SHA-1.
- PKCS7 مع خوارزمية توقيع RSA وتجزيء SHA-1.
- PKCS7 مفصول مع خوارزميات توقيع DSA وRSA وECDSA. تعتمد خوارزميات التجزئة المدعومة على خوارزمية التوقيع.
- توقيع مؤرخ.

خوارزميات التجزئة لـ PKCS7 المفصول:
- DSA - SHA-1.
- RSA - SHA-1، SHA-256، SHA-384، SHA-512.
- ECDSA - SHA-256، SHA-384، SHA-512، SHA3-256، SHA3-384، SHA3-512.

يوصى بتجنب التوقيعات الرقمية مع خوارزمية التجزئة SHA-1 بسبب عدم أمانها.

- [توقيع ملف PDF رقميًا](/pdf/net/digitally-sign-pdf-file/)
- [تعيين الامتيازات، تشفير وفك تشفير ملف PDF](/pdf/net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [استخراج معلومات الصورة والتوقيع](/pdf/net/extract-image-and-signature-information/)
- [توقيع مستند PDF من بطاقة ذكية](/pdf/net/sign-pdf-document-from-smart-card/)

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