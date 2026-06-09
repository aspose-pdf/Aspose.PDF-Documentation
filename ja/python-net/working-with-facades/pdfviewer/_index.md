---
title: PDF ビューアクラス
type: docs
weight: 135
url: /ja/python-net/pdfviewer-class/
description: .NET 経由で Aspose.PDF for Python の PDFViewer クラスを使用して、すべての PDF ページをデコードし、特定のページをデコードし、ビューアに関連する PDF メタデータを検査する方法を説明します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDFViewer を使用して Python で PDF ページをデコードし、ビューアデータを検査できます
Abstract: この記事では、.NET 経由で Aspose.PDF for Python の PDFViewer ファサードを使用して、ページのデコードとビューア関連の検査タスクを実行する方法について説明します。すべての PDF ページをデコードし、特定のページをレンダリングし、ページ数、座標タイプ、解像度などのプロパティを検査する方法を学びます。
---

.NET 経由の Python 用 Aspose.PDF は [PDF ビューア](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfviewer/) PDF 表示およびページデコードのシナリオを操作するためのファサード。一般的な使用例の 1 つは、PDF ページをイメージオブジェクトに変換してディスクに保存することです。

## 再利用可能な PDFViewer ヘルパーの作成

ページをデコードしたり、ビューア関連のプロパティを読み込んだりする前に、初期化して返す小さなヘルパーを作成してください `PdfViewer` インスタンス。これにより、以下の例は独立しており、PDF ドキュメントにバインドされる前にビューアオブジェクトがどのように作成されるかが明確になります。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades


def _create_viewer() -> pdf_facades.PdfViewer:
    """Create a PdfViewer configured for decoding examples."""
    viewer = pdf_facades.PdfViewer()
    viewer.coordinate_type = ap.PageCoordinateType.MEDIA_BOX
    viewer.resolution = 150
    viewer.scale_factor = 1.0
    viewer.show_hidden_areas = False
    return viewer
```

## すべての PDF ページをデコード

使用 `decode_all_pages()` PDFのすべてのページを個別の画像に変換したい場合。返されたページ画像を 1 つずつ出力ディレクトリに保存できます。

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def decode_all_pages(infile: str, output_dir: str) -> None:
    """Decode all pages of a PDF document into image files."""
    viewer = _create_viewer()
    try:
        viewer.open_pdf_file(infile)
        decoded_pages = viewer.decode_all_pages()

        for index, page_image in enumerate(decoded_pages, start=1):
            image_path = path.join(output_dir, f"decode_all_pages_{index}.png")
            page_image.save(image_path)
    finally:
        viewer.close_pdf_file()
```

## 特定の PDF ページをデコードする

使用 `decode_page()` ドキュメントから1ページしか必要ない場合。これは、プレビュー、サムネイル、またはページ固有のエクスポートを生成する場合に便利です。

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def decode_specific_page(infile: str, outfile: str, page_number: int = 1) -> None:
    """Decode a specific PDF page into an image file."""
    viewer = _create_viewer()
    try:
        viewer.bind_pdf(infile)
        page_image = viewer.decode_page(page_number)
        page_image.save(outfile)

    finally:
        viewer.close()
```

## PDF メタデータを検査

ザの `inspect_pdf_metadata` 関数は、Aspose.PDF を使用して PDF ドキュメントを開き、基本的なビューア関連のメタデータを取得する方法を示します。文書の内容ではなく、文書がどのように解釈され、表示されるかを説明する情報を抽出することに重点を置いています。

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def inspect_pdf_metadata(infile: str) -> None:
    """Open a PDF and print page-count related viewer metadata."""
    viewer = _create_viewer()
    try:
        viewer.open_pdf_file(infile)
        print(f"Page count: {viewer.page_count}")
        print(f"Coordinate type: {viewer.coordinate_type}")
        print(f"Resolution: {viewer.resolution}")
    finally:
        viewer.close_pdf_file()
```
