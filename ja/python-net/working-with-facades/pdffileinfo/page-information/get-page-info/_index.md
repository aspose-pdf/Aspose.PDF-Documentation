---
title: ページ情報を取得
type: docs
weight: 10
url: /ja/python-net/get-page-info/
description: Aspose.PDF for Python を使用して PDF 内のページレベルの情報にプログラムでアクセスする方法を学習します。このガイドでは、PDF 文書内の特定のページのページの幅、高さ、回転、オフセットを取得する方法を示します。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python 用 Aspose.PDF を使用して PDF ページ情報を取得する
Abstract: この関数は、PDF ページの幅、高さ、回転、水平 (X) および垂直 (Y) のオフセットを抽出します。これらのプロパティはポイント単位で返され、ページの物理的なサイズと PDF 内のコンテンツの位置を反映します。この関数は取得した値を出力するので、開発者はページのレイアウトと向きを理解してさらに PDF を操作できます。
---

「get_page_information」ユーティリティ関数は、開発者がPDFページの構造とレイアウトを理解するのに役立ちます。PDF ページごとにサイズ、回転、内部オフセットが異なる場合があり、コンテンツの配置や自動化タスクに影響する可能性があります。

PDFファイル内の特定のページの主要なメタデータとレイアウト情報を取得する機能を備えています。Aspose.PDF Facades API は、ページの幅、高さ、回転、X/Y オフセットなどの詳細を提供します。この情報は、ページレイアウトの分析、注釈の配置、PDF の自動処理などのタスクに不可欠です。

1. PDF ファサードオブジェクトを作成します。
1. ページのサイズとレイアウトを取得します。
1. 取得した値を印刷または保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_page_information(infile):

    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    page_width = pdf_info.get_page_width(1)
    page_height = pdf_info.get_page_height(1)
    page_rotation = pdf_info.get_page_rotation(1)
    page_x_offset = pdf_info.get_page_x_offset(1)
    page_y_offset = pdf_info.get_page_y_offset(1)

    print(f"Page Width: {page_width}")
    print(f"Page Height: {page_height}")
    print(f"Page Rotation: {page_rotation}")
```
