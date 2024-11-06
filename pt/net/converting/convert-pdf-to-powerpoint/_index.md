---
title: Converter PDF para PowerPoint em .NET
linktitle: Converter PDF para PowerPoint
type: docs
weight: 30
url: pt/net/convert-pdf-to-powerpoint/
lastmod: "2021-11-01"
description: Aspose.PDF permite converter PDF para o formato PPT (PowerPoint) usando .NET. Há uma maneira de converter PDF para PPTX com Slides como Imagens.
lastmod: "2021-10-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Visão Geral

Este artigo explica como **converter PDF para PowerPoint usando C#**. Ele cobre os seguintes tópicos.

_Formato_: **PPTX**
- [C# PDF para PPTX](#csharp-pdf-to-pptx)
- [C# Converter PDF para PPTX](#csharp-pdf-to-pptx)
- [C# Como converter arquivo PDF para PPTX](#csharp-pdf-to-pptx)

_Formato_: **PowerPoint**
- [C# PDF para PowerPoint](#csharp-pdf-to-powerpoint)
- [C# Converter PDF para PowerPoint](#csharp-pdf-to-powerpoint)
- [C# Como converter arquivo PDF para PowerPoint](#csharp-pdf-to-powerpoint)

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## C# Conversão de PDF para PowerPoint e PPTX
## Conversão de PDF para PowerPoint e PPTX em C#

**Aspose.PDF for .NET** permite acompanhar o progresso da conversão de PDF para PPTX.

Temos uma API chamada Aspose.Slides que oferece a funcionalidade de criar e manipular apresentações PPT/PPTX. Esta API também fornece a funcionalidade de converter arquivos PPT/PPTX para formato PDF. Recentemente, recebemos requisitos de muitos de nossos clientes para suportar a capacidade de transformação de PDF para formato PPTX. A partir da versão Aspose.PDF for .NET 10.3.0, introduzimos uma funcionalidade para transformar documentos PDF em formato PPTX. Durante essa conversão, as páginas individuais do arquivo PDF são convertidas em slides separados no arquivo PPTX.

Durante a conversão de PDF para <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>, o texto é renderizado como Texto onde você pode selecionar/atualizar.
Durante a conversão de PDF para <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>, o texto é renderizado como Texto onde você pode selecionar/atualizar.

## Conversão simples de PDF para PowerPoint usando C# e Aspose.PDF .NET

Para converter PDF para PPTX, Aspose.PDF para .NET aconselha usar os seguintes passos de código.

<a name="csharp-pdf-to-powerpoint"><strong>Passos: Converter PDF para PowerPoint em C#</strong></a> | <a name="csharp-pdf-to-pptx"><strong>Passos: Converter PDF para PPTX em C#</strong></a>

1. Crie uma instância da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
2. Crie uma instância da classe [PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions)
3. Use o método **Save** do objeto **Document** para salvar o PDF como PPTX

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Carregar documento PDF
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// Instanciar a instância PptxSaveOptions
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();
// Salvar a saída no formato PPTX
doc.Save(dataDir + "PDFToPPT_out.pptx", pptx_save);
```
## Converter PDF para PPTX com Slides como Imagens

{{% alert color="success" %}}
**Tente converter PDF para PowerPoint online**

Aspose.PDF for .NET apresenta a você a aplicação gratuita online ["PDF para PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), onde você pode experimentar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de PDF para PPTX com App Gratuito](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

Caso você precise converter um PDF pesquisável para PPTX como imagens em vez de texto selecionável, Aspose.PDF oferece tal recurso através da classe [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions). Para alcançar isso, defina a propriedade [SlidesAsImages](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/slidesasimages) da classe [PptxSaveOptios](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) como 'true', conforme mostrado no exemplo de código a seguir.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Carregar documento PDF
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// Instanciar instância de PptxSaveOptions
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();
// Salvar a saída no formato PPTX
pptx_save.SlidesAsImages = true;
doc.Save(dataDir + "PDFToPPT_out_.pptx", pptx_save);
```
## Detalhe do Progresso da Conversão de PPTX

Aspose.PDF para .NET permite acompanhar o progresso da conversão de PDF para PPTX. A classe [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) fornece a propriedade [CustomProgressHandler](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/customprogresshandler) que pode ser especificada para um método personalizado para rastrear o progresso da conversão, conforme mostrado no seguinte exemplo de código.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Carregar documento PDF
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// Instanciar a instância de PptxSaveOptions
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();

//Especificar o Manipulador de Progresso Personalizado
pptx_save.CustomProgressHandler = ShowProgressOnConsole;
// Salvar a saída no formato PPTX
doc.Save(dataDir + "PDFToPPTWithProgressTracking_out_.pptx", pptx_save);
```
A seguir está o método personalizado para exibir o progresso da conversão.

```csharp
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
switch (eventInfo.EventType)
{
    case ProgressEventType.TotalProgress:
        Console.WriteLine(String.Format("{0}  - Progresso da conversão: {1}% .", DateTime.Now.TimeOfDay, eventInfo.Value.ToString()));
        break;
    case ProgressEventType.ResultPageCreated:
        Console.WriteLine(String.Format("{0}  - Página de resultado {1} de {2} layout criado.", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
        break;
    case ProgressEventType.ResultPageSaved:
        Console.WriteLine(String.Format("{0}  - Página de resultado {1} de {2} exportada.", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
        break;
    case ProgressEventType.SourcePageAnalysed:
        Console.WriteLine(String.Format("{0}  - Página fonte {1} de {2} analisada.", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));

        break;
    default:
        break;
}
```
## Veja Também

Este artigo também cobre estes tópicos. Os códigos são os mesmos que os acima.

_Formato_: **PowerPoint**
- [Código C# PDF para PowerPoint](#csharp-pdf-to-powerpoint)
- [API C# PDF para PowerPoint](#csharp-pdf-to-powerpoint)
- [Programaticamente C# PDF para PowerPoint](#csharp-pdf-to-powerpoint)
- [Biblioteca C# PDF para PowerPoint](#csharp-pdf-to-powerpoint)
- [C# Salvar PDF como PowerPoint](#csharp-pdf-to-powerpoint)
- [C# Gerar PowerPoint a partir de PDF](#csharp-pdf-to-powerpoint)
- [C# Criar PowerPoint a partir de PDF](#csharp-pdf-to-powerpoint)
- [Conversor C# PDF para PowerPoint](#csharp-pdf-to-powerpoint)

_Formato_: **PPTX**
- [Código C# PDF para PPTX](#csharp-pdf-to-pptx)
- [API C# PDF para PPTX](#csharp-pdf-to-pptx)
- [Programaticamente C# PDF para PPTX](#csharp-pdf-to-pptx)
- [Biblioteca C# PDF para PPTX](#csharp-pdf-to-pptx)
- [C# Salvar PDF como PPTX](#csharp-pdf-to-pptx)
- [C# Gerar PPTX a partir de PDF](#csharp-pdf-to-pptx)
- [C# Criar PPTX a partir de PDF](#csharp-pdf-to-pptx)
- [Conversor C# PDF para PPTX](#csharp-pdf-to-pptx)
