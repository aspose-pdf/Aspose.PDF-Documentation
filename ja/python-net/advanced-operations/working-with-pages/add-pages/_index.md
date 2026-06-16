---
title: Python で PDF ページを追加する
linktitle: ページを追加する
type: docs
weight: 10
url: /ja/python-net/add-pages/
description: Python で PDF ドキュメントにページを追加または挿入する方法を学びます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF ページを追加または挿入する
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ファイルにページを追加する方法について説明します。ドキュメント API と PageCollection API を使用して、空白ページを特定の位置に挿入する方法、文書の末尾にページを追加する方法、別の PDF からページを読み込む方法を説明します。
---

.NET 経由の Python 用 Aspose.PDF では、PDF ドキュメントをページレベルで柔軟に操作できます。ページは次の方法で管理できます。 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) そして、にページを追加します [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 特定の位置またはファイルの末尾にあります。

このページは、生成ワークフロー中に既存の PDF に新しい空白ページを挿入したり、文書の末尾にページを追加したりする必要がある場合に使用します。

## PDF ファイルへのページの追加または挿入

.NET 経由の Aspose.PDF は、特定の索引へのページ挿入と PDF の末尾へのページの追加の両方をサポートしています。

### PDF ファイルへの空白ページの挿入

PDF ファイルに空のページを挿入するには：

1. 既存のものを開く [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 適切な方法を使用する。
1. を使用して特定のインデックスに新しい空のページを挿入します [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) `insert()` 方法。
1. 変更を保存する [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 目的の出力パスに。

既存の PDF ファイルの指定した位置に空のページを挿入します。

```python
import aspose.pdf as ap

def insert_empty_page(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.insert(2)
    document.save(output_file_name)
```

### PDF ファイルの末尾に空白ページを追加する

文書が空白ページで終わっていることを確認したい場合があります。このトピックでは、PDF 文書の末尾に空白ページを挿入する方法を説明します。

PDF ファイルの末尾に空白ページを挿入するには：

1. 既存のものを開く [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 適切な方法を使用する。
1. を使用して、ドキュメントの末尾に新しい空白ページを追加します [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) `add()` 方法。
1. 更新を保存する [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

次のコードスニペットは、PDF ファイルの末尾に空のページを挿入する方法を示しています。

```python
import aspose.pdf as ap

def add_empty_page_to_end(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.add()
    document.save(output_file_name)
```

### 別の PDF ドキュメントからページを追加

.NET 経由の Python 用 Aspose.PDF を使用すると、新しいものを作成できます [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)、最初のページを追加し、そのページに別の PDF からページをインポートします。

1. 新規作成 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 新しい空白を追加 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) それを使ってテキストを書いてください [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/).
1. 別の既存のものを開く [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. をコピー [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) その文書から。
1. コピーしたページを、以下を使用してメイン文書に貼り付けます [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. 結合したファイルを保存します。

```python
import aspose.pdf as ap

def add_page_from_another_document(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("This is first page!")
    page.paragraphs.add(text_fragment)

    another_document = ap.Document(input_file_name)
    document.pages.add(another_document.pages[1])

    document.save(output_file_name)
```

## 関連ページトピック

- [Python で PDF ページを操作する](/pdf/ja/python-net/working-with-pages/)
- [Python で PDF ページを移動する](/pdf/ja/python-net/move-pages/)
- [Python で PDF ページを削除する方法](/pdf/ja/python-net/delete-pages/)
- [Python で PDF ページを抽出](/pdf/ja/python-net/extract-pages/)
