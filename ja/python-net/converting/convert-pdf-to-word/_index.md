---
title: PythonでPDFをWordに変換
linktitle: PDFをWordに変換
type: docs
weight: 10
url: /ja/python-net/convert-pdf-to-word/
lastmod: "2026-04-14"
description: PythonでPDFをWordに変換する方法を学び、PDFからDOC、PDFからDOCXへの変換、およびAspose.PDFを使用した高度なレイアウト認識を含みます。
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PythonでPDFをDOCおよびDOCXに変換
Abstract: この記事では、Aspose.PDF for Python via .NET を使用して PDF ファイルを Microsoft Word フォーマットに変換する方法を示します。PDF から DOC、PDF から DOCX への変換、および PDF コンテンツから編集可能な Word ドキュメントを作成するための高度なレイアウト認識オプションについて説明します。
---

このページでは、**Python で PDF を Word に変換する方法**を示します。PDF ファイルから編集可能な DOC または DOCX 出力が必要な場合、改訂、再利用、またはオフィス文書ワークフローのためにこれらの例を使用してください。

## Python で PDF を DOC に変換

最も人気のある機能のひとつは、PDF から Microsoft Word DOC への変換で、コンテンツ管理が容易になります。**Aspose.PDF for Python via .NET** を使用すると、PDF ファイルを DOC だけでなく DOCX フォーマットにも簡単かつ効率的に変換できます。

テキストを修正したり、オフィスワークフローでコンテンツを再利用したり、PDF コンテンツを編集可能な DOC または DOCX ドキュメントに移動する必要がある場合は、Word 変換を使用してください。

その [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) クラスは、PDF ファイルを DOC 形式に変換するプロセスを改善する多数のプロパティを提供します。これらのプロパティの中で、Mode は PDF コンテンツの認識モードを指定できるようにします。このプロパティには RecognitionMode 列挙体の任意の値を指定できます。これらの値それぞれには特定の利点と制限があります：

手順: PythonでPDFをDOCに変換する

1. PDFを'ap.Document'オブジェクトにロードします。
1. 'DocSaveOptions' インスタンスを作成します。
1. 出力が .doc 形式（旧Word形式）になるよう、format プロパティを 'DocFormat.DOC' に設定します。
1. 指定された保存オプションを使用して、PDF を Word 文書として保存します。
1. 確認メッセージを出力します。

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOC(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**PDF を DOC にオンラインで変換してみてください**

Aspose.PDF for Python はオンラインアプリケーションを提供します ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), そこで機能と品質がどのように動作するかを調査できます。

[![PDF を DOC に変換](/pdf/ja/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Python で PDF を DOCX に変換

Aspose.PDF for Python API は、Python via .NET を使用して PDF ドキュメントを DOCX に読み取りおよび変換できます。DOCX は、構造がプレーンバイナリから XML とバイナリファイルの組み合わせに変更された、Microsoft Word ドキュメント用の広く知られたフォーマットです。Docx ファイルは Word 2007 およびそれ以降のバージョンで開くことができますが、DOC ファイル拡張子をサポートする以前のバージョンの MS Word では開けません。

以下の Python コードスニペットは、PDF ファイルを DOCX 形式に変換するプロセスを示しています。

手順: Python で PDF を DOCX に変換する

1. 'ap.Document' を使用してソース PDF を読み込みます。
1. 'DocSaveOptions' のインスタンスを作成します。
1. format プロパティを 'DocFormat.DOC_X' に設定して、.docx ファイル（モダンな Word フォーマット）を生成します。
1. 設定した保存オプションで PDF を DOCX ファイルとして保存します。
1. 変換後に確認メッセージを出力します。

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOCX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    document.save(outfile, save_options)
```

## 高度なレイアウト認識による PDF から DOCX への変換

Python と Aspose.PDF を使用し、詳細な認識設定で PDF ドキュメントを DOCX（Word）ファイルに変換します。強化されたフローモードを使用して文書構造を保持し、出力をより編集しやすく、元のレイアウトに近い形にします。

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOCX_advanced(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    save_options.mode = ap.DocSaveOptions.RecognitionMode.ENHANCED_FLOW
    document.save(outfile, save_options)
```

その [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) クラスには Format というプロパティがあり、生成されるドキュメントの形式（DOC または DOCX）を指定する機能を提供します。PDF ファイルを DOCX 形式に変換するには、DocSaveOptions.DocFormat 列挙体の Docx 値を渡してください。

{{% alert color="warning" %}}
**PDF を DOCX にオンラインで変換してみましょう**

Aspose.PDF for Python はオンラインアプリケーションを提供します ["PDF を Word に"](https://products.aspose.app/pdf/conversion/pdf-to-docx), そこで機能と品質がどのように動作するかを調査できます。

[![Aspose.PDF コンバージョン PDF to Word アプリ](/pdf/ja/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## 関連する変換

- [PDF を Excel に変換](/pdf/ja/python-net/convert-pdf-to-excel/) スプレッドシート指向のエクスポート用です。
- [PDF を PowerPoint に変換](/pdf/ja/python-net/convert-pdf-to-powerpoint/) ワードプロセッシング出力ではなく、プレゼンテーションスライドが必要な場合。
- [PDF を HTML に変換](/pdf/ja/python-net/convert-pdf-to-html/) ウェブ公開やブラウザベースのコンテンツワークフロー向け。
