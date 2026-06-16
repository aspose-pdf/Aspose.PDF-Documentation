---
title: Python で PDF ファイルを作成
linktitle: PDF ドキュメントを作成
type: docs
weight: 10
url: /ja/python-net/create-pdf-document/
description: .NET 経由で Aspose.PDF for Python を使用して Python で PDF ファイルを作成し、検索可能な PDF を作成する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF ファイルを作成
Abstract: Aspose.PDF for Python via .NET は、開発者が.NET フレームワークを対象とする Python アプリケーション内で PDF ファイルを操作できるように設計された多用途の API です。これにより、ユーザーは PDF ドキュメントを簡単に作成、読み込み、変更、および変換できます。この記事では、Aspose.PDF を使用して簡単な PDF ファイルを作成する方法を段階的に説明します。このプロセスには、「Document」オブジェクトを初期化し、「Page」を文書に追加し、ページの段落に「TextFragment」を挿入し、ファイルを PDF として保存することが含まれます。付属の Python コードスニペットでは、「Hello World!」というテキストを含む PDF ドキュメントを作成することで、これらの手順を示しています。この API により、最小限のコードで PDF の処理が簡単になり、.NET 環境で PDF を扱う開発者の生産性が向上します。
---

**.NET 経由の Python 用 Aspose.PDF ** は、開発者がほんの数行のコードで Python for .NET アプリケーションから PDF ファイルを直接作成、ロード、変更、および変換できる PDF 操作 API です。

新しい PDF ファイルを最初から生成する必要がある場合や、OCR 出力を Python で検索可能な PDF ドキュメントに変換する必要がある場合は、これらの例を使用してください。

## 簡単な PDF ファイルの作成方法

Python を使用して.NET 経由で Aspose.PDF を使用して PDF を作成するには、次の手順に従います。

1. のオブジェクトを作成 [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラス
1. を追加 [ページ](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) への対象 [ページ数](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) ドキュメントオブジェクトのコレクション
1. 追加 [テキストフラグメント](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) に [段落](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) ページのコレクション
1. 結果の PDF ドキュメントを保存する

```python
import sys
from os import path
import aspose.pdf as ap

def create_new_document(output_pdf):
    """Create a simple PDF with a single “Hello World!” page."""
    document = ap.Document()
    page = document.pages.add()
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    document.save(output_pdf)
```

## 検索可能な PDF ドキュメントを作成する方法

.NET 経由の Python 用 Aspose.PDF では、既存の PDF ドキュメントを作成および操作できます。PDF ファイルにテキストエレメントを追加すると、生成された PDF が検索可能になります。ただし、テキストを含む画像を PDF ファイルに変換する場合、変換後の PDF の内容は検索できません。回避策として、変換後のファイルに OCR を適用して検索できるようにする方法があります。

この要件を満たすための完全なコードを次に示します。

1. 「AP.ドキュメント」を使用してPDFをロードします。
1. レンダリング解像度を設定します。
1. 「PNGDevice.Process」を使用して、選択した PDF ページを画像に変換します。
1. 生成された画像で OCR を実行します。
1. OCR 出力から新しい PDF を作成します。
1. 検索可能な PDF を保存します。

```python
import aspose.pdf as ap
import io

# Requires: pip install pytesseract
# Also ensure the Tesseract OCR engine is installed and available on your system PATH.
import pytesseract
from pathlib import Path


# Path to the source PDF
input_pdf_path = "input.pdf"
# Path for the temporary image
temp_image_path = "temp_image.png"
# Path for the searchable PDF
output_pdf_path = "output_searchable.pdf"
page_number = 1
image_stream = io.FileIO(temp_image_path, "w")
try:
    document = ap.Document(input_pdf_path)
    resolution = ap.devices.Resolution(300)
    png_device = ap.devices.PngDevice(resolution)
    png_device.process(document.pages[page_number], image_stream)
    image_stream.close()
    pdf = pytesseract.image_to_pdf_or_hocr(temp_image_path, extension="pdf")
    document = ap.Document(io.BytesIO(pdf))
    document.save(output_pdf_path)
finally:
    image_file = Path(temp_image_path)
    image_file.unlink(missing_ok=True)
```

## 関連ドキュメントトピック

- [Python で PDF ドキュメントを操作する](/pdf/ja/python-net/working-with-documents/)
- [Python で PDF ドキュメントをフォーマットする](/pdf/ja/python-net/formatting-pdf-document/)
- [Python で PDF ドキュメントを操作する方法](/pdf/ja/python-net/manipulate-pdf-document/)
- [Python で PDF ファイルを最適化する方法](/pdf/ja/python-net/optimize-pdf/)

