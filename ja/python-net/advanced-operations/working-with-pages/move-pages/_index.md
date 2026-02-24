---
title: Python を使用した PDF ページのプログラムによる移動
linktitle: PDF ページの移動
type: docs
weight: 100
url: /ja/python-net/move-pages/
description: Aspose.PDF for Python via .NET を使用して、PDF ファイルの任意の位置または末尾にページを移動してみましょう。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用した PDF ドキュメント間のページ移動
Abstract: この記事では、Python を使用して PDF ドキュメント間または単一の PDF ドキュメント内でページを移動するための包括的なガイドを提供します。特に Aspose.PDF ライブラリを利用します。3 つのシナリオ――1 つの PDF から別の PDF へ単一ページを移動する、複数ページを転送する、同一ドキュメント内でページを再配置する――のステップバイステップの手順を概説します。各シナリオでは、ソースと宛先の PDF 用に `Document` クラスのオブジェクトを作成し、`PageCollection` クラスを介してページを操作し、`add`、`delete`、`save` メソッドを使用して目的のページ再配置を実現します。実装のためのコードスニペットが提供されており、Python スクリプトを使用してページを効率的に移動する方法を示しています。
---

## 1 つの PDF ドキュメントから別の PDF ドキュメントへページを移動する

Aspose.PDF for Python を使用すると、ページを（単にコピーするのではなく）別の PDF に移動できます。選択したページは元のドキュメントから削除され、新しい PDF ファイルに追加されます。

これは、1 冊の本からページを切り取って別の本に貼り付けるようなものです — 移動後、そのページは元のファイルには存在しなくなります。

1. [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスを使用して、ソース PDF ドキュメントを開きます。
1. 移動する特定のページ（この場合はページ 2）を選択します — これは [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) を指します。
1. 新しい PDF ドキュメントを作成します（別の [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) をインスタンス化）。
1. 宛先ドキュメントの [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) を使用して、選択したページを新しい PDF ドキュメントに追加します（例: `another_document.pages.add(page)`）。
1. 元のドキュメントの [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) を使用してページを削除します（例: `document.pages.delete(index)`）。
1. 両方のドキュメントを保存します。

以下のコードスニペットは、1 ページを移動する方法を示しています。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_page_from_one_document_to_another(input_file_name, output_file_name):
    """
    Move a single page from one PDF document to another.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file after moving the page.
    """
    document = ap.Document(input_file_name)
    page = document.pages[2]
    another_document = ap.Document()
    another_document.pages.add(page)
    document.pages.delete(2)
    document.save(input_file_name.replace(".pdf","_new.pdf"))
    another_document.save(output_file_name)
```

## 複数のページを 1 つの PDF ドキュメントから別の PDF ドキュメントへ移動する

コピーとは異なり、この操作は選択されたページを転送します — ソースファイルから削除し、新しい PDF に保存します。

1. 新しい空の宛先ドキュメント（`Document`）を作成します。
1. ソースドキュメントの [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) から複数のページ（この場合はページ 1 と 3）を選択します。
1. 選択したページをループで処理し、各ページを宛先ドキュメントの [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) に追加します。
1. 移動したページを含む宛先ドキュメントを保存します。
1. ソースドキュメントの [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) を使用して、移動したページを削除します。
1. 両方のバージョンを保持できるように、変更されたソースドキュメントを新しいファイル名で保存します。

以下のコードスニペットは、PDF ファイルの末尾に空白ページを挿入する方法を示しています。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_bunch_pages_from_one_document_to_another(input_file_name, output_file_name):
    """
    Move a set of pages from one PDF document to another.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file where selected pages will be saved.
    """
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    pages = [1, 3]
    for page_index in pages:
        page = src_document.pages[page_index]
        dst_document.pages.add(page)
    # Save output files
    dst_document.save(output_file_name)
    src_document.pages.delete(pages)
    src_document.save(input_file_name.replace(".pdf","_new.pdf"))
```

## 現在の PDF ドキュメント内でページを新しい位置に移動する

同じドキュメント内で特定のページを別の位置に移動する方法を示しています — PDF のレイアウトを再編成または編集する際によくあるニーズです。

1. [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスを使用して入力 PDF ドキュメントを読み込みます。
1. 移動したいページ（ページ 2）を選択します — これは [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) です。
1. ドキュメントの [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) を使用して、文書の末尾に追加します。
1. 元のページを、以前の位置から [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) を介して削除します。
1. 変更されたドキュメントを新しいファイルとして保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_page_in_new_location_in_same_document(input_file_name, output_file_name):
    """
    Move a page to a new location within the same PDF document.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file after moving the page.
    """
    srcDocument = ap.Document(input_file_name)

    page = srcDocument.pages[2]
    srcDocument.pages.add(page)
    srcDocument.pages.delete(2)

    # Save output file
    srcDocument.save(output_file_name)
```


