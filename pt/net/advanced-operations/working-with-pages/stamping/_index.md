---
title: Carimbando com Aspose.PDF usando C#
linktitle: Carimbando
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 120
url: /pt/net/stamping/
description: Esta seção descreve como adicionar carimbos de imagem e carimbos de texto a uma página PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/adding-stamp-in-a-pdf-file/
    - /net/adding-text-stamp-watermark/
    - /net/add-text-and-image-stamp/
    - /net/add-pdf-page-stamp/
    - /net/extract-image-and-change-position-of-a-stamp/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with PDF Pages in C#",
    "alternativeHeadline": "Enhance PDF Management with C# Page Features",
    "abstract": "Descubra as capacidades avançadas de **Aspose.PDF for .NET** para gerenciar páginas PDF, incluindo adicionar, mover e excluir páginas com precisão. Este recurso permite que os usuários aprimorem seus documentos PDF incorporando cabeçalhos, rodapés, marcas d'água e tamanhos de página personalizados, tudo através de código C# intuitivo. Otimize seus fluxos de trabalho de documentos com manipulação e funcionalidades de personalização de PDF sem costura.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, add pages, rotate pages, delete pages, add watermarks, page numbering, crop pages, Aspose.PDF for .NET",
    "wordcount": "450",
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
    "url": "/net/working-with-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

Um carimbo em um documento PDF é análogo a aplicar um carimbo de borracha em um documento em papel. O carimbo no arquivo PDF fornece informações adicionais para o arquivo PDF, como proteger o arquivo PDF para ser usado por outros e confirmar a segurança do conteúdo do arquivo PDF. **Aspose.PDF for .NET** permite adicionar carimbo de imagem ou carimbo de texto ao seu documento PDF.

Verifique as seções a seguir para aprender como adicionar um carimbo com C#:

- [Adicionar carimbos de imagem na página PDF](/pdf/net/image-stamps-in-pdf-page/) - adicionar carimbo de imagem, controlar a qualidade da imagem, carimbo de imagem como fundo do seu arquivo PDF.
- [Adicionar carimbos de texto no arquivo PDF](/pdf/net/text-stamps-in-the-pdf-file/) - adicionar carimbo de texto, definir alinhamento para o objeto TextStamp, preencher texto de contorno como carimbo no arquivo PDF.
- [Carimbos de página no arquivo PDF](/pdf/net/page-stamps-in-the-pdf-file/) - adicionar um carimbo de página ao documento PDF usando a classe PdfPageStamp.

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