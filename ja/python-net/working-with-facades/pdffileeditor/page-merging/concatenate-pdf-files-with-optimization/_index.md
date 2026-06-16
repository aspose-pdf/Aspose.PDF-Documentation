---
title: PDF ファイルを最適化して連結する
type: docs
weight: 30
url: /ja/python-net/concatenate-pdf-files-with-optimization/
description: Python 用 Aspose.PDF を使用して、複数の PDF ファイルを連結して 1 つの最適化された PDF にします。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で最適化された出力を使用して PDF ファイルをマージする
Abstract: Aspose.PDF for Python を使用して複数の PDF ファイルを連結して 1 つの最適化された PDF にする方法を学びましょう。この例は、サイズ最適化を有効にして、コンテンツと書式を維持しながら出力ファイルのサイズを小さくする方法を示しています。
---

複数の PDF を結合すると、特に画像や複雑なコンテンツが含まれていると、結果のファイルが大きくなることがあります。Aspose.PDF for Python を使用すると、開発者は連結中の最適化を有効にして、品質を損なうことなくファイルサイズを縮小できます。の optimize_size プロパティは [PDF ファイルエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class を使用すると、マージされた PDF がコンパクトで効率的になり、共有、保存、アーカイブに適しています。

1. PDF ファイルエディターオブジェクトを作成し、最適化を有効にします。
1. PDF ファイルを結合します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_pdf_files_with_optimization(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.optimize_size = True  # Enable optimization for smaller output file size
    pdf_editor.concatenate(files_to_merge, output_file)
```
