---
title: 多数の PDF ファイルを連結
type: docs
weight: 10
url: /ja/python-net/concatenate-large-number-files/
description: Python 用 Aspose.PDF を使用すると、多数の PDF ファイルを効率的にマージできます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: ディスクバッファリングを使用して Python で大きな PDF ファイルを連結する方法
Abstract: Aspose.PDF for Python を使用して多数の PDF ファイルを効率的に結合する方法を学びましょう。この例は、システムメモリを使い果たすことなくディスクバッファリングを有効にして大容量の PDF を処理し、多数のファイルをスムーズに連結する方法を示しています。
---

PDF ファイルの大規模なコレクションを扱う場合、連結時にメモリ消費がボトルネックになることがあります。Aspose.PDF for Python を使用すると、でディスクバッファリングを有効にできます。 [PDF ファイルエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 多数の PDF を効率的にマージするためのクラス。concatenate メソッドは入力ファイルを 1 つの PDF に結合しますが、ディスクバッファはメモリの使用量が多くなるのを防ぎます。この方法は、大量の文書の処理、自動レポート生成、または大容量の PDF アーカイブの統合に最適です。

1. PDF ファイルエディターオブジェクトを作成します。
1. 複数の PDF ファイルを結合します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_large_number_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.use_disk_buffer = True  # Enable disk buffering for large files
    pdf_editor.concatenate(files_to_merge, output_file)
```
