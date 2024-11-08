---
title: PythonでPDFをテキストに変換する
linktitle: PDFを他の形式に変換
type: docs
weight: 90
url: /ja/python-cpp/convert-pdf-to-other-files/
lastmod: "2022-12-23"
keywords: convert, PDF, EPUB, LaText, Text, XPS, Python
description: このトピックでは、Pythonを使用してPDFファイルをテキストなどの他のファイル形式に変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## PDFをテキストに変換

**Aspose.PDF for Python**は、PDFドキュメント全体および単一ページをテキストファイルに変換することをサポートしています。

### PDFドキュメントをテキストファイルに変換

'TextDevice'クラスを使用してPDFドキュメントをTXTファイルに変換できます。

1. 入力ファイルと出力ファイルのパスを作成
1. PDF抽出ファサードのインスタンスを[extractor_create](https://reference.aspose.com/pdf/python-cpp/core/extractor_create/)で作成
1. PDFファイルを[extractor_bind_pdf](https://reference.aspose.com/pdf/python-cpp/core/extractor_bind_pdf/)で抽出器にバインド

1. [extractor_extract_text](https://reference.aspose.com/pdf/python-cpp/core/extractor_extract_text/)を使用してPDFファイルからテキストを抽出する
1. 抽出されたテキストを書き出しファイルに書き込む
1. 'document.save'メソッドで出力PDFを保存する

以下のコードスニペットは、すべてのページからテキストを抽出する方法を説明しています。

```python

    from AsposePdfPython import *

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_txt.txt"

    extactor = extractor_create()
    extractor_bind_pdf(extactor,input_pdf)
    text = extractor_extract_text(extactor)

    with open(output_pdf, 'w') as f:
        f.write(text)
```