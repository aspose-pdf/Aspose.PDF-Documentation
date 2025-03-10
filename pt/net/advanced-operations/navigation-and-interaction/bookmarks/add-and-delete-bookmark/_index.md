---
title: Adicionar e Excluir um Marcador
linktitle: Adicionar e Excluir um Marcador
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /pt/net/add-and-delete-bookmark/
description: Você pode adicionar um marcador a um documento PDF com C#. É possível excluir todos ou marcadores específicos de um documento PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add and Delete a Bookmark",
    "alternativeHeadline": "Manage PDF Bookmarks: Add and Delete with Ease",
    "abstract": "O novo recurso permite que os usuários gerenciem eficientemente marcadores dentro de documentos PDF usando C#. Você pode facilmente adicionar novos marcadores ou excluir os existentes, seja para remover todos os marcadores ou direcionar entradas específicas. Essa funcionalidade melhora a navegação e organização do documento para uma melhor experiência do usuário.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "add bookmark, delete bookmark, PDF document, C# programming, OutlineItemCollection, OutlineCollection, child bookmark, parent bookmark",
    "wordcount": "851",
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
    "url": "/net/add-and-delete-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-and-delete-bookmark/"
    },
    "dateModified": "2024-11-25",
    "description": "Você pode adicionar um marcador a um documento PDF com C#. É possível excluir todos ou marcadores específicos de um documento PDF."
}
</script>

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

## Adicionar um Marcador a um Documento PDF

Os marcadores são mantidos na coleção [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) do objeto Document, que está na coleção [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).

Para adicionar um marcador a um PDF:

1. Abra um documento PDF usando o objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Crie um marcador e defina suas propriedades.
1. Adicione a coleção [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) à coleção de Outlines.

O seguinte trecho de código mostra como adicionar um marcador em um documento PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddBookmark.pdf"))
    {
        // Create a bookmark object
        var pdfOutline = new Aspose.Pdf.OutlineItemCollection(document.Outlines);
        pdfOutline.Title = "Test Outline";
        pdfOutline.Italic = true;
        pdfOutline.Bold = true;

        // Set the destination page number
        pdfOutline.Action = new Aspose.Pdf.Annotations.GoToAction(document.Pages[1]);

        // Add bookmark in the document's outline collection.
        document.Outlines.Add(pdfOutline);

        // Save PDF document
        document.Save(dataDir + "AddBookmark_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "AddBookmark.pdf");

    // Create a bookmark object
    var pdfOutline = new Aspose.Pdf.OutlineItemCollection(document.Outlines);
    pdfOutline.Title = "Test Outline";
    pdfOutline.Italic = true;
    pdfOutline.Bold = true;

    // Set the destination page number
    pdfOutline.Action = new Aspose.Pdf.Annotations.GoToAction(document.Pages[1]);

    // Add bookmark in the document's outline collection.
    document.Outlines.Add(pdfOutline);

    // Save PDF document
    document.Save(dataDir + "AddBookmark_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Adicionar um Marcador Filho ao Documento PDF

Os marcadores podem ser aninhados, indicando uma relação hierárquica com marcadores pai e filho. Este artigo explica como adicionar um marcador filho, ou seja, um marcador de segundo nível, a um PDF.

Para adicionar um marcador filho a um arquivo PDF, primeiro adicione um marcador pai:

1. Abra um documento.
1. Adicione um marcador à [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection), definindo suas propriedades.
1. Adicione a OutlineItemCollection à coleção [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) do objeto Document.

O marcador filho é criado da mesma forma que o marcador pai, explicado acima, mas é adicionado à coleção de Outlines do marcador pai.

Os seguintes trechos de código mostram como adicionar um marcador filho a um documento PDF.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddChildBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddChildBookmark.pdf"))
    {
        // Create a parent bookmark object
        var pdfOutline = new Aspose.Pdf.OutlineItemCollection(document.Outlines);
        pdfOutline.Title = "Parent Outline";
        pdfOutline.Italic = true;
        pdfOutline.Bold = true;

        // Create a child bookmark object
        var pdfChildOutline = new Aspose.Pdf.OutlineItemCollection(document.Outlines);
        pdfChildOutline.Title = "Child Outline";
        pdfChildOutline.Italic = true;
        pdfChildOutline.Bold = true;

        // Add child bookmark in parent bookmark's collection
        pdfOutline.Add(pdfChildOutline);

        // Add parent bookmark in the document's outline collection.
        document.Outlines.Add(pdfOutline);

        // Save PDF document
        document.Save(dataDir + "AddChildBookmark_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddChildBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "AddChildBookmark.pdf");

    // Create a parent bookmark object
    var pdfOutline = new Aspose.Pdf.OutlineItemCollection(document.Outlines);
    pdfOutline.Title = "Parent Outline";
    pdfOutline.Italic = true;
    pdfOutline.Bold = true;

    // Create a child bookmark object
    var pdfChildOutline = new Aspose.Pdf.OutlineItemCollection(document.Outlines);
    pdfChildOutline.Title = "Child Outline";
    pdfChildOutline.Italic = true;
    pdfChildOutline.Bold = true;

    // Add child bookmark in parent bookmark's collection
    pdfOutline.Add(pdfChildOutline);

    // Add parent bookmark in the document's outline collection.
    document.Outlines.Add(pdfOutline);

    // Save PDF document
    document.Save(dataDir + "AddChildBookmark_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Excluir Todos os Marcadores de um Documento PDF

Todos os marcadores em um PDF estão na coleção [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection). Este artigo explica como excluir todos os marcadores de um arquivo PDF.

Para excluir todos os marcadores de um arquivo PDF:

1. Chame o método Delete da coleção [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).
1. Salve o arquivo modificado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) do objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

Os seguintes trechos de código mostram como excluir todos os marcadores de um documento PDF.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteAllBookmarks.pdf"))
    {
        // Delete all bookmarks
        document.Outlines.Delete();

        // Save PDF document
        document.Save(dataDir + "DeleteAllBookmarks_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "DeleteAllBookmarks.pdf");

    // Delete all bookmarks
    document.Outlines.Delete();

    // Save PDF document
    document.Save(dataDir + "DeleteAllBookmarks_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Excluir um Marcador Específico de um Documento PDF

Para excluir um marcador específico de um arquivo PDF:

1. Passe o título do marcador como parâmetro para o método Delete da coleção [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).
1. Em seguida, salve o arquivo atualizado com o método Save do objeto Document.

A classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) fornece a coleção [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection). O método [Delete](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection/methods/delete) remove qualquer marcador com o título passado para o método.

Os seguintes trechos de código mostram como excluir um marcador específico do documento PDF.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteParticularBookmark.pdf"))
    {
        // Delete particular outline by Title
        document.Outlines.Delete("Child Outline");

        // Save PDF document
        document.Save(dataDir + "DeleteParticularBookmark_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "DeleteParticularBookmark.pdf");

    // Delete particular outline by Title
    document.Outlines.Delete("Child Outline");

    // Save PDF document
    document.Save(dataDir + "DeleteParticularBookmark_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

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