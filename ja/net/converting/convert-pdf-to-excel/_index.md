---
title: .NETでPDFをExcelに変換
linktitle: PDFをExcelに変換
type: docs
weight: 20
url: /ja/net/convert-pdf-to-excel/
lastmod: "2021-11-01"
description: Aspose.PDF for .NET ライブラリを使用して、C#を使用してPDFをExcel形式に変換できます。これらの形式には、XLS、XLSX、XML 2003 スプレッドシート、CSV、ODSが含まれます。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 概要

この記事では、**C#を使用してPDFをExcel形式に変換する方法**について説明します。次のトピックをカバーしています。

次のコードスニペットも [Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリで動作します。

_形式_: **XLS**

- [C# PDFをXLSに](#csharp-pdf-to-xls)
- [C# PDFをXLSに変換](#csharp-pdf-to-xls)
- [C# PDFファイルをXLSに変換する方法](#csharp-pdf-to-xls)

_形式_: **XLSX**

- [C# PDFをXLSXに](#csharp-pdf-to-xlsx)
- [C# PDFをXLSXに変換](#csharp-pdf-to-xlsx)
- [C# PDFファイルをXLSXに変換する方法](#csharp-pdf-to-xlsx)
- [C# PDFファイルをXLSXに変換する方法](#csharp-pdf-to-xlsx)

_フォーマット_: **Excel**

- [C# PDFをExcelに変換](#csharp-pdf-to-xlsx)
- [C# PDFをExcel XLSに変換](#csharp-pdf-to-xls)
- [C# PDFをExcel XLSXに変換](#csharp-pdf-to-xlsx)

_フォーマット_: **シングルExcelワークシート**

- [C# PDFをシングルワークシートがあるXLSに変換](#csharp-pdf-to-excel-single)
- [C# PDFをシングルワークシートがあるXLSXに変換](#csharp-pdf-to-excel-single)

_フォーマット_: **XMLスプレッドシート2003形式**

- [C# PDFをXML Excelに変換](#csharp-pdf-to-excel-xml-2003)
- [C# PDFをXML Excelスプレッドシートに変換](#csharp-pdf-to-excel-xml-2003)

_フォーマット_: **CSV**

- [C# PDFをCSVに変換](#csharp-pdf-to-csv)
- [C# PDFをCSVに変換する方法](#csharp-pdf-to-csv)

_フォーマット_: **ODS**

- [C# PDFをODSに変換](#csharp-pdf-to-ods)
- [C# PDFをODSに変換する方法](#csharp-pdf-to-ods)

## C# PDFからExcelへの変換

**Aspose.PDF for .NET**はPDFファイルをExcel 2007、CSV、およびSpeadsheetML形式に変換する機能をサポートしています。
**Aspose.PDF for .NET** は、PDFファイルをExcel 2007、CSV、およびSpeadsheetML形式に変換する機能をサポートしています。

Aspose.PDF for .NETはPDF操作コンポーネントであり、PDFファイルをExcelワークブック（XLSXファイル）にレンダリングする機能を導入しました。この変換中に、PDFファイルの個々のページがExcelワークシートに変換されます。

{{% alert color="success" %}}
**PDFをExcelにオンラインで変換してみる**

Aspose.PDF for .NETは、無料のアプリケーション["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)をオンラインで提供しており、機能性や品質を試すことができます。

[![Aspose.PDF Convertion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

PDFファイルを<abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr>形式に変換するために、Aspose.PDFには[ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions)というクラスがあります。
PDFファイルを<abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr>形式に変換するために、Aspose.PDFには[ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions)というクラスがあります。

以下のコードスニペットは、Aspose.PDF for .NETを使用してPDFファイルをXLSまたはXLSX形式に変換するプロセスを示しています。

<a name="csharp-pdf-to-xls"><strong>手順: C#でPDFをXLSに変換</strong></a>

1. ソースPDFドキュメントで**Document**オブジェクトのインスタンスを作成します。
2. **ExcelSaveOptions**のインスタンスを作成します。
3. **Document.Save()** メソッドを呼び出し、**ExcelSaveOptions**を渡すことで、**.xls拡張子**を指定して**XLS**形式で保存します。

<a name="csharp-pdf-to-xlsx"><strong>手順: C#でPDFをXLSXに変換</strong></a>

1. ソースPDFドキュメントで**Document**オブジェクトのインスタンスを作成します。
2. **ExcelSaveOptions**のインスタンスを作成します。
3. **Document.Save()** メソッドを呼び出し、**ExcelSaveOptions**を渡すことで、**.xlsx拡張子**を指定して**XLSX**形式で保存します。

```csharp
```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// PDFドキュメントを読み込む
Document pdfDocument = new Document(dataDir + "input.pdf");

// ExcelSave Option オブジェクトをインスタンス化する
Aspose.Pdf.ExcelSaveOptions excelsave = new Aspose.Pdf.ExcelSaveOptions();

// 出力をXLS形式で保存する
pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
```

## PDFをXLSに変換する際の制御列

PDFをXLS形式に変換するとき、出力ファイルの最初の列として空白の列が追加されます。これを制御するためにExcelSaveOptionsクラスのInsertBlankColumnAtFirstオプションを使用します。デフォルト値は`false`で、これは空白の列が挿入されないことを意味します。

```csharp
public static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst()
{
    // 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
    // PDFドキュメントを読み込む
    Document pdfDocument = new Document(_dataDir + "input.pdf");
    // ExcelSave Option オブジェクトをインスタンス化する
    Aspose.Pdf.ExcelSaveOptions excelsave = new Aspose.Pdf.ExcelSaveOptions {InsertBlankColumnAtFirst = false};
    // 出力をXLS形式で保存する
    pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
}
```
## PDFを単一のExcelワークシートに変換する

PDFファイルに多くのページが含まれている場合、XLSへのエクスポートでは、各ページがExcelファイルの異なるシートにエクスポートされます。これは、MinimizeTheNumberOfWorksheetsプロパティがデフォルトでfalseに設定されているためです。出力Excelファイルのすべてのページが1つのシートにエクスポートされるようにするには、MinimizeTheNumberOfWorksheetsプロパティをtrueに設定します。

<a name="csharp-pdf-to-excel-single"><strong>手順: C#でPDFをXLSまたはXLSXの単一ワークシートに変換する</strong></a>

1. ソースPDFドキュメントで**Document**オブジェクトのインスタンスを作成します。
2. **MinimizeTheNumberOfWorksheets = true**で**ExcelSaveOptions**のインスタンスを作成します。
3. **Document.Save()**メソッドを呼び出し、**ExcelSaveOptions**を渡すことで、単一ワークシートを持つ**XLS**または**XLSX**形式で保存します。

```csharp
public static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets()
{
    // 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください
    // PDFドキュメントをロード
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // ExcelSaveオプションオブジェクトのインスタンス化
    Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions {MinimizeTheNumberOfWorksheets = true};
    // 出力をXLS形式で保存
    pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
}
```
## 他のスプレッドシート形式に変換する

### XMLスプレッドシート2003形式に変換

バージョン20.8以降、Aspose.PDFはデータ格納のデフォルトとしてMicrosoft Excel Open XML Spreadsheet 2007ファイル形式を使用しています。PDFファイルをXMLスプレッドシート2003形式に変換するために、Aspose.PDFには[ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions)クラスがあり、[Format](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions/properties/format)プロパティがあります。[ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions)クラスのオブジェクトを[Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index)メソッドの第二引数として渡します。

次のコードスニペットは、PDFファイルをXLS Excel 2003 XML形式に変換するプロセスを示しています。

<a name="csharp-pdf-to-excel-xml-2003"><strong>手順: C#でPDFをExcel 2003 XML形式に変換する</strong></a>

1. ソースPDFドキュメントを持つ**Document**オブジェクトのインスタンスを作成します。
2.
2.
3. **Document.Save()** メソッドを呼び出し、**ExcelSaveOptions** を渡して **XLS - Excel 2003 XML Format** 形式で保存します。

```csharp
public static void ConvertPDFtoExcelAdvanced_SaveXLS2003()
{
    // 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください

    // PDF文書をロード
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // ExcelSave Option オブジェクトをインスタンス化
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003 };

    // 出力をXLS形式で保存
    pdfDocument.Save("PDFToXLS_out.xls", excelSave);
}
```

### CSVへの変換

CSV形式への変換は上記と同じ方法で行います。必要なのは適切な形式を設定することです。

<a name="csharp-pdf-to-csv"><strong>手順: C#でPDFをCSVに変換</strong></a>

1. ソースPDF文書を持つ **Document** オブジェクトのインスタンスを作成します。
2.
**CSV形式で保存する**

**Document.Save()** メソッドを呼び出し、**ExcelSaveOptions** を渡すことによって、**CSV** 形式で保存します。

```csharp
 // ExcelSaveオプションオブジェクトをインスタンス化
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.CSV };
```

### ODSへ変換

<a name="csharp-pdf-to-ods"><strong>手順: C#でPDFをODSに変換</strong></a>

1. ソースPDFドキュメントで **Document** オブジェクトのインスタンスを作成します。
2. **Format = ExcelSaveOptions.ExcelFormat.ODS** で **ExcelSaveOptions** のインスタンスを作成します。
3. **Document.Save()** メソッドを呼び出し、**ExcelSaveOptions** を渡して **ODS** 形式で保存します。

ODS形式への変換は、他のすべての形式と同じ方法で行います。

```csharp
 // ExcelSaveオプションオブジェクトをインスタンス化
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.ODS };
```

## 参照 

この記事では、上記と同じコードで以下のトピックもカバーしています。

_フォーマット_: **Excel**
- [C# PDF to Excel Code](#csharp-pdf-to-xlsx)
- [C# PDF to Excel API](#csharp-pdf-to-xlsx)
- [C# PDFからExcelへのAPI](#csharp-pdf-to-xlsx)
- [C# プログラムでPDFからExcelへ](#csharp-pdf-to-xlsx)
- [C# PDFからExcelへのライブラリ](#csharp-pdf-to-xlsx)
- [C# PDFをExcelとして保存](#csharp-pdf-to-xlsx)
- [C# PDFからExcelを生成](#csharp-pdf-to-xlsx)
- [C# PDFからExcelを作成](#csharp-pdf-to-xlsx)
- [C# PDFからExcelへのコンバータ](#csharp-pdf-to-xlsx)

_Format_: **XLS**
- [C# PDFからXLSコード](#csharp-pdf-to-xls)
- [C# PDFからXLSへのAPI](#csharp-pdf-to-xls)
- [C# プログラムでPDFからXLSへ](#csharp-pdf-to-xls)
- [C# PDFからXLSへのライブラリ](#csharp-pdf-to-xls)
- [C# PDFをXLSとして保存](#csharp-pdf-to-xls)
- [C# PDFからXLSを生成](#csharp-pdf-to-xls)
- [C# PDFからXLSを作成](#csharp-pdf-to-xls)
- [C# PDFからXLSへのコンバータ](#csharp-pdf-to-xls)

_Format_: **XLSX**
- [C# PDFからXLSXコード](#csharp-pdf-to-xlsx)
- [C# PDFからXLSXへのAPI](#csharp-pdf-to-xlsx)
- [C# プログラムでPDFからXLSXへ](#csharp-pdf-to-xlsx)
- [C# PDFからXLSXへのライブラリ](#csharp-pdf-to-xlsx)
- [C# PDFをXLSXとして保存](#csharp-pdf-to-xlsx)
- [C# PDFからXLSXを生成](#csharp-pdf-to-xlsx)
- [C# PDFからXLSXを生成](#csharp-pdf-to-xlsx)
- [C# PDFからXLSXを作成](#csharp-pdf-to-xlsx)
- [C# PDFからXLSXへのコンバータ](#csharp-pdf-to-xlsx)

_Format_: **CSV**
- [C# PDFからCSVコード](#csharp-pdf-to-csv)
- [C# PDFからCSV API](#csharp-pdf-to-csv)
- [C# プログラムによるPDFからCSVへの変換](#csharp-pdf-to-csv)
- [C# PDFからCSVライブラリ](#csharp-pdf-to-csv)
- [C# PDFをCSVとして保存](#csharp-pdf-to-csv)
- [C# PDFからCSVを生成](#csharp-pdf-to-csv)
- [C# PDFからCSVを作成](#csharp-pdf-to-csv)
- [C# PDFからCSVへのコンバータ](#csharp-pdf-to-csv)

_Format_: **ODS**
- [C# PDFからODSコード](#csharp-pdf-to-ods)
- [C# PDFからODS API](#csharp-pdf-to-ods)
- [C# プログラムによるPDFからODSへの変換](#csharp-pdf-to-ods)
- [C# PDFからODSライブラリ](#csharp-pdf-to-ods)
- [C# PDFをODSとして保存](#csharp-pdf-to-ods)
- [C# PDFからODSを生成](#csharp-pdf-to-ods)
- [C# PDFからODSを作成](#csharp-pdf-to-ods)
- [C# PDFからODSへのコンバータ](#csharp-pdf-to-ods)
