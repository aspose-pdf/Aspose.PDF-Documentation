---
title: リストスタンプ
type: docs
weight: 70
url: /ja/python-net/list-stamps/
description: 次の使用例は、PDF を読み込み、1 ページ目からすべてのスタンプを取得して印刷し、スタンプが見つからない場合はメッセージを表示します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDF コンテンツエディタを使用して PDF 内のラバースタンプ注釈を一覧表示する
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF ドキュメントからラバースタンプの注釈を取得して一覧表示する方法を示しています。特定のページのスタンプにアクセスしてその詳細を表示する方法を示しています。
---

注釈付きPDFで作業する場合、既存のラバースタンプを変更したり削除したりする前に、それらを調べる必要がある場合があります。'get_stamps () 'メソッドを使うと、特定のページに置かれたすべてのスタンプを取得できます。その後、結果を繰り返し処理してプログラムで処理できます。

1. を作成 [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) インスタンス。
1. 入力 PDF ドキュメントをバインドします。
1. 1ページ目からすべてのスタンプを取得
1. スタンプコレクションを繰り返し処理します。
1. 各スタンプを印刷します。
1. スタンプが存在しない場合はメッセージを表示します。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def list_stamps(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # List all stamps on page 1
    stamps = content_editor.get_stamps(1)

    count = 0
    for stamp in stamps:
        count += 1
        print(f"Stamp {count}: {stamp}")

    if count == 0:
        print("No stamps found")
```
