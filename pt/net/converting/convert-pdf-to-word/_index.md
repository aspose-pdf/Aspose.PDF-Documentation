---
title: Converter PDF em Documentos do Microsoft Word no .NET
linktitle: Converter PDF para Word
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /pt/net/convert-pdf-to-word/
lastmod: "2022-08-04"
description: Aprenda como escrever código C# para conversão de PDF para formatos do Microsoft Word com Aspose.PDF for .NET. e ajuste a conversão de PDF para DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to Microsoft Word Documents in .NET",
    "alternativeHeadline": "Seamlessly Convert PDFs to Word Documents with C#",
    "abstract": "Aspose.PDF for .NET apresenta um recurso poderoso para converter arquivos PDF em formatos do Microsoft Word (DOC e DOCX) usando C#. Essa funcionalidade não apenas melhora a edição de documentos, mas também fornece opções flexíveis para reconhecimento de texto e formatação, garantindo alta fidelidade entre o PDF de origem e o documento Word resultante.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1321",
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
    "url": "/net/convert-pdf-to-word/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-word/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Visão Geral

Este artigo explica como **converter PDF em Documentos do Microsoft Word usando C#**. Ele cobre os seguintes tópicos.

- [Converter PDF para DOC](#csharp-pdf-to-doc)
- [Converter PDF para DOCX](#csharp-pdf-to-docx)

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

## Conversão de PDF para DOC e DOCX

Uma das funcionalidades mais populares é a conversão de PDF para DOC do Microsoft Word, que torna o gerenciamento de conteúdo mais fácil. **Aspose.PDF for .NET** permite que você converta arquivos PDF para os formatos DOC e DOCX de forma rápida e eficiente.

## Converter arquivo PDF para DOC (Microsoft Word 97-2003)

Converta arquivos PDF para o formato DOC com facilidade e controle total. Aspose.PDF for .NET é flexível e suporta uma ampla variedade de conversões. Converter páginas de documentos PDF em imagens, por exemplo, é um recurso muito popular.

Muitos de nossos clientes solicitaram uma conversão de PDF para DOC: converter um arquivo PDF em um documento do Microsoft Word. Os clientes desejam isso porque arquivos PDF não podem ser facilmente editados, enquanto documentos do Word podem. Algumas empresas querem que seus usuários possam manipular texto, tabelas e imagens em arquivos que começaram como PDFs.

Mantendo viva a tradição de tornar as coisas simples e compreensíveis, Aspose.PDF for .NET permite que você transforme um arquivo PDF de origem em um arquivo DOC com duas linhas de código. Para realizar essa funcionalidade, introduzimos uma enumeração chamada SaveFormat e seu valor .Doc permite que você salve o arquivo de origem no formato do Microsoft Word.

O seguinte trecho de código C# mostra como converter um arquivo PDF em formato DOC.

<a name="csharp-pdf-to-doc" id="csharp-pdf-to-doc"><strong>Converter PDF para DOC</strong></a>

1. Crie uma instância do objeto [Document](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document/) com o documento PDF de origem.
2. Salve-o no formato **SaveFormat.Doc** chamando o método **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    usnig (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Save the file into MS document format
        document.Save(dataDir + "PDFToDOC_out.doc", SaveFormat.Doc);
    }
}
```

### Usando a Classe DocSaveOptions

A classe [`DocSaveOptions`](https://reference.aspose.com/pdf/pt/net/aspose.pdf/docsaveoptions) fornece inúmeras propriedades que melhoram a conversão de arquivos PDF para o formato DOC. Entre essas propriedades, Mode permite que você especifique o modo de reconhecimento para o conteúdo PDF. Você pode selecionar qualquer valor da enumeração RecognitionMode para esta propriedade. Cada um desses valores tem benefícios e limitações específicos:

- O modo [`Textbox`](https://reference.aspose.com/pdf/pt/net/aspose.pdf.docsaveoptions/recognitionmode) é rápido e bom para preservar a aparência original do arquivo PDF, mas a editabilidade do documento resultante pode ser limitada. Cada bloco de texto visualmente agrupado no PDF original é convertido em uma caixa de texto no documento de saída. Isso alcança a máxima semelhança com o original, então o documento de saída parece bom, mas consiste inteiramente de caixas de texto, que podem ser editadas no Microsoft Word, o que é bastante desafiador.
- [`Flow`](https://reference.aspose.com/pdf/pt/net/aspose.pdf.docsaveoptions/recognitionmode) é o modo de reconhecimento completo, onde o mecanismo realiza agrupamento e análise em múltiplos níveis para restaurar o documento original conforme a intenção do autor, enquanto produz um documento facilmente editável. A limitação é que o documento de saída pode parecer diferente do original.

A propriedade [`RelativeHorizontalProximity`](https://reference.aspose.com/pdf/pt/net/aspose.pdf/docsaveoptions/properties/relativehorizontalproximity) pode ser usada para controlar a proximidade relativa entre elementos textuais. Isso significa que a distância é normalizada pelo tamanho da fonte. Fontes maiores podem ter espaços maiores entre as sílabas e ainda serem consideradas um todo único. É especificado como uma porcentagem do tamanho da fonte; por exemplo, 1 = 100%. Isso significa que dois caracteres de 12pt colocados a 12 pt de distância são proximais.
- [`RecognitionBullets`](https://reference.aspose.com/pdf/pt/net/aspose.pdf/docsaveoptions/properties/recognizebullets) é usado para ativar o reconhecimento de marcadores durante a conversão.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWordDocAdvanced()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDF-to-DOC.pdf"))
    {
        var saveOptions = new Aspose.Pdf.DocSaveOptions
        {
            // Set format to save MS document
            Format = Aspose.Pdf.DocSaveOptions.DocFormat.Doc,
            // Set the recognition mode as Flow
            Mode = Aspose.Pdf.DocSaveOptions.RecognitionMode.Flow,
            // Set the Horizontal proximity as 2.5
            RelativeHorizontalProximity = 2.5f,
            // Enable the value to recognize bullets during the conversion process
            RecognizeBullets = true
        };
        // Save the file into MS document with save options
        document.Save(dataDir + "PDFtoDOC_out.doc", saveOptions);
    }
}
```

{{% alert color="success" %}}
**Tente converter PDF para DOC online**

Aspose.PDF for .NET apresenta a você um aplicativo online gratuito ["PDF para DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Converter PDF para DOC](/pdf/pt/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Converter arquivo PDF para DOCX (Microsoft Word 2007-2024)

A API Aspose.PDF for .NET permite que você leia e converta documentos PDF para DOCX usando C# e qualquer linguagem .NET. DOCX é um formato bem conhecido para documentos do Microsoft Word, cuja estrutura foi alterada de binária simples para uma combinação de arquivos XML e binários. Arquivos Docx podem ser abertos com o Word 2007 e versões posteriores, mas não com versões anteriores do MS Word, que suportam extensões de arquivo DOC.

O seguinte trecho de código C# mostra como converter um arquivo PDF em formato DOCX.

<a name="csharp-pdf-to-docx" id="csharp-pdf-to-docx"><strong>Converter PDF para DOCX</strong></a>

1. Crie uma instância do objeto [Document](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document/) com o documento PDF de origem.
2. Salve-o no formato **SaveFormat.DocX** chamando o método **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord_DOCX_Format()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Save the file into MS document format
        document.Save(dataDir + "PDFtoDOC_out.docx", SaveFormat.DocX);
    }
}
```

### Converter PDF para DOCX em Modo Aprimorado

Para obter melhores resultados na conversão de PDF para DOCX, você pode usar o modo `EnhancedFlow`.
A principal diferença entre Flow e Enhanced Flow é que tabelas (tanto com quanto sem bordas) são reconhecidas como tabelas reais, não como texto com uma imagem de fundo.
Há também reconhecimento de listas numeradas e muitas outras pequenas coisas.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord_Advanced_DOCX_Format()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Instantiate DocSaveOptions object
        DocSaveOptions saveOptions = new Aspose.Pdf.DocSaveOptions
        {
            // Set format to save MS document
            Format = Aspose.Pdf.DocSaveOptions.DocFormat.DocX,
            // Set the recognition mode as EnhancedFlow
            Mode = Aspose.Pdf.DocSaveOptions.RecognitionMode.EnhancedFlow
        };

        // Save the file into MS document format
        document.Save(dataDir + "PDFToDOC_out.docx", saveOptions);
    }
}
```

{{% alert color="warning" %}}
**Tente converter PDF para DOCX online**

Aspose.PDF for .NET apresenta a você um aplicativo online gratuito ["PDF para Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de PDF para Word Aplicativo Gratuito](/pdf/pt/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}