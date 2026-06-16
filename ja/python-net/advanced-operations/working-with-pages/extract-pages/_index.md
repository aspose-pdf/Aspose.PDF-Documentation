---
title: Python で PDF ページを抽出
linktitle: PDF ページの抽出
type: docs
weight: 80
url: /ja/python-net/extract-pages/
description: Python で 1 つまたは複数の PDF ページを新しいファイルに抽出する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF ページを抽出する方法
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ファイルからページを抽出する方法について説明します。1 ベースのページインデックスと PageCollection API を使用して、1 ページまたは複数ページを新しい文書にコピーする方法を学びましょう。
---

## PDF から 1 ページを抽出

PDF ドキュメントから特定のページを抽出し、新しいファイルとして保存します。Aspose.PDF ライブラリを使用して、スクリプトは元の文書を変更せずに目的のページを新しい PDF にコピーします。PDF を分割したり、重要なページを分離して配布したりする場合に便利です。

1. を使用してソース PDF をロードします。 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) アピ (`ap.Document()`).
1. 新規作成 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 抽出されたページを保持します。
1. 必要なものを追加 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) ソース文書から宛先文書を使用して新規 PDF へ [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (`dst_document.pages.add(...)`).
    -この例では、ページ 2 が抽出されます (1 ベースのインデックス)。
1. 新しいものを保存 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 抽出されたページを指定された出力ファイルに保存します。

```python
import aspose.pdf as ap

def extract_page(input_file_name: str, output_file_name: str) -> None:
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    dst_document.pages.add(src_document.pages[2])
    dst_document.save(output_file_name)
```

## PDF から複数のページを抽出

PDF ドキュメントから複数の特定のページを抽出し、新しいファイルに保存します。Aspose.PDF ライブラリを使用すると、選択したページは元の文書はそのままの状態で新しい PDF にコピーされます。これは、大きな文書の関連部分だけを含む小さな PDF を作成する場合に便利です。

1. を使用してソース PDF をロードします。 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) アピ (`ap.Document()`).
1. 新規作成 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 抽出されたページを保存します。
1. 抽出するページを選択します (この例では、2 ページ目と 3 ページ目に 1 ベースのインデックスを使用しています)。
1. 選択した各項目を追加 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) ソース文書から、その PDF を使用して新しい PDF へ [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. 新しいものを保存 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 抽出されたページを指定された出力ファイルに保存します。

```python
import aspose.pdf as ap

def extract_multiple_pages(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    pages = [2, 3]
    another_document = ap.Document()
    for page_index in pages:
        another_document.pages.add(document.pages[page_index])
    another_document.save(output_file_name)
```

## 関連ページトピック

- [Python で PDF ページを操作する](/pdf/ja/python-net/working-with-pages/)
- [Python で PDF ページを削除する方法](/pdf/ja/python-net/delete-pages/)
- [Python で PDF ページを移動する](/pdf/ja/python-net/move-pages/)
- [Python で PDF ファイルを分割する方法](/pdf/ja/python-net/split-document/)
