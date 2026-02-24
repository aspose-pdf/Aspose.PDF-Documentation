---
title: Python を使用した PDF ページの回転
linktitle: PDF ページの回転
type: docs
weight: 110
url: /ja/python-net/rotate-pages/
description: このトピックでは、Python を使用して既存の PDF ファイルのページ向きをプログラムで回転させる方法について説明します。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF のページを回転させる方法
Abstract: この記事では、Python を使用して既存の PDF ファイル内のページの向きをプログラムで更新または変更する方法についてガイドします。Aspose.PDF for Python via .NET を利用することで、ページの MediaBox プロパティを調整して横向きと縦向きの間を簡単に切り替えることができます。この記事には、PDF ドキュメント内のページを反復処理し、MediaBox のサイズと位置を変更し、必要に応じて CropBox を調整する Python コードスニペットが含まれています。さらに、'rotate' メソッドを使用してページの回転角度を設定し、目的の向きを実現する方法も説明しています。最後に、更新された PDF ファイルを保存する手順で締めくくられます。
---

このトピックでは、Python を使用して既存の PDF ファイル内のページの向きをプログラムで更新または変更する方法について説明します。

## ページ向きの変更

この関数は、Aspose.PDF for Python を使用して PDF の [`ドキュメント`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) の各ページを時計回りに 90 度回転させます。
スキャンした文書が横向きになるなど、ページ向きの問題を修正するのに便利です。元の PDF は変更されず、回転されたバージョンは新しいファイルとして保存されます。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_page(infile, outfile):
    """
    Rotate all pages in a PDF document by 90 degrees clockwise.

    Demonstrates how to rotate PDF pages using the Aspose.PDF library.
    This function applies a 90-degree clockwise rotation to every page
    in the input document and saves the result to a new file.

    Args:
        infile (str): Path to the input PDF file to rotate.
        outfile (str): Path where the rotated PDF will be saved.

    Returns:
        None: The function modifies the PDF pages and saves to the output path.

    Note:
        - Applies 90-degree clockwise rotation (ap.Rotation.ON90) to all pages
        - Rotates every page in the document uniformly
        - The original document is not modified; a new file is created
        - Rotation options include: ON90 (90°), ON180 (180°), ON270 (270°)
        - Useful for correcting page orientation or adjusting layout

    Example:
        >>> rotate_page("input.pdf", "rotated_output.pdf")
        # Rotates all pages 90 degrees clockwise and saves to rotated_output.pdf
    """
    document = ap.Document(infile)
    for page in document.pages:
        # `page` is a `Page` object; `rotate` uses the `Rotation` enum
        page.rotate = ap.Rotation.ON90

    document.save(outfile)
```


