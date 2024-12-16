---
title: PDFをTXTに変換するPython
linktitle: PDFをTXTに変換する
type: docs
weight: 20
url: /ja/python-cpp/convert-pdf-to-txt/
lastmod: "2024-04-23"
description: Aspose.PDF for Python via C++ライブラリを使用して、PDFをTXT形式に変換できます。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDFをTXTに変換する

Aspose.PDF for Python via C++は、次のステップに従ってPDFドキュメントをテキストファイルに変換することをサポートします：

1. 入力ファイルと出力ファイルのパスを作成する
1. [extractor_create](https://reference.aspose.com/pdf/python-cpp/core/extractor_create/)を使用して、PDFエクストラクターファサードのインスタンスを作成する
1. [extractor_bind_pdf](https://reference.aspose.com/pdf/python-cpp/core/extractor_bind_pdf/)を使用して、PDFファイルをエクストラクターにバインドする
1. [extractor_extract_text](https://reference.aspose.com/pdf/python-cpp/core/extractor_extract_text/)を使用して、PDFファイルからテキストを抽出する
1. 抽出したテキストを出力ファイルに書き込む
1. 'document.save' メソッドで出力PDFを保存する

以下のコードスニペットは、Pythonを介してC++でJPG画像をPDFに変換する方法を示しています：

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # データディレクトリパスを作成
    dataDir = os.path.join(os.getcwd(), "samples")

    # 入力ファイルパスを作成
    input_file = os.path.join(dataDir, "sample.pdf")

    # 出力ファイルパスを作成
    output_file = os.path.join(dataDir, "results", "pdf-to-txt.txt")

    # PDF抽出ファサードのインスタンスを作成
    extactor = apCore.facades_pdf_extractor_create()

    # PDFファイルを抽出器にバインド
    apCore.facades_facade_bind_pdf(extactor, input_file)

    # PDFファイルからテキストを抽出
    text = apCore.facades_pdf_extractor_extract_text(extactor)

    # 抽出したテキストを出力ファイルに書き込み
    with open(output_file, 'w') as f:
        f.write(text)
```