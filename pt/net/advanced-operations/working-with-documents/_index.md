---
title: Trabalhando com Documentos PDF usando C#
linktitle: Trabalhando com Documentos
type: docs
weight: 10
url: /pt/net/working-with-documents/
description: Este artigo descreve quais manipulações podem ser feitas com o documento com a biblioteca Aspose.PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-document/
    - /net/working-with-document-facades/
    - /net/create-document/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabalhando com Documentos PDF usando C#",
    "alternativeHeadline": "Manipulando Documentos PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos pdf",
    "keywords": "pdf, c#, documentos pdf",
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
    "url": "/net/working-with-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-documents/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artigo descreve quais manipulações podem ser feitas com o documento com a biblioteca Aspose.PDF."
}
</script>
PDF representa o Formato de Documento Portátil, usado para exibir documentos de forma eletrônica independente do software, hardware ou sistema operacional em que são visualizados.

O PDF é um padrão aberto, mantido pela Organização Internacional para Padronização (ISO) hoje.

O objetivo original era preservar e proteger o conteúdo e o layout de um documento - não importa em qual plataforma ou programa de computador ele seja visualizado. É por isso que os PDFs são difíceis de editar e, às vezes, até mesmo extrair informações deles é um desafio.

Mas **Aspose.PDF for .NET** pode ajudá-lo a lidar com a maioria das tarefas que surgem ao trabalhar com um documento PDF.

Você é capaz de fazer o seguinte:

- [Formatar Documento PDF](/pdf/pt/net/formatting-pdf-document/) - criar um documento, obter e definir propriedades do documento, incorporar fontes e outras operações com arquivos PDF.
- [Manipular Documento PDF](/pdf/pt/net/manipulate-pdf-document/) - validar um documento PDF para o padrão PDF A, trabalhar com TOC, definir data de expiração do PDF, e etc.
- [Otimizar PDF](/pdf/pt/net/optimize-pdf/) - otimizar conteúdo da página, otimizar tamanho do arquivo, remover objetos não utilizados, comprimir todas as imagens para uma otimização de documento bem-sucedida.
- [Otimizar PDF](/pdf/pt/net/optimize-pdf/) - otimize o conteúdo da página, reduza o tamanho do arquivo, remova objetos não utilizados, comprima todas as imagens para uma otimização de documentos bem-sucedida.
- [Mesclar PDF](/pdf/pt/net/merge-pdf-documents/) - mesclar vários arquivos PDF em um único documento PDF usando C#.
- [Dividir PDF](/pdf/pt/net/split-document/) - dividir páginas de PDF em arquivos PDF individuais em suas aplicações .NET.
- [Concatenar arquivos PDF em uma pasta](/pdf/pt/net/concatenating-all-pdf-files-in-particular-folder/) - concatenar todos os arquivos PDF em uma pasta específica usando a classe PdfFileEditor.
- [Concatenar vários arquivos PDF usando MemoryStreams](/pdf/pt/net/concatenate-pdf-documents/) - você aprenderá como concatenar vários arquivos PDF usando MemoryStreams com C#.
- [Trabalhando com Títulos](/pdf/pt/net/working-with-headings/) - você pode criar numeração nos títulos do seu documento PDF com C#.

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

