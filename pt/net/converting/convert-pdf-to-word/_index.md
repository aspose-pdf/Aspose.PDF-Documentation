---
title: Converter Documentos PDF para Microsoft Word em .NET
linktitle: Converter PDF para Word
type: docs
weight: 10
url: /pt/net/convert-pdf-to-word/
lastmod: "2022-08-04"
description: Aprenda como escrever código em C# para conversão de PDF para formatos Microsoft Word com Aspose.PDF para .NET. e ajuste a conversão de PDF para DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Visão Geral

Este artigo explica como **converter documentos PDF para Microsoft Word usando C#**. Ele cobre os seguintes tópicos.

_Formato_: **DOC**

- [C# PDF para DOC](#csharp-pdf-to-doc)
- [C# Converter PDF para DOC](#csharp-pdf-to-doc)
- [C# Como converter arquivo PDF para DOC](#csharp-pdf-to-doc)

_Formato_: **DOCX**

- [C# PDF para DOCX](#csharp-pdf-to-docx)
- [C# Converter PDF para DOCX](#csharp-pdf-to-docx)
- [C# Como converter arquivo PDF para DOCX](#csharp-pdf-to-docx)

_Formato_: **Word**

- [C# PDF para Word](#csharp-pdf-to-docx)
- [C# Converter PDF para Word](#csharp-pdf-to-doc)
- [C# Como converter arquivo PDF para Word](#csharp-pdf-to-docx)

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).
O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

## Conversão de PDF para DOC e DOCX

Uma das características mais populares é a conversão de PDF para Microsoft Word DOC, o que torna a gestão de conteúdo mais fácil. **Aspose.PDF for .NET** permite converter arquivos PDF para os formatos DOC e DOCX de forma rápida e eficiente.

## Converter PDF para arquivo DOC (Microsoft Word 97-2003)

Converta arquivos PDF para o formato DOC com facilidade e controle completo. Aspose.PDF for .NET é flexível e suporta uma grande variedade de conversões. Converter páginas de documentos PDF em imagens, por exemplo, é uma funcionalidade muito popular.

Muitos de nossos clientes solicitaram uma conversão de PDF para DOC: converter um arquivo PDF em um documento do Microsoft Word. Os clientes desejam isso porque arquivos PDF não podem ser facilmente editados, enquanto que documentos Word podem. Algumas empresas querem que seus usuários possam manipular texto, tabelas e imagens em arquivos que começaram como PDFs.

Mantendo viva a tradição de tornar as coisas simples e compreensíveis, Aspose.PDF for .NET permite transformar um arquivo PDF de origem em um arquivo DOC com apenas duas linhas de código.
Mantendo viva a tradição de tornar as coisas simples e compreensíveis, o Aspose.PDF para .NET permite transformar um arquivo PDF fonte em um arquivo DOC com apenas duas linhas de código.

O seguinte trecho de código C# mostra a conversão de um arquivo PDF para o formato DOC.

<a name="csharp-pdf-to-doc"><strong>Passos: Converter PDF para DOC em C#</strong></a>

1. Crie uma instância do objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) com o documento PDF fonte.
2. Salve no formato **SaveFormat.Doc** chamando o método **Document.Save()**.

```csharp
public static void ConvertPDFtoWord()
{
    // Abrir o documento PDF fonte
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");
    // Salvar o arquivo no formato de documento MS
    pdfDocument.Save(_dataDir + "PDFToDOC_out.doc", SaveFormat.Doc);

}
```

### Usando a Classe DocSaveOptions

A classe [`DocSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) oferece várias propriedades que melhoram a conversão de arquivos PDF para o formato DOC.
A classe [`DocSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) oferece várias propriedades que melhoram a conversão de arquivos PDF para o formato DOC.

- O modo [`Textbox`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) é rápido e bom para preservar a aparência original do arquivo PDF, mas a editabilidade do documento resultante pode ser limitada. Cada bloco de texto visualmente agrupado no PDF original é convertido em uma caixa de texto no documento de saída. Isso alcança uma máxima semelhança com o original, então o documento de saída parece bom, mas consiste inteiramente em caixas de texto, o que pode ser desafiador de editar no Microsoft Word.
- O modo [`Flow`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) é um modo de reconhecimento completo, onde o motor realiza agrupamento e análise multinível para restaurar o documento original conforme a intenção do autor, produzindo um documento facilmente editável.
- [`Flow`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) é o modo de reconhecimento completo, onde o motor realiza agrupamentos e análises multinível para restaurar o documento original conforme a intenção do autor, enquanto produz um documento facilmente editável.

A propriedade [`RelativeHorizontalProximity`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/relativehorizontalproximity) pode ser usada para controlar a proximidade relativa entre elementos textuais. Isso significa que a distância é normatizada pelo tamanho da fonte. Fontes maiores podem ter maiores espaços entre sílabas e ainda ser consideradas um todo único. É especificada como uma porcentagem do tamanho da fonte; por exemplo, 1 = 100%. Isso significa que dois caracteres de 12pt colocados a 12 pt de distância são proximais.
- [`RecognitionBullets`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/recognizebullets) é usado para ativar o reconhecimento de marcadores durante a conversão.

```csharp
public static void ConvertPDFtoWordDocAdvanced()
{
    var pdfFile = Path.Combine(_dataDir, "PDF-to-DOC.pdf");
    var docFile = Path.Combine(_dataDir, "PDF-to-DOC.doc");
    Document pdfDocument = new Document(pdfFile);
    DocSaveOptions saveOptions = new DocSaveOptions
    {
        Format = DocSaveOptions.DocFormat.Doc,
        // Definir o modo de reconhecimento como Flow
        Mode = DocSaveOptions.RecognitionMode.Flow,
        // Definir a proximidade horizontal como 2.5
        RelativeHorizontalProximity = 2.5f,
        // Ativar o valor para reconhecer marcadores durante o processo de conversão
        RecognizeBullets = true
    };
    pdfDocument.Save(docFile, saveOptions);
}
```
{{% alert color="success" %}}
**Tente converter PDF para DOC online**

Aspose.PDF para .NET apresenta a aplicação gratuita online ["PDF para DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), onde você pode experimentar a funcionalidade e a qualidade com que funciona.

[![Converter PDF para DOC](/pdf/pt/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Converter PDF para arquivo DOCX (Microsoft Word 2007-2021)

Aspose.PDF para .NET API permite ler e converter documentos PDF para o formato DOCX usando C# e qualquer linguagem .NET. DOCX é um formato bem conhecido para documentos do Microsoft Word cuja estrutura mudou de binário simples para uma combinação de arquivos XML e binários. Arquivos docx podem ser abertos com o Word 2007 e versões posteriores, mas não com versões anteriores do MS Word, que suportam extensões de arquivo DOC.

O seguinte trecho de código C# mostra a conversão de um arquivo PDF para o formato DOCX.

<a name="csharp-pdf-to-docx"><strong>Passos: Converter PDF para DOCX em C#</strong></a>

1.
1.
2. Salve no formato **SaveFormat.DocX** chamando o método **Document.Save()**.

```csharp
public static void ConvertPDFtoWord_DOCX_Format()
{
    // Abra o documento PDF de origem
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");
    // Salve o arquivo DOC resultante
    pdfDocument.Save(_dataDir + "saveOptionsOutput_out.doc", SaveFormat.DocX);
}
```

### Converter PDF para DOCX em Modo Aprimorado

Para obter melhores resultados na conversão de PDF para DOCX, você pode usar o modo `EnhancedFlow`.
A principal diferença entre Flow e Enhanced Flow é que tabelas (com ou sem bordas) são reconhecidas como tabelas reais, não como texto com uma imagem ao fundo.
Há também o reconhecimento de listas numeradas e muitas outras coisas menores.

```csharp
public static void ConvertPDFtoWord_Advanced_DOCX_Format()
{    
    // Abra o documento PDF de origem
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");

    // Instancie o objeto DocSaveOptions
    DocSaveOptions saveOptions = new DocSaveOptions
    {
        // Especifique o formato de saída como DOCX
        Format = DocSaveOptions.DocFormat.DocX
        // Defina outros parâmetros do DocSaveOptions
        Mode = DocSaveOptions.RecognitionMode.EnhancedFlow
    };
    // Salve o documento no formato docx
    pdfDocument.Save("ConvertToDOCX_out.docx", saveOptions);
}
```
{{% alert color="warning" %}}
**Tente converter PDF para DOCX online**

Aspose.PDF para .NET apresenta a você uma aplicação gratuita online ["PDF para Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), onde você pode explorar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão PDF para Word Aplicativo Gratuito](/pdf/pt/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Veja Também

Este artigo também abrange estes tópicos. Os códigos são os mesmos mencionados acima.

_Formato_: **Word**

- [Código C# PDF para Word](#csharp-pdf-to-docx)
- [API C# PDF para Word](#csharp-pdf-to-docx)
- [C# PDF para Word Programaticamente](#csharp-pdf-to-docx)
- [Biblioteca C# PDF para Word](#csharp-pdf-to-docx)
- [C# Salvar PDF como Word](#csharp-pdf-to-docx)
- [C# Gerar Word a partir de PDF](#csharp-pdf-to-docx)
- [C# Criar Word a partir de PDF](#csharp-pdf-to-docx)
- [Conversor C# PDF para Word](#csharp-pdf-to-docx)

_Formato_: **DOC**

- [Código C# PDF para DOC](#csharp-pdf-to-doc)
- [API C# PDF para DOC](#csharp-pdf-to-doc)
- [API de PDF para DOC em C#](#csharp-pdf-to-doc)
- [Programaticamente PDF para DOC em C#](#csharp-pdf-to-doc)
- [Biblioteca de PDF para DOC em C#](#csharp-pdf-to-doc)
- [Salvar PDF como DOC em C#](#csharp-pdf-to-doc)
- [Gerar DOC a partir de PDF em C#](#csharp-pdf-to-doc)
- [Criar DOC a partir de PDF em C#](#csharp-pdf-to-doc)
- [Conversor de PDF para DOC em C#](#csharp-pdf-to-doc)

_Formato_: **DOCX**

- [Código de PDF para DOCX em C#](#csharp-pdf-to-docx)
- [API de PDF para DOCX em C#](#csharp-pdf-to-docx)
- [Programaticamente PDF para DOCX em C#](#csharp-pdf-to-docx)
- [Biblioteca de PDF para DOCX em C#](#csharp-pdf-to-docx)
- [Salvar PDF como DOCX em C#](#csharp-pdf-to-docx)
- [Gerar DOCX a partir de PDF em C#](#csharp-pdf-to-docx)
- [Criar DOCX a partir de PDF em C#](#csharp-pdf-to-docx)
- [Conversor de PDF para DOCX em C#](#csharp-pdf-to-docx)
