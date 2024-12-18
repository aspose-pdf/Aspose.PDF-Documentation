---
title: PythonでPDFをExcelに変換
linktitle: PDFをExcelに変換
type: docs
weight: 20
url: /ja/python-net/convert-pdf-to-excel/
lastmod: "2022-12-23"
description: Aspose.PDF for Pythonライブラリを使用すると、PythonでPDFをExcel形式に変換できます。これらの形式には、XLS、XLSX、XML 2003スプレッドシート、CSV、ODSが含まれます。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 概要

この記事では、Pythonを使用して**PDFをExcel形式に変換する方法**を説明します。次のトピックをカバーしています。

_フォーマット_: **XLS**

- [Python PDFをXLSに変換](#python-pdf-to-xls)
- [Python PDFをXLSに変換する](#python-pdf-to-xls)
- [Python PDFファイルをXLSに変換する方法](#python-pdf-to-xls)

_フォーマット_: **XLSX**

- [Python PDFをXLSXに変換](#python-pdf-to-xlsx)
- [Python PDFをXLSXに変換する](#python-pdf-to-xlsx)
- [Python PDFファイルをXLSXに変換する方法](#python-pdf-to-xlsx)

_フォーマット_: **Excel**

- [Python PDF to Excel](#python-pdf-to-xlsx)
- [Python PDF to Excel XLS](#python-pdf-to-xls)
- [Python PDF to Excel XLSX](#python-pdf-to-xlsx)

_フォーマット_: **CSV**

- [Python PDF to CSV](#python-pdf-to-csv)
- [Python Convert PDF to CSV](#python-pdf-to-csv)
- [Python How to convert PDF file to CSV](#python-pdf-to-csv)

_フォーマット_: **ODS**

- [Python PDF to ODS](#python-pdf-to-ods)
- [Python Convert PDF to ODS](#python-pdf-to-ods)
- [Python How to convert PDF file to ODS](#python-pdf-to-ods)

## PDFをPython経由でEXCELに変換

**Aspose.PDF for Python via .NET**は、PDFファイルをExcelおよびCSV形式に変換する機能をサポートしています。

Aspose.PDF for Python via .NETはPDF操作コンポーネントであり、PDFファイルをExcelワークブック（XLSXファイル）にレンダリングする機能を導入しました。この変換中に、PDFファイルの個々のページがExcelワークシートに変換されます。

{{% alert color="success" %}}
**PDFをExcelにオンラインで変換してみる**

Aspose.PDFは、オンラインで無料のアプリケーション["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)を提供しており、そこで機能と品質を調査してみることができます。

[![Aspose.PDF Convertion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

次のコードスニペットは、Aspose.PDF for Python via .NETを使用してPDFファイルをXLSまたはXLSX形式に変換するプロセスを示しています。

<a name="python-pdf-to-xls"><strong>手順: PythonでPDFをXLSに変換する</strong></a>

1. ソースPDFドキュメントで[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)オブジェクトのインスタンスを作成します。
2. [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)のインスタンスを作成します。
3. [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)メソッドを呼び出し、[ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)を渡して、**.xls拡張子**を指定して**XLS**形式で保存します。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xls.xls"
    # PDFドキュメントを開く
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003

    # ファイルをMS Excel形式で保存
    document.save(output_pdf, save_option)
```


<a name="python-pdf-to-xlsx"><strong>ステップ: PythonでPDFをXLSXに変換する</strong></a>

1. ソースPDFドキュメントで[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)オブジェクトのインスタンスを作成します。
2. [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)のインスタンスを作成します。
3. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)メソッドを呼び出し、[ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)を渡すことで、**.xlsx拡張子**を指定して**XLSX**形式で保存します。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_xlsx.xlsx"
    # PDFドキュメントを開く
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()

    # ファイルをMS Excel形式で保存
    document.save(output_pdf, save_option)
```

## PDFをXLSに変換し、列を制御する

PDFをXLS形式に変換すると、最初の列として空白の列が出力ファイルに追加されます。
 'ExcelSaveOptions クラス' の InsertBlankColumnAtFirst オプションは、この列を制御するために使用されます。デフォルト値は true です。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xlsx_with_control_column.xls"
    # PDF ドキュメントを開く
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    save_option.insert_blank_column_at_first = True

    # ファイルを MS Excel 形式で保存
    document.save(output_pdf, save_option)
```

## PDF を単一の Excel ワークシートに変換

多くのページを含む PDF ファイルを XLS にエクスポートする際、各ページは Excel ファイルの異なるシートにエクスポートされます。これは、MinimizeTheNumberOfWorksheets プロパティがデフォルトで false に設定されているためです。出力 Excel ファイルで全てのページを一つのシートにエクスポートするには、MinimizeTheNumberOfWorksheets プロパティを true に設定します。

<a name="python-pdf-to-excel-single"><strong>手順: Python で PDF を XLS または XLSX 単一ワークシートに変換</strong></a>
1. ソースPDFドキュメントで[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)オブジェクトのインスタンスを作成します。
2. **MinimizeTheNumberOfWorksheets = true**を使用して[ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)のインスタンスを作成します。
3. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)メソッドを呼び出し、[ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)を渡すことで、単一のワークシートを持つ**XLS**または**XLSX**形式で保存します。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xlsx_single_excel_worksheet.xls"
    # PDFドキュメントを開く
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    save_option.minimize_the_number_of_worksheets = True

    # ファイルをMS Excel形式で保存
    document.save(output_pdf, save_option)

```


## 他のスプレッドシート形式に変換

### CSVに変換

CSV形式への変換は、上記と同じ方法で行われます。必要なのは適切な形式を設定することです。

<a name="python-pdf-to-csv"><strong>手順: PDFをPythonでCSVに変換</strong></a>

1. ソースPDFドキュメントを持つ[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)オブジェクトのインスタンスを作成します。
2. **Format = ExcelSaveOptions.ExcelFormat.CSV**を使用して、[ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)のインスタンスを作成します。
3. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)*メソッドを呼び出し、[ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)を渡すことで、**CSV**形式に保存します。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_csv.csv"
    # PDFドキュメントを開く
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.CSV

    # ファイルを保存
    document.save(output_pdf, save_option)
```


### ODSに変換

<a name="python-pdf-to-ods"><strong>手順: PDFをPythonでODSに変換</strong></a>

1. ソースPDFドキュメントを持つ[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)オブジェクトのインスタンスを作成します。
2. [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)のインスタンスを**Format = ExcelSaveOptions.ExcelFormat.ODS**で作成します。
3. [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)を渡して[save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)メソッドを呼び出し、**ODS**形式で保存します。

ODS形式への変換は、他のすべての形式と同じ方法で行われます。

```python

    import aspose.pdf as ap
    
    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_ods.ods"
    # PDFドキュメントを開く
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.ODS

    # ファイルを保存する
    document.save(output_pdf, save_option)
```


## See Also 

この記事では、これらのトピックについても説明します。コードは上記と同じです。

_Format_: **Excel**
- [Python PDFをExcelコードに](#python-pdf-to-xlsx)
- [Python PDFをExcel APIに](#python-pdf-to-xlsx)
- [Python PDFをExcelプログラムで](#python-pdf-to-xlsx)
- [Python PDFをExcelライブラリに](#python-pdf-to-xlsx)
- [Python PDFをExcelとして保存](#python-pdf-to-xlsx)
- [Python PDFからExcelを生成](#python-pdf-to-xlsx)
- [Python PDFからExcelを作成](#python-pdf-to-xlsx)
- [Python PDFをExcelに変換](#python-pdf-to-xlsx)

_Format_: **XLS**
- [Python PDFをXLSコードに](#python-pdf-to-xls)
- [Python PDFをXLS APIに](#python-pdf-to-xls)
- [Python PDFをXLSプログラムで](#python-pdf-to-xls)
- [Python PDFをXLSライブラリに](#python-pdf-to-xls)
- [Python PDFをXLSとして保存](#python-pdf-to-xls)
- [Python PDFからXLSを生成](#python-pdf-to-xls)
- [Python PDFからXLSを作成](#python-pdf-to-xls)
- [Python PDFをXLSに変換](#python-pdf-to-xls)

_Format_: **XLSX**

- [Python PDFをXLSXコードに](#python-pdf-to-xlsx)
- [Python PDF to XLSX API](#python-pdf-to-xlsx)
- [Python PDF to XLSX Programmatically](#python-pdf-to-xlsx)
- [Python PDF to XLSX Library](#python-pdf-to-xlsx)
- [Python Save PDF as XLSX](#python-pdf-to-xlsx)
- [Python Generate XLSX from PDF](#python-pdf-to-xlsx)
- [Python Create XLSX from PDF](#python-pdf-to-xlsx)
- [Python PDF to XLSX Converter](#python-pdf-to-xlsx)

_フォーマット_: **CSV**
- [Python PDF to CSV Code](#python-pdf-to-csv)
- [Python PDF to CSV API](#python-pdf-to-csv)
- [Python PDF to CSV Programmatically](#python-pdf-to-csv)
- [Python PDF to CSV Library](#python-pdf-to-csv)
- [Python Save PDF as CSV](#python-pdf-to-csv)
- [Python Generate CSV from PDF](#python-pdf-to-csv)
- [Python Create CSV from PDF](#python-pdf-to-csv)
- [Python PDF to CSV Converter](#python-pdf-to-csv)

_フォーマット_: **ODS**
- [Python PDF to ODS Code](#python-pdf-to-ods)
- [Python PDF to ODS API](#python-pdf-to-ods)
- [Python PDF to ODS Programmatically](#python-pdf-to-ods)
- [Python PDF to ODS Library](#python-pdf-to-ods)

- [Python Save PDF as ODS](#python-pdf-to-ods)
- [Python PDFからODSを生成](#python-pdf-to-ods)
- [Python PDFからODSを作成](#python-pdf-to-ods)
- [Python PDFからODSへのコンバーター](#python-pdf-to-ods)