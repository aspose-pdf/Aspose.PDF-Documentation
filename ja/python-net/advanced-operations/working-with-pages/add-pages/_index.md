---
title: PythonでPDFにページを追加する
linktitle: ページの追加
type: docs
weight: 10
url: /ja/python-net/add-pages/
description: Aspose.PDF を使用して、柔軟な文書作成と編集が可能な Python で PDF ドキュメントにページを追加する方法を紹介します。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF にページを追加する方法
Abstract: この記事では、Aspose.PDF for Python via .NET API を使用して PDF ドキュメントのページを操作する方法についてガイドしています。特に PDF 内のすべてのページを管理する `PageCollection` クラスを通じて提供される API の柔軟性を強調しています。ドキュメントでは、PDF ファイルの特定の場所にページを追加または挿入する手順を詳述しています。主に 2 つの操作、すなわちドキュメント内の任意の場所に空白ページを挿入することと、ドキュメントの末尾に空白ページを追加することが説明されています。両方の操作では、`Document` オブジェクトを作成し、`PageCollection` の `insert` または `add` メソッドを使用し、変更されたドキュメントを保存するプロセスが含まれます。この記事には、これらのタスクを示すコードスニペットが含まれており、Python とこの API を使用して PDF ドキュメントを簡単に操作できることを示しています。
---

Aspose.PDF for Python via .NET API は、Python を使用して PDF ドキュメントのページを操作するための完全な柔軟性を提供します。PDF ドキュメントのすべてのページは、PDF ページの操作に使用できる [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) に保持されます。
Aspose.PDF for Python via .NET は、ファイル内の任意の場所にページを挿入できるだけでなく、PDF ファイルの末尾にページを追加することも可能です。[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) にページを挿入できます。このセクションでは、Python を使用して PDF にページを追加する方法を示します。

## PDF ファイルにページを追加または挿入する

Aspose.PDF for Python via .NET は、ファイル内の任意の場所にページを挿入でき、PDF ファイルの末尾にページを追加することも可能です。[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を使用します。

### PDF ファイルに空白ページを挿入する

PDF ファイルに空白ページを挿入するには:

1. 適切な方法で既存の [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を開きます。
1. [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) の `insert()` メソッドを使用して、特定のインデックスに新しい空白ページを挿入します。
1. 変更された [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を目的の出力パスに保存します。

既存の PDF ファイルに指定された位置で空白ページを挿入します:

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def insert_empty_page(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    document.pages.insert(2)
    document.save(output_file_name)
```

### PDF ファイルの末尾に空白ページを追加する

場合によっては、文書が空白ページで終わるようにしたいことがあります。このトピックでは、PDF 文書の末尾に空白ページを挿入する方法を説明します。

PDF ファイルの末尾に空白ページを挿入するには:

1. 適切な方法で既存の [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を開きます。
1. [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) の `add()` メソッドを使用して、文書の末尾に新しい空白ページを追加します。
1. 更新された [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を保存します。

以下のコードスニペットは、PDF ファイルの末尾に空白ページを挿入する方法を示しています。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_empty_page_to_end(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Insert an empty page at the end of a PDF file
    document.pages.add()

    # Save output file
    document.save(output_file_name)
```

### 別の PDF ドキュメントからページを追加する

Aspose.PDF for Python ライブラリを使用すると、新しい [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を作成し、最初のページを追加した後、別の PDF からページをインポートできます。

1. 新しい [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を作成します。
1. 新しい空白の [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) を追加し、[`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) を使用してテキストを書き込みます。
1. 別の既存の [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を開きます。
1. そのドキュメントから [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) をコピーします。
1. コピーしたページを [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) を使用してメインドキュメントに貼り付けます。
1. 結合されたファイルを保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_from_another_document(input_file_name, output_file_name):
    # Open document
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("This is first page!")
    page.paragraphs.add(text_fragment)

    another_document = ap.Document(input_file_name)
    document.pages.add(another_document.pages[1])

    # Save output file
    document.save(output_file_name)
```
