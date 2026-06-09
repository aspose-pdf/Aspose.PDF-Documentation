---
title: PDF へのページの挿入
type: docs
weight: 40
url: /ja/python-net/insert-pages-into-pdf/
description: Python 用 Aspose.PDF を使用して、ある PDF から別の PDF にページを挿入します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で別の PDF から既存の PDF にページを挿入する方法
Abstract: Aspose.PDF for Python を使用して、ある PDF から別の PDF にページを挿入する方法を説明します。この例は、セカンダリ PDF から選択したページを元の文書の特定の位置に追加して、正確なページ配置で結合 PDF を作成する方法を示しています。
---

既存の PDF へのページの挿入は、文書を結合したり、コンテンツを追加したり、レポートを再編成したりするときによく必要になります。Aspose.PDF for Python を使用すると、開発者はプログラムによって、ある PDF のページを別の PDF に指定した場所に挿入できます。

この記事では、の insert メソッドの使用方法を説明します [PDF ファイルエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) クラス。挿入するページ番号と挿入先の場所を指定することで、元の書式と構造を維持したまま、異なる PDF のコンテンツを結合できます。

1. PDF ファイルエディターオブジェクトを作成します。
1. 挿入位置とページを定義します。
1. ページの挿入。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Insert Pages into PDF
def insert_pages_into_pdf(infile, sample_file, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    # Define the page number where new pages will be inserted (1-based index)
    insert_page_number = 2

    pdf_editor.insert(infile, insert_page_number, sample_file, [1, 2], outfile)
```
