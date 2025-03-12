---
title: Защита и подписание PDF-файлов на C#
linktitle: Защита и подписывание в PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 210
url: /ru/net/securing-and-signing/
description: В этом разделе описаны функции использования подписи и защиты PDF-документов с помощью C#.
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
    "abstract": "Откройте для себя расширенные возможности защиты и цифровой подписи PDF-документов с помощью C#. Эта функция позволяет пользователям применять надёжные цифровые подписи с различными алгоритмами и параметрами дайджеста, обеспечивая целостность и подлинность документа. Усильте безопасность ваших PDF-файлов с помощью комплексных функций подписания Aspose.PDF, адаптированных для беспроблемной интеграции в приложения .NET",
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
    "description": "Этот раздел описывает особенности использования подписи и защиты PDF-документа с помощью C#."
}
</script>

Этот раздел описывает, как безопасно и надёжно подписывать PDF-документы с помощью C#. Термины «электронная подпись» и «цифровая подпись» используются взаимозаменяемо, но по сути это разные понятия. В более общем смысле цифровая подпись сопровождается печатью, одобренной центром сертификации, и используется для защиты подписанного документа от несанкционированного доступа. Электронная подпись, напротив, часто используется для демонстрации намерения подписать документ.

Aspose.PDF поддерживает цифровые подписи:
* PKCS1 с алгоритмом подписи RSA и дайджестом SHA-1.
* PKCS7 с алгоритмом подписи RSA и дайджестом SHA-1.
* PKCS7 отдельно с алгоритмами подписи DSA, RSA и ECDSA. Поддерживаемые алгоритмы дайджеста зависят от алгоритма подписи.
* Подпись с отметкой времени.

Алгоритмы дайджеста для PKCS7 отдельно:
* DSA — SHA-1.
* RSA — SHA-1, SHA-256, SHA-384, SHA-512.
* ECDSA — SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384, SHA3-512.

Рекомендуется избегать использования цифровых подписей с алгоритмом дайджеста SHA-1 из-за его небезопасности.

- [Цифровое подписывание PDF-файла](/pdf/ru/net/digitally-sign-pdf-file/)
- [Установка привилегий, шифрование и расшифровка PDF-файла](/pdf/ru/net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [Извлечение информации об изображении и подписи](/pdf/ru/net/extract-image-and-signature-information/)
- [Подписание PDF-документа со смарт-карты](/pdf/ru/net/sign-pdf-document-from-smart-card/)

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