---
title: Converter PDF para Excel em .NET
linktitle: Converter PDF para Excel
type: docs
weight: 20
url: /pt/net/convert-pdf-to-excel/
lastmod: "2021-11-01"
keywords: converter PDF para Excel usando c#, converter PDF para XLS usando csharp, converter PDF para XLSX usando csharp, exportar tabela de PDF para Excel em csharp.
description: A biblioteca Aspose.PDF para .NET permite converter PDF para o formato Excel usando C#. Esses formatos incluem XLS, XLSX, Planilha XML 2003, CSV, ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Visão Geral

Este artigo explica como **converter PDF para formatos Excel usando C#**. Ele aborda os seguintes tópicos.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

_Formato_: **XLS**

- [C# PDF para XLS](#csharp-pdf-to-xls)
- [C# Converter PDF para XLS](#csharp-pdf-to-xls)
- [C# Como converter arquivo PDF para XLS](#csharp-pdf-to-xls)

_Formato_: **XLSX**

- [C# PDF para XLSX](#csharp-pdf-to-xlsx)
- [C# Converter PDF para XLSX](#csharp-pdf-to-xlsx)
- [C# Como converter arquivo PDF para XLSX](#csharp-pdf-to-xlsx)
- [C# Como converter arquivo PDF para XLSX](#csharp-pdf-to-xlsx)

_Formato_: **Excel**

- [C# PDF para Excel](#csharp-pdf-to-xlsx)
- [C# PDF para Excel XLS](#csharp-pdf-to-xls)
- [C# PDF para Excel XLSX](#csharp-pdf-to-xlsx)

_Formato_: **Única Planilha de Excel**

- [C# Converter PDF para XLS com Única Planilha](#csharp-pdf-to-excel-single)
- [C# Converter PDF para XLSX com Única Planilha](#csharp-pdf-to-excel-single)

_Formato_: **Formato de Planilha XML 2003**

- [C# PDF para Excel XML](#csharp-pdf-to-excel-xml-2003)
- [C# Converter PDF para Planilha Excel XML](#csharp-pdf-to-excel-xml-2003)

_Formato_: **CSV**

- [C# PDF para CSV](#csharp-pdf-to-csv)
- [C# Converter PDF para CSV](#csharp-pdf-to-csv)
- [C# Como converter arquivo PDF para CSV](#csharp-pdf-to-csv)

_Formato_: **ODS**

- [C# PDF para ODS](#csharp-pdf-to-ods)
- [C# Converter PDF para ODS](#csharp-pdf-to-ods)
- [C# Como converter arquivo PDF para ODS](#csharp-pdf-to-ods)

## Conversões de PDF para Excel em C#

**Aspose.PDF for .NET** suporta a funcionalidade de converter arquivos PDF para os formatos Excel 2007, CSV e SpeadsheetML.
**Aspose.PDF para .NET** suporta a funcionalidade de conversão de arquivos PDF para os formatos Excel 2007, CSV e SpeadsheetML.

Aspose.PDF para .NET é um componente de manipulação de PDF, introduzimos uma funcionalidade que renderiza arquivos PDF para a planilha do Excel (arquivos XLSX). Durante essa conversão, as páginas individuais do arquivo PDF são convertidas em planilhas do Excel.

{{% alert color="success" %}}
**Tente converter PDF para Excel online**

Aspose.PDF para .NET apresenta a você a aplicação gratuita online ["PDF para XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), onde você pode experimentar investigar a funcionalidade e a qualidade com que funciona.

[![Conversão de Aspose.PDF de PDF para Excel com Aplicativo Gratuito](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

Para converter arquivos PDF para o formato <abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr>, Aspose.PDF possui uma classe chamada [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions).
Para converter arquivos PDF para o formato <abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr>, o Aspose.PDF possui uma classe chamada [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions).

O seguinte trecho de código mostra o processo de conversão de um arquivo PDF para o formato XLS ou XLSX com o Aspose.PDF para .NET.

<a name="csharp-pdf-to-xls"><strong>Passos: Converter PDF para XLS em C#</strong></a>

1. Crie uma instância do objeto **Document** com o documento PDF de origem.
2. Crie uma instância de **ExcelSaveOptions**.
3. Salve no formato **XLS** especificando a **extensão .xls** ao chamar o método **Document.Save()** e passando **ExcelSaveOptions**

<a name="csharp-pdf-to-xlsx"><strong>Passos: Converter PDF para XLSX em C#</strong></a>

1. Crie uma instância do objeto **Document** com o documento PDF de origem.
2. Crie uma instância de **ExcelSaveOptions**.
3. Salve no formato **XLSX** especificando a **extensão .xlsx** ao chamar o método **Document.Save()** e passando **ExcelSaveOptions**

```csharp
// The code snippet remains the same in the translated document and should be included as provided initially.
```
```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Carregar documento PDF
Document pdfDocument = new Document(dataDir + "input.pdf");

// Instanciar objeto de opção de salvamento em Excel
Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions();

// Salvar a saída no formato XLS
pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
```

## Converter PDF para XLS com Controle de Coluna

Ao converter um PDF para o formato XLS, uma coluna em branco é adicionada ao arquivo de saída como primeira coluna. A opção InsertBlankColumnAtFirst na classe ExcelSaveOptions é usada para controlar essa coluna. O valor padrão é `false`, o que significa que colunas em branco não serão inseridas.

```csharp
public static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst()
{
    // Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    // Carregar documento PDF
    Document pdfDocument = new Document(_dataDir + "input.pdf");
    // Instanciar objeto de opção de salvamento em Excel
    Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions {InsertBlankColumnAtFirst = false};
    // Salvar a saída no formato XLS
    pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
}
```
## Converter PDF para uma única planilha do Excel

Ao exportar um arquivo PDF com várias páginas para XLS, cada página é exportada para uma diferente planilha no arquivo Excel. Isso ocorre porque a propriedade MinimizeTheNumberOfWorksheets está definida como false por padrão. Para garantir que todas as páginas sejam exportadas para uma única planilha no arquivo Excel final, defina a propriedade MinimizeTheNumberOfWorksheets como true.

<a name="csharp-pdf-to-excel-single"><strong>Passos: Converter PDF para XLS ou XLSX em uma única planilha em C#</strong></a>

1. Crie uma instância do objeto **Document** com o documento PDF de origem.
2. Crie uma instância de **ExcelSaveOptions** com **MinimizeTheNumberOfWorksheets = true**.
3. Salve no formato **XLS** ou **XLSX** tendo uma única planilha ao chamar o método **Document.Save()** e passando **ExcelSaveOptions**.

```csharp
public static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets()
{
    // Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    // Carregar o documento PDF
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // Instanciar objeto de opção de salvamento Excel
    Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions {MinimizeTheNumberOfWorksheets = true};
    // Salvar a saída no formato XLS
    pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
}
```
## Converter para outros formatos de planilha

### Converter para o formato XML Spreadsheet 2003

Desde a versão 20.8, o Aspose.PDF usa o formato de arquivo Microsoft Excel Open XML Spreadsheet 2007 como padrão para armazenar dados. Para converter arquivos PDF para o formato XML Spreadsheet 2003, o Aspose.PDF possui uma classe chamada [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions) com [Format](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions/properties/format). Um objeto da classe [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions) é passado como segundo argumento para o método [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index).

O seguinte trecho de código mostra o processo para converter um arquivo PDF em formato XLS Excel 2003 XML.

<a name="csharp-pdf-to-excel-xml-2003"><strong>Passos: Converter PDF para Formato XML Excel 2003 em C#</strong></a>

1. Crie uma instância do objeto **Document** com o documento PDF de origem.
2.
2.
3. Salve-o no formato **XLS - Excel 2003 XML Format** chamando o método **Document.Save()** e passando **ExcelSaveOptions**.

```csharp
public static void ConvertPDFtoExcelAdvanced_SaveXLS2003()
{
    // Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET

    // Carregar documento PDF
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // Instanciar objeto de opções de salvamento Excel
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003 };

    // Salvar a saída no formato XLS
    pdfDocument.Save("PDFToXLS_out.xls", excelSave);
}
```

### Converter para CSV

A conversão para o formato CSV é realizada da mesma forma que acima. Tudo o que você precisa é definir o formato apropriado.

<a name="csharp-pdf-to-csv"><strong>Passos: Converter PDF para CSV em C#</strong></a>

1. Crie uma instância do objeto **Document** com o documento PDF de origem.
2.
2.
3. Salve-o em formato **CSV** chamando o método **Document.Save()** e passando **ExcelSaveOptions**.

```csharp
 // Instancie o objeto ExcelSave Options
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.CSV };
```

### Converter para ODS

<a name="csharp-pdf-to-ods"><strong>Passos: Converter PDF para ODS em C#</strong></a>

1. Crie uma instância do objeto **Document** com o documento PDF fonte.
2. Crie uma instância de **ExcelSaveOptions** com **Format = ExcelSaveOptions.ExcelFormat.ODS**
3. Salve-o em formato **ODS** chamando o método **Document.Save()** e passando **ExcelSaveOptions**.

A conversão para o formato ODS é realizada da mesma maneira que todos os outros formatos.

```csharp
 // Instancie o objeto ExcelSave Options
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.ODS };
```

## Veja Também

Este artigo também abrange estes tópicos. Os códigos são os mesmos que acima.

_Formato_: **Excel**
- [Código C# PDF para Excel](#csharp-pdf-to-xlsx)
- [API C# PDF para Excel](#csharp-pdf-to-xlsx)
- [API C# de PDF para Excel](#csharp-pdf-to-xlsx)
- [C# PDF para Excel Programaticamente](#csharp-pdf-to-xlsx)
- [Biblioteca C# PDF para Excel](#csharp-pdf-to-xlsx)
- [C# Salvar PDF como Excel](#csharp-pdf-to-xlsx)
- [C# Gerar Excel a partir de PDF](#csharp-pdf-to-xlsx)
- [C# Criar Excel a partir de PDF](#csharp-pdf-to-xlsx)
- [Conversor C# de PDF para Excel](#csharp-pdf-to-xlsx)

_Formato_: **XLS**
- [Código C# PDF para XLS](#csharp-pdf-to-xls)
- [API C# de PDF para XLS](#csharp-pdf-to-xls)
- [C# PDF para XLS Programaticamente](#csharp-pdf-to-xls)
- [Biblioteca C# PDF para XLS](#csharp-pdf-to-xls)
- [C# Salvar PDF como XLS](#csharp-pdf-to-xls)
- [C# Gerar XLS a partir de PDF](#csharp-pdf-to-xls)
- [C# Criar XLS a partir de PDF](#csharp-pdf-to-xls)
- [Conversor C# de PDF para XLS](#csharp-pdf-to-xls)

_Formato_: **XLSX**
- [Código C# PDF para XLSX](#csharp-pdf-to-xlsx)
- [API C# de PDF para XLSX](#csharp-pdf-to-xlsx)
- [C# PDF para XLSX Programaticamente](#csharp-pdf-to-xlsx)
- [Biblioteca C# PDF para XLSX](#csharp-pdf-to-xlsx)
- [C# Salvar PDF como XLSX](#csharp-pdf-to-xlsx)
- [C# Gerar XLSX a partir de PDF](#csharp-pdf-to-xlsx)
- [C# Gerar XLSX a partir de PDF](#csharp-pdf-to-xlsx)
- [C# Criar XLSX a partir de PDF](#csharp-pdf-to-xlsx)
- [C# Conversor de PDF para XLSX](#csharp-pdf-to-xlsx)

_Formato_: **CSV**
- [C# Código de PDF para CSV](#csharp-pdf-to-csv)
- [C# API de PDF para CSV](#csharp-pdf-to-csv)
- [C# PDF para CSV Programaticamente](#csharp-pdf-to-csv)
- [C# Biblioteca de PDF para CSV](#csharp-pdf-to-csv)
- [C# Salvar PDF como CSV](#csharp-pdf-to-csv)
- [C# Gerar CSV a partir de PDF](#csharp-pdf-to-csv)
- [C# Criar CSV a partir de PDF](#csharp-pdf-to-csv)
- [C# Conversor de PDF para CSV](#csharp-pdf-to-csv)

_Formato_: **ODS**
- [C# Código de PDF para ODS](#csharp-pdf-to-ods)
- [C# API de PDF para ODS](#csharp-pdf-to-ods)
- [C# PDF para ODS Programaticamente](#csharp-pdf-to-ods)
- [C# Biblioteca de PDF para ODS](#csharp-pdf-to-ods)
- [C# Salvar PDF como ODS](#csharp-pdf-to-ods)
- [C# Gerar ODS a partir de PDF](#csharp-pdf-to-ods)
- [C# Criar ODS a partir de PDF](#csharp-pdf-to-ods)
- [C# Conversor de PDF para ODS](#csharp-pdf-to-ods)
