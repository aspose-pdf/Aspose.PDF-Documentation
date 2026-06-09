---
title: Python で PDF をワードに変換
linktitle: PDF をワードに変換
type: docs
weight: 10
url: /ja/python-net/convert-pdf-to-word/
lastmod: "2026-06-09"
description: Python で PDF を Word に変換する方法 (PDF から DOC、PDF から DOCX、Aspose.PDF を使った高度なレイアウト認識など) を学びましょう。
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF を DOC と DOCX に変換
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ファイルを Microsoft Word 形式に変換する方法を説明します。PDF から DOC、PDF から DOC へ、PDF から DOCX へ、および PDF コンテンツから編集可能な Word 文書を作成するための高度なレイアウト認識オプションについて説明します。
---

このページでは、**Python で PDF を Word に変換する方法**を示しています。改訂、再利用、またはオフィス文書のワークフローのために PDF ファイルからの編集可能な DOC または DOCX 出力が必要な場合は、これらの例を使用してください。

## Python で PDF を DOC に変換

最も人気のある機能の1つは、PDFからMicrosoft Word DOCへの変換です。これにより、コンテンツ管理が容易になります。**.NET 経由の Python 用の Aspose.PDF を使用すると、PDF ファイルを DOC 形式だけでなく DOCX 形式にも簡単かつ効率的に変換できます。

テキストを修正したり、オフィスのワークフローでコンテンツを再利用したり、PDF コンテンツを編集可能な DOC や DOCX ドキュメントに移動したりする必要がある場合は、Word 変換を使用してください。

ザの [ドキュメント保存オプション](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) クラスには、PDF ファイルを DOC 形式に変換するプロセスを改善する多数のプロパティが用意されています。これらのプロパティの中でも、Mode では PDF コンテンツの認識モードを指定できます。このプロパティには RecognitionMode 列挙から任意の値を指定できます。これらの値にはそれぞれ固有の利点と制限があります。

手順:Python で PDF を DOC に変換する方法

1. PDF を「AP.Document」オブジェクトに読み込みます。
1. 「DocSaveOptions」インスタンスを作成します。
1. フォーマットプロパティを 'DocFormat.DOC' に設定して、出力が.doc 形式 (古い Word 形式) になるようにします。
1. 指定した保存オプションを使用して PDF を Word 文書として保存します。
1. 確認メッセージを印刷します。

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
**オンラインでPDFをDOCに変換してみてください**

Python 用の Aspose.PDF はオンラインアプリケーションを提供します [「PDF ファイルから DOC へ」](https://products.aspose.app/pdf/conversion/pdf-to-doc)ここで、機能や動作品質を調べてみるといいかもしれません。

[![PDF ファイルを DOC ファイルに変換](/pdf/ja/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Python で PDF を DOCX に変換

Aspose.PDF for Python API を使用すると、.NET 経由で Python を使用して PDF ドキュメントを読み取り、DOCX に変換できます。DOCX は Microsoft Word 文書でよく使われるフォーマットで、その構造は普通のバイナリファイルから XML ファイルとバイナリファイルの組み合わせに変更されました。Docx ファイルは Word 2007 およびラテラルバージョンで開くことができますが、DOC ファイル拡張子をサポートしている以前のバージョンの MS Word では開くことができません。

次の Python コードスニペットは、PDF ファイルを DOCX 形式に変換するプロセスを示しています。

手順:Python で PDF を DOCX に変換する

1. 「AP.ドキュメント」を使用してソースPDFをロードします。
1. 「DocSaveOptions」のインスタンスを作成します。
1. .docx ファイル (最新の Word フォーマット) を生成するには、フォーマットプロパティを 'DocFormat.doc_x' に設定します。
1. 設定した保存オプションを使用して PDF を DOCX ファイルとして保存します。
1. 変換後に確認メッセージを印刷します。

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

## 高度なレイアウト認識でPDFをDOCXに変換

高度な認識設定を備えた Python と Aspose.PDF を使用して PDF ドキュメントを DOCX (Word) ファイルに変換します。拡張フローモードを使用して文書構造を維持し、出力をより編集しやすくして元のレイアウトに近づけます。

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

ザの [ドキュメント保存オプション](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) class には Format という名前のプロパティがあり、生成されるドキュメントのフォーマット (DOC または DOCX) を指定できます。PDF ファイルを DOCX フォーマットに変換するには、docSaveOptions.docFormat 列挙の Docx 値を渡してください。

{{% alert color="warning" %}}
** PDFをDOCXにオンラインで変換してみてください**

Python 用の Aspose.PDF はオンラインアプリケーションを提供します [「PDF からワードへ」](https://products.aspose.app/pdf/conversion/pdf-to-docx)ここで、機能や動作品質を調べてみるといいかもしれません。

[![Aspose.PDF PDF から Word アプリへの変換](/pdf/ja/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## 関連コンバージョン

- [PDF をエクセルに変換](/pdf/ja/python-net/convert-pdf-to-excel/) スプレッドシート指向のエクスポート用。
- [PDF をパワーポイントに変換](/pdf/ja/python-net/convert-pdf-to-powerpoint/) ワープロ出力の代わりにプレゼンテーションスライドが必要な場合。
- [PDF ファイルを HTML 形式に変換](/pdf/ja/python-net/convert-pdf-to-html/) Web パブリッシングおよびブラウザベースのコンテンツワークフロー用。
