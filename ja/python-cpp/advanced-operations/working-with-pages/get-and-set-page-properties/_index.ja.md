---
title: C++を介してPythonを使用してPDFのサイズを設定する
linktitle: PDFのサイズを設定する
type: docs
weight: 30
url: /python-cpp/get-and-set-page-properties/
description: このセクションでは、C++を介してPythonを使用して、ドキュメントのサイズなどのPDFページのプロパティを取得または設定する方法を示します。
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFファイルのサイズを設定する

Aspose.PDF for Python via C++を使用すると、PythonアプリケーションでPDFファイルのページのプロパティを読み取り、設定することができます。

次のコードスニペットは、PDFファイルを開き、**Crop box**を調整することで最初のページをリサイズし（Crop boxはAdobe AcrobatでPDFドキュメントが表示される「ページ」サイズです）、変更されたドキュメントを新しいファイルに保存します。

1. 入力ファイルからドキュメントオブジェクトを作成する
1. [document_get_pages](https://reference.aspose.com/pdf/python-cpp/core/document_get_pages/)を使用して、ドキュメントからページコレクションを取得する

1. [page_collection_get_page](https://reference.aspose.com/pdf/python-cpp/core/page_collection_get_page/)を使用して、ページコレクションから最初のページを取得します。
1. [page_get_rectangle](https://reference.aspose.com/pdf/python-cpp/core/page_get_rectangle/)を使用して、ページからクロップボックスの長方形を取得します。
1. クロップボックスの新しい座標を計算します。
1. 新しい値でクロップボックスの座標を更新します。
1. 'document.save'メソッドで修正されたドキュメントを出力ファイルに保存します。

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # 現在の作業ディレクトリを取得し、"samples"ディレクトリへのパスを作成します
    dataDir = os.path.join(os.getcwd(), "samples")

    # 入力ファイルと出力ファイルのパスを作成します
    input_file = os.path.join(dataDir, "sample0.pdf")
    output_file = os.path.join(dataDir, "results", "resized_document.pdf")

    # 入力ファイルからドキュメントオブジェクトを作成します
    doc = apCore.document_create_from_file(inputFile)

    # ドキュメントからページコレクションを取得します
    pages = apCore.document_get_pages(doc)

    # ページコレクションから最初のページを取得します
    page = apCore.page_collection_get_page(pages, 1)

    # ページからクロップボックスの長方形を取得します
    crop_box = apCore.page_get_rectangle(page)

    # クロップボックスの新しい座標を計算します
    LLX = apCore.rectangle_get_LLX(crop_box) + 10
    LLY = apCore.rectangle_get_LLY(crop_box) + 10
    URX = apCore.rectangle_get_URX(crop_box) - 10
    URY = apCore.rectangle_get_URY(crop_box) - 10

    # 新しい値でクロップボックスの座標を更新します
    apCore.rectangle_set_LLX(crop_box, LLX)
    apCore.rectangle_set_LLY(crop_box, LLY)
    apCore.rectangle_set_URX(crop_box, URX)
    apCore.rectangle_set_URY(crop_box, URY)

    # 修正されたドキュメントを出力ファイルに保存します
    apCore.document_save(doc, output_file)

    # ドキュメントハンドルを閉じます
    apCore.close_handle(doc)
```