---
title: Adicionar Páginas ao Documento PDF
linktitle: Adicionar Páginas
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /pt/net/add-pages/
description: Explore como adicionar páginas a um PDF existente em .NET com Aspose.PDF para aprimorar e expandir seus documentos.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Pages to PDF Document",
    "alternativeHeadline": "Insert and Manage Pages in PDF Easily with C#",
    "abstract": "O recurso em Aspose.PDF for .NET permite que os usuários insiram facilmente páginas em um documento PDF em qualquer local especificado, aprimorando a flexibilidade e a organização do documento. Essa funcionalidade não apenas suporta a adição de páginas, mas também inclui opções para mover ou remover páginas existentes usando C#. Simplifique sua gestão de PDF com essa adição intuitiva ao seu kit de ferramentas de desenvolvimento",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Pages to PDF, insert PDF page, empty page PDF, C# PDF manipulation, PDF document generation, PageCollection, Aspose.PDF for .NET, move PDF pages, remove PDF pages, add pages to PDF",
    "wordcount": "651",
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
    "url": "/net/add-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "Este artigo ensina como inserir (adicionar) uma página na localização desejada do arquivo PDF. Aprenda como mover, remover (excluir) páginas de um arquivo PDF usando C#."
}
</script>

Aspose.PDF for .NET API fornece total flexibilidade para trabalhar com páginas em um documento PDF usando C# ou qualquer outra linguagem .NET. Ele mantém todas as páginas de um documento PDF na [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) que pode ser usada para trabalhar com páginas PDF.
Aspose.PDF for .NET permite que você insira uma página em um documento PDF em qualquer local do arquivo, bem como adicione páginas ao final de um arquivo PDF.
Esta seção mostra como adicionar páginas a um PDF usando C#.

## Adicionar ou Inserir Página em um Arquivo PDF

Aspose.PDF for .NET permite que você insira uma página em um documento PDF em qualquer local do arquivo, bem como adicione páginas ao final de um arquivo PDF.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

### Inserir Página Vazia em um Arquivo PDF na Localização Desejada

Para inserir uma página vazia em um arquivo PDF:

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) com o arquivo PDF de entrada.
1. Chame o método [Insert](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection/methods/insert) da coleção [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) com o índice especificado.
1. Salve o PDF de saída usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

O seguinte trecho de código mostra como inserir uma página em um arquivo PDF.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertAnEmptyPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "InsertEmptyPage.pdf"))
    {
       // Insert an empty page in a PDF
       document.Pages.Insert(2);
        // Save PDF document
       document.Save(dataDir + "InsertEmptyPage_out.pdf");
    }
}
```

No exemplo acima, adicionamos uma página vazia com parâmetros padrão. Se você precisar fazer o tamanho da página igual ao de outra página no documento, deve adicionar
algumas linhas de código:

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertAnEmptyPageWithParameters()
{
    var page = document.Pages.Insert(2);
    //copy page parameters from page 1
    page.ArtBox = document.Pages[1].ArtBox;
    page.BleedBox = document.Pages[1].BleedBox;
    page.CropBox = document.Pages[1].CropBox;
    page.MediaBox = document.Pages[1].MediaBox;
    page.TrimBox = document.Pages[1].TrimBox;
}
```

### Adicionar uma Página Vazia ao Final de um Arquivo PDF

Às vezes, você quer garantir que um documento termine em uma página vazia. Este tópico explica como inserir uma página vazia ao final do documento PDF.

Para inserir uma página vazia ao final de um arquivo PDF:

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) com o arquivo PDF de entrada.
1. Chame o método [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) da coleção [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection), sem parâmetros.
1. Salve o PDF de saída usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

O seguinte trecho de código mostra como inserir uma página vazia ao final de um arquivo PDF.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertAnEmptyPageAtTheEnd()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "InsertEmptyPageAtEnd.pdf"))
    {
        // Insert an empty page at the end of a PDF file
        document.Pages.Add();
        // Save PDF document
        document.Save(dataDir + "InsertEmptyPageAtEnd_out.pdf");
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