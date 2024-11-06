---
title: プログラムでPDFドキュメントを保存する
linktitle: PDFを保存
type: docs
weight: 30
url: ja/python-cpp/save-pdf-document/
description: Python Aspose.PDF for Python via C++ライブラリでPDFファイルを保存する方法を学びます。PDFドキュメントをファイルシステム、ストリーム、およびWebアプリケーションに保存します。
lastmod: "2023-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## ファイルシステムにPDFドキュメントを保存する

```python

    import AsposePDFPythonWrappers as ap

    document = ap.Document("sample.pdf")
    document.pages.add()
    document.save("sample_mod.pdf")
```