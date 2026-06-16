---
title: PDF ページの内容のサイズを変更
type: docs
weight: 30
url: /ja/python-net/resize-pdf-page-contents/
description: Python 用 Aspose.PDF を使用して特定の PDF ページのコンテンツのサイズを変更します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python でプログラムによる PDF ページの内容のサイズ変更
Abstract: Aspose.PDF for Python を使用して特定の PDF ページのコンテンツのサイズを変更する方法を学びましょう。この例は、文書構造を維持したままページコンテンツの幅と高さを調整して、印刷や表示用にレイアウトを簡単に最適化する方法を示しています。
---

PDF ページのコンテンツのサイズ調整は、印刷用に文書を準備したり、コンテンツを特定のレイアウトに合わせたり、文書全体でページ形式を標準化したりする場合に必要になることがよくあります。Aspose.PDF for Python を使用すると、開発者は文書を手動で編集しなくても、選択したページのコンテンツをプログラムでサイズ変更できます。

この記事では、の「resize_contents」メソッドの使用方法を説明します [PDF ファイルエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) クラスを使用して、PDF ファイル内の特定のページのページコンテンツのサイズを変更します。ターゲットの幅と高さを指定すると、選択したページのコンテンツがそれに応じてサイズ変更されます。

1. PDF ファイルエディターオブジェクトを作成します。
1. ページコンテンツのサイズを変更します。

パラメーター:

- [1, 3] — 内容のサイズが変更されるページ番号のリスト。
- 400 — ページコンテンツの新しい幅 (ポイント単位)。
- 750 — ページコンテンツの新しい高さ (ポイント単位)。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Resize PDF Page Contents
def resize_pdf_page_contents(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    if not pdf_editor.resize_contents(
        FileIO(infile), FileIO(outfile, "w"), [1, 3], 400, 750
    ):
        raise Exception("Failed to resize PDF page contents.")
```
