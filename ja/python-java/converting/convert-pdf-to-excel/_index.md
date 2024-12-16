---
title: PDFをExcelに変換するPython
linktitle: PDFをExcelに変換
type: docs
weight: 20
url: /ja/python-java/convert-pdf-to-excel/
lastmod: "2022-12-23"
description: Aspose.PDF for Pythonライブラリは、Pythonを使用してPDFをExcel形式に変換することを可能にします。これらの形式には、XLS、XLSX、XML 2003スプレッドシート、CSV、ODSが含まれます。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 概要

この記事は、Pythonを使用して**PDFをExcel形式に変換する方法**を説明します。以下のトピックをカバーしています。

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

## PDFからEXCELへの変換をPythonで行う

**Aspose.PDF for Python via .NET**は、PDFファイルをExcelやCSV形式に変換する機能をサポートしています。

Aspose.PDF for Python via JavaはPDF操作コンポーネントであり、PDFファイルをExcelワークブック（XLSXファイル）にレンダリングする機能を導入しました。この変換中に、PDFファイルの各ページがExcelワークシートに変換されます。

{{% alert color="success" %}}
**PDFをExcelにオンラインで変換してみてください**

Aspose.PDFは、オンラインで無料のアプリケーション["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)を提供しており、その機能と品質を調査することができます。

[![Aspose.PDF Convertion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

次のコードスニペットは、Aspose.PDF for Python via Java を使用して PDF ファイルを XLS または XLSX 形式に変換するプロセスを示しています。

<a name="python-pdf-to-xls"><strong>手順: Python で PDF を XLS に変換</strong></a>

1. ソース PDF ドキュメントで [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) オブジェクトのインスタンスを作成します。
2. [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) のインスタンスを作成します。
3. [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) メソッドを呼び出し、[ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) を渡して、**.xls 拡張子**を指定して **XLS** 形式で保存します。

```python
from asposepdf import Api

# ライセンスを初期化
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# バイト配列からの変換
documentName = "testdata/source.pdf"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array)
documentOutName = "testout/result1.xls"
doc.save(documentOutName, Api.SaveFormat.Excel)

# ファイルからの変換
documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result2.xls"
doc.save(documentOutName, Api.SaveFormat.Excel)

# バイト配列からの変換
documentName = "testdata/source.pdf"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array)
documentOutName = "testout/result3.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
doc.save(documentOutName, Api.SaveFormat.Excel)

# ファイルからの変換
documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result4.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
doc.save(documentOutName, Api.SaveFormat.Excel)
```


<a name="python-pdf-to-xlsx"><strong>手順: PDFをPythonでXLSXに変換する</strong></a>

1. ソースPDFドキュメントを使用して[Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/)オブジェクトのインスタンスを作成します。
2. [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/)のインスタンスを作成します。
3. [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods)メソッドを呼び出し、[ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/)を渡すことで、**.xlsx拡張子**を指定して**XLSX**形式で保存します。

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.xlsx"
doc.save(documentOutName, save_option)
```

## 列を制御してPDFをXLSに変換する

PDFをXLS形式に変換する際、空白の列が最初の列として出力ファイルに追加されます。
 'ExcelSaveOptions クラス' の InsertBlankColumnAtFirst オプションは、この列を制御するために使用されます。デフォルト値は true です。

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.xlsx"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
save_option._insertBlankColumnAtFirst = True
doc.save(documentOutName, save_option)

```

## PDF を単一の Excel ワークシートに変換

多くのページを持つ PDF ファイルを XLS にエクスポートする場合、各ページは Excel ファイルの異なるシートにエクスポートされます。これは、MinimizeTheNumberOfWorksheets プロパティがデフォルトで false に設定されているためです。出力 Excel ファイルのすべてのページが単一のシートにエクスポートされるようにするには、MinimizeTheNumberOfWorksheets プロパティを true に設定します。

<a name="python-pdf-to-excel-single"><strong>手順: Python で PDF を XLS または XLSX の単一ワークシートに変換する</strong></a>
1. ソースPDFドキュメントを使用して、[Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) オブジェクトのインスタンスを作成します。
2. **MinimizeTheNumberOfWorksheets = True** を使用して、[ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) のインスタンスを作成します。
3. [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) メソッドを呼び出し、それに [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) を渡すことにより、単一のワークシートを持つ **XLS** または **XLSX** 形式で保存します。

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
save_option._minimizeTheNumberOfWorksheets = True
# ファイルをMS Excel形式で保存
doc.save(documentOutName, save_option)

```

## 他のスプレッドシート形式に変換する

### CSVに変換する

CSV形式への変換は、上記と同じ方法で行われます。必要なのは適切な形式を設定することです。

<a name="python-pdf-to-csv"><strong>手順: PythonでPDFをCSVに変換する</strong></a>

1. ソースPDFドキュメントで[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)オブジェクトのインスタンスを作成します。
2. **Format = ExcelSaveOptions.ExcelFormat.CSV**を使用して[ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/)のインスタンスを作成します。
3. [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods)メソッドを呼び出し、[ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/)を渡して**CSV**形式で保存します。

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.csv"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.CSV
doc.save(documentOutName, save_option)
```


### ODSに変換

<a name="python-pdf-to-ods"><strong>手順: PythonでPDFをODSに変換</strong></a>

1. ソースPDFドキュメントで[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)オブジェクトのインスタンスを作成します。
2. **Format = ExcelSaveOptions.ExcelFormat.ODS**で[ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/)のインスタンスを作成します。
3. [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods)メソッドを呼び出し、[ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/)を渡して、**ODS**形式で保存します。

ODS形式への変換は他のすべての形式と同じ方法で行われます。

```python

from asposepdf import Api

documentName = "../../testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "../../testout/result1.ods"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.ODS
doc.save(documentOutName, save_option)
```


## 参照

この記事はまたこれらのトピックもカバーしています。コードは上記と同じです。

_フォーマット_: **Excel**
- [Python PDF to Excel コード](#python-pdf-to-xlsx)
- [Python PDF to Excel API](#python-pdf-to-xlsx)
- [Python PDF to Excel プログラム的に](#python-pdf-to-xlsx)
- [Python PDF to Excel ライブラリー](#python-pdf-to-xlsx)
- [Python PDFをExcelとして保存](#python-pdf-to-xlsx)
- [Python PDFからExcelを生成](#python-pdf-to-xlsx)
- [Python PDFからExcelを作成](#python-pdf-to-xlsx)
- [Python PDF to Excel コンバーター](#python-pdf-to-xlsx)

_フォーマット_: **XLS**
- [Python PDF to XLS コード](#python-pdf-to-xls)
- [Python PDF to XLS API](#python-pdf-to-xls)
- [Python PDF to XLS プログラム的に](#python-pdf-to-xls)
- [Python PDF to XLS ライブラリー](#python-pdf-to-xls)
- [Python PDFをXLSとして保存](#python-pdf-to-xls)
- [Python PDFからXLSを生成](#python-pdf-to-xls)
- [Python PDFからXLSを作成](#python-pdf-to-xls)
- [Python PDF to XLS コンバーター](#python-pdf-to-xls)

_フォーマット_: **XLSX**

- [Python PDF to XLSX コード](#python-pdf-to-xlsx)
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