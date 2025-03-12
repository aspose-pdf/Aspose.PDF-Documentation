---
title: Fazer NUp de arquivos PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /pt/net/make-nup-of-pdf-files/
description: Este artigo mostra como fazer NUp de arquivos PDF usando a classe PdfFileEditor do Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Make NUp of PDF files",
    "alternativeHeadline": "Create NUp PDFs with Flexible Input Methods",
    "abstract": "O recurso NUp em Aspose.PDF for .NET permite que os usuários combinem eficientemente vários arquivos PDF em um único documento de saída, personalizando o tamanho da página e as configurações de layout. Essa funcionalidade suporta tanto caminhos de arquivos quanto streams, permitindo uma integração flexível em vários fluxos de trabalho enquanto melhora a apresentação do documento.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "895",
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
    "url": "/net/make-nup-of-pdf-files/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/make-nup-of-pdf-files/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Fazer NUp de PDF Usando Caminhos de Arquivos

O método [MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite que você faça NUp do arquivo PDF de entrada e o salve no arquivo PDF de saída. Esta sobrecarga permite que você faça NUp usando caminhos de arquivos. O seguinte trecho de código mostra como fazer NUP usando caminhos de arquivos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "MakeNupInput.pdf", dataDir + "MakeNupInput2.pdf", "MakeNUpUsingPaths_out.pdf");
}
```

## Fazer NUp Usando Tamanho de Página e Caminhos de Arquivos

O método [MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite que você faça NUp do arquivo PDF de entrada e o salve no arquivo PDF de saída. Esta sobrecarga permite que você faça NUp usando caminhos de arquivos. Você também pode definir o tamanho da página do arquivo PDF de saída usando esta sobrecarga. O seguinte trecho de código mostra como fazer NUp usando tamanho de página e caminhos de arquivos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupUsingPageSizeAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "MakeNupMultiplePagesInput.pdf", dataDir + "MakeNUpUsingPageSizeAndPaths_out.pdf", 2, 3, PageSize.A5);
}
```

## Fazer NUp de PDF Usando Tamanho de Página, Valores Horizontais e Verticais, e Caminhos de Arquivos

O método [MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite que você faça NUp do arquivo PDF de entrada e o salve no arquivo PDF de saída. Esta sobrecarga permite que você faça NUp usando caminhos de arquivos. Você também pode definir o tamanho da página do arquivo PDF de saída e o número horizontal e vertical de páginas em cada página de saída usando esta sobrecarga. O seguinte trecho de código mostra como fazer NUp usando tamanho de página, valores horizontais e verticais, e caminhos de arquivos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingPageSizeHorizontalAndVerticalValuesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "MakeNupInput.pdf", "MakeNUpUsingPageSizeHorizontalAndVerticalValues_out.pdf", 2, 3);
}
```

## Fazer NUp de PDF Usando Array de Arquivos PDF e Caminhos de Arquivos

O método [MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite que você faça NUp de um array de arquivos PDF de entrada e os salve em um único arquivo PDF de saída. Esta sobrecarga permite que você faça NUp usando caminhos de arquivos. O seguinte trecho de código mostra como fazer NUp usando um array de arquivos PDF e caminhos de arquivos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingArrayOfPdfFilesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create array of files
    string[] filesArray = new string[2];
    filesArray[0] = dataDir + "MakeNupInput.pdf";
    filesArray[1] = dataDir + "MakeNupInput2.pdf";
    // Make NUp
    pdfEditor.MakeNUp(filesArray, dataDir + "MakeNupUsingArrayOfFilesAndPaths_out.pdf", true);
}
```

## Fazer NUp de PDF Usando Streams

O método [MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite que você faça NUp do stream PDF de entrada e o salve no stream PDF de saída. Esta sobrecarga permite que você faça NUp usando streams em vez de caminhos de arquivos. O seguinte trecho de código mostra como fazer NUp usando streams.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream1 = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var inputStream2 = new FileStream(dataDir + "MakeNupInput2.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "MakeNUpUsingStreams_out.pdf", FileMode.Create))
            {
                // Make NUp
                pdfEditor.MakeNUp(inputStream1, inputStream2, outputStream);
            }
        }
    }
}
```

## Fazer NUp de PDF Usando Tamanho de Página e Streams

O método [MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite que você faça NUp do stream PDF de entrada e o salve no stream PDF de saída. Esta sobrecarga permite que você faça NUp usando streams em vez de caminhos de arquivos. Você também pode definir o tamanho da página do stream PDF de saída usando esta sobrecarga. O seguinte trecho de código mostra como fazer NUp usando tamanho de página e streams.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingPageSizeAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeNUpUsingPageSizeAndStreams_out.pdf", FileMode.Create))
        {
            // Make NUp
            pdfEditor.MakeNUp(inputStream, outputStream, 2, 3, PageSize.A5);    
        }    
    }
}
```

## Fazer NUp de PDF Usando Tamanho de Página, Valores Horizontais e Verticais, e Streams

O método [MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite que você faça NUp do stream PDF de entrada e o salve no stream PDF de saída. Esta sobrecarga permite que você faça NUp usando streams em vez de caminhos de arquivos. Você também pode definir o tamanho da página do stream PDF de saída e o número horizontal e vertical de páginas em cada página de saída usando esta sobrecarga. O seguinte trecho de código mostra como fazer NUp usando tamanho de página, valores horizontais e verticais, e streams.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingPageSizeHorizontalAndVerticalValuesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeNUpUsingPageSizeHorizontalVerticalValuesAndStreams_out.pdf", FileMode.Create))
        {
            // Make NUp
            pdfEditor.MakeNUp(inputStream, outputStream, 2, 3); 
        }
    }
}
```

## Fazer NUp de PDF Usando Array de Arquivos PDF e Streams

O método [MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite que você faça NUp de um array de streams PDF de entrada e os salve em um único stream PDF de saída. Esta sobrecarga permite que você faça NUp usando streams em vez de caminhos de arquivos. O seguinte trecho de código mostra como fazer NUp usando um array de arquivos PDF usando streams.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingArrayOfPdfFilesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var stream1 = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var stream2 = new FileStream(dataDir + "MakeNupInput2.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "MakeNUpUsingArrayOfFilesAndStreams_out.pdf", FileMode.Create))
            {
                var fileStreams = new Stream[2];
                fileStreams[0] = stream1;
                fileStreams[1] = stream2;
                // Make NUp
                pdfEditor.MakeNUp(fileStreams, outputStream, true);
            }
        }
    }
}
```