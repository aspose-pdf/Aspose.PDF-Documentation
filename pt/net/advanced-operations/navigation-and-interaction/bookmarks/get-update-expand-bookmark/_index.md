---
title: Obter, Atualizar e Expandir um Marcador
linktitle: Obter, Atualizar e Expandir um Marcador
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /pt/net/get-update-and-expand-bookmark/
description: Este artigo descreve como usar marcadores em um arquivo PDF com nossa biblioteca Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get, Update and Expand a Bookmark",
    "alternativeHeadline": "Effortlessly Manage PDF Bookmarks",
    "abstract": "O novo recurso Obter, Atualizar e Expandir um Marcador aprimora a biblioteca Aspose.PDF for .NET, fornecendo aos usuários a capacidade de recuperar, modificar e expandir visualmente marcadores dentro de documentos PDF. Essa funcionalidade permite uma navegação e organização eficientes do conteúdo PDF, facilitando a gestão de documentos complexos com estruturas de marcadores hierárquicas.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "get bookmarks, update bookmarks, expand bookmarks, PDF bookmarks, Aspose.PDF for .NET, OutlineCollection, OutlineItemCollection, child bookmarks",
    "wordcount": "1050",
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
    "url": "/net/get-update-and-expand-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-update-and-expand-bookmark/"
    },
    "dateModified": "2024-11-25",
    "description": "Este artigo descreve como usar marcadores em um arquivo PDF com nossa biblioteca Aspose.PDF for .NET."
}
</script>

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

## Obter Marcadores

A coleção [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) do objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) contém todos os marcadores de um arquivo PDF. Este artigo explica como obter marcadores de um arquivo PDF e como descobrir em qual página um determinado marcador está.

