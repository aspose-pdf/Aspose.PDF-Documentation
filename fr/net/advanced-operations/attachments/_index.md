---
title: Travailler avec des pièces jointes dans un PDF
linktitle: Travailler avec des pièces jointes
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 190
url: /fr/net/attachments/
description: Utilisez l'API PDF C# pour accéder, ajouter et supprimer des pièces jointes dans des fichiers PDF en utilisant C# depuis vos applications. Guide complet avec des exemples de code C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Attachments in PDF",
    "alternativeHeadline": "Effortlessly Manage PDF Attachments with C#",
    "abstract": "Découvrez comment gérer efficacement les pièces jointes dans des fichiers PDF en utilisant la puissante API PDF C#. Cette fonctionnalité permet aux développeurs d'accéder, d'ajouter et de supprimer divers types de fichiers attachés aux PDF, accompagnée d'exemples de code C# détaillés pour une intégration transparente dans les applications. Améliorez vos capacités de manipulation de PDF en tirant parti de ce guide complet",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "C#, PDF API, attachments in PDF, add attachments, remove attachments, extract attachments, Aspose.PDF for .NET, manipulate PDF documents, save attachment to file, delete attachment from PDF",
    "wordcount": "181",
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
    "url": "/net/attachments/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/attachments/"
    },
    "dateModified": "2024-11-25",
    "description": "Utilisez l'API PDF C# pour accéder, ajouter et supprimer des pièces jointes dans des fichiers PDF en utilisant C# depuis vos applications. Guide complet avec des exemples de code C#."
}
</script>

Dans cette section, nous expliquerons comment travailler avec des pièces jointes dans un PDF en utilisant Aspose.PDF for .NET.
Une pièce jointe est un fichier supplémentaire qui est attaché à un document parent, il peut s'agir de divers types de fichiers, tels que pdf, word, image ou d'autres fichiers.
Vous apprendrez comment ajouter des pièces jointes à un pdf, obtenir les informations d'une pièce jointe et l'enregistrer dans un fichier, supprimer la pièce jointe d'un PDF par programmation avec C#.

- [Ajouter une pièce jointe à un document PDF](/pdf/fr/net/add-attachment-to-pdf-document/)
- [Extraire et enregistrer une pièce jointe](/pdf/fr/net/extract-and-save-an-attachment/)
- [Supprimer une pièce jointe d'un PDF existant](/pdf/fr/net/removing-attachment-from-an-existing-pdf/)
- [Portfolio](/pdf/fr/net/portfolio/)

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