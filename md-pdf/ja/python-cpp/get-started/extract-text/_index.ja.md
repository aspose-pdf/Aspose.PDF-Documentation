---
title: Pythonを使用してPDFからテキストを抽出
linktitle: PDFからテキストを抽出
type: docs
weight: 10
url: /python-cpp/extract-text/
description: このセクションでは、Pythonライブラリを使用してPDFドキュメントからテキストを抽出する方法について説明します。
lastmod: "2024-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDFドキュメントのすべてのページからテキストを抽出

PDFからテキストを抽出するのは簡単ではありません。多くのPDFリーダーはPDF画像やスキャンされたPDFからテキストを抽出できません。しかし、**Aspose.PDF for Python via C++**ツールを使用すると、すべてのPDFファイルから簡単にテキストを抽出できます。

コードスニペットを確認し、PDFからテキストを抽出する手順に従ってください：

1. Python用のAspose.PDFライブラリをインポート
1. PDFドキュメントからテキストと画像を抽出するために使用される新しい抽出オブジェクトを作成
1. 抽出のソースとなるPDFファイルに抽出オブジェクトをバインド
1. PDFドキュメントからすべてのテキストを抽出し、いくつかの変数に格納

1. 何でもしてください。抽出されたテキストをコンソールに出力し、一部の断片を検索するなど

```python
# AsposePdfPythonからインポート
from AsposePdfPython import *

# 抽出器を作成する
extactor = Extract()
# PDFドキュメントを抽出器にバインドする
extractor_bind_pdf(extactor,"blank_pdf_document.pdf")
# テキストを抽出する
text = extractor_extract_text(extactor)

# テキストを出力する
print(text)
```