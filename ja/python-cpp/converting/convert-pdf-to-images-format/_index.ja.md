---
title: PythonでPDFを異なる画像フォーマットに変換
linktitle: PDFを画像に変換
type: docs
weight: 70
url: /python-cpp/convert-pdf-to-images-format/
lastmod: "2023-06-23"
description: このトピックでは、Aspose.PDF for Pythonを使用してPDFをTIFF、BMP、EMF、JPEG、PNG、GIF、SVGなどの様々な画像フォーマットに数行のコードで変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 概要

この記事では、Pythonを使用してPDFを異なる画像フォーマットに変換する方法を説明します。以下のトピックをカバーしています。

## PythonでPDFを画像に変換

### PythonでPDFをPNGに変換

1. Aspose.PDFライブラリのPythonラッパーを提供するAsposePdfPythonモジュールをインポートします。
1. ファイル名を引数として取り、Documentオブジェクトを返す`document_open`関数を使用してPDFドキュメントを開きます。
1. Documentオブジェクトを引数として取り、PageCollectionオブジェクトを返す`document_get_pages`関数を使用してドキュメントのページを取得します。

1. `page_collection_get_page` 関数を使用してドキュメントの目的のページを取得します。この関数は、PageCollection オブジェクトとインデックスを引数として受け取り、Page オブジェクトを返します。
1. `png_device_create` 関数を使用して PngDevice オブジェクトを作成します。この関数は引数を取りません。このオブジェクトは、PDF ページをデフォルトのパラメーターで PNG 画像に変換できます。
1. `png_device_save_page_to_file` 関数を使用して、ドキュメントの目的のページを PNG 画像として保存します。この関数は、PngDevice オブジェクト、Page オブジェクト、およびファイル名を引数として受け取ります。
1. `close_handle` 関数を使用して、PngDevice と Document オブジェクトのハンドルを閉じます。この関数はオブジェクトを引数として受け取り、そのリソースを解放します。

```python

from AsposePdfPython import *

doc = document_open("blank_pdf_document.pdf")
pages = document_get_pages(doc)
page = page_collection_get_page(pages,1)

pngDevice = png_device_create()
png_device_save_page_to_file(pngDevice,page,"test.png")

```

### Python Convert PDF to JPEG

1. `document_open` 関数を使用して PDF ドキュメントを開きます。この関数はファイル名を引数として受け取り、Document オブジェクトを返します。
1. `document_get_pages` 関数を使用してドキュメントのページを取得します。この関数は Document オブジェクトを引数として受け取り、PageCollection オブジェクトを返します。
1. `page_collection_get_page` 関数を使用してドキュメントの目的のページを取得します。この関数は PageCollection オブジェクトとインデックスを引数として受け取り、Page オブジェクトを返します。
1. `resolution_create` 関数を使用して Resolution オブジェクトを作成します。この関数はドット毎インチ (DPI) で解像度の値を引数として受け取ります。
1. `jpeg_device_create_from_width_height_resolution` 関数を使用して JpegDevice オブジェクトを作成します。この関数は幅、高さ、解像度の値を引数として受け取ります。このオブジェクトは指定したパラメータで PDF ページを JPEG 画像に変換できます。

1. `jpeg_device_save_page_to_file` 関数を使用して、ドキュメントの希望するページを JPEG 画像として保存します。この関数は、JpegDevice オブジェクト、Page オブジェクト、およびファイル名を引数として受け取ります。
1. `close_handle` 関数を使用して、JpegDevice および Document オブジェクトのハンドルを閉じます。この関数はオブジェクトを引数として受け取り、そのリソースを解放します。

```python

    from AsposePdfPython import *

    doc = document_open("blank_pdf_document.pdf")
    pages = document_get_pages(doc)
    page = page_collection_get_page(pages,1)

    res = resolution_create(300)
    jpegDevice = jpeg_device_create_from_width_height_resolution(1239,1754,res)
    jpeg_device_save_page_to_file(jpegDevice,page,"test.jpeg")
```