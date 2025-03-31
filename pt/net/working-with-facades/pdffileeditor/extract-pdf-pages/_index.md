---
title: Extrair páginas PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /pt/net/extract-pdf-pages/
description: Esta seção explica como extrair páginas PDF com Aspose.PDF Facades usando a classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract PDF pages",
    "alternativeHeadline": "Effortlessly Extract Selected Pages from PDF Files",
    "abstract": "O recurso Extrair Páginas PDF em Aspose.PDF for .NET Facades fornece aos usuários capacidades aprimoradas para extrair seletivamente páginas de documentos PDF. Ao utilizar a classe PdfFileEditor, os usuários podem extrair de forma eficiente um intervalo especificado ou um conjunto de páginas através de caminhos de arquivos ou streams, tornando a manipulação de documentos mais simplificada e flexível. Essa funcionalidade é particularmente benéfica para usuários que desejam personalizar seu conteúdo PDF sem alterar os arquivos originais.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "660",
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
    "url": "/net/extract-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Extrair Páginas PDF entre Dois Números Usando Caminhos de Arquivo

O método [Extract](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdffileeditor) permite extrair um intervalo especificado de páginas de um arquivo PDF. Esta sobrecarga permite que você extraia páginas enquanto manipula os arquivos PDF do disco. Esta sobrecarga requer os seguintes parâmetros: caminho do arquivo de entrada, página inicial, página final e caminho do arquivo de saída. As páginas da página inicial até a página final serão extraídas e a saída será salva no disco. O seguinte trecho de código mostra como extrair páginas PDF entre dois números usando caminhos de arquivo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_PDFPages_FilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // Extract pages
    pdfEditor.Extract(dataDir + "MultiplePages.pdf", 1, 3, dataDir + "ExtractPagesBetweenNumbers_out.pdf");
}
```

## Extrair Array de Páginas PDF Usando Caminhos de Arquivo

Se você não deseja extrair um intervalo de páginas, mas sim um conjunto de páginas específicas, o método [Extract](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) também permite fazer isso. Você primeiro precisa criar um array de inteiros com todos os números das páginas que precisam ser extraídas. Esta sobrecarga do método [Extract](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) aceita os seguintes parâmetros: arquivo PDF de entrada, array de inteiros das páginas a serem extraídas e arquivo PDF de saída. O seguinte trecho de código mostra como extrair páginas PDF usando caminhos de arquivo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_PDFPages_Streams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // Create streams
    using (FileStream inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (FileStream outputStream = new FileStream(dataDir + "ExtractPagesBetweenTwoNumbers_out.pdf", FileMode.Create))
        {
            // Extract pages
            pdfEditor.Extract(inputStream, 1, 3, outputStream);
        }
    }
}
```

## Extrair Páginas PDF entre Dois Números Usando Streams

O método [Extract](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdffileeditor) permite extrair um intervalo de páginas usando streams. Você precisa passar os seguintes parâmetros para esta sobrecarga: stream de entrada, página inicial, página final e stream de saída. As páginas especificadas pelo intervalo entre a página inicial e a página final serão extraídas do stream de entrada e salvas no stream de saída. O seguinte trecho de código mostra como extrair páginas PDF entre dois números usando streams.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_ArrayPDFPages_FilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();
    int[] pagesToExtract = new int[] { 1, 2 };
    // Extract pages
    pdfEditor.Extract(dataDir + "Extract.pdf", pagesToExtract, dataDir + "ExtractArrayOfPages_out.pdf");
}
```

## Extrair Array de Páginas PDF Usando Streams

Um array de páginas pode ser extraído do stream PDF e salvo no stream de saída usando a sobrecarga apropriada do método [Extract](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdffileeditor/methods/extract/index). Se você não deseja extrair um intervalo de páginas, mas sim um conjunto de páginas específicas, o método [Extract](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) também permite fazer isso. Você primeiro precisa criar um array de inteiros com todos os números das páginas que precisam ser extraídas. Esta sobrecarga do método [Extract](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) aceita os seguintes parâmetros: stream de entrada, array de inteiros das páginas a serem extraídas e stream de saída. O seguinte trecho de código mostra como extrair páginas PDF usando streams.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_ArrayPDFPages_Streams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    
    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // Create streams
    using (FileStream inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (FileStream outputStream = new FileStream(dataDir + "ExtractArrayOfPagesUsingStreams_out.pdf", FileMode.Create))
        {
            int[] pagesToExtract = new int[] { 1, 2 };
            // Extract pages
            pdfEditor.Extract(inputStream, pagesToExtract, outputStream);
        }
    }
}
```