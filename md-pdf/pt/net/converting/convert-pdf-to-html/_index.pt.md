---
title: Converter PDF para HTML em .NET
linktitle: Converter formato PDF para HTML
type: docs
weight: 50
url: /net/convert-pdf-to-html/
lastmod: "2021-11-01"
description: Este tópico mostra como converter um arquivo PDF para formato HTML com a biblioteca Aspose.PDF C#.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Visão Geral

Este artigo explica como **converter PDF para HTML usando C#**. Ele abrange estes tópicos.

_Formato_: **HTML**
- [C# PDF para HTML](#csharp-pdf-to-html)
- [C# Converter PDF para HTML](#csharp-pdf-to-html)
- [C# Como converter arquivo PDF para HTML](#csharp-pdf-to-html)

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Converter PDF para HTML

**Aspose.PDF para .NET** oferece muitos recursos para converter vários formatos de arquivo em documentos PDF e converter arquivos PDF em vários formatos de saída.
**Aspose.PDF para .NET** oferece muitos recursos para converter vários formatos de arquivo em documentos PDF e converter arquivos PDF em vários formatos de saída.

**Aspose.PDF para .NET** suporta os recursos para converter um arquivo PDF em HTML. As principais tarefas que você pode realizar com a biblioteca Aspose.PDF estão listadas:

- converter PDF para HTML;
- divisão de Saída para HTML de Múltiplas Páginas;
- especificar Pasta para Armazenar Arquivos SVG;
- compressão de Imagens SVG Durante a Conversão;
- especificação da Pasta de Imagens;
- criar Arquivos Subsequentes com Apenas o Conteúdo do Corpo;
- renderização de Texto Transparente;
- renderização de camadas de documentos PDF.

{{% alert color="success" %}}
**Tente converter PDF para HTML online**

Aspose.PDF para .NET apresenta a você a aplicação gratuita online ["PDF para HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), onde você pode experimentar investigar a funcionalidade e a qualidade com que funciona.

[![Conversão Aspose.PDF de PDF para HTML com Aplicativo Gratuito](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Aspose.PDF para .NET fornece um código de duas linhas para transformar um arquivo PDF fonte em HTML.
Aspose.PDF for .NET fornece um código de duas linhas para transformar um arquivo PDF de origem em HTML.

<a name="csharp-pdf-to-html"><strong>Passos: Converter PDF para HTML em C#</strong></a>

1. Crie uma instância do objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) com o documento PDF de origem.
2. Salve-o no formato **SaveFormat.Html** chamando o método **Document.Save()**.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Abra o documento PDF de origem
Document pdfDocument = new Document(dataDir + "PDFToHTML.pdf");

// Salve o arquivo no formato de documento MS
pdfDocument.Save(dataDir + "output_out.html", SaveFormat.Html);
```

### Dividindo a Saída em HTML Multi-página

Ao converter um arquivo PDF grande com várias páginas para o formato HTML, a saída aparece como uma única página HTML.
Ao converter um arquivo PDF grande com várias páginas para o formato HTML, a saída aparece como uma única página HTML.

```csharp
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Abrir o documento PDF de origem
Document pdfDocument = new Document(dataDir + "PDFToHTML.pdf");

// Instanciar objeto de opções de salvamento HTML
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// Especificar para dividir a saída em várias páginas
htmlOptions.SplitIntoPages = true;

// Salvar o documento
pdfDocument.Save(@"MultiPageHTML_out.html", htmlOptions);
```

### Especificar Pasta para Armazenar Arquivos SVG

Durante a conversão de PDF para HTML, é possível especificar a pasta em que as imagens SVG devem ser salvas.
Durante a conversão de PDF para HTML, é possível especificar a pasta onde as imagens SVG devem ser salvas.

```csharp
// Carregar o arquivo PDF
Document doc = new Document(dataDir + "PDFToHTML.pdf");

// Instanciar o objeto de opções de salvamento HTML
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// Especificar a pasta onde as imagens SVG são salvas durante a conversão de PDF para HTML
newOptions.SpecialFolderForSvgImages = dataDir;

// Salvar o arquivo de saída
doc.Save(dataDir + "SaveSVGFiles_out.html", newOptions);
```

### Comprimindo Imagens SVG Durante a Conversão

Para comprimir imagens SVG durante a conversão de PDF para HTML, por favor, tente usar o seguinte código:

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Criar HtmlSaveOption com recurso testado
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// Comprimir as imagens SVG se houver alguma
newOptions.CompressSvgGraphicsIfAny = true;
```

### Especificando a Pasta de Imagens

Também podemos especificar a pasta onde as imagens serão salvas durante a conversão de PDF para HTML:
Também podemos especificar a pasta em que as imagens serão salvas durante a conversão de PDF para HTML:

```csharp
// Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Criar HtmlSaveOption com recurso testado
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// Especificar a pasta separada para salvar imagens
newOptions.SpecialFolderForAllImages = dataDir;
```

### Criar Arquivos Subsequentes Apenas com o Conteúdo do Corpo

Recentemente, fomos solicitados a introduzir um recurso onde arquivos PDF são convertidos para HTML e o usuário pode obter apenas os conteúdos da tag `<body>` de cada página. Isso produziria um arquivo com CSS, detalhes de `<html>`, `<head>` e todas as páginas em outros arquivos apenas com os conteúdos de `<body>`.

Para atender a essa necessidade, uma nova propriedade, HtmlMarkupGenerationMode, foi introduzida na classe HtmlSaveOptions.

Com o seguinte trecho de código simples, você pode dividir o HTML de saída em páginas.
Com o seguinte trecho de código simples, você pode dividir a saída HTML em páginas.

```csharp
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");
           
HtmlSaveOptions options = new HtmlSaveOptions();
// Esta é a configuração testada
options.HtmlMarkupGenerationMode = HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent;
options.SplitIntoPages = true;

doc.Save(dataDir + "CreateSubsequentFiles_out.html", options);
```

### Renderização de Texto Transparente

Caso o arquivo PDF de origem/entrada contenha textos transparentes sombreados por imagens de primeiro plano, então pode haver problemas de renderização de texto. Assim, para atender tais cenários, as propriedades SaveShadowedTextsAsTransparentTexts e SaveTransparentTexts podem ser usadas.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.SaveShadowedTextsAsTransparentTexts = true;
htmlOptions.SaveTransparentTexts = true;
doc.Save(dataDir + "TransparentTextRendering_out.html", htmlOptions);
```
### Renderização de camadas de documentos PDF

Podemos renderizar camadas de documentos PDF em um elemento de tipo de camada separado durante a conversão de PDF para HTML:

```csharp
// Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");
// Instanciar objeto HtmlSaveOptions
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// Especificar para renderizar as camadas do documento PDF separadamente em HTML de saída
htmlOptions.ConvertMarkedContentToLayers = true;

// Salvar o documento
doc.Save(dataDir + "LayersRendering_out.html", htmlOptions);
```

## Veja Também

Este artigo também cobre estes tópicos. Os códigos são os mesmos acima.

_Formato_: **HTML**
- [Código C# PDF para HTML](#csharp-pdf-to-html)
- [API C# PDF para HTML](#csharp-pdf-to-html)
- [C# PDF para HTML Programaticamente](#csharp-pdf-to-html)
- [Biblioteca C# PDF para HTML](#csharp-pdf-to-html)
- [C# Salvar PDF como HTML](#csharp-pdf-to-html)
- [C# Salvar PDF como HTML](#csharp-pdf-to-html)
- [C# Gerar HTML a partir de PDF](#csharp-pdf-to-html)
- [C# Criar HTML a partir de PDF](#csharp-pdf-to-html)
- [C# Conversor de PDF para HTML](#csharp-pdf-to-html)
