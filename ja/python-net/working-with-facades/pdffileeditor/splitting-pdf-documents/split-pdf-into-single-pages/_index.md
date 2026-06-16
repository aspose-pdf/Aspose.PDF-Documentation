---
title: PDF を 1 ページに分割
type: docs
weight: 30
url: /ja/python-net/split-pdf-into-single-pages/
description: Python 用 Aspose.PDF を使用して PDF ドキュメントを 1 ページの PDF に分割します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF を個々のページに分割する方法
Abstract: Aspose.PDF for Python を使用して PDF ドキュメントを 1 ページの PDF に分割する方法を学習します。この方法では、元の PDF から各ページを抽出し、それを個別のファイルとして保存し、柔軟な文書管理と処理を実現します。
---

PDF を 1 ページに分割すると、文書の各セクションをページレベルで処理したり、印刷したり、個別に配布したりする場合に便利です。Python 用の Aspose.PDF を使用すると、の「split_to_pages」メソッドが [PDF ファイルエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class は、ソースドキュメントの各ページに個別の PDF ファイルを作成します。この方法では、元のレイアウトとコンテンツを維持したまま、ページを自動抽出してアーカイブ、レビュー、または個別の共有を行うことができます。

1. PDF ファイルエディターオブジェクトを作成します。
1. PDF を個々のページに分割します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF into Single Pages
def split_pdf_into_single_pages(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_to_pages(input_pdf_path, output_pdf_path)
```
