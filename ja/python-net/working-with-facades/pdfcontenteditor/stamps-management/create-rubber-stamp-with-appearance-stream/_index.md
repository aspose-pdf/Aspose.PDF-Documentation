---
title: アピアランスストリームでラバースタンプを作成
type: docs
weight: 30
url: /ja/python-net/create-rubber-stamp-with-appearance-stream/
description: 次の使用例は、PDF を読み込み、外観のイメージファイルを使用して 1 ページ目にラバースタンプを作成し、変更した文書を保存します。✨
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDFContentEditor を使用してカスタムイメージ外観のラバースタンプを作成する
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して、PDF 内の画像表示をカスタマイズしたラバースタンプ注釈を作成する方法を示しています。この方法では、ロゴ、シール、署名などのブランドスタンプや視覚的に豊かなスタンプを適用できます。
---

ラバースタンプの注釈は、外部画像ファイルを使用してカスタマイズできます。テキストベースのスタンプだけに頼るのではなく、外観 (会社のロゴや承認バッジなど) を定義してページに配置することができます。

1. を作成 [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) インスタンス。
1. 入力 PDF ドキュメントをバインドします。
1. スタンプ位置の長方形を定義します。
1. スタンプの外観には画像ファイルを使用してください。
1. テキストと色の設定を適用します。
1. 更新した PDF ドキュメントを保存します。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_rubber_stamp_with_appearance_file(infile, image_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Create rubber stamp using appearance_file overload (image path)
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(100, 400, 200, 60),
        "Stamp with custom appearance",
        apd.Color.dark_green,
        image_file,
    )
    # Save updated document
    content_editor.save(outfile)
```    
