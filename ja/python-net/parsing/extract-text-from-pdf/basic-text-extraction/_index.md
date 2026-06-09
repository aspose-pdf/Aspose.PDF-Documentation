---
title: Python を使用した基本的なテキスト抽出
linktitle: 基本的なテキスト抽出
type: docs
weight: 10
url: /ja/python-net/basic-text-extraction/
description: Aspose.PDF for Python を使用して PDF 文書からテキストを抽出する方法を学びましょう。すべてのページから一度に抽出することも、特定のページから抽出することもできます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF 文書のすべてのページからテキストを抽出

使用 [テキストアブソーバー](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) PDF ドキュメントのすべてのページからすべてのテキストをキャプチャし、テキストファイルに書き込みます。このアプローチは、PDF を検索可能なテキストに変換したり、コンテンツ分析を実行したり、索引付けやダウンストリーム処理のためにテキストを準備したりする場合に適しています。

1. を使用して PDF ドキュメントを開きます。 [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. を作成 `TextAbsorber` インスタンス。
1. コール `document.pages.accept(text_absorber)` すべてのページをスキャンします。
1. 抽出したテキストをから取得 `text_absorber.text`.
1. 結果を出力テキストファイルに書き込みます。

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
    # Create a TextAbsorber to extract text
    text_absorber = ap.text.TextAbsorber()
    # Accept the absorber for all pages
    document.pages.accept(text_absorber)
    # Get extracted text
    extracted_text = text_absorber.text
    # Write the text to an output file
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```

## 特定のページからテキストを抽出する

申し込む [テキストアブソーバー](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) 単一ページに変換して、複数ページの文書のそのセクションからテキストを分離して保存します。これは、請求書、レポートセクション、フォームサマリーなど、1 ページだけのコンテンツが必要な場合に便利です。

1. を使用して PDF ドキュメントを開きます。 [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. を作成 `TextAbsorber` インスタンス。
1. コール `accept` ターゲットページ上: `document.pages[page_number].accept(text_absorber)`.
1. 抽出されたテキストを取得し、ファイルに書き込みます。

```python
import os
import aspose.pdf as ap


def extract_text_from_page(infile, outfile, page_number):
    """
    Extract text from a specific page number of the PDF.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1-based page index to extract.
    """
    document = ap.Document(infile)
    text_absorber = ap.text.TextAbsorber()
    # Accept the absorber on only the specified page
    document.pages[page_number].accept(text_absorber)
    extracted_text = text_absorber.text
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```
