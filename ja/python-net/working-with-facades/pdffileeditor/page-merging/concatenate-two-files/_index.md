---
title: 2 つの PDF ファイルを連結
type: docs
weight: 60
url: /ja/python-net/concatenate-two-files/
description: Python 用 Aspose.PDF を使用して、2 つの PDF ファイルを 1 つのドキュメントに連結します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で 2 つの PDF ファイルを 1 つの PDF に結合する方法
Abstract: Aspose.PDF for Python を使用して 2 つの PDF ファイルを連結して 1 つのドキュメントにする方法を学びましょう。この例は、2 つの PDF を元のコンテンツと書式を維持したままシームレスに結合する方法を示しています。
---

レポート、契約書、またはフォームを統合する場合、2 つの PDF ファイルを結合することはよくある作業です。Aspose.PDF for Python を使用すると、以下の連結方法を使用して 2 つの PDF をプログラムで 1 つの文書に結合できます。 [PDF ファイルエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) クラス。これにより、元のレイアウト、コンテンツ、構造を維持したまま、両方のファイルのすべてのページが出力 PDF に含まれます。

1. PDF ファイルエディターオブジェクトを作成します。
1. 2 つの PDF ファイルを結合します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_two_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.concatenate(files_to_merge[0], files_to_merge[1], output_file)
```
