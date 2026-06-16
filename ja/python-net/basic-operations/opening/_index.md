---
title: PDF ドキュメントをプログラムで開く
linktitle: PDF を開く
type: docs
weight: 20
url: /ja/python-net/open-pdf-document/
description: .NET ライブラリ経由で Python Aspose.PDF for Python で PDF ファイルを開く方法を学びましょう。既存の PDF、ストリームからのドキュメント、および暗号化された PDF ドキュメントを開くことができます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の Aspose.PDF ライブラリを使用して PDF ドキュメントを開く
Abstract: この記事では、Python の Aspose.PDF ライブラリを使用して既存の PDF ドキュメントを開くためのガイドを提供します。そのために、ファイル名を指定して PDF を開く方法、ストリームから PDF を開く方法、パスワードを入力して暗号化された PDF を開く方法の 3 つの方法を概説しています。それぞれの方法には、Aspose.PDF ライブラリを使用して PDF にアクセスし、PDF に含まれるページ数を印刷する方法を示すコードスニペットが含まれています。これらの例は、さまざまな PDF ファイルアクセスシナリオを処理するための Aspose.PDF の柔軟性と機能性を示しています。
---

## 既存の PDF ドキュメントを開く

文書を開く方法はいくつかあります。最も簡単なのは、ファイル名を指定することです。

```python
import aspose.pdf as ap

def open_document_from_file(infile):

    # Open document
    document = ap.Document(infile)
    print("Pages: " + str(len(document.pages)))
```

## ストリームから既存の PDF ドキュメントを開く

```python
import aspose.pdf as ap
import io

def open_document_from_stream(infile):
    with io.FileIO(infile, "r") as stream:
        # Open document
        document = ap.Document(stream)
        print("Pages: " + str(len(document.pages)))
```

## 暗号化された PDF ドキュメントを開く

```python
import aspose.pdf as ap

def open_document_encrypted(infile):
    password = "P@ssw0rd"
    # Open document
    document = ap.Document(infile, password)
    print("Pages: " + str(len(document.pages)))
```
