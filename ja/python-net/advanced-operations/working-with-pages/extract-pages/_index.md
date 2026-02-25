---
title: Pythonでページをプログラム的に抽出
linktitle: PDFページの抽出
type: docs
weight: 80
url: /ja/python-net/extract-pages/
description: Aspose.PDF for Python via .NET ライブラリを使用して、PDFファイルからページを抽出できます。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pythonを使用してPDFページを抽出する方法
Abstract: この記事では、Aspose.PDF for Python ライブラリを使用して PDF ドキュメントからページを抽出する方法を示します。この手法は、単一ページの抽出と複数ページの抽出の両方をカバーし、開発者が選択したページのみを含む新しい PDF ファイルを作成できるようにします。例では、1 ベースのインデックスで特定のページにアクセスし、それらを新しい PDF ドキュメントにコピーして、元のドキュメントをそのままに結果を保存する方法を示しています。これらの方法は、大規模なドキュメントを分割したり、選択したセクションを共有したり、配布や分析のためにカスタマイズされた PDF サブセットを作成するのに役立ちます。
---

## PDFから単一ページを抽出

PDF ドキュメントから特定のページを抽出し、新しいファイルとして保存します。Aspose.PDF ライブラリを使用して、スクリプトは目的のページを新しい PDF にコピーし、元のドキュメントは変更されません。これは、PDF を分割したり、配布用に重要なページを切り出すのに役立ちます。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`) を使用してロードします。
1. 抽出したページを保持する新しい [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を作成します。
1. ソース ドキュメントから目的の [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) を取得し、宛先ドキュメントの [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)（`dst_document.pages.add(...)`）を使用して新しい PDF に追加します。
- この例では、ページ 2 が抽出されます（1 ベースのインデックス）。
1. 抽出したページを含む新しい [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を指定された出力ファイルに保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def extract_page(input_file_name, output_file_name):
    """
    Extract a single page from a PDF document.

    Demonstrates how to extract a specific page from a PDF document using
    the Aspose.PDF library. This function extracts page 2 from the input
    document and saves it as a new file containing only that page.

    Args:
        input_file_name (str): Path to the input PDF file from which to extract a page.
        output_file_name (str): Path where the extracted page will be saved.

    Returns:
        None: The function creates a new PDF containing the extracted page and saves it to the output path.

    Note:
        - Extracts page 2 (1-based indexing) from the document
        - Page numbering is 1-based (page 2 is the second page)
        - The original document is not modified; a new file is created
        - If the document has fewer than 2 pages, this may raise an error

    Example:
        >>> extract_page("input.pdf", "output.pdf")
        # Extracts page 2 from input.pdf and saves result as output.pdf
    """
    # Open source PDF as Document
    src_document = ap.Document(input_file_name)
    # Create destination Document to hold extracted pages
    dst_document = ap.Document()
    # Add a Page from source to destination using PageCollection API
    dst_document.pages.add(src_document.pages[2])
    # Save destination Document
    dst_document.save(output_file_name)
```

## PDFから複数ページを抽出

PDF ドキュメントから複数の特定ページを抽出し、新しいファイルに保存します。Aspose.PDF ライブラリを使用して、選択したページを新しい PDF にコピーし、元のドキュメントはそのままにします。これは、より大きなドキュメントの関連セクションのみを含む小さな PDF を作成するのに役立ちます。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`) を使用してロードします。
1. 抽出したページを保持する新しい [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を作成します。
1. 抽出するページを選択します（この例では、1 ベースのインデックスを使用してページ 2 と 3）。
1. ソースドキュメントから選択した各 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) を取得し、その [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) を使用して新しい PDF に追加します。
1. 抽出したページを含む新しい [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を指定された出力ファイルに保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def extract_bunch_pages(input_file_name, output_file_name):
    """
    Extract specific pages from a PDF document and save them to a new file.

    This function reads a PDF document, extracts pages 2 and 3 (1-indexed),
    and saves them to a new PDF file.

    Args:
        input_file_name (str): Path to the input PDF file to extract pages from.
        output_file_name (str): Path where the new PDF file with extracted pages will be saved.

    Returns:
        None

    Note:
        The function specifically extracts pages 2 and 3 from the source document.
        Page indexing appears to be 1-based in this implementation.
    """
    # Open source Document
    document = ap.Document(input_file_name)
    pages = [2,3]
    # Create destination Document
    another_document = ap.Document()
    # Copy selected Page objects via PageCollection API
    for page_index in pages:
        another_document.pages.add(document.pages[page_index])
    # Save destination Document
    another_document.save(output_file_name)
```
