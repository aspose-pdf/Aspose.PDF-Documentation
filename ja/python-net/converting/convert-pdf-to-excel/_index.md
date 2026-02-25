---
title: PythonでPDFをExcelに変換する
linktitle: PDFをExcelに変換
type: docs
weight: 20
url: /ja/python-net/convert-pdf-to-excel/
lastmod: "2025-09-27"
description: Aspose.PDF for Python via .NET を使用して、PDF を簡単に Excel スプレッドシートに変換できます。このガイドに従って、正確な PDF から XLSX への変換を行ってください
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PythonでPDFをExcelに変換する方法
Abstract: この記事は、Python（特に Aspose.PDF for Python via .NET ライブラリ）を使用して PDF ファイルをさまざまな Excel 形式に変換する包括的なガイドを提供します。XLS、XLSX、CSV、ODS 形式への変換プロセスを詳細に説明します。本文では、PDF を XLS および XLSX に変換する手順を解説し、Document と ExcelSaveOptions インスタンスの作成および Document.Save() メソッドを使用して出力形式を指定する方法を強調します。また、変換時に空白列の挿入を制御したり、ワークシート数を最小化したりする機能についても議論します。さらに、PDF を単一の Excel ワークシートや CSV、ODS などの他の形式に変換する例を示し、Aspose.PDF の柔軟性と機能性を強調しています。PDF から XLSX へのオンライン変換ツールも紹介され、ユーザーが変換品質を確認できるようになっています。最後に、関連トピックのリストとコードスニペットを提供し、これらの変換をプログラムで実装する際の理解と実装を支援します。
---

## PythonによるPDFからEXCELへの変換

**Aspose.PDF for Python via .NET** は、PDF ファイルを Excel および CSV 形式に変換する機能をサポートしています。

**Aspose.PDF for Python via .NET** は PDF 操作コンポーネントであり、PDF ファイルを Excel ワークブック（XLSX ファイル）に変換する機能を導入しました。この変換では、PDF の各ページが Excel のワークシートに変換されます。

{{% alert color="success" %}}
**PDF をオンラインで Excel に変換してみる**

Aspose.PDF は、オンラインの無料アプリケーション ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx) を提供しています。機能と品質を試すことができます。

[![Aspose.PDF 無料アプリによる PDF から Excel への変換](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

以下のコードスニペットは、Aspose.PDF for Python via .NET を使用して PDF ファイルを XLS または XLSX 形式に変換するプロセスを示しています。

手順: PDF ファイルを Excel (XML Spreadsheet 2003) 形式に変換する

1. PDF ドキュメントを読み込む。
1. [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) を使用して Excel 保存オプションを設定する。
1. 変換されたファイルを保存する。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

手順: PDF ファイルを XLSX 形式（Excel 2007 以降）に変換する

1. PDF ドキュメントを読み込む。
1. [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) を使用して Excel 保存オプションを設定する。
1. 変換されたファイルを保存する。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSX
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## 列制御で PDF を XLS に変換

PDF を XLS 形式に変換する際、出力ファイルの最初の列に空白列が追加されます。'ExcelSaveOptions クラス' の 'insert_blank_column_at_first' オプションでこの列を制御します。デフォルト値は true です。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.insert_blank_column_at_first = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## PDF を単一の Excel ワークシートに変換する

Aspose.PDF for Python via .NET は、'minimize_the_number_of_worksheets' オプションを有効にして、PDF を Excel（.xlsx）ファイルに変換する方法を示しています。

手順: Python で PDF を XLS または XLSX の単一ワークシートに変換する

1. PDF ドキュメントを読み込む。
1. [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) を使用して Excel 保存オプションを設定する。
1. 'minimize_the_number_of_worksheets' オプションは、PDF ページを結合して Excel シートの数を減らし、可能であれば文書全体を 1 つのワークシートにします。
1. 変換されたファイルを保存する。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.minimize_the_number_of_worksheets = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## PDF ファイルを XLSM 形式の Excel ファイルに変換する

この Python の例は、PDF ファイルを XLSM 形式（Excel マクロ有効ブック）の Excel ファイルに変換する方法を示しています。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSM
    document.save(path_outfile, save_options)
    print(infile + " converted into " + outfile)
```

## 他のスプレッドシート形式に変換する

### CSV に変換する

'convert_pdf_to_excel_2007_csv' 関数は、前と同じ操作を実行しますが、今回はターゲット形式が XLSM ではなく CSV（カンマ区切り値）になります。

手順: Python で PDF を CSV に変換する

1. ソース PDF ドキュメントを使用して [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトのインスタンスを作成する。
1. **ExcelSaveOptions.ExcelFormat.CSV** を指定して [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) のインスタンスを作成する。
1. **CSV** 形式で保存するには、[save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* メソッドを呼び出し、[ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) を渡します。

```python

from os import path
import aspose.pdf as apdf

def convert_pdf_to_excel_2007_csv(infile, outfile):
    path_infile = path.join(data_dir, infile)
    path_outfile = path.join(data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### ODS に変換する

手順: Python で PDF を ODS に変換する

1. ソースPDFドキュメントで [ドキュメント](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトのインスタンスを作成します。
1. **ExcelSaveOptions.ExcelFormat.ODS** を使用して [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) のインスタンスを作成します。
1. **ODS** 形式で保存するには、[save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを呼び出し、[ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) を渡します。

ODS 形式への変換は、他のすべての形式と同じ方法で実行されます。

```python

    from os import path
    import aspose.pdf as apdf
    
    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.ODS
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

