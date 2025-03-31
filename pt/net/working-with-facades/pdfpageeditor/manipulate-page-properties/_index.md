---
title: Manipular Propriedades da Página
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /pt/net/manipulate-page-properties/
description: Esta seção explica como manipular Propriedades da Página com Aspose.PDF Facades usando a Classe PdfPageEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipulate Page Properties",
    "alternativeHeadline": "Enhance PDF Page Control with PdfPageEditor Features",
    "abstract": "Apresentando a classe PdfPageEditor, uma ferramenta poderosa para gerenciar propriedades de páginas PDF com Aspose.PDF for .NET Facades. Este recurso permite que os desenvolvedores recuperem e modifiquem atributos essenciais da página, como rotação, níveis de zoom e dimensões da página, proporcionando controle refinado sobre a apresentação do conteúdo PDF. Com métodos diretos para obter e definir propriedades, incluindo a capacidade de redimensionar conteúdos de páginas específicas, aprimorar documentos PDF nunca foi tão fácil.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "483",
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
    "url": "/net/manipulate-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-page-properties/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Obter Propriedades da Página PDF de um Arquivo PDF Existente

[PdfPageEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfpageeditor) permite que você trabalhe com páginas individuais do arquivo PDF. Ele ajuda você a obter as propriedades da página individual, como diferentes tamanhos de caixa de página, rotação da página, zoom da página, etc. Para obter essas propriedades, você precisa criar um objeto [PdfPageEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfpageeditor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.facade/bindpdf/methods/3). Depois disso, você pode usar diferentes métodos para obter as propriedades da página, como [GetPageRotation](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfpageeditor/methods/getpagerotation), [GetPages](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfpageeditor/methods/getpages), [GetPageBoxSize](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfpageeditor/methods/getpageboxsize), etc.

O seguinte trecho de código mostra como obter propriedades da página PDF de um arquivo PDF existente.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPdfPageProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var pageEditor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        pageEditor.BindPdf(dataDir + "input.pdf");

        // Get page properties and print them to the console
        Console.WriteLine($"Page 1 Rotation: {pageEditor.GetPageRotation(1)}");
        Console.WriteLine($"Total Pages: {pageEditor.GetPages()}");
        Console.WriteLine($"Trim Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "trim")}");
        Console.WriteLine($"Art Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "art")}");
        Console.WriteLine($"Bleed Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "bleed")}");
        Console.WriteLine($"Crop Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "crop")}");
        Console.WriteLine($"Media Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "media")}");
    }
}
```

## Definir Propriedades da Página PDF em um Arquivo PDF Existente

Para definir propriedades da página, como rotação da página, zoom ou ponto de origem, você precisa usar a classe [PdfPageEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfpageeditor). Esta classe fornece diferentes métodos e propriedades para definir essas propriedades da página. Primeiro de tudo, você precisa criar um objeto da classe [PdfPageEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfpageeditor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.facade/bindpdf/methods/3). Depois disso, você pode usar esses métodos e propriedades para definir as propriedades da página. Finalmente, salve o arquivo PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document/methods/save).

O seguinte trecho de código mostra como definir propriedades da página PDF em um arquivo PDF existente.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPdfPageProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var pageEditor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        pageEditor.BindPdf(dataDir + "input.pdf");

        // Set page properties
        // Move origin from (0,0)
        pageEditor.MovePosition(100, 100);

        // Set page rotations
        var pageRotations = new System.Collections.Hashtable
        {
            { 1, 90 },
            { 2, 180 },
            { 3, 270 }
        };

        // Set zoom where 1.0f = 100% zoom
        pageEditor.Zoom = 2.0f;

        // Save PDF document
        pageEditor.Save(dataDir + "SetPageProperties_out.pdf");
    }
}
```

## Redimensionar Conteúdos de Páginas Específicas em um Arquivo PDF

O método ResizeContents da classe [PdfPageEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfpageeditor) permite que você redimensione os conteúdos da página em um arquivo PDF. A classe [ContentsResizeParameters](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.pdffileeditor/contentsresizeparameters) é usada para especificar os parâmetros a serem usados para redimensionar a(s) página(s), por exemplo, margens em porcentagem ou unidades, etc. Você pode redimensionar todas as páginas ou especificar um array de páginas a serem redimensionadas usando o método ResizeContents.

O seguinte trecho de código mostra como redimensionar os conteúdos de algumas páginas específicas do arquivo PDF.

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ResizePdfPageContents()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create PdfFileEditor Object
     var fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();

     // Open PDF Document
     using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
     {
         // Specify Parameters to be used for resizing
         var parameters = new Aspose.Pdf.Facades.PdfFileEditor.ContentsResizeParameters(
             // Left margin = 10% of page width
             PdfFileEditor.ContentsResizeValue.Percents(10),
             // New contents width calculated automatically as width - left margin - right margin (100% - 10% - 10% = 80%)
             null,
             // Right margin is 10% of page
             PdfFileEditor.ContentsResizeValue.Percents(10),
             // Top margin = 10% of height
             PdfFileEditor.ContentsResizeValue.Percents(10),
             // New contents height is calculated automatically (similar to width)
             null,
             // Bottom margin is 10%
             PdfFileEditor.ContentsResizeValue.Percents(10)
         );

         // Resize Page Contents
         fileEditor.ResizeContents(document, new[] { 1, 2 }, parameters);

         // Save PDF document
         document.Save(dataDir + "ResizePageContents_out.pdf");
     }
 }
```