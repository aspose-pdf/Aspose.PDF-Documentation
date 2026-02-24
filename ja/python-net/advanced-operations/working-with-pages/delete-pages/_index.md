---
title: PythonでPDFページをプログラム的に削除
linktitle: PDFページの削除
type: docs
weight: 80
url: /ja/python-net/delete-pages/
description: Aspose.PDF for Python via .NET ライブラリを使用して、PDFファイルからページを削除できます。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PythonでPDFページを削除する方法
Abstract: 本記事では、Aspose.PDF ライブラリ for Python via .NET を使用して PDF ファイルからページを削除する方法について簡潔に解説します。特定のページを削除するために `PageCollection` クラスを利用することに焦点を当てています。プロセスは、削除するページのインデックスを指定して `delete()` メソッドを呼び出し、続いて `save()` メソッドで更新されたドキュメントを保存するという流れです。さらに、PDF ファイルからページを削除するコードスニペットを提供し、実践的なコンテキストで Aspose.PDF ライブラリの使用例を示しています。
---

Aspose.PDF for Python via .NET を使用して PDF ファイルからページを削除できます。特定のページを削除するには、[`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) を使用した [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を利用します。

## PDFファイルからページを削除

Aspose.PDF for Python via .NET は、入力 PDF の 2 ページ目を削除し、更新されたドキュメントを新しいファイルに保存します。この機能は、不要または機密のページを他の部分に影響を与えずに削除するのに便利です。

1. 入力 PDF を [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) としてロードします。
1. [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) を使用してページを削除します。
1. 更新された PDF ファイルを保存するために [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを呼び出します。

次のコードスニペットは、Python を使用して PDF ファイルから特定のページを削除する方法を示しています。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def delete_page(input_file_name, output_file_name):
    """
    Delete a single page from a PDF document.

    Demonstrates how to remove a specific page from a PDF document using
    the Aspose.PDF library. This function deletes page 2 from the input
    document and saves the result to a new file.

    Args:
        input_file_name (str): Path to the input PDF file from which to delete a page.
        output_file_name (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Deletes page 2 (1-based indexing) from the document
        - Page numbering is 1-based (page 2 is the second page)
        - The original document is not modified; a new file is created
        - If the document has fewer than 2 pages, this may raise an error

    Example:
        >>> delete_page("input.pdf", "output.pdf")
        # Removes page 2 from input.pdf and saves result as output.pdf
    """
    # Open the PDF as a Document
    document = ap.Document(input_file_name)
    # Delete page using PageCollection API
    document.pages.delete(2)
    # Save updated Document
    document.save(output_file_name)
```

## PDFドキュメントから複数ページを削除

複数ページを削除すると、指定したページのセットを一度の操作で削除でき、ページを1つずつ削除するより効率的です。結果として得られる PDF は新しいファイルに保存され、元のドキュメントが保護されます。

1. 入力 PDF を [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) としてロードします。
1. ページ配列にリストされたページを [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) を使用して削除します。
1. 更新された [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を新しいファイルに保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def delete_bunch_pages(input_file_name, output_file_name):
    """
    Delete multiple pages from a PDF document in a single operation.

    Demonstrates bulk page deletion by removing multiple specified pages
    from a PDF document. This is more efficient than deleting pages
    one by one when removing multiple pages.

    Args:
        input_file_name (str): Path to the input PDF file from which to delete pages.
        output_file_name (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Deletes pages 2, 3, 4, 6, 7, and 9 in this example
        - Page numbers are 1-based (page 2 is the second page)
        - Pages are deleted in the order specified in the list
        - The original document is not modified; a new file is created
        - Ensure the document has enough pages to avoid errors
        - Page numbers should be adjusted if the source document has fewer pages

    Example:
        >>> delete_bunch_pages("input.pdf", "output.pdf")
        # Removes pages 2, 3, 4, 6, 7, and 9 from input.pdf
    """
    # Open the PDF as a Document
    document = ap.Document(input_file_name)
    # Example: Deleting pages 2, 3, 4, 6, 7, and 9; modify this list as needed for your use case.
    pages = [2,3,4,6,7,9]
    # Delete pages via PageCollection API
    document.pages.delete(pages)
    # Save updated Document
    document.save(output_file_name)
```

