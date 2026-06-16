---
title: PDF にページを追加
type: docs
weight: 10
url: /ja/python-net/append-pages-to-pdf/
description: Python 用 Aspose.PDF を使用して、ある PDF ドキュメントから別の PDF ドキュメントにページを追加します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python である PDF から別の PDF にページを追加する方法
Abstract: Aspose.PDF for Python を使用して、ある PDF ドキュメントから別の PDF ドキュメントにページを追加する方法を学びます。この例は、PDFFileEditor クラスを使用して複数の PDF のページを組み合わせて 1 つの出力文書を作成する方法を示しています。
---

異なるPDF文書のページを組み合わせることは、文書処理ワークフローにおける一般的な要件です。Aspose.PDF for Python を使用すると、開発者は 1 つ以上の PDF ファイルのページを既存の文書に簡単に追加できます。

このコードスニペットは、の append メソッドの使用方法を示しています。 [PDF ファイルエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) クラス:別の PDF ファイルから選択したページをソース PDF の末尾に追加します。ページ範囲を指定することで、開発者は最終文書にどのページを含めるかを正確に制御できます。

1. PDF ファイルエディターオブジェクトを作成します。
1. 別の PDF からページを追加します。

セカンダリ PDF ドキュメントから指定されたページが元の PDF の末尾に追加され、結合された出力ファイルが作成されます。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Append Pages to PDF
def append_pages_to_pdf(infile, sample_file, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    # Append pages from the specified PDF document to the end of the source PDF document
    pdf_editor.append(infile, [sample_file], 1, 2, outfile)
```
