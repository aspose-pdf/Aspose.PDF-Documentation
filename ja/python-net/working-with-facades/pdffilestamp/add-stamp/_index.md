---
title: PDF にスタンプを追加
type: docs
weight: 40
url: /ja/python-net/add-stamp/
description: Python の PDFFileStamp を使って PDF ページにスタンプを追加する方法を学びましょう。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Python で PDF にテキストスタンプを追加する方法
Abstract: この記事では、PDFFileStamp ファサードを使用して、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントにスタンプコンテンツを追加する方法について説明します。スタンプの作成、ページへの配置、回転と不透明度の制御、更新された PDF の保存の方法を説明します。
---

.NET 経由の Python 用 Aspose.PDF は [PDF ファイルスタンプ](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) PDF ページに繰り返しコンテンツを追加するためのファサード。ヘッダー、フッター、ページ番号だけでなく、文書の各ページにテキストベースのスタンプを貼ることもできます。

## PDF へのスタンプの追加

スタンプを設定したら、入力 PDF をにバインドします `PdfFileStamp`、スタンプを追加し、出力ファイルを保存します。これにより、設定したスタンプが文書全体に適用されます。

```python
import sys
from os import path

import aspose.pdf.facades as pdf_facades

CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import initialize_data_dir, set_license


def add_stamp_to_pdf(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp to a PDF file."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
