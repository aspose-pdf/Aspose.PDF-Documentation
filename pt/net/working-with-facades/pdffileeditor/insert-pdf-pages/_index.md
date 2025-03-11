---
title: Inserir páginas PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /pt/net/insert-pdf-pages/
description: Esta seção explica como inserir páginas PDF com Aspose.PDF Facades usando a classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Insert PDF pages",
    "alternativeHeadline": "Insert Specific PDF Pages into Existing Documents",
    "abstract": "Otimize sua gestão de PDF com o novo recurso que permite aos usuários inserir páginas específicas de um PDF em outro usando a classe Aspose.PDF for .NET PdfFileEditor. Essa funcionalidade suporta tanto a inserção de páginas baseada em intervalo quanto em array, aumentando a eficiência do fluxo de trabalho ao combinar documentos de forma contínua através de caminhos de arquivo ou streams",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "751",
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
    "url": "/net/insert-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/insert-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Inserir Páginas PDF Entre Dois Números Usando Caminhos de Arquivo

Um intervalo específico de páginas pode ser inserido de um PDF em outro usando o método [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor). Para fazer isso, você precisa de um arquivo PDF de entrada no qual deseja inserir as páginas, um arquivo de origem do qual as páginas precisam ser retiradas para inserção, um local onde as páginas devem ser inseridas e um intervalo de páginas do arquivo de origem que devem ser inseridas no arquivo PDF de entrada. Esse intervalo é especificado com os parâmetros de página inicial e página final. Finalmente, o arquivo PDF de saída é salvo com o intervalo especificado de páginas inseridas no arquivo de entrada. O seguinte trecho de código mostra como inserir páginas PDF entre dois números usando streams de arquivo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertPdfPagesBetweenTwoNumbersUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Insert pages
    pdfEditor.Insert(
        dataDir + "MultiplePages.pdf", 1, 
        dataDir + "InsertPages.pdf", 2, 5, 
        dataDir + "InsertPagesBetweenNumbers_out.pdf");
}
```

## Inserir Array de Páginas PDF Usando Caminhos de Arquivo

Se você deseja inserir algumas páginas específicas em outro arquivo PDF, pode usar uma sobrecarga do método [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) que requer um array inteiro de páginas. Neste array, você pode especificar quais páginas específicas deseja inserir no arquivo PDF de entrada. Para fazer isso, você precisa de um arquivo PDF de entrada no qual deseja inserir as páginas, um arquivo de origem do qual as páginas precisam ser retiradas para inserção, um local onde as páginas devem ser inseridas e um array inteiro das páginas do arquivo de origem que devem ser inseridas no arquivo PDF de entrada. Este array contém uma lista de páginas específicas que você está interessado em inserir no arquivo PDF de entrada. Finalmente, o arquivo PDF de saída é salvo com o array especificado de páginas inseridas no arquivo de entrada. O seguinte trecho de código mostra como inserir um array de páginas PDF usando caminhos de arquivo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertArrayOfPdfPagesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    var pagesToInsert = new int[] { 2, 3 };
    // Insert pages
    pdfEditor.Insert(
        dataDir + "MultiplePages.pdf", 1, 
        dataDir + "InsertPages.pdf", pagesToInsert, 
        dataDir + "InsertArrayOfPages_out.pdf");
}
```

## Inserir Páginas PDF entre Dois Números Usando Streams

Se você deseja inserir o intervalo de páginas usando streams, você só precisa usar a sobrecarga apropriada do método [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor). Para fazer isso, você precisa de um stream PDF de entrada no qual deseja inserir as páginas, um stream de origem do qual as páginas precisam ser retiradas para inserção, um local onde as páginas devem ser inseridas e um intervalo de páginas do stream de origem que devem ser inseridas no stream PDF de entrada. Esse intervalo é especificado com os parâmetros de página inicial e página final. Finalmente, o stream PDF de saída é salvo com o intervalo especificado de páginas inseridas no stream de entrada. O seguinte trecho de código mostra como inserir páginas PDF entre dois números usando streams.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertPdfPagesBetweenTwoNumbersUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var portStream = new FileStream(dataDir + "InsertPages.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "InsertPagesBetweenNumbersUsingStreams_out.pdf", FileMode.Create))
            {
                // Insert pages
                pdfEditor.Insert(inputStream, 1, portStream, 1, 4, outputStream);
            }
        }
    }
}
```

## Inserir Array de Páginas PDF Usando Streams

Você também pode inserir um array de páginas em outro arquivo PDF usando streams com a ajuda da sobrecarga apropriada do método Insert que requer um array inteiro de páginas. Neste array, você pode especificar quais páginas específicas deseja inserir no stream PDF de entrada. Para fazer isso, você precisa de um stream PDF de entrada no qual deseja inserir as páginas, um stream de origem do qual as páginas precisam ser retiradas para inserção, um local onde as páginas devem ser inseridas e um array inteiro das páginas do stream de origem que devem ser inseridas no arquivo PDF de entrada. Este array contém uma lista de páginas específicas que você está interessado em inserir no stream PDF de entrada. Finalmente, o stream PDF de saída é salvo com o array especificado de páginas inseridas no arquivo de entrada. O seguinte trecho de código mostra como inserir um array de páginas PDF usando streams.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertArrayOfPdfPagesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Pages to insert
    var pagesToInsert = new int[] { 2, 3 };
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var portStream = new FileStream(dataDir + "InsertPages.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "InsertPagesUsingStreams_out.pdf", FileMode.Create))
            {
                // Insert pages
                pdfEditor.Insert(inputStream, 1, portStream, pagesToInsert, outputStream);
            }
        }
    }
}
```