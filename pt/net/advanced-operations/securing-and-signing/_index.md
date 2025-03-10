---
title: Protegendo e assinando PDF em C#
linktitle: Protegendo e assinando em PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 210
url: /pt/net/securing-and-signing/
description: Esta seção descreve os recursos de uso de uma assinatura e proteção do seu documento PDF usando C#
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
    "abstract": "Descubra as capacidades avançadas de proteger e assinar digitalmente documentos PDF usando C#. Este recurso permite que os usuários apliquem assinaturas digitais robustas com vários algoritmos e opções de resumo, garantindo a integridade e autenticidade do documento. Melhore a segurança do seu PDF com as funcionalidades abrangentes de assinatura do Aspose.PDF, adaptadas para uma integração perfeita em aplicações .NET",
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
    "description": "Esta seção descreve os recursos de uso de uma assinatura e proteção do seu documento PDF usando C#"
}
</script>

Esta seção descreve como assinar digitalmente documentos PDF de forma segura usando C#. Os termos assinatura eletrônica e assinatura digital são usados de forma intercambiável, mas essencialmente os dois são diferentes. De forma mais geral, uma assinatura digital vem com um selo aprovado por uma [autoridade certificadora](https://en.wikipedia.org/wiki/Certificate_authority) e é usada para proteger o documento assinado contra adulterações. Em vez disso, uma assinatura eletrônica é frequentemente usada para demonstrar a intenção de assinar um documento.

Aspose.PDF suporta assinaturas digitais:
- PKCS1 com algoritmo de assinatura RSA e resumo SHA-1.
- PKCS7 com algoritmo de assinatura RSA e resumo SHA-1.
- PKCS7 destacado com algoritmos de assinatura DSA, RSA e ECDSA. Os algoritmos de resumo suportados dependem do algoritmo de assinatura.
- Assinatura com timestamp.

Algoritmos de resumo para PKCS7 destacado:
- DSA - SHA-1.
- RSA - SHA-1, SHA-256, SHA-384, SHA-512.
- ECDSA - SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384, SHA3-512.

É recomendado evitar assinaturas digitais com o algoritmo de resumo SHA-1 devido à sua insegurança.

- [Assinar digitalmente arquivo PDF](/pdf/pt/net/digitally-sign-pdf-file/)
- [Definir privilégios, criptografar e descriptografar arquivo PDF](/pdf/pt/net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [Extrair informações de imagem e assinatura](/pdf/pt/net/extract-image-and-signature-information/)
- [Assinar documento PDF de cartão inteligente](/pdf/pt/net/sign-pdf-document-from-smart-card/)

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