Para obter os marcadores, percorra a coleção [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) e obtenha cada marcador na OutlineItemCollection. A OutlineItemCollection fornece acesso a todos os atributos do marcador. O seguinte trecho de código mostra como obter marcadores do arquivo PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetBookmarks.pdf"))
    {
        // Loop through all the bookmarks
        foreach (var outlineItem in document.Outlines)
        {
            Console.WriteLine(outlineItem.Title);
            Console.WriteLine(outlineItem.Italic);
            Console.WriteLine(outlineItem.Bold);
            Console.WriteLine(outlineItem.Color);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "GetBookmarks.pdf");

    // Loop through all the bookmarks
    foreach (var outlineItem in document.Outlines)
    {
        Console.WriteLine(outlineItem.Title);
        Console.WriteLine(outlineItem.Italic);
        Console.WriteLine(outlineItem.Bold);
        Console.WriteLine(outlineItem.Color);
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Obtendo o Número da Página de um Marcador

Uma vez que você adicionou um marcador, pode descobrir em qual página ele está obtendo o número da página de destino associado ao objeto Bookmark.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetBookmarkPageNumber()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Create PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "GetBookmarks.pdf");

        // Extract bookmarks
        Aspose.Pdf.Facades.Bookmarks bookmarks = bookmarkEditor.ExtractBookmarks();

        foreach (var bookmark in bookmarks)
        {
            string strLevelSeparator = string.Empty;

            for (int i = 1; i < bookmark.Level; i++)
            {
                strLevelSeparator += "----";
            }

            Console.WriteLine("{0}Title: {1}", strLevelSeparator, bookmark.Title);
            Console.WriteLine("{0}Page Number: {1}", strLevelSeparator, bookmark.PageNumber);
            Console.WriteLine("{0}Page Action: {1}", strLevelSeparator, bookmark.Action);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetBookmarkPageNumber()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Create PdfBookmarkEditor
    using var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor();

    // Bind PDF document
    bookmarkEditor.BindPdf(dataDir + "GetBookmarks.pdf");

    // Extract bookmarks
    Aspose.Pdf.Facades.Bookmarks bookmarks = bookmarkEditor.ExtractBookmarks();

    foreach (var bookmark in bookmarks)
    {
        string strLevelSeparator = string.Empty;

        for (int i = 1; i < bookmark.Level; i++)
        {
            strLevelSeparator += "----";
        }

        Console.WriteLine("{0}Title: {1}", strLevelSeparator, bookmark.Title);
        Console.WriteLine("{0}Page Number: {1}", strLevelSeparator, bookmark.PageNumber);
        Console.WriteLine("{0}Page Action: {1}", strLevelSeparator, bookmark.Action);
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Obter Marcadores Filhos de um Documento PDF

Os marcadores podem ser organizados em uma estrutura hierárquica, com pais e filhos. Para obter todos os marcadores, percorra as coleções Outlines do objeto Document. No entanto, para obter marcadores filhos também, percorra todos os marcadores em cada objeto [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) obtido no primeiro loop. Os seguintes trechos de código mostram como obter marcadores filhos de um documento PDF.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetChildBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetChildBookmarks.pdf"))
    {
        // Loop through all the bookmarks
        foreach (var outlineItem in document.Outlines)
        {
            Console.WriteLine(outlineItem.Title);
            Console.WriteLine(outlineItem.Italic);
            Console.WriteLine(outlineItem.Bold);
            Console.WriteLine(outlineItem.Color);

            if (outlineItem.Count > 0)
            {
                Console.WriteLine("Child Bookmarks");

                // There are child bookmarks then loop through that as well
                foreach (var childOutline in outlineItem)
                {
                    Console.WriteLine(childOutline.Title);
                    Console.WriteLine(childOutline.Italic);
                    Console.WriteLine(childOutline.Bold);
                    Console.WriteLine(childOutline.Color);
                }
            }
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetChildBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "GetChildBookmarks.pdf");

    // Loop through all the bookmarks
    foreach (var outlineItem in document.Outlines)
    {
        Console.WriteLine(outlineItem.Title);
        Console.WriteLine(outlineItem.Italic);
        Console.WriteLine(outlineItem.Bold);
        Console.WriteLine(outlineItem.Color);

        if (outlineItem.Count > 0)
        {
            Console.WriteLine("Child Bookmarks");

            // There are child bookmarks then loop through that as well
            foreach (var childOutline in outlineItem)
            {
                Console.WriteLine(childOutline.Title);
                Console.WriteLine(childOutline.Italic);
                Console.WriteLine(childOutline.Bold);
                Console.WriteLine(childOutline.Color);
            }
        }
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Atualizar Marcadores em um Documento PDF

Para atualizar um marcador em um arquivo PDF, primeiro, obtenha o marcador específico da coleção OutlineColletion do objeto Document especificando o índice do marcador. Uma vez que você tenha recuperado o marcador no objeto [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection), você pode atualizar suas propriedades e, em seguida, salvar o arquivo PDF atualizado usando o método Save. Os seguintes trechos de código mostram como atualizar marcadores em um documento PDF.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateBookmarks.pdf"))
    {
        // Get a bookmark object
        var pdfOutline = document.Outlines[1];
        pdfOutline.Title = "Updated Outline";
        pdfOutline.Italic = true;
        pdfOutline.Bold = true;

        // Save PDF document
        document.Save(dataDir + "UpdateBookmarks_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "UpdateBookmarks.pdf");

    // Get a bookmark object
    var pdfOutline = document.Outlines[1];
    pdfOutline.Title = "Updated Outline";
    pdfOutline.Italic = true;
    pdfOutline.Bold = true;

    // Save PDF document
    document.Save(dataDir + "UpdateBookmarks_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Atualizar Marcadores Filhos em um Documento PDF

Para atualizar um marcador filho:

1. Recupere o marcador filho que você deseja atualizar do arquivo PDF, primeiro obtendo o marcador pai e, em seguida, o marcador filho usando os valores de índice apropriados.
1. Salve o arquivo PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/1).

{{% alert color="primary" %}}

Obtenha um marcador da coleção OutlineCollection do objeto Document especificando o índice do marcador, e então obtenha o marcador filho especificando o índice deste marcador pai.

{{% /alert %}}

O seguinte trecho de código mostra como atualizar marcadores filhos em um documento PDF.

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateChildBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateChildBookmarks.pdf"))
    {
        // Get a bookmark object
        var pdfOutline = document.Outlines[1];

        // Get child bookmark object
        Aspose.Pdf.OutlineItemCollection childOutline = pdfOutline[1];
        childOutline.Title = "Updated Outline";
        childOutline.Italic = true;
        childOutline.Bold = true;

        // Save PDF document
        document.Save(dataDir + "UpdateChildBookmarks_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateChildBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "UpdateChildBookmarks.pdf");

    // Get a bookmark object
    var pdfOutline = document.Outlines[1];

    // Get child bookmark object
    Aspose.Pdf.OutlineItemCollection childOutline = pdfOutline[1];
    childOutline.Title = "Updated Outline";
    childOutline.Italic = true;
    childOutline.Bold = true;

    // Save PDF document
    document.Save(dataDir + "UpdateChildBookmarks_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Marcadores Expandidos ao visualizar o documento

Os marcadores são mantidos na coleção [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) do objeto Document, que está na coleção [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection). No entanto, podemos ter a necessidade de ter todos os marcadores expandidos ao visualizar o arquivo PDF.

Para atender a essa necessidade, podemos definir o status de abertura para cada item de contorno/marcador como Aberto. O seguinte trecho de código mostra como definir o status de abertura para cada marcador como expandido em um documento PDF.

{{< tabs tabID="6" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExpandBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Set page view mode i.e. show thumbnails, full-screen, show attachment panel
        document.PageMode = Aspose.Pdf.PageMode.UseOutlines;

        // Traverse through each Outline item in outlines collection of PDF file
        foreach (var item in document.Outlines)
        {
            // Set open status for outline item
            item.Open = true;
        }

        // Save PDF document
        document.Save(dataDir + "ExpandBookmarks_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExpandBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Set page view mode i.e. show thumbnails, full-screen, show attachment panel
    document.PageMode = Aspose.Pdf.PageMode.UseOutlines;

    // Traverse through each Outline item in outlines collection of PDF file
    foreach (var item in document.Outlines)
    {
        // Set open status for outline item
        item.Open = true;
    }

    // Save PDF document
    document.Save(dataDir + "ExpandBookmarks_out.pdf");
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