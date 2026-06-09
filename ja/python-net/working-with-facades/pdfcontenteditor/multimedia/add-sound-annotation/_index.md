---
title: サウンド注釈を追加
type: docs
weight: 20
url: /ja/python-net/add-sound-annotation/
description: この例では、入力 PDF をバインドし、1 ページにサウンド注釈を追加し、変更した PDF を保存します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDF コンテンツエディターを使用して PDF にサウンドアノテーションを追加
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF ドキュメントにオーディオを埋め込む方法を示しています。PDF 内でオーディオファイルを直接再生するクリック可能なサウンドアノテーションを追加する方法を示しています。
---

PDF のサウンド注釈を使用すると、音声メモ、音楽、効果音などのオーディオコンテンツを文書に追加できます。を使用する [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)ページ上にクリック可能な小さな四角形を定義して、アクティブにすると指定したオーディオファイルを再生できます。

1. PDF コンテンツエディターのインスタンスを作成します。
1. 入力 PDF ドキュメントをバインドします。
1. サウンドアノテーションの長方形を定義します。
1. オーディオファイル、注釈名、ページ番号、およびサンプリングレートを指定します。
1. 更新した PDF ドキュメントを保存します。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_sound_annotation(infile, sound_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add sound annotation to page 1
    content_editor.create_sound(
        apd.Rectangle(80, 450, 30, 30), sound_file, "Speaker", 1, "8000"
    )
    # Save updated document
    content_editor.save(outfile)
```
