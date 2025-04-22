---
title: Защита и подпись PDF в C#
linktitle: Защита и подпись в PDF
type: docs
weight: 210
url: /ru/net/securing-and-signing/
description: Этот раздел описывает функции использования подписи и защиты вашего PDF-документа с помощью C#
lastmod: "2024-11-23"
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
    "abstract": "Откройте для себя расширенные возможности защиты и цифровой подписи PDF-документов с помощью C#. Эта функция позволяет пользователям применять надежные цифровые подписи с различными алгоритмами и вариантами дайджеста, обеспечивая целостность и подлинность документа. Улучшите безопасность вашего PDF с помощью комплексных функций подписи Aspose.PDF, адаптированных для бесшовной интеграции в .NET-приложения",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Securing PDF, signing PDF, digital signature, electronic signature, PKCS1, PKCS7, digest algorithms, Aspose.PDF, C# PDF manipulation, timestamp signature",
    "wordcount": "213",
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
    "dateModified": "2025-04-09",
    "description": "Этот раздел описывает функции использования подписи и защиты вашего PDF-документа с помощью C#"
}
</script>

Этот раздел описывает, как безопасно цифрово подписывать PDF-документы с помощью C#. Термины электронная подпись и цифровая подпись используются взаимозаменяемо, но по сути они различны. Более общим образом, цифровая подпись сопровождается печатью, одобренной [сертификационным центром](https://en.wikipedia.org/wiki/Certificate_authority), и используется для защиты подписанного документа от подделки. Вместо этого электронная подпись часто используется для демонстрации намерения подписать документ.

Aspose.PDF поддерживает цифровые подписи:
- PKCS1 с алгоритмом подписи RSA и дайджестом SHA-1.
- PKCS7 с алгоритмом подписи RSA и дайджестом SHA-1.
- PKCS7 отделенная с алгоритмами подписи DSA, RSA и ECDSA. Поддерживаемые алгоритмы дайджеста зависят от алгоритма подписи.
- Подпись с временной меткой.

Алгоритмы дайджеста для PKCS7 отделенной:
- DSA - SHA-1.
- RSA - SHA-1, SHA-256, SHA-384, SHA-512.
- ECDSA - SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384, SHA3-512.

Рекомендуется избегать цифровых подписей с алгоритмом дайджеста SHA-1 из-за его небезопасности.

- [Цифровая подпись PDF-файла](/pdf/ru/net/digitally-sign-pdf-file/)
- [Установить привилегии, зашифровать и расшифровать PDF-файл](/pdf/ru/net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [Извлечь информацию об изображении и подписи](/pdf/ru/net/extract-image-and-signature-information/)
- [Подписать PDF-документ с помощью смарт-карты](/pdf/ru/net/sign-pdf-document-from-smart-card/)
- [Пользовательский обработчик безопасности](/pdf/ru/net/custom-security-handler/)

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