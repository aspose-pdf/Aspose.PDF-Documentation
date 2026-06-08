---
title: PythonでPDFをExcelに変換する
linktitle: PDFをExcelに変換する
type: docs
weight: 20
url: /ja/python-net/convert-pdf-to-excel/
lastmod: "2026-04-14"
description: PythonでPDFをExcelに変換する方法を学ぶ、XLS、XLSX、CSV、ODS、単一シート出力、列処理を含み、Aspose.PDFを使用して。
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PythonでPDFをExcel、XLSX、CSV、ODSに変換する。
Abstract: この記事では、Aspose.PDF for Python via .NET を使用して PDF ファイルをスプレッドシート形式に変換する方法を示します。XLS、XLSX、XLSM、CSV、ODS の出力に加え、空白列の制御や生成されるワークシート数の削減オプションについて説明します。
---

## PythonでPDFをExcelに変換する

**Aspose.PDF for Python via .NET** は、PythonコードからPDFファイルをExcelやその他のスプレッドシート形式に変換することをサポートしています。

PDFをXLS、XLSX、CSV、またはODSに変換してテーブル抽出、レポート再利用、ソート、フィルタリング、または下流分析が必要な場合は、このページを使用してください。PDFからExcelへの変換中に、個々のPDFページをExcelのワークシートとしてレンダリングできます。

最初の例では、PDF ファイルを Spreadsheet 2003 XML 形式に変換します。後のセクションでは、XLSX、XLSM、CSV、ODS、および単一シートの出力を示します。

{{% alert color="success" %}}
**PDF をオンラインで Excel に変換してみましょう**

Aspose.PDF はオンラインアプリケーションを提供します ["PDFからXLSXへ"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)、機能と品質がどのように動作するかを調査できる場所です。

[![Aspose.PDF アプリで PDF を Excel に変換](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

次のコードスニペットは、Aspose.PDF for Python via .NET を使用して PDF ファイルを XLS または XLSX 形式に変換する手順を示しています。

手順: PDF ファイルを Excel (XML Spreadsheet 2003) 形式に変換する

1. PDFドキュメントを読み込む。
1. 使用してExcelの保存オプションを設定する [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. 変換されたファイルを保存してください。

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_spread_sheet2003(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## PythonでPDFをXLSXに変換する

手順: PDF ファイルを XLSX 形式 (Excel 2007 以上) に変換する

1. PDFドキュメントを読み込む。
1. 使用してExcelの保存オプションを設定する [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. 変換されたファイルを保存してください。

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## 列制御付きで PDF を XLSX に変換

PDF を Excel 形式に変換する際、出力ファイルの最初の列として空白列が追加されることがあります。使用してください `insert_blank_column_at_first` オプションの `ExcelSaveOptions` この動作を制御するクラス。そのデフォルト値は `true`.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_control_column(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.insert_blank_column_at_first = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## PDF を単一の Excel ワークシートに変換

Aspose.PDF for Python via .NET は、'minimize_the_number_of_worksheets' オプションを有効にして、PDF を Excel（.xlsx）ファイルに変換する方法を示しています。

手順: PythonでPDFをXLSまたはXLSXの単一ワークシートに変換

1. PDFドキュメントを読み込む。
1. 使用してExcelの保存オプションを設定する [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. 「'minimize_the_number_of_worksheets' オプションは、PDF ページを結合して Excel シートの数を減らし、より少ないワークシートにします（例: 可能であれば文書全体を1つのワークシートに）。
1. 変換されたファイルを保存してください。

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_single_excel_worksheet(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.minimize_the_number_of_worksheets = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## PDFをExcel 2007マクロ有効（XLSM）に変換

このPythonの例では、PDFファイルをXLSM形式（Excelマクロ有効ブック）のExcelファイルに変換する方法を示しています。

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_macro(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSM
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## 他のスプレッドシート形式に変換

### PDFをCSVに変換

‘convert_pdf_to_excel_2007_csv’ 関数は、以前と同じ操作を実行しますが、今回はターゲット形式がXLSMではなくCSV（カンマ区切り値）です。

手順: PythonでPDFをCSVに変換

1. インスタンスを作成する [ドキュメント](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) ソースPDFドキュメントを持つオブジェクト。
1. インスタンスを作成する [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) **ExcelSaveOptions.ExcelFormat.CSV** を使用して
1. 呼び出すことで **CSV** 形式で保存します [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* メソッドとそれを渡す [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_csv(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.CSV
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### PDF を ODS に変換

手順: PythonでPDFをODSに変換する

1. インスタンスを作成する [ドキュメント](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) ソースPDFドキュメントを持つオブジェクト。
1. インスタンスを作成する [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) **ExcelSaveOptions.ExcelFormat.ODS** を使用して
1. **ODS**形式で保存するには、呼び出すことで [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドとそれを渡す [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

ODS形式への変換は、他のすべての形式と同じ方法で実行されます。

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_ods(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.ODS
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## 関連する変換

- [PDF を Word に変換](/pdf/ja/python-net/convert-pdf-to-word/) 優先事項がスプレッドシート構造ではなく、編集可能なテキストフローである場合。
- [PDF を HTML に変換](/pdf/ja/python-net/convert-pdf-to-html/) ブラウザ向けの出力が必要なとき。
- [PDF を他の形式に変換する](/pdf/ja/python-net/convert-pdf-to-other-files/) EPUB、Markdown、テキスト、XPS、そして関連するエクスポートワークフロー用に。
