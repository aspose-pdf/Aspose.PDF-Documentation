---
title: PDF を最後まで分割
type: docs
weight: 40
url: /ja/python-net/split-pdf-to-end/
description: Python 用 Aspose.PDF を使用して PDF ドキュメントを特定のページから最後のページに分割します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF を特定のページから最後まで分割する方法
Abstract: Aspose.PDF for Python を使用して PDF ドキュメントを特定のページから最後のページに分割する方法を学習します。この例は、指定したページから始まるすべてのページを抽出して新しい PDF ファイルを作成する方法を示しています。
---

PDF を特定のページから最後まで分割すると、文書の後半部分を別のファイルとして保存する必要がある場合に便利です。Python 用の「Aspose.PDF」を使うと、その split_to_end メソッドが [PDF ファイルエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) クラスを使用すると、任意のページ番号からドキュメントの最後のページまでのページを抽出できます。これは抜粋を作成したり、章を抽出したり、大きな PDF を手動で編集せずにその一部を処理したりする場合に最適です。

1. PDF ファイルエディターオブジェクトを作成します。
1. PDF を特定のページから最後まで分割します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF to End
def split_pdf_to_end(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_to_end(input_pdf_path, 2, output_pdf_path)
```
