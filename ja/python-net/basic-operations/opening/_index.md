---
title: PDFドキュメントをプログラムで開く
linktitle: PDFを開く
type: docs
weight: 20
url: /ja/python-net/open-pdf-document/
description: Python用Aspose.PDF for .NETライブラリでPDFファイルを開く方法を学びます。既存のPDF、ストリームからのドキュメント、暗号化されたPDFドキュメントを開くことができます。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PythonでAspose.PDFライブラリを使用してPDFドキュメントを開く
Abstract: 本記事では、PythonでAspose.PDFライブラリを使用して既存のPDFドキュメントを開く方法についてガイドします。ファイル名を指定してPDFを開く方法、ストリームからPDFを開く方法、パスワードを提供して暗号化されたPDFを開く方法という3つの手法を概説しています。各手法には、Aspose.PDFライブラリを利用してPDFにアクセスし、ページ数を出力するコードスニペットが含まれています。これらの例は、さまざまなPDFファイルアクセスシナリオに対応するAspose.PDFの柔軟性と機能性を示しています。
---

## 既存のPDFドキュメントを開く

ドキュメントを開く方法は複数あります。最も簡単なのはファイル名を指定することです。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    print("Pages: " + str(len(document.pages)))
```

## ストリームから既存のPDFドキュメントを開く

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    stream = io.FileIO(input_pdf, 'r')
    # Open document
    document = ap.Document(stream)
    print("Pages: " + str(len(document.pages)))
```

## 暗号化されたPDFドキュメントを開く

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf, password)
    print("Pages: " + str(len(document.pages)))
```

