---
title: PDF を最初から分割
type: docs
weight: 10
url: /ja/python-net/split-pdf-from-beginning/
description: Python 用 Aspose.PDF を使用して PDF ドキュメントを最初から分割します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF を使って Python で PDF を最初から分割する
Abstract: Python 用 Aspose.PDF を使用して PDF ドキュメントを最初から分割する方法を学習します。この例は、最初のページから特定のページ数を抽出して新しい PDF 文書を作成する方法を示しています。
---

PDF を最初から分割しておくと、文書の最初の数ページを別のファイルとしてまとめる必要がある場合に便利です。Python 用の Aspose.PDF を使うと、中の split_from_first メソッドが [PDF ファイルエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) クラスを使用すると、1 ページ目から定義した数のページを抽出できます。この機能は、元のファイルを手動で編集しなくても、大きな PDF の抜粋、プレビュー、または小さなセクションを生成するのに理想的です。

1. PDF ファイルエディターオブジェクトを作成します。
1. 最初のページから PDF を分割します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF from Beginning
def split_pdf_from_beginning(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_from_first(input_pdf_path, 3, output_pdf_path)
```
