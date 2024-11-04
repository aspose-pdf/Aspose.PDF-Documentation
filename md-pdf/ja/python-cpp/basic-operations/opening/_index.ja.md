---
title: PDFドキュメントをプログラムで開く
linktitle: PDFを開く
type: docs
weight: 20
url: /python-cpp/open-pdf-document/
description: Python Aspose.PDF for Python via C++ライブラリでPDFファイルを開く方法を学びます。既存のPDF、ストリームからのドキュメント、および暗号化されたPDFドキュメントを開くことができます。
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 既存のPDFドキュメントを開く

ドキュメントを開く方法はいくつかあります。最も簡単なのはファイル名を指定することです。

```python

    import AsposePDFPythonWrappers as ap
    # ドキュメントを開く
    document = ap.Document("sample.pdf")
    count = document.pages.count()
    print("ページ数: " + str(count))
```

## 暗号化されたPDFドキュメントを開く

```python

    import AsposePDFPythonWrappers as ap
    # ドキュメントを開く
    document = ap.Document("sample.pdf","password")
    count = document.pages.count()
    print("ページ数: " + str(count))
```