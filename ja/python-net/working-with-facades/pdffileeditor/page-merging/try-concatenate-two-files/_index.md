---
title: 2 つの PDF ファイルを連結してみてください
type: docs
weight: 90
url: /ja/python-net/try-concatenate-two-files/
description: Python 用 Aspose.PDF を使用して 2 つの PDF ファイルを連結します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で 2 つの PDF ファイルを例外なく安全にマージする方法
Abstract: Aspose.PDF for Python を使用して 2 つの PDF ファイルを安全に連結する方法を学びましょう。try_concatenate メソッドは例外を発生させずにファイルをマージするので、操作が失敗した場合でも適切にエラー処理を行うことができます。
---

2つのPDFファイルの結合は、ファイルの破損、互換性のない形式、またはその他の問題により失敗することがあります。Python 用の Aspose.PDF を使用すると、PDFFileEditor クラスの try_concatenate メソッドを使用すると、2 つの PDF を安全にマージすることができます。操作が失敗すると、例外を発生させる代わりに False が返されるので、自動化されたワークフローやバッチ処理におけるエラー処理を完全に制御できます。

1. PDF ファイルエディターオブジェクトを作成します。
1. 2 つの PDF ファイルを結合してみます。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def try_concatenate_two_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    if not pdf_editor.try_concatenate(
        files_to_merge[0], files_to_merge[1], output_file
    ):
        print("Concatenation failed for the provided files.")
```
