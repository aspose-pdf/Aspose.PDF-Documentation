---
title: Trabalhando com Anotações
linktitle: Anotações em PDF
type: docs
weight: 100
url: /net/annotations/
description: Esta seção mostra como usar todos os tipos de anotações em seu arquivo PDF com a biblioteca Aspose.PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/working-with-annotations/
    - /net/annotation/
    - /net/working-with-annotations-facades/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Anotações em PDF",
    "alternativeHeadline": "Trabalhando com Anotações em PDFs",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, anotações",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe de Documentação Aspose.PDF",
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
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/annotations/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta seção mostra como usar todos os tipos de anotações em seu arquivo PDF com a biblioteca Aspose.PDF."
}
</script>

O conteúdo dentro de uma página PDF é difícil de editar, mas a especificação PDF define um conjunto completo de objetos que podem ser adicionados às páginas PDF sem alterar o conteúdo da página.

Esses objetos são chamados de anotações, e seu propósito varia desde marcar o conteúdo da página até implementar recursos interativos como formulários.

Visualizadores de PDF geralmente permitem a criação e edição de vários tipos de anotações, como destaques de texto, notas, linhas ou formas. Independentemente dos tipos de anotações que podem ser criadas, os visualizadores de PDF que seguem a especificação PDF também devem suportar a renderização para todos os tipos de anotações.

A anotação é uma parte importante do arquivo PDF. Usando Aspose.PDF para .NET, você pode adicionar uma nova anotação, editar uma anotação existente e deletar anotações, entre outros. Esta seção aborda o seguinte tópico:

Você é capaz de fazer o seguinte:

- [Visão Geral das Anotações](/pdf/net/overview-of-annotations/) - aprenda quais tipos de anotações são definidos pela especificação PDF e o que Aspose.PDF suporta.
- [Adicionar, Deletar e Obter Anotação](/pdf/net/add-delete-and-get-annotation/) - esta seção explica como trabalhar com todos os tipos de anotações permitidas.
- [Adicionar, Excluir e Obter Anotação](/pdf/net/add-delete-and-get-annotation/) - esta seção explica como trabalhar com todos os tipos de anotações permitidas.
- [Importar e exportar anotação com formato XFDF](/pdf/net/import-export-xfdf/) - A biblioteca Aspose.PDF fornece métodos para importar e exportar dados de anotações para arquivos XFDF.

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


