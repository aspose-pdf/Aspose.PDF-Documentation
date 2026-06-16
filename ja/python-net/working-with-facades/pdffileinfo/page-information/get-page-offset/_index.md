---
title: ページオフセットを取得
type: docs
weight: 20
url: /ja/python-net/get-page-offset/
description: この例は、PDFFileInfoを使用して特定のページのXオフセットとYオフセットを取得し、それらをインチに変換して正確なレイアウトと位置分析を行う方法を示しています。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF ページオフセットを取得する
Abstract: 「get_page_offsets」関数は、PDF ファイル内の各ページの水平（X）および垂直（Y）オフセットを抽出します。これらのオフセットは、PDF の原点を基準としたページコンテンツの位置を表します。この関数はポイントをインチに変換することで、注釈、画像、またはテキストを正確に配置できるので、人間が読める正確な測定値が得られます。複数ページの PDF をサポートしており、PDF レイアウト、自動化、またはコンテンツの配置作業を行う開発者を対象としています。
---

「get_page_offsets」関数を使用すると、開発者はPDFファイル内のページの正確な水平（X）および垂直（Y）オフセットを取得できます。PDF 文書では、各ページの内部原点がページの左上隅とは異なる場合があり、これがテキスト、画像、注釈、その他のコンテンツの位置に影響する可能性があります。

Aspose.PDF Facadesを使用することで、この関数はこれらのオフセットをポイント単位で抽出し、簡単に解釈できるようにインチに変換します。複数ページの PDF をサポートしているため、正確なコンテンツ配置を必要とする自動ワークフローに適しています。

1. PDF ファサードオブジェクトを作成します。
1. PDF 内のページ数を取得します。
1. 各ページをループしてオフセットを取得します。
1. オフセットを印刷または保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_page_offsets(infile):
    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    page_x_offset = pdf_info.get_page_x_offset(1) / 72.0
    page_y_offset = pdf_info.get_page_y_offset(1) / 72.0
    print(f"Page X Offset: {page_x_offset} inches")
    print(f"Page Y Offset: {page_y_offset} inches")
```
