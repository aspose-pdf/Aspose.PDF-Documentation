---
title: PythonでPDFをプログラムで分割
linktitle: PDFファイルを分割
type: docs
weight: 20
url: /ja/python-cpp/split-pdf-document/
description: このトピックでは、C++アプリケーション経由でPythonにおいてPDFページを個々のPDFファイルに分割する方法を示します。
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDFページを分割することは、大きなファイルを個別のページやページグループに分割したい人にとって便利な機能です。

## ライブ例

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter)は、プレゼンテーション分割機能がどのように機能するかを調査することができる無料のオンラインウェブアプリケーションです。

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

このトピックでは、Python C++アプリケーションでPDFページを個々のPDFファイルに分割する方法を示します。Pythonを使用してPDFページを単一ページのPDFファイルに分割するには、次の手順を実行します:

コードスニペットは、必要なディレクトリとファイルパスを設定し、PDFドキュメントを開き、その後ドキュメントの各ページをループします。
 各ページについて、新しいドキュメントを作成し、現在のページを新しいドキュメントにコピーし、特定の命名規則で新しいドキュメントを個別のPDFファイルとして保存します。

1. 入力ドキュメントを開く
1. ページ数を初期化する
1. ドキュメントのすべてのページをループする

## PDFを複数のファイルまたは個別のPDFに分割するPython

以下のPythonコードスニペットは、PDFページを個々のPDFファイルに分割する方法を示しています。

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    dataDir = os.path.join(os.getcwd(), "samples")
    input_file= os.path.join(dataDir , "sample.pdf")
    outputFolder = os.path.join(dataDir , "results")
    # ドキュメントを開く
    document = apw.Document(inputFile)

    pageCount = 1

    # すべてのページをループする

    while (pageCount <= document.pages.count()):
        page = document.pages[pageCount]    
        newDocument = apw.Document()
        newDocument.pages.copy_page(page)
        newDocument.save(os.path.join(outputFolder,"page_" + str(pageCount) + "_out" + ".pdf"))
        pageCount += 1
```