---
title: Python経由でC++を使用してPDFにページを追加
linktitle: ページを追加
type: docs
weight: 10
url: /ja/python-cpp/add-pages/
description: この記事では、C++を使用してPythonでPDFファイルの希望の位置にページを挿入（追加）する方法を教えます。
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 希望の位置にPDFファイルに空白ページを挿入

このコードスニペットはPDFドキュメントを開き、空白ページを追加し、変更されたドキュメントを新しいPDFファイルとして保存します。

PDFファイルに空白ページを挿入するには:

1. PDFドキュメントを開く
1. ドキュメントに新しい空白ページを追加する
1. 'document.save'メソッドで変更されたドキュメントを出力ファイルに保存する

以下のコードスニペットは、PDFファイルにページを挿入する方法を示しています:

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # サンプルPDFファイルがあるディレクトリパスを設定
    dataDir = os.path.join(os.getcwd(), "samples")

    # 入力ファイルパスを設定
    input_file = os.path.join(dataDir, "sample0.pdf")

    # 出力ファイルパスを設定
    output_file = os.path.join(dataDir, "results", "blank_pdf_document.pdf")

    # PDFドキュメントを開く
    document = apw.Document(input_file)

    # ドキュメントに新しい空白ページを追加
    document.pages.add()

    # 変更されたドキュメントを出力ファイルに保存
    document.save(output_file)
```