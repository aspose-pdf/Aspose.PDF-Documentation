---
title: Mover Páginas PDF programaticamente C#
linktitle: Mover Páginas PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /pt/net/move-pages/
description: Tente mover páginas para o local desejado ou para o final de um arquivo PDF usando Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Move PDF Pages programmatically C#",
    "alternativeHeadline": "Programmatically Rearrange PDF Pages with .NET",
    "abstract": "Aspose.PDF for .NET introduz um novo recurso poderoso que permite aos usuários mover programaticamente páginas PDF entre documentos ou reorganizá-las dentro do mesmo documento. Essa funcionalidade aprimora as capacidades de manipulação de PDF, permitindo que os desenvolvedores insiram páginas em locais designados e gerenciem facilmente a organização das páginas, mantendo a integridade do documento.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "668",
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
    "url": "/net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/move-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "Tente mover páginas para o local desejado ou para o final de um arquivo PDF usando Aspose.PDF for .NET."
}
</script>

## Movendo uma Página de um Documento PDF para Outro

Este tópico explica como mover uma página de um documento PDF para o final de outro documento usando C#.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

Para mover uma página, devemos:

1. Criar um objeto da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) com o arquivo PDF de origem.
1. Criar um objeto da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) com o arquivo PDF de destino.
1. Obter a Página da coleção [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. [Adicionar](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) a página ao documento de destino.
1. Salvar o PDF de saída usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).
1. [Excluir](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) a página no documento de origem.
1. Salvar o PDF de origem usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

O seguinte trecho de código mostra como mover uma página.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingAPageFromOnePdfDocumentToAnother()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF documents
    using (var srcDocument = new Aspose.Pdf.Document(dataDir + "MovingPageInput.pdf"))
    {
        using (var dstDocument = new Aspose.Pdf.Document())
        {
            var page = srcDocument.Pages[2];
            dstDocument.Pages.Add(page);
            // Save PDF document
            dstDocument.Save(dataDir + "MovingPage_out.pdf");
            srcDocument.Pages.Delete(2);
            // Save PDF document
            srcDocument.Save(dataDir + "MovingPageInput_out.pdf");
        }
    }
}
```

## Movendo um Conjunto de Páginas de um Documento PDF para Outro

1. Criar um objeto da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) com o arquivo PDF de origem.
1. Criar um objeto da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) com o arquivo PDF de destino.
1. Definir um array com os números das páginas a serem movidas.
1. Executar um loop através do array:
    1. Obter a Página da coleção [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
    1. [Adicionar](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) a página ao documento de destino.
1. Salvar o PDF de saída usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).
1. [Excluir](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/2) a página no documento de origem usando o array.
1. Salvar o PDF de origem usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

O seguinte trecho de código mostra como mover um conjunto de páginas de um documento PDF para outro.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingBunchOfPagesFromOnePdfDocumentToAnother()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF documents
    using (var srcDocument = new Aspose.Pdf.Document(dataDir + "MovingBunchOfPagesInput.pdf"))
    {
        using (var dstDocument = new Aspose.Pdf.Document())
        {
            var pages = new[] { 1, 3 };
            foreach (int pageIndex in pages)
            {
                var page = srcDocument.Pages[pageIndex];
                dstDocument.Pages.Add(page);
            }
            // Save PDF document
            dstDocument.Save(dataDir + "MovingBunchOfPages_out.pdf");
            srcDocument.Pages.Delete(pages);
            // Save PDF document
            srcDocument.Save(dataDir + "MovingBunchOfPagesInput_out.pdf";
        }
    }
}
```

## Movendo uma Página para um Novo Local no Documento PDF Atual

1. Criar um objeto da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) com o arquivo PDF de origem.
1. Obter a Página da coleção [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. [Adicionar](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) a página ao novo local (por exemplo, ao final).
1. [Excluir](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) a página no local anterior.
1. Salvar o PDF de saída usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingAPageInNewLocationInTheCurrentPdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "MovingAPageInNewLocationInTheCurrentPdfDocumentInput.pdf"))
    {
        var page = document.Pages[2];
        document.Pages.Add(page);
        document.Pages.Delete(2);
        // Save PDF document
        document.Save(dataDir + "MovingAPageInNewLocationInTheCurrentPdfDocument_out.pdf");
    }
}
```

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