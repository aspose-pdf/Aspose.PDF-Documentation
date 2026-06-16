---
title: Python で PDF を Excel に変換
linktitle: PDF をエクセルに変換
type: docs
weight: 20
url: /ja/python-net/convert-pdf-to-excel/
lastmod: "2026-06-09"
description: XLS、XLSX、CSV、ODS、単一ワークシート出力、Aspose.PDF による列処理など、Python で PDF を Excel に変換する方法を学びましょう。
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF をエクセル、XLSX、CSV、ODS に変換
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ファイルをスプレッドシート形式に変換する方法を説明します。XLS、XLSX、XLSM、CSV、ODS 出力のほか、空白列を制御して生成されるワークシートの数を減らすためのオプションについても説明します。
---

## Python で PDF を Excel に変換

**.NET 経由の Python 用 Aspose.PDF ** は、PDF ファイルを Python コードから Excel やその他のスプレッドシート形式に変換することをサポートしています。

このページは、表の抽出、レポートの再利用、ソート、フィルタリング、またはダウンストリーム分析のためにPDFをXLS、XLSX、CSV、またはODSに変換する必要がある場合に使用します。PDF から Excel への変換中に、個々の PDF ページを Excel ワークシートとしてレンダリングできます。

最初の例では、PDF ファイルをスプレッドシート 2003 の XML 形式に変換します。後のセクションでは、XLSX、XLSM、CSV、ODS、および単一ワークシートの出力について説明します。

{{% alert color="success" %}}
**オンラインでPDFをExcelに変換してみてください**

Aspose.PDF はオンライン申請書を提示します [「PDF から XLSX へ」](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)ここで、機能や動作品質を調べてみるといいかもしれません。

[![Aspose.PDF アプリで PDF を Excel に変換](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

次のコードスニペットは、.NET 経由で Aspose.PDF for Python を使用して PDF ファイルを XLS 形式または XLSX 形式に変換するプロセスを示しています。

手順:PDF ファイルを Excel (XML スプレッドシート 2003) 形式に変換する

1. PDF ドキュメントをロードします。
1. Excel の保存オプションの設定方法 [Excel 保存オプション](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. 変換したファイルを保存します。

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

## Python で PDF を XLSX に変換

手順:PDF ファイルを XLSX 形式に変換する (エクセル 2007+)

1. PDF ドキュメントをロードします。
1. Excel の保存オプションの設定方法 [Excel 保存オプション](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. 変換したファイルを保存します。

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

## カラムコントロールを使用して PDF を XLSX に変換

PDF を Excel 形式に変換する場合、出力ファイルの最初の列として空白の列を追加できます。を使用してください。 `insert_blank_column_at_first` のオプション `ExcelSaveOptions` この動作を制御するクラス。デフォルト値は `true`.

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

Aspose.PDF for Python via .NET では、「minimize_the_number_of_worksheets」オプションを有効にして PDF を Excel (.xlsx) ファイルに変換する方法を示しています。

手順:Python で PDF を XLS または XLSX の単一ワークシートに変換する

1. PDF ドキュメントをロードします。
1. Excel の保存オプションの設定方法 [Excel 保存オプション](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. 「minimize_the_number_of_worksheets」オプションを使用すると、PDF ページをより少ない数のワークシートにまとめることで、Excel シートの数を減らすことができます（たとえば、可能であれば、ドキュメント全体に 1 つのワークシート）。
1. 変換したファイルを保存します。

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

## PDF を Excel 2007 マクロ対応 (XLSM) に変換

この Python の例は、PDF ファイルを XLSM フォーマットの Excel ファイル (Excel マクロが有効なワークブック) に変換する方法を示しています。

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

### PDF ファイルを CSV ファイルに変換

「convert_pdf_to_excel_2007_csv」関数は以前と同じ操作を実行しますが、今回のターゲットフォーマットはXLSMではなくCSV（カンマ区切り値）です。

手順:Python で PDF を CSV に変換する

1. のインスタンスを作成 [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) ソース PDF ドキュメントを含むオブジェクト。
1. のインスタンスを作成 [Excel 保存オプション](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) **Excel保存オプション.Excelフォーマット.csv**付き
1. を呼び出して**CSV**形式に保存 [保存 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* メソッドと渡し [Excel 保存オプション](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

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

### PDF ファイルを ODS ファイルに変換

手順:Python で PDF を ODS に変換する

1. のインスタンスを作成 [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) ソース PDF ドキュメントを含むオブジェクト。
1. のインスタンスを作成 [Excel 保存オプション](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) **Excel保存オプション.ExcelFormat.ods**付き
1. を呼び出して**ODS**形式に保存します [保存 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドとそれを渡す [Excel 保存オプション](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

ODS 形式への変換は、他のすべての形式と同じ方法で実行されます。

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

## 関連コンバージョン

- [PDF をワードに変換](/pdf/ja/python-net/convert-pdf-to-word/) スプレッドシート構造よりも編集可能なテキストフローを優先する場合
- [PDF ファイルを HTML 形式に変換](/pdf/ja/python-net/convert-pdf-to-html/) ブラウザに適した出力が必要な場合。
- [PDF を他の形式に変換](/pdf/ja/python-net/convert-pdf-to-other-files/) EPUB、マークダウン、テキスト、XPS、および関連するエクスポートワークフロー用。
