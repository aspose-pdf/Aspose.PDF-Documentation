---
title: Adicionar, Excluir e Obter Anotação
linktitle: Adicionar, Excluir e Obter Anotação
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /pt/net/add-delete-and-get-annotation/
description: Com Aspose.PDF for .NET você pode adicionar, excluir e obter anotações do seu arquivo PDF. Verifique todas as listas de anotações para resolver sua tarefa.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add, Delete and Get Annotation",
    "alternativeHeadline": "Manage PDF Annotations with Aspose.PDF for .NET",
    "abstract": "Aprimore suas capacidades de manipulação de PDF com o novo recurso Adicionar, Excluir e Obter Anotação no Aspose.PDF for .NET. Essa funcionalidade poderosa permite que os usuários gerenciem anotações em seus arquivos PDF de forma contínua, oferecendo edição simplificada e melhor interação com o conteúdo. Descubra como trabalhar com vários tipos de anotações para atender às suas necessidades específicas de documentos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "add annotation, delete annotation, get annotation, Aspose.PDF for .NET, PDF document generation, PDF annotations, multimedia annotation, PDF text annotation, highlights annotation, PDF manipulation library",
    "wordcount": "174",
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
    "url": "/net/add-delete-and-get-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-delete-and-get-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Com Aspose.PDF for .NET você pode adicionar, excluir e obter anotações do seu arquivo PDF. Verifique todas as listas de anotações para resolver sua tarefa."
}
</script>

**O que são anotações em documentos PDF?**

Esses são objetos adicionais que você adiciona ao seu arquivo para expandir o conteúdo do texto, fazer edições, comentários para outros usuários. Também é possível tornar o texto no documento mais legível, destacá-lo, sublinhá-lo ou adicionar texto completamente novo.

Agrupamos os diferentes tipos de anotações disponíveis para a biblioteca Aspose.PDF for .NET em grupos:

- [Anotação de Texto PDF](/pdf/net/text-annotation/)
- [Anotação de Destaques PDF](/pdf/net/highlights-annotation/)
- [Anotação de Figuras PDF](/pdf/net/figures-annotation/)
- [Anotação Multimídia](/pdf/net/multimedia-annotation/)
- [Anotações Pegajosas PDF](/pdf/net/sticky-annotations/)
- [Anotações de Link](/pdf/net/link-annotations/)
- [Anotações Extras](/pdf/net/extra-annotations/)

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