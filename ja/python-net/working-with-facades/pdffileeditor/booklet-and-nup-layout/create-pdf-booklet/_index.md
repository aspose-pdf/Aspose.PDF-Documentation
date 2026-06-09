---
title: PDF ブックレットを作成
type: docs
weight: 20
url: /ja/python-net/create-pdf-booklet/
description: Python 用 Aspose.PDF を使用して既存のドキュメントからブックレットスタイルの PDF を生成します
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して既存の PDF ファイルから PDF ブックレットを作成する
Abstract: Aspose.PDF for Python を使用して既存の文書から小冊子スタイルの PDF を生成する方法を学びましょう。この例は、PDFFileEditor クラスを使用してページを再配置し、小冊子として印刷したり折りたたんだりできるようにする方法を示しています。このメソッドは、適切な小冊子のレイアウトになるように自動的にページの順序を決めます。
---

小冊子スタイルの文書を作成することは、印刷用の PDF を作成するときの一般的な要件です。小冊子レイアウトでは、印刷して折りたたんだときに正しい順序で表示されるように、ページが再配置されます。

Aspose.PDF for Python を使用すると、開発者は標準の PDF を簡単に小冊子に変換できます。 [PDF ファイルエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) クラス。'make_booklet' メソッドは、入力文書のページを自動的に再編成し、小冊子の印刷に最適化された新しい PDF を生成します。

1. 既存の PDF ドキュメントを開きます。
1. PDF ファイルエディターのインスタンスを作成します。
1. make_booklet メソッドを使用してページを再編成します。
1. 出力を小冊子対応の PDF ファイルとして保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create PDF Booklet
def create_pdf_booklet(infile, outfile):
    # Create BookletMaker object
    booklet_maker = pdf_facades.PdfFileEditor()
    # Make booklet from input PDF file and save to output PDF file
    booklet_maker.make_booklet(FileIO(infile), FileIO(outfile, "w"))
```

このコードスニペットは、の「try_make_booklet」メソッドの使用方法を示しています [PDF ファイルエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) クラスを使用すると、操作が失敗した場合に例外を発生させずに小冊子印刷用にページを再配置できます。

小冊子のレイアウトでは、印刷したり折りたたんだりしたときに文書が正しい順序で読み込まれるようにページが再配置されます。このプロセスを自動化すると、一貫した結果が得られ、手動でページを再配置する必要がなくなります。

「try_make_booklet」メソッドは「make_booklet」メソッドと同様に機能しますが、重要な違いがあります。

- 'make_booklet' は、操作が失敗した場合に例外を投げます。
- 'try_make_booklet' は True または False を返すため、開発者はエラーをより安全に管理できます。

1. 既存の PDF ドキュメントを開きます。
1. PDF ファイルエディターのインスタンスを作成します。
1. ブックレットを作成してみます。
1. 結果を処理します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def try_create_pdf_booklet(infile, outfile):
    # Create BookletMaker object
    booklet_maker = pdf_facades.PdfFileEditor()
    # Make booklet from input PDF file and save to output PDF file
    # The try_make_booklet method is like the make_booklet method,
    # except the try_make_booklet method does not throw an exception if the operation fails.
    if not booklet_maker.try_make_booklet(FileIO(infile), FileIO(outfile, "w")):
        print("Failed to create booklet.")
```
