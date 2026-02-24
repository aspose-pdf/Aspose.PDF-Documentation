---
title: Python を使用した基本的なテキスト抽出
linktitle: 基本的なテキスト抽出
type: docs
weight: 10
url: /ja/python-net/basic-text-extraction/
description: このセクションには、Python で Aspose.PDF を使用した PDF ドキュメントからの基本的なテキスト抽出に関する記事が含まれています。
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## PDF ドキュメントのすべてのページからテキストを抽出

Python 用 Aspose.PDF は、PDF ドキュメントのすべてのページからテキストを抽出する方法を教えます。TextAbsorber クラスを使用して、文書全体のテキストコンテンツを取得し、別のテキストファイルに保存します。
PDF を検索可能なテキストに変換したり、コンテンツ分析を行ったり、インデックス作成や処理タスクのためにテキストをエクスポートしたりするのに最適です。

1. PDF ファイルを読み込みます。
1. 'TextAbsorber' オブジェクトを作成します。
1. 'document.pages.accept(text_absorber)' を呼び出して、すべてのページを走査します。
1. 'text_absorber.text' を使用して全文テキストを取得します。
1. 結果をテキストファイルに書き込みます。

```python

import os
import aspose.pdf as ap

def extract_text_from_all_pages(infile, outfile):
    """
    Extract all text from every page of the PDF and write to an output text file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    # Open the PDF document
    document = ap.Document(infile)
    try:
        # Create a TextAbsorber to extract text
        text_absorber = ap.text.TextAbsorber()
        # Accept the absorber for all pages
        document.pages.accept(text_absorber)
        # Get extracted text
        extracted_text = text_absorber.text
        # Write the text to an output file
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```

## 特定のページからテキストを抽出

PDF ドキュメントの単一ページからテキストを抽出します。指定したページにのみ TextAbsorber を適用することで、複数ページの PDF の特定セクションからテキストを分離して保存できます。

1 ページ分のコンテンツだけが必要な場合に便利です。たとえば、請求書ページ、レポートのセクション、またはフォームフィールドのサマリーからテキストを抽出する場合などです。

1. PDF を開きます。
1. TextAbsorber を作成します。
1. 指定されたページだけを受け入れます（pages[page_number]）。
1. テキストを抽出し、ファイルに書き込みます。

```python

import os
import aspose.pdf as ap

def extract_text_from_page(infile, page_number, outfile):
    """
    Extract text from a specific page number of the PDF.
    Args:
        infile (str): Path to input PDF file.
        page_number (int): 1-based page index to extract.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        text_absorber = ap.text.TextAbsorber()
        # Accept the absorber on only the specified page
        document.pages[page_number].accept(text_absorber)
        extracted_text = text_absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```

