---
title: PDFドキュメントをプログラムで開く
linktitle: PDFを開く
type: docs
weight: 20
url: /ja/python-net/open-pdf-document/
description: Python Aspose.PDF for Python via .NETライブラリでPDFファイルを開く方法を学びます。既存のPDF、ストリームからのドキュメント、および暗号化されたPDFドキュメントを開くことができます。
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 既存のPDFドキュメントを開く

ドキュメントを開く方法はいくつかあります。最も簡単なのはファイル名を指定することです。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)
    print("ページ数: " + str(len(document.pages)))
```

## ストリームから既存のPDFドキュメントを開く

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    stream = io.FileIO(input_pdf, 'r')
    # ドキュメントを開く
    document = ap.Document(stream)
    print("ページ数: " + str(len(document.pages)))
```

## 暗号化されたPDFドキュメントを開く

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf, password)
    print("ページ数: " + str(len(document.pages)))
```