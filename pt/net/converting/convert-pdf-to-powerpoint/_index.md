---
title: Converter PDF para PowerPoint em .NET
linktitle: Converter PDF para PowerPoint
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /pt/net/convert-pdf-to-powerpoint/
lastmod: "2021-11-01"
description: Aspose.PDF permite que você converta PDF para o formato PPT (PowerPoint) usando .NET. Uma maneira é a possibilidade de converter PDF para PPTX com Slides como Imagens.
lastmod: "2021-10-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to PowerPoint in .NET",
    "alternativeHeadline": "Convert PDF Documents to PowerPoint Presentations Efficiently in C#",
    "abstract": "Aspose.PDF for .NET introduz um recurso poderoso que permite a conversão sem costura de documentos PDF para o formato PowerPoint (PPTX), permitindo que cada página PDF se transforme em um slide distinto. Com a opção de renderizar texto como selecionável ou como imagens, os usuários podem personalizar facilmente suas apresentações enquanto acompanham o progresso da conversão de forma eficiente. Otimize seu fluxo de trabalho de documentos aproveitando essa funcionalidade inovadora para aumentar a produtividade",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "931",
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
    "url": "/net/convert-pdf-to-powerpoint/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-powerpoint/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Visão Geral

Este artigo explica como **converter PDF para PowerPoint usando C#**. Ele cobre estes tópicos.

- [Converter PDF para PowerPoint](#csharp-pdf-to-powerpoint)

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

## Conversão de C# PDF para PowerPoint e PPTX

<a name="csharp-convert-pdf-to-powerpoint" id="csharp-convert-pdf-to-powerpoint"><strong>Converter PDF para PowerPoint</strong></a>

**Aspose.PDF for .NET** permite que você acompanhe o progresso da conversão de PDF para PPTX.

Temos uma API chamada Aspose.Slides que oferece o recurso de criar e manipular apresentações PPT/PPTX. Esta API também fornece o recurso de converter arquivos PPT/PPTX para o formato PDF. Recentemente, recebemos solicitações de muitos de nossos clientes para suportar a capacidade de transformação de PDF para o formato PPTX. A partir do lançamento de Aspose.PDF for .NET 10.3.0, introduzimos um recurso para transformar documentos PDF em formato PPTX. Durante essa conversão, as páginas individuais do arquivo PDF são convertidas em slides separados no arquivo PPTX.

Durante a conversão de PDF para <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>, o texto é renderizado como Texto onde você pode selecionar/atualizá-lo. Observe que, para converter arquivos PDF para o formato PPTX, o Aspose.PDF fornece uma classe chamada [`PptxSaveOptions`](https://reference.aspose.com/pdf/pt/net/aspose.pdf/pptxsaveoptions). Um objeto da classe PptxSaveOptions é passado como um segundo argumento para o [`Document.Save(..) method`](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document/methods/save). O seguinte trecho de código mostra o processo de conversão de arquivos PDF para o formato PPTX.

## Conversão simples de PDF para PowerPoint usando C# e Aspose.PDF .NET

Para converter PDF para PPTX, Aspose.PDF for .NET recomenda usar os seguintes passos de código.

<a name="csharp-pdf-to-powerpoint"><strong>Converter PDF para PowerPoint</strong></a>

1. Crie uma instância da classe [Document](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document).
2. Crie uma instância da classe [PptxSaveOptions](https://reference.aspose.com/pdf/pt/net/aspose.pdf/pptxsaveoptions).
3. Use o método **Save** do objeto **Document** para salvar o PDF como PPTX.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToPPTX()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate PptxSaveOptions object
        var saveOptions = new Aspose.Pdf.PptxSaveOptions();

        // Save the file in PPTX format
        document.Save(dataDir + "PDFToPPT_out.pptx", saveOptions);
    }
}
```

## Converter PDF para PPTX com Slides como Imagens

{{% alert color="success" %}}
**Tente converter PDF para PowerPoint online**

Aspose.PDF for .NET apresenta a você um aplicativo online gratuito ["PDF para PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão PDF para PPTX com Aplicativo Gratuito](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

Caso você precise converter um PDF pesquisável para PPTX como imagens em vez de texto selecionável, o Aspose.PDF fornece esse recurso através da classe [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/pt/net/aspose.pdf/pptxsaveoptions). Para alcançar isso, defina a propriedade [SlidesAsImages](https://reference.aspose.com/pdf/pt/net/aspose.pdf/pptxsaveoptions/properties/slidesasimages) da classe [PptxSaveOptios](https://reference.aspose.com/pdf/pt/net/aspose.pdf/pptxsaveoptions) como 'true', conforme mostrado no seguinte exemplo de código.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToPPTWithSlidesAsImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate PptxSaveOptions object
        var saveOptions = new Aspose.Pdf.PptxSaveOptions
        {
            SlidesAsImages = true
        };

        // Save the file in PPTX format with slides as images
        document.Save(dataDir + "PDFToPPT_out.pptx", saveOptions);
    }
}
```

## Detalhe do Progresso da Conversão de PPTX

Aspose.PDF for .NET permite que você acompanhe o progresso da conversão de PDF para PPTX. A classe [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/pt/net/aspose.pdf/pptxsaveoptions) fornece a propriedade [CustomProgressHandler](https://reference.aspose.com/pdf/pt/net/aspose.pdf/pptxsaveoptions/properties/customprogresshandler) que pode ser especificada para um método personalizado para rastrear o progresso da conversão, conforme mostrado no seguinte exemplo de código.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToPPTWithCustomProgressHandler()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {

        // Instantiate PptxSaveOptions object
        var saveOptions = new Aspose.Pdf.PptxSaveOptions();

        // Specify custom progress handler
        saveOptions.CustomProgressHandler = ShowProgressOnConsole;

        // Save the file in PPTX format with progress tracking
        document.Save(dataDir + "PDFToPPTWithProgressTracking_out.pptx", saveOptions);
    }
}

 // Define the method to handle progress events and display them on the console
private static void ShowProgressOnConsole(Aspose.Pdf.UnifiedSaveOptions.ProgressEventHandlerInfo eventInfo)
{
    switch (eventInfo.EventType)
    {
        case Aspose.Pdf.ProgressEventType.TotalProgress:
            // Display overall progress of the conversion
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Conversion progress: {eventInfo.Value}%.");
            break;

        case Aspose.Pdf.ProgressEventType.ResultPageCreated:
            // Display progress of the page layout creation
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Result page {eventInfo.Value} of {eventInfo.MaxValue} layout created.");
            break;

        case Aspose.Pdf.ProgressEventType.ResultPageSaved:
            // Display progress of the page being exported
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Result page {eventInfo.Value} of {eventInfo.MaxValue} exported.");
            break;

        case Aspose.Pdf.ProgressEventType.SourcePageAnalysed:
            // Display progress of the source page analysis
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Source page {eventInfo.Value} of {eventInfo.MaxValue} analyzed.");
            break;

        default:
            break;
    }
}
```