---
title: Sécuriser et signer des PDF en C#
linktitle: Sécuriser et signer en PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 210
url: /fr/net/securing-and-signing/
description: Cette section décrit les fonctionnalités d'utilisation d'une signature et de sécurisation de votre document PDF en utilisant C#
lastmod: "2024-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - net/working-with-security-and-signatures/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Securing and signing PDF in C#",
    "alternativeHeadline": "Securely Digitally Sign PDFs with C#",
    "abstract": "Découvrez les capacités avancées de sécurisation et de signature numérique des documents PDF en utilisant C#. Cette fonctionnalité permet aux utilisateurs d'appliquer des signatures numériques robustes avec divers algorithmes et options de hachage, garantissant l'intégrité et l'authenticité du document. Améliorez la sécurité de votre PDF avec les fonctionnalités de signature complètes d'Aspose.PDF adaptées pour une intégration transparente dans les applications .NET",
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
    "description": "Cette section décrit les fonctionnalités d'utilisation d'une signature et de sécurisation de votre document PDF en utilisant C#"
}
</script>

Cette section décrit comment signer numériquement des documents PDF de manière sécurisée en utilisant C#. Les termes signature électronique et signature numérique sont utilisés de manière interchangeable, mais en réalité, les deux sont différents. Plus généralement, une signature numérique est accompagnée d'un [autorité de certification](https://en.wikipedia.org/wiki/Certificate_authority) approuvée et est utilisée pour protéger le document signé contre toute falsification. En revanche, une signature électronique est souvent utilisée pour démontrer l'intention de signer un document.

Aspose.PDF prend en charge les signatures numériques :
- PKCS1 avec algorithme de signature RSA et hachage SHA-1.
- PKCS7 avec algorithme de signature RSA et hachage SHA-1.
- PKCS7 détaché avec algorithmes de signature DSA, RSA et ECDSA. Les algorithmes de hachage pris en charge dépendent de l'algorithme de signature.
- Signature horodatée.

Algorithmes de hachage pour PKCS7 détaché :
- DSA - SHA-1.
- RSA - SHA-1, SHA-256, SHA-384, SHA-512.
- ECDSA - SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384, SHA3-512.

Il est recommandé d'éviter les signatures numériques avec l'algorithme de hachage SHA-1 en raison de son insécurité.

- [Signer numériquement un fichier PDF](/pdf/net/digitally-sign-pdf-file/)
- [Définir des privilèges, chiffrer et déchiffrer un fichier PDF](/pdf/net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [Extraire des informations sur les images et les signatures](/pdf/net/extract-image-and-signature-information/)
- [Signer un document PDF depuis une carte intelligente](/pdf/net/sign-pdf-document-from-smart-card/)

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