---
title: Converter PDF para Excel em .NET
linktitle: Converter PDF para Excel
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /pt/net/convert-pdf-to-excel/
lastmod: "2021-11-01"
description: A biblioteca Aspose.PDF for .NET permite que você converta PDF para o formato Excel usando C#. Esses formatos incluem XLS, XLSX, XML 2003 Spreadsheet, CSV, ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to Excel in .NET",
    "alternativeHeadline": "Convert PDF Files to Excel Formats with C#",
    "abstract": "Descubra a poderosa capacidade da Aspose.PDF for .NET para converter documentos PDF em vários formatos Excel, incluindo XLS, XLSX, CSV e ODS, usando C#. Este recurso não apenas permite a transformação de páginas individuais de PDF em planilhas Excel separadas, mas também oferece opções para planilhas combinadas, proporcionando flexibilidade para os usuários gerenciarem seus dados PDF de forma eficiente.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1780",
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
    "url": "/net/convert-pdf-to-excel/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-excel/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Visão Geral

Este artigo explica como **converter PDF para formatos Excel usando C#**. Ele cobre os seguintes tópicos.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

_Formatação_: **XLS**

- [C# PDF para XLS](#csharp-pdf-to-xls)
- [C# Converter PDF para XLS](#csharp-pdf-to-xls)
- [C# Como converter arquivo PDF para XLS](#csharp-pdf-to-xls)

_Formatação_: **XLSX**

- [C# PDF para XLSX](#csharp-pdf-to-xlsx)
- [C# Converter PDF para XLSX](#csharp-pdf-to-xlsx)
- [C# Como converter arquivo PDF para XLSX](#csharp-pdf-to-xlsx)

_Formatação_: **Excel**

- [C# PDF para Excel](#csharp-pdf-to-xlsx)
- [C# PDF para Excel XLS](#csharp-pdf-to-xls)
- [C# PDF para Excel XLSX](#csharp-pdf-to-xlsx)

_Formatação_: **Planilha Excel Única**

- [C# Converter PDF para XLS com Planilha Única](#csharp-pdf-to-excel-single)
- [C# Converter PDF para XLSX com Planilha Única](#csharp-pdf-to-excel-single)

_Formatação_: **Formato XML Spreadsheet 2003**

- [C# PDF para XML Excel](#csharp-pdf-to-excel-xml-2003)
- [C# Converter PDF para XML Excel Spreadsheet](#csharp-pdf-to-excel-xml-2003)

_Formatação_: **CSV**

- [C# PDF para CSV](#csharp-pdf-to-csv)
- [C# Converter PDF para CSV](#csharp-pdf-to-csv)
- [C# Como converter arquivo PDF para CSV](#csharp-pdf-to-csv)

_Formatação_: **ODS**

- [C# PDF para ODS](#csharp-pdf-to-ods)
- [C# Converter PDF para ODS](#csharp-pdf-to-ods)
- [C# Como converter arquivo PDF para ODS](#csharp-pdf-to-ods)

## Conversões de C# PDF para Excel

**Aspose.PDF for .NET** suporta a funcionalidade de converter arquivos PDF para os formatos Excel 2007, CSV e SpeadsheetML.

Aspose.PDF for .NET é um componente de manipulação de PDF, introduzimos um recurso que renderiza arquivos PDF em uma pasta de trabalho Excel (arquivos XLSX). Durante essa conversão, as páginas individuais do arquivo PDF são convertidas em planilhas Excel.

{{% alert color="success" %}}
**Tente converter PDF para Excel online**

Aspose.PDF for .NET apresenta a você um aplicativo online gratuito ["PDF para XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão PDF para Excel com Aplicativo Gratuito](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

Para converter arquivos PDF para o formato <abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr>, Aspose.PDF possui uma classe chamada [ExcelSaveOptions](https://reference.aspose.com/pdf/pt/net/aspose.pdf/excelsaveoptions). Um objeto da classe ExcelSaveOptions é passado como segundo argumento para o construtor Document.Save(..).

O seguinte trecho de código mostra o processo de conversão de um arquivo PDF para o formato XLS ou XLSX com Aspose.PDF for .NET.

<a name="csharp-pdf-to-xls"><strong>Passos: Converter PDF para XLS em C#</strong></a>

1. Crie uma instância do objeto **Document** com o documento PDF de origem.
2. Crie uma instância de **ExcelSaveOptions**.
3. Salve-o no formato **XLS** especificando a **extensão .xls** chamando o método **Document.Save()** e passando **ExcelSaveOptions**.

<a name="csharp-pdf-to-xlsx"><strong>Passos: Converter PDF para XLSX em C#</strong></a>

1. Crie uma instância do objeto **Document** com o documento PDF de origem.
2. Crie uma instância de **ExcelSaveOptions**.
3. Salve-o no formato **XLSX** especificando a **extensão .xlsx** chamando o método **Document.Save()** e passando **ExcelSaveOptions**.

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertPDFtoExcel()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
     {
         // Instantiate ExcelSaveOptions object
         var saveOptions = new Aspose.Pdf.ExcelSaveOptions();

         // Save the file in XLSX format
         document.Save(dataDir + "PDFToXLS_out.xlsx", saveOptions);
     }
 }
```

## Converter PDF para XLS com Controle de Coluna

Ao converter um PDF para o formato XLS, uma coluna em branco é adicionada ao arquivo de saída como a primeira coluna. A opção InsertBlankColumnAtFirst da classe ExcelSaveOptions é usada para controlar essa coluna. O valor padrão é `false`, o que significa que colunas em branco não serão inseridas.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            InsertBlankColumnAtFirst = false
        };

        // Save the file in XLSX format
        document.Save(dataDir + "PDFToXLS_out.xlsx", saveOptions);
    }
}
```

## Converter PDF para Planilha Excel Única

Ao exportar um arquivo PDF com muitas páginas para XLS, cada página é exportada para uma planilha diferente no arquivo Excel. Isso ocorre porque a propriedade MinimizeTheNumberOfWorksheets é definida como falsa por padrão. Para garantir que todas as páginas sejam exportadas para uma única planilha no arquivo Excel de saída, defina a propriedade MinimizeTheNumberOfWorksheets como verdadeira.

<a name="csharp-pdf-to-excel-single"><strong>Passos: Converter PDF para XLS ou XLSX Planilha Única em C#</strong></a>

1. Crie uma instância do objeto **Document** com o documento PDF de origem.
2. Crie uma instância de **ExcelSaveOptions** com **MinimizeTheNumberOfWorksheets = true**.
3. Salve-o no formato **XLS** ou **XLSX** tendo uma única planilha chamando o método **Document.Save()** e passando **ExcelSaveOptions**.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            MinimizeTheNumberOfWorksheets = true
        };

        // Save the file in XLSX format
        document.Save(dataDir + "PDFToXLS_out.xlsx", saveOptions);
    }
}
```

## Converter para outros formatos de planilha

### Converter para formato XML Spreadsheet 2003

Desde a versão 20.8, Aspose.PDF usa o formato de arquivo Microsoft Excel Open XML Spreadsheet 2007 como padrão para armazenar dados. Para converter arquivos PDF para o formato XML Spreadsheet 2003, Aspose.PDF possui uma classe chamada [ExcelSaveOptions](https://reference.aspose.com/pdf/pt/net/aspose.pdf/excelsaveoptions) com [Format](https://reference.aspose.com/pdf/pt/net/aspose.pdf/excelsaveoptions/properties/format). Um objeto da classe [ExcelSaveOptions](https://reference.aspose.com/pdf/pt/net/aspose.pdf/excelsaveoptions) é passado como segundo argumento para o método [Document.Save(..)](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document/methods/save/index).

O seguinte trecho de código mostra o processo de conversão de um arquivo PDF para o formato XLS Excel 2003 XML.

<a name="csharp-pdf-to-excel-xml-2003"><strong>Passos: Converter PDF para Excel 2003 XML em C#</strong></a>

1. Crie uma instância do objeto **Document** com o documento PDF de origem.
2. Crie uma instância de **ExcelSaveOptions** com **Format = ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003**.
3. Salve-o no formato **XLS - Excel 2003 XML Format** chamando o método **Document.Save()** e passando **ExcelSaveOptions**.

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertPDFtoExcelAdvanced_SaveXLS2003()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
     {
         // Instantiate ExcelSaveOptions object
         var saveOptions = new Aspose.Pdf.ExcelSaveOptions
         {
             Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
         };

         // Save the file in XLS format
         document.Save(dataDir + "PDFToXLS_out.xls", saveOptions);
     }
 }
```

### Converter para CSV

A conversão para o formato CSV é realizada da mesma forma que acima. Tudo o que você precisa fazer é definir o formato apropriado.

<a name="csharp-pdf-to-csv"><strong>Passos: Converter PDF para CSV em C#</strong></a>

1. Crie uma instância do objeto **Document** com o documento PDF de origem.
2. Crie uma instância de **ExcelSaveOptions** com **Format = ExcelSaveOptions.ExcelFormat.CSV**.
3. Salve-o no formato **CSV** chamando o método **Document.Save()** e passando **ExcelSaveOptions**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToCSV()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.CSV
        };
        
        // Save the file in CSV format
        document.Save(dataDir + "PDFToXLS_out.csv", saveOptions);
    }
}
```

### Converter para ODS

<a name="csharp-pdf-to-ods"><strong>Passos: Converter PDF para ODS em C#</strong></a>

1. Crie uma instância do objeto **Document** com o documento PDF de origem.
2. Crie uma instância de **ExcelSaveOptions** com **Format = ExcelSaveOptions.ExcelFormat.ODS**.
3. Salve-o no formato **ODS** chamando o método **Document.Save()** e passando **ExcelSaveOptions**.

A conversão para o formato ODS é realizada da mesma forma que todos os outros formatos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToODS()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.ODS
        };

        // Save the file in ODS format
        document.Save(dataDir + "PDFToODS_out.ods", saveOptions);
    }
}
```

## Veja Também 

Este artigo também cobre estes tópicos. Os códigos são os mesmos que acima.

_Formatação_: **Excel**
- [C# PDF para Código Excel](#csharp-pdf-to-xlsx)
- [C# PDF para API Excel](#csharp-pdf-to-xlsx)
- [C# PDF para Excel Programaticamente](#csharp-pdf-to-xlsx)
- [C# PDF para Biblioteca Excel](#csharp-pdf-to-xlsx)
- [C# Salvar PDF como Excel](#csharp-pdf-to-xlsx)
- [C# Gerar Excel a partir de PDF](#csharp-pdf-to-xlsx)
- [C# Criar Excel a partir de PDF](#csharp-pdf-to-xlsx)
- [C# PDF para Conversor Excel](#csharp-pdf-to-xlsx)

_Formatação_: **XLS**
- [C# PDF para Código XLS](#csharp-pdf-to-xls)
- [C# PDF para API XLS](#csharp-pdf-to-xls)
- [C# PDF para XLS Programaticamente](#csharp-pdf-to-xls)
- [C# PDF para Biblioteca XLS](#csharp-pdf-to-xls)
- [C# Salvar PDF como XLS](#csharp-pdf-to-xls)
- [C# Gerar XLS a partir de PDF](#csharp-pdf-to-xls)
- [C# Criar XLS a partir de PDF](#csharp-pdf-to-xls)
- [C# PDF para Conversor XLS](#csharp-pdf-to-xls)

_Formatação_: **XLSX**
- [C# PDF para Código XLSX](#csharp-pdf-to-xlsx)
- [C# PDF para API XLSX](#csharp-pdf-to-xlsx)
- [C# PDF para XLSX Programaticamente](#csharp-pdf-to-xlsx)
- [C# PDF para Biblioteca XLSX](#csharp-pdf-to-xlsx)
- [C# Salvar PDF como XLSX](#csharp-pdf-to-xlsx)
- [C# Gerar XLSX a partir de PDF](#csharp-pdf-to-xlsx)
- [C# Criar XLSX a partir de PDF](#csharp-pdf-to-xlsx)
- [C# PDF para Conversor XLSX](#csharp-pdf-to-xlsx)

_Formatação_: **CSV**
- [C# PDF para Código CSV](#csharp-pdf-to-csv)
- [C# PDF para API CSV](#csharp-pdf-to-csv)
- [C# PDF para CSV Programaticamente](#csharp-pdf-to-csv)
- [C# PDF para Biblioteca CSV](#csharp-pdf-to-csv)
- [C# Salvar PDF como CSV](#csharp-pdf-to-csv)
- [C# Gerar CSV a partir de PDF](#csharp-pdf-to-csv)
- [C# Criar CSV a partir de PDF](#csharp-pdf-to-csv)
- [C# PDF para Conversor CSV](#csharp-pdf-to-csv)

_Formatação_: **ODS**
- [C# PDF para Código ODS](#csharp-pdf-to-ods)
- [C# PDF para API ODS](#csharp-pdf-to-ods)
- [C# PDF para ODS Programaticamente](#csharp-pdf-to-ods)
- [C# PDF para Biblioteca ODS](#csharp-pdf-to-ods)
- [C# Salvar PDF como ODS](#csharp-pdf-to-ods)
- [C# Gerar ODS a partir de PDF](#csharp-pdf-to-ods)
- [C# Criar ODS a partir de PDF](#csharp-pdf-to-ods)
- [C# PDF para Conversor ODS](#csharp-pdf-to-ods)