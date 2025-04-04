---
title: PDFをExcelに変換する .NET
linktitle: PDFをExcelに変換
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ja/net/convert-pdf-to-excel/
lastmod: "2021-11-01"
description: Aspose.PDF for .NETライブラリを使用して、C#でPDFをExcel形式に変換できます。これらの形式には、XLS、XLSX、XML 2003スプレッドシート、CSV、ODSが含まれます。
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
    "abstract": "Aspose.PDF for .NETの強力な機能を発見し、PDF文書をXLS、XLSX、CSV、ODSなどのさまざまなExcel形式に簡単に変換します。この機能により、個々のPDFページを別々のExcelワークシートに変換するだけでなく、結合シートのオプションも提供され、ユーザーがPDFデータを効率的に管理できる柔軟性が得られます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "983",
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
    "dateModified": "2025-04-04",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## 概要

この記事では、**C#を使用してPDFをExcel形式に変換する方法**について説明します。以下のトピックをカバーしています。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

- [PDFをXLSに変換](#csharp-pdf-to-xls)
- [PDFをXLSXに変換](#csharp-pdf-to-xlsx)
- [PDFをExcelに変換](#csharp-pdf-to-xlsx)
- [単一ワークシートを持つPDFをXLSに変換](#csharp-pdf-to-excel-single)
- [単一ワークシートを持つPDFをXLSXに変換](#csharp-pdf-to-excel-single)
- [PDFをXML Excelに変換](#csharp-pdf-to-excel-xml-2003)
- [PDFをCSVに変換](#csharp-pdf-to-csv)
- [PDFをODSに変換](#csharp-pdf-to-ods)
- [PDFをXLSMに変換](#csharp-pdf-to-xlsm)

## C# PDFからExcelへの変換

**Aspose.PDF for .NET**は、PDFファイルをExcel 2007、CSV、およびSpreadsheetML形式に変換する機能をサポートしています。

Aspose.PDF for .NETはPDF操作コンポーネントであり、PDFファイルをExcelワークブック（XLSXファイル）にレンダリングする機能を導入しました。この変換中に、PDFファイルの個々のページがExcelワークシートに変換されます。

{{% alert color="success" %}}
**PDFをExcelにオンラインで変換してみてください**

Aspose.PDF for .NETは、機能と品質を調査できるオンライン無料アプリケーション["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)を提供しています。

[![Aspose.PDF PDFをExcelに変換する無料アプリ](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

PDFファイルを<abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr>形式に変換するために、Aspose.PDFには[ExcelSaveOptions](https://reference.aspose.com/pdf/ja/net/aspose.pdf/excelsaveoptions)というクラスがあります。ExcelSaveOptionsクラスのオブジェクトは、Document.Save(..)コンストラクタの第2引数として渡されます。

次のコードスニペットは、Aspose.PDF for .NETを使用してPDFファイルをXLSまたはXLSX形式に変換するプロセスを示しています。

<a name="csharp-pdf-to-xls" id="cshart-pdf-to-xls"><strong>PDFをXLSに変換</strong></a>

1. ソースPDF文書で**Document**オブジェクトのインスタンスを作成します。
2. **ExcelSaveOptions**のインスタンスを作成します。
3. **Document.Save()**メソッドを呼び出し、**ExcelSaveOptions**を渡して**XLS**形式で保存します。

<a name="csharp-pdf-to-xlsx" id="cshart-pdf-to-xlsx"><strong>PDFをXLSXに変換</strong></a>

1. ソースPDF文書で**Document**オブジェクトのインスタンスを作成します。
2. **ExcelSaveOptions**のインスタンスを作成します。
3. **Document.Save()**メソッドを呼び出し、**ExcelSaveOptions**を渡して**XLSX**形式で保存します。

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

## コントロール列を持つPDFをXLSに変換

PDFをXLS形式に変換する際、出力ファイルの最初の列に空白の列が追加されます。この列を制御するために、ExcelSaveOptionsクラスのInsertBlankColumnAtFirstオプションが使用されます。デフォルト値は`false`であり、空白の列は挿入されません。

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

## 単一ExcelワークシートへのPDFの変換

ページ数の多いPDFファイルをXLSにエクスポートする場合、各ページはExcelファイルの異なるシートにエクスポートされます。これは、MinimizeTheNumberOfWorksheetsプロパティがデフォルトでfalseに設定されているためです。出力Excelファイルの1つのシートにすべてのページをエクスポートするには、MinimizeTheNumberOfWorksheetsプロパティをtrueに設定します。

<a name="csharp-pdf-to-excel-single" id="cshart-pdf-to-excel-single"><strong>PDFをXLSまたはXLSXの単一ワークシートに変換</strong></a>

1. ソースPDF文書で**Document**オブジェクトのインスタンスを作成します。
2. **MinimizeTheNumberOfWorksheets = true**で**ExcelSaveOptions**のインスタンスを作成します。
3. **Document.Save()**メソッドを呼び出し、**ExcelSaveOptions**を渡して単一ワークシートを持つ**XLS**または**XLSX**形式で保存します。

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

## 他のスプレッドシート形式への変換

### XMLスプレッドシート2003形式への変換

バージョン20.8以降、Aspose.PDFはデフォルトでデータを保存するためにMicrosoft Excel Open XMLスプレッドシート2007ファイル形式を使用します。PDFファイルをXMLスプレッドシート2003形式に変換するために、Aspose.PDFには[ExcelSaveOptions](https://reference.aspose.com/pdf/ja/net/aspose.pdf/excelsaveoptions)というクラスがあり、[Format](https://reference.aspose.com/pdf/ja/net/aspose.pdf/excelsaveoptions/properties/format)があります。[ExcelSaveOptions](https://reference.aspose.com/pdf/ja/net/aspose.pdf/excelsaveoptions)クラスのオブジェクトは、[Document.Save(..)](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document/methods/save/index)メソッドの第2引数として渡されます。

次のコードスニペットは、PDFファイルをXLS Excel 2003 XML形式に変換するプロセスを示しています。

<a name="csharp-pdf-to-excel-xml-2003" id="cshart-pdf-to-excel-xml-2003"><strong>PDFをExcel 2003 XML形式に変換</strong></a>

1. ソースPDF文書で**Document**オブジェクトのインスタンスを作成します。
2. **Format = ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003**で**ExcelSaveOptions**のインスタンスを作成します。
3. **Document.Save()**メソッドを呼び出し、**ExcelSaveOptions**を渡して**XLS - Excel 2003 XML形式**で保存します。

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

### CSVへの変換

CSV形式への変換は、上記と同様に行われます。必要なことは、適切な形式を設定することだけです。

<a name="csharp-pdf-to-csv"  id="cshart-pdf-to-csv"><strong>PDFをCSVに変換</strong></a>

1. ソースPDF文書で**Document**オブジェクトのインスタンスを作成します。
2. **Format = ExcelSaveOptions.ExcelFormat.CSV**で**ExcelSaveOptions**のインスタンスを作成します。
3. **Document.Save()**メソッドを呼び出し、**ExcelSaveOptions**を渡して**CSV**形式で保存します。

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

### ODSへの変換

<a name="csharp-pdf-to-ods"  id="cshart-pdf-to-ods"><strong>PDFをODSに変換</strong></a>

1. ソースPDF文書で**Document**オブジェクトのインスタンスを作成します。
2. **Format = ExcelSaveOptions.ExcelFormat.ODS**で**ExcelSaveOptions**のインスタンスを作成します。
3. **Document.Save()**メソッドを呼び出し、**ExcelSaveOptions**を渡して**ODS**形式で保存します。

ODS形式への変換は、他のすべての形式と同様に行われます。

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

### XLSMへの変換

<a name="csharp-pdf-to-xlsm" id="cshart-pdf-to-xlsm"><strong>PDFをXLSMに変換</strong></a>

1. ソースPDF文書で**Document**オブジェクトのインスタンスを作成します。
2. **Format = ExcelSaveOptions.ExcelFormat.XLSM**で**ExcelSaveOptions**のインスタンスを作成します。
3. **Document.Save()**メソッドを呼び出し、**ExcelSaveOptions**を渡して**XLSM**形式で保存します。

XLSM形式への変換は、他のすべての形式と同様に行われます。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToXLSM()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.XLSM
        };

        // Save the file in ODS format
        document.Save(dataDir + "PDFToODS_out.xlsm", saveOptions);
    }
}
```