---
title: Pythonを使用してPDFをC++経由でマージする方法
linktitle: PDFファイルをマージする
type: docs
weight: 10
url: /python-cpp/merge-pdf-documents/
keywords: "複数のPDFを単一のPDFにマージするPython, 複数のPDFを1つに結合するPython, 複数のPDFを1つにまとめるPython"
description: このページでは、Pythonを使用してPDFドキュメントを1つのPDFファイルにマージする方法を説明します。
lastmod: "2024-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Pythonを使用して複数のPDFをC++経由で単一のPDFにマージまたは結合する

PythonとAsposeのC++ライブラリを活用することで、複数のPDFファイルを効率的に簡単に1つのPDFにマージできます。

2つのPDFファイルを連結するには:

1. 最初のドキュメントを開く
1. 次に2番目のドキュメントのページを最初のドキュメントに追加する
1. 'document.save'メソッドで連結された出力ファイルを保存する

以下のコードスニペットは、PDFファイルを連結する方法を示しています。

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    dataDir = os.path.join(os.getcwd(), "samples")
    input_file= os.path.join(dataDir , "sample0.pdf")
    output_file = os.path.join(dataDir , "results", "concatenated-files.pdf")

    # 最初のドキュメントを開く
    document1 = apw.Document(inputFile)
    document2 = apw.Document(inputFile)

    # 2番目のドキュメントのページを最初のドキュメントに追加
    document1.pages.add(document2.pages)

    # 連結された出力ファイルを保存
    document1.save(output_file)
```