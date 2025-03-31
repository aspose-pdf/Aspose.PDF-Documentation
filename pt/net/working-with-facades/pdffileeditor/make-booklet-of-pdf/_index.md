---
title: Criar Booklet de PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /pt/net/make-booklet-of-pdf/
description: Esta seção explica como criar um booklet de PDF com Aspose.PDF Facades usando a classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Make Booklet of PDF",
    "alternativeHeadline": "Create Booklets from PDFs with Enhanced Flexibility",
    "abstract": "O recurso Criar Booklet de PDF no Aspose.PDF permite que os usuários criem facilmente booklets a partir de arquivos PDF usando a classe PdfFileEditor. Essa funcionalidade suporta tanto caminhos de arquivos quanto streams, permitindo a personalização dos tamanhos das páginas e a especificação de páginas esquerda e direita para um controle de saída aprimorado. Esta ferramenta poderosa simplifica o processo de criação de booklets, tornando-se um recurso essencial para a manipulação de PDFs.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "946",
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
    "url": "/net/make-booklet-of-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/make-booklet-of-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Criar Booklet de PDF Usando Caminhos de Arquivo

O método [MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite que você crie um booklet do arquivo PDF de entrada e o salve no arquivo PDF de saída. Esta sobrecarga permite que você crie um booklet usando caminhos de arquivo. O seguinte trecho de código mostra como criar um booklet usando caminhos de arquivo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletInput.pdf", dataDir + "MakeBookletUsingPaths_out.pdf");
}
```

## Criar Booklet de PDF Usando Tamanho de Página e Caminhos de Arquivo

O método [MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite que você crie um booklet do arquivo PDF de entrada e o salve no arquivo PDF de saída. Esta sobrecarga permite que você crie um booklet usando caminhos de arquivo. Você também pode definir o tamanho da página do arquivo PDF de saída com esta sobrecarga. O seguinte trecho de código mostra como criar um booklet usando tamanho de página e caminhos de arquivo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletInput.pdf", dataDir + "MakeBookletUsingPageSizeAndPaths_out.pdf", PageSize.A5);
}
```

## Criar Booklet de PDF Usando Tamanho de Página, Páginas Esquerda e Direita Especificadas, e Caminhos de Arquivo

O método [MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite que você crie um booklet do arquivo PDF de entrada e o salve no arquivo PDF de saída. Esta sobrecarga permite que você crie um booklet usando caminhos de arquivo. Você também pode definir o tamanho da página do arquivo PDF de saída e especificar páginas particulares para os lados esquerdo e direito do arquivo PDF de saída com esta sobrecarga. O seguinte trecho de código mostra como criar um booklet usando tamanho de página, páginas esquerda e direita especificadas e caminhos de arquivo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeSpecifiedLeftAndRightPagesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Set left and right pages
    var leftPages = new int[] { 1, 5 };
    var rightPages = new int[] { 2, 3 };
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletMultiplePagesInput.pdf", dataDir + "MakeBookletUsingLeftRightPagesAndPaths_out.pdf", PageSize.A5, leftPages, rightPages);
}
```

## Criar Booklet de PDF Usando Páginas Esquerda e Direita Especificadas, e Caminhos de Arquivo

O método [MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite que você crie um booklet do arquivo PDF de entrada e o salve no arquivo PDF de saída. Esta sobrecarga permite que você crie um booklet usando caminhos de arquivo. Você também pode especificar páginas particulares para os lados esquerdo e direito do arquivo PDF de saída com esta sobrecarga. O seguinte trecho de código mostra como criar um booklet usando páginas esquerda e direita especificadas e caminhos de arquivo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingSpecifiedLeftAndRightPagesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Set left and right pages
    var leftPages = new int[] { 1, 5 };
    var rightPages = new int[] { 2, 3 };
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletMultiplePagesInput.pdf", dataDir + "MakeBookletUsingLeftRightPagesAndPaths_out.pdf", leftPages, rightPages);
}
```

## Criar Booklet de PDF Usando Streams

O método [MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite que você crie um booklet do stream PDF de entrada e o salve nos streams PDF de saída. Esta sobrecarga permite que você crie um booklet usando streams em vez de caminhos de arquivo. O seguinte trecho de código mostra como criar um booklet usando streams.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingStreams_out.pdf", FileMode.Create))
        {
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream);
        }
    }
}
```

## Criar Booklet de PDF Usando Tamanho de Página e Streams

O método [MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite que você crie um booklet do stream PDF de entrada e o salve no stream PDF de saída. Esta sobrecarga permite que você crie um booklet usando streams em vez de caminhos de arquivo. Você também pode definir o tamanho da página do stream PDF de saída com esta sobrecarga. O seguinte trecho de código mostra como criar um booklet usando tamanho de página e streams.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingPageSizeAndStreams_out.pdf", FileMode.Create))
        {
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream, PageSize.A5);
        }
    }
}
```

## Criar Booklet de PDF Usando Tamanho de Página, Páginas Esquerda e Direita Especificadas, e Streams

O método [MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite que você crie um booklet do stream PDF de entrada e o salve no stream PDF de saída. Esta sobrecarga permite que você crie um booklet usando streams em vez de caminhos de arquivo. Você também pode definir o tamanho da página do arquivo PDF de saída e especificar páginas particulares para os lados esquerdo e direito do stream PDF de saída com esta sobrecarga. O seguinte trecho de código mostra como criar um booklet usando tamanho de página, páginas esquerda e direita especificadas e streams.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeSpecifiedLeftAndRightPagesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletMultiplePagesInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingPageSizeLeftRightPagesAndStreams_out.pdf", FileMode.Create))
        {
            // Set left and right pages
            var leftPages = new int[] { 1, 5 };
            var rightPages = new int[] { 2, 3 };
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream, PageSize.A5, leftPages, rightPages);
        }
    }
}
```

## Criar Booklet de PDF Usando Páginas Esquerda e Direita Especificadas, e Streams

O método [MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite que você crie um booklet do stream PDF de entrada e o salve no stream PDF de saída. Esta sobrecarga permite que você crie um booklet usando streams em vez de caminhos de arquivo. Você também pode especificar páginas particulares para os lados esquerdo e direito do stream PDF de saída com esta sobrecarga. O seguinte trecho de código mostra como criar um booklet usando páginas esquerda e direita especificadas e streams.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingSpecifiedLeftAndRightPagesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletMultiplePagesInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingLeftRightPagesAndStreams_out.pdf", FileMode.Create))
        {
            // Set left and right pages
            var leftPages = new int[] { 1, 5 };
            var rightPages = new int[] { 2, 3 };
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream, leftPages, rightPages);
        }
    }
}
```