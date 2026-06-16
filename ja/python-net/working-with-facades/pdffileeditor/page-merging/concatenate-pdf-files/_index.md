---
title: 複数の PDF ファイルを連結
type: docs
weight: 20
url: /ja/python-net/concatenate-pdf-files/
description: Python 用 Aspose.PDF を使用して、複数の PDF ファイルを 1 つのドキュメントに結合します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で複数の PDF ファイルを 1 つの PDF にマージする方法
Abstract: Aspose.PDF for Python を使用して複数の PDF ファイルを 1 つのドキュメントに結合する方法を学びましょう。この例は、Concatenate メソッドを使用して、コンテンツやフォーマットを維持したまま、複数の PDF をシームレスに結合する方法を示しています。
---

PDF ファイルの結合は、文書管理、レポート作成、および自動化されたワークフローでは一般的な作業です。Aspose.PDF for Python を使用すると、開発者は複数の PDF ファイルを 1 つの統合文書に簡単に結合できます。の連結メソッドです。 [PDF ファイルエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) クラスは、入力ファイルのすべてのページが元のレイアウトと内容を維持したまま、最終出力に保存されることを保証します。この方法は、包括的なレポートを作成したり、フォームを組み合わせたり、複数の文書を効率的にアーカイブしたりする場合に便利です。

1. PDF ファイルエディターオブジェクトを作成します。
1. 複数の PDF ファイルを結合します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_pdf_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.concatenate(files_to_merge, output_file)
```
