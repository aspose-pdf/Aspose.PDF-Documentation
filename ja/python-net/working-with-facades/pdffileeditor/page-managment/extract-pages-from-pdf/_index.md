---
title: PDF からページを抽出
type: docs
weight: 30
url: /ja/python-net/extract-pages-from-pdf/
description: Python 用 Aspose.PDF を使用して PDF ドキュメントから選択したページを抽出します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF ドキュメントから特定のページを抽出する方法
Abstract: Aspose.PDF for Python を使用して PDF ドキュメントから選択したページを抽出する方法を説明します。この例は、必要なページのみを含む新しい PDF を作成して、カスタムドキュメントの作成とページレベルの操作を可能にする方法を示しています。
---

PDF からのページの抽出は、文書のサブセットを作成したり、特定のコンテンツのみを共有したり、プレゼンテーション、レポート、印刷用に PDF を再編成したりする必要がある場合に便利です。Aspose.PDF for Python を使用すると、開発者はプログラムで PDF ファイルからページを抽出し、新しい文書として保存できます。

の抽出法の使い方を学びましょう [PDF ファイルエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) クラス。抽出するページのリストを指定すると、元のコンテンツと書式を維持したまま、選択したページのみを含む新しい PDF を生成できます。

1. PDF ファイルエディターオブジェクトを作成します。
1. 抽出するページを定義します。
1. ページを抽出します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Extract Pages from PDF
def extract_pages_from_pdf(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    # Define the page numbers to be extracted (1-based index)
    pages_to_extract = [1, 4, 3]

    # Extract the specified pages from the PDF document and save to a new PDF document
    pdf_editor.extract(infile, pages_to_extract, outfile)
```
