---
title: Dividir páginas PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /pt/net/split-pdf-pages/
description: Esta seção explica como dividir páginas PDF com Aspose.PDF Facades usando a classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Split PDF pages",
    "alternativeHeadline": "Effortlessly Split PDF Pages via File Paths and Streams",
    "abstract": "O novo recurso Dividir Páginas PDF em Aspose.PDF for .NET permite que os usuários dividam documentos PDF de forma eficiente em vários segmentos usando a classe PdfFileEditor. Essa funcionalidade suporta a divisão da primeira página até uma página especificada, divisão em conjuntos em massa e até mesmo isolamento de páginas individuais, tudo através de caminhos de arquivo ou streams, proporcionando opções versáteis para manipulação de PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1017",
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
    "url": "/net/split-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/split-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Dividir Páginas PDF a Partir da Primeira Usando Caminhos de Arquivo

O método [SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite que você divida o arquivo PDF começando pela primeira página e terminando no número da página especificada. Se você quiser manipular os arquivos PDF do disco, pode passar os caminhos dos arquivos PDF de entrada e saída para este método. O seguinte trecho de código mostra como dividir páginas PDF a partir da primeira usando caminhos de arquivo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesFromFirstUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Split pages
    pdfEditor.SplitFromFirst(dataDir + "MultiplePages.pdf", 3, dataDir + "SplitPagesUsingPaths_out.pdf");
}
```

## Dividir Páginas PDF a Partir da Primeira Usando Streams de Arquivo

O método [SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite que você divida o arquivo PDF começando pela primeira página e terminando no número da página especificada. Se você quiser manipular os arquivos PDF a partir dos streams, pode passar os streams de entrada e saída PDF para este método. O seguinte trecho de código mostra como dividir páginas PDF a partir da primeira usando streams de arquivo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesFromFirstUsingFileStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "SplitPagesUsingStreams_out.pdf", FileMode.Create))
        {
            // Split pages
            pdfEditor.SplitFromFirst(inputStream, 3, outputStream);
        }
    }
}
```

## Dividir Páginas PDF em Lotes Usando Caminhos de Arquivo

O método [SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittobulks/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite que você divida o arquivo PDF em vários conjuntos de páginas. Neste exemplo, precisamos de dois conjuntos de páginas (1, 2) e (5, 6). Se você quiser acessar o arquivo PDF do disco, precisará passar o PDF de entrada como caminho de arquivo. Este método retorna um array de MemoryStream. Você pode percorrer este array e salvar os conjuntos individuais de páginas como arquivos separados. O seguinte trecho de código mostra como dividir páginas PDF em lotes usando caminhos de arquivo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToBulkUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    var fileNumber = 1;
    // Create array of pages to split
    var numberOfPages = new int[][] { new int[] { 1, 2 }, new int[] { 3, 4 } };
    // Split to bulk
    var outBuffer = pdfEditor.SplitToBulks(dataDir + "MultiplePages.pdf", numberOfPages);
    // Save individual files
    foreach (var outStream in outBuffer)
    {
        using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
        {
            outStream.WriteTo(outFileStream);
            fileNumber++;
        }
    }
}
```

## Dividir Páginas PDF em Lotes Usando Streams

O método [SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittobulks/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite que você divida o arquivo PDF em vários conjuntos de páginas. Neste exemplo, precisamos de dois conjuntos de páginas (1, 2) e (5, 6). Você pode passar um stream para este método em vez de acessar o arquivo do disco. Este método retorna um array de MemoryStream. Você pode percorrer este array e salvar os conjuntos individuais de páginas como arquivos separados. O seguinte trecho de código mostra como dividir páginas PDF em lotes usando streams.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToBulkUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create input stream
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        var fileNumber = 1;
        // Create array of pages to split
        var numberOfPages = new int[][] { new int[] { 1, 2 }, new int[] { 3, 4 } };
        // Split to bulk
        var outBuffer = pdfEditor.SplitToBulks(inputStream, numberOfPages);
        // Save individual files
        foreach (var outStream in outBuffer)
        {
            using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
            {
                outStream.WriteTo(outFileStream);
                fileNumber++;
            }
        }
    }
}
```

## Dividir Páginas PDF até o Fim Usando Caminhos de Arquivo

O método [SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite que você divida o PDF a partir do número da página especificada até o final do arquivo PDF e salve-o como um novo PDF. Para fazer isso, usando caminhos de arquivo, você precisa passar os caminhos dos arquivos de entrada e saída e o número da página a partir da qual a divisão deve ser iniciada. O PDF de saída será salvo no disco. O seguinte trecho de código mostra como dividir páginas PDF até o fim usando caminhos de arquivo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToEndUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Split pages
    pdfEditor.SplitToEnd(dataDir + "MultiplePages.pdf", 3, dataDir + "SplitPagesToEndUsingPaths_out.pdf");
}
```

## Dividir Páginas PDF até o Fim Usando Streams

O método [SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite que você divida o PDF a partir do número da página especificada até o final do arquivo PDF e salve-o como um novo PDF. Para fazer isso, usando streams, você precisa passar os streams de entrada e saída e o número da página a partir da qual a divisão deve ser iniciada. O PDF de saída será salvo no stream de saída. O seguinte trecho de código mostra como dividir páginas PDF até o fim usando streams.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToEndUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "SplitPagesToEndUsingStreams_out.pdf", FileMode.Create))
        {
            // Split pages
            pdfEditor.SplitToEnd(inputStream, 3, outputStream);   
        }
    }
}
```

## Dividir PDF em Páginas Individuais Usando Caminhos de Arquivo

{{% alert color="primary" %}}

Você pode tentar dividir o documento PDF e visualizar os resultados online neste link:

[products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter) {{% /alert %}}

Para dividir o arquivo PDF em páginas individuais, você precisa passar o PDF como caminho de arquivo para o método [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index). Este método retornará um array de MemoryStream contendo páginas individuais do arquivo PDF. Você pode percorrer este array de MemoryStream e salvar páginas individuais como arquivos PDF individuais no disco. O seguinte trecho de código mostra como dividir PDF em páginas individuais usando caminhos de arquivo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfToIndividualPagesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    var fileNumber = 1;
    // Split to pages
    var outBuffer = pdfEditor.SplitToPages(dataDir + "splitPdfToIndividualPagesInput.pdf");
    // Save individual files
    foreach (var outStream in outBuffer)
    {
        using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
        {
            outStream.WriteTo(outFileStream);
            fileNumber++;
        }
    }
}
```

## Dividir PDF em Páginas Individuais Usando Streams

Para dividir o arquivo PDF em páginas individuais, você precisa passar o PDF como stream para o método [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index). Este método retornará um array de MemoryStream contendo páginas individuais do arquivo PDF. Você pode percorrer este array de MemoryStream e salvar páginas individuais como arquivos PDF individuais no disco, ou pode manter essas páginas individuais no stream de memória para uso posterior em sua aplicação. O seguinte trecho de código mostra como dividir PDF em páginas individuais usando streams.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfToIndividualPagesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create input stream
    using (var inputStream = new FileStream(dataDir + "splitPdfToIndividualPagesInput.pdf", FileMode.Open))
    {
        var fileNumber = 1;
        // Split to pages
        var outBuffer = pdfEditor.SplitToPages(inputStream);
        // Save individual files
        foreach (var outStream in outBuffer)
        {
            using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
            {
                outStream.WriteTo(outFileStream);
                fileNumber++;
            }
        }
    }
}
```