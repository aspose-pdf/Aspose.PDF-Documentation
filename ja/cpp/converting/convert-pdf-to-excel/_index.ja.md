---
title: C++でPDFをExcelに変換
linktitle: PDFをExcelに変換
type: docs
weight: 20
url: /cpp/convert-pdf-to-excel/
lastmod: "2021-11-19"
description: Aspose.PDF for C++を使用して、PDFをExcel形式に変換することができます。この過程で、PDFファイルの各ページがExcelワークシートに変換されます。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 概要

この記事では、**C++を使用してPDFをExcel形式に変換する方法**を説明します。以下のトピックをカバーしています。

_形式_: **XLS**
- [C++ PDFをXLSに](#cpp-pdf-to-xls)
- [C++ PDFをXLSに変換](#cpp-pdf-to-xls)
- [C++ PDFファイルをXLSに変換する方法](#cpp-pdf-to-xls)

_形式_: **XLSX**
- [C++ PDFをXLSXに](#cpp-pdf-to-xlsx)
- [C++ PDFをXLSXに変換](#cpp-pdf-to-xlsx)
- [C++ PDFファイルをXLSXに変換する方法](#cpp-pdf-to-xlsx)

_形式_: **Microsoft Excel XLS形式**
- [C++ PDFをExcelに](#cpp-pdf-to-excel-xls)
- [C++ PDFをExcelに変換](#cpp-pdf-to-excel-xls)
- [C++ PDFファイルをExcelに変換する方法](#cpp-pdf-to-excel-xls)

_形式_: **Microsoft Excel XLSX形式**
```
- [C++ PDFからExcelへの変換](#cpp-pdf-to-excel-xlsx)
- [C++ PDFをExcelに変換する](#cpp-pdf-to-excel-xlsx)
- [C++ PDFファイルをExcelに変換する方法](#cpp-pdf-to-excel-xlsx)

この記事で取り上げるその他のトピック
- [関連項目](#see-also)

## C++ PDFからExcelへの変換

**Aspose.PDF for C++** は、PDFファイルをExcel形式に変換する機能をサポートしています。

Aspose.PDF for C++はPDFの操作コンポーネントであり、PDFファイルをExcelワークブック（XLSファイル）にレンダリングする機能を導入しました。この変換中に、PDFファイルの各ページがExcelワークシートに変換されます。

PDFファイルを<abbr title="Microsoft Excel Spreadsheet">XLS</abbr>形式に変換するために、Aspose.PDFにはExcelSaveOptionsというクラスがあります。ExcelSaveOptionsクラスのオブジェクトは、Document.Save(..)コンストラクタの第二引数として渡されます。

次のコードスニペットは、Aspose.PDF for C++を使用してPDFファイルをXLS形式に変換するプロセスを示しています。

<a name="cpp-pdf-to-xls" id="cpp-pdf-to-xls"><strong>手順: C++でPDFをXLSに変換する</strong></a> | <a name="cpp-pdf-to-excel-xls" id="cpp-pdf-to-excel-xls"><strong>手順: C++でPDFをExcel XLS形式に変換する</strong></a>

1. ソースPDFドキュメントを使用して[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)オブジェクトのインスタンスを作成します。
2. **Document->Save()** メソッドを呼び出して_XLS_形式で保存します。

```cpp
void ConvertPDFtoExcel()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名の文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // ファイル名の文字列
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
    // 出力をXLS形式で保存
    document->Save(_dataDir + outfilename, SaveFormat::Excel);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message();
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## コントロールカラムを使用してPDFをXLSに変換

PDFをXLS形式に変換する際、出力ファイルの最初の列として空の列が追加されます。 ExcelSaveOptions クラスの InsertBlankColumnAtFirst オプションは、この列を制御するために使用されます。そのデフォルト値は true です。

```cpp
void ConvertPDFtoExcel_Advanced_InsertBlankColumnAtFirst()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名の文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // ファイル名の文字列
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    // ExcelSave Option オブジェクトをインスタンス化
    auto excelSave = MakeObject<ExcelSaveOptions>();

    // ExcelSaveOptions クラスの InsertBlankColumnAtFirst オプションは、この列を制御するために使用されます。そのデフォルト値は true です。
    excelSave->set_InsertBlankColumnAtFirst(false);

    // 出力を XLS 形式で保存
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PDF を単一の Excel ワークシートに変換

多数のページを含む PDF ファイルを XLS にエクスポートする場合、各ページは Excel ファイルの異なるシートにエクスポートされます。 これは、MinimizeTheNumberOfWorksheets プロパティがデフォルトで false に設定されているためです。出力 Excel ファイル内のすべてのページを 1 つのシートにエクスポートするには、MinimizeTheNumberOfWorksheets プロパティを true に設定します。

```cpp
void ConvertPDFtoExcel_Advanced_MinimizeTheNumberOfWorksheets()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名の文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // ファイル名の文字列
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    // ExcelSave オプションオブジェクトをインスタンス化
    auto excelSave = MakeObject<ExcelSaveOptions>();

    excelSave->set_MinimizeTheNumberOfWorksheets(true);

    // 出力を XLS 形式で保存
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## XLSX 形式への変換

デフォルトでは、Aspose.PDF はデータを保存するために XML スプレッドシート 2003 を使用します。 PDFファイルをXLSX形式に変換するために、Aspose.PDFには[ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options)の「Format」というクラスがあります。[ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options)クラスのオブジェクトは、[Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa)メソッドの第二引数として渡されます。

次のコードスニペットは、PDFファイルをXLSX形式に変換するプロセスを示しています。

<a name="cpp-pdf-to-xlsx" id="cpp-pdf-to-xlsx"><strong>ステップ: C++でPDFをXLSXに変換</strong></a> | <a name="cpp-pdf-to-excel-xlsx" id="cpp-pdf-to-excel-xlsx"><strong>ステップ: C++でPDFをExcel XLSX形式に変換</strong></a>

1. ソースPDFドキュメントを持つ[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)オブジェクトのインスタンスを作成します。
2. インスタンスを作成します [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options)。
3. フォーマットを _ExcelSaveOptions::ExcelFormat::XLSX_ に設定します。
4. **Document->Save()** メソッドを呼び出し、_ExcelSaveOptions_ のインスタンスを渡して _XLSX_ 形式で保存します。

```cpp
void ConvertPDFtoExcel_Advanced_SaveXLSX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名の文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // ファイル名の文字列
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    // ExcelSaveオプションオブジェクトをインスタンス化
    auto excelSave = MakeObject<ExcelSaveOptions>();

    excelSave->set_Format(ExcelSaveOptions::ExcelFormat::XLSX);

    // 出力をXLS形式で保存
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}

**PDFをExcelにオンラインで変換してみてください**
Aspose.PDF for C++は、オンラインで無料のアプリケーション["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)を提供しており、その機能と品質を調査することができます。

[![Aspose.PDF Convertion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## 関連項目

この記事は、次のトピックもカバーしています。コードは上記と同じです。

_フォーマット_: **Microsoft Excel XLS形式**
- [C++ PDFからExcel XLSへのコード](#cpp-pdf-to-excel-xls)
- [C++ プログラムによるPDFからExcel XLSへの変換](#cpp-pdf-to-excel-xls)
- [C++ PDFからExcel XLSへのライブラリ](#cpp-pdf-to-excel-xls)
- [C++ PDFをExcel XLSとして保存](#cpp-pdf-to-excel-xls)
- [C++ PDFからExcel XLSを生成](#cpp-pdf-to-excel-xls)
- [C++ PDFからExcel XLSを作成](#cpp-pdf-to-excel-xls)
- [C++ PDFからExcel XLSへのコンバータ](#cpp-pdf-to-excel-xls)

_フォーマット_: **Microsoft Excel XLSX形式**
- [C++ PDFからExcel XLSXへのコード](#cpp-pdf-to-excel-xlsx)

- [C++ プログラムによるPDFからExcel XLSXへの変換](#cpp-pdf-to-excel-xlsx)
- [C++ PDFからExcel XLSXライブラリ](#cpp-pdf-to-excel-xlsx)
- [C++ PDFをExcel XLSXとして保存](#cpp-pdf-to-excel-xlsx)
- [C++ PDFからExcel XLSXを生成](#cpp-pdf-to-excel-xlsx)
- [C++ PDFからExcel XLSXを作成](#cpp-pdf-to-excel-xlsx)
- [C++ PDFからExcel XLSXコンバーター](#cpp-pdf-to-excel-xlsx)

_フォーマット_: **XLS**
- [C++ PDFからXLSコード](#cpp-pdf-to-xls)
- [C++ PDFをXLSでプログラム的に](#cpp-pdf-to-xls)
- [C++ PDFからXLSライブラリ](#cpp-pdf-to-xls)
- [C++ PDFをXLSとして保存](#cpp-pdf-to-xls)
- [C++ PDFからXLSを生成](#cpp-pdf-to-xls)
- [C++ PDFからXLSを作成](#cpp-pdf-to-xls)
- [C++ PDFからXLSコンバーター](#cpp-pdf-to-xls)

_フォーマット_: **XLSX**
- [C++ PDFからXLSXコード](#cpp-pdf-to-xlsx)
- [C++ PDFをXLSXでプログラム的に](#cpp-pdf-to-xlsx)
- [C++ PDFからXLSXライブラリ](#cpp-pdf-to-xlsx)
- [C++ PDFをXLSXとして保存](#cpp-pdf-to-xlsx)
- [C++ PDFからXLSXを生成](#cpp-pdf-to-xlsx)
- [C++ PDFからXLSXを作成](#cpp-pdf-to-xlsx)
- [C++ PDFからXLSXコンバーター](#cpp-pdf-to-xlsx)