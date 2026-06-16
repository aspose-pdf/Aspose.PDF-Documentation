---
title: Python で PDF ページを削除する方法
linktitle: PDF ページの削除
type: docs
weight: 80
url: /ja/python-net/delete-pages/
description: Python で PDF ファイルからページを削除する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で 1 つまたは複数の PDF ページを削除する方法
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ファイルからページを削除する方法について説明します。PageCollection API を使用して文書から 1 ページまたは複数ページを削除し、更新された PDF を保存する方法を説明します。
---

.NET 経由の Python 用 Aspose.PDF を使用すると、PDF ファイルからページを削除できます。特定のページを削除するには、 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) の [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

このワークフローは、文書を共有、アーカイブ、または結合する前に PDF から不要なページを削除する必要がある場合に使用します。

## PDF ファイルからページを削除

Aspose.PDF for Python via .NET は、入力 PDF から 2 ページ目を削除し、更新されたドキュメントを新しいファイルに保存します。この機能は、文書の残りの部分を変更せずに、不要なページや機密ページを削除するのに役立ちます。

1. 入力 PDF をとして読み込む [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. を使用してページを削除します [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. に電話してください [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 更新された PDF ファイルを保存する方法。

次のコードスニペットは、Python を使用して PDF ファイルから特定のページを削除する方法を示しています。

```python
import aspose.pdf as ap

def delete_page(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.delete(2)
    document.save(output_file_name)
```

## PDF ドキュメントから複数のページを削除する

複数のページを削除すると、指定した一連のページを 1 回の操作で削除できます。これは、ページを 1 つずつ削除するよりも効率的です。作成された PDF は、元の文書を保持したまま、新しいファイルに保存されます。

1. 入力 PDF をとして読み込む [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. ページ配列にリストされているページを、以下を使用して削除します。 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. 更新を保存する [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 新しいファイルへ。

```python
import aspose.pdf as ap

def delete_multiple_pages(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    # Example: delete pages 2, 3, and 4.
    pages = [2, 3, 4]
    document.pages.delete(pages)
    document.save(output_file_name)
```

## 関連ページトピック

- [Python で PDF ページを操作する](/pdf/ja/python-net/working-with-pages/)
- [Python で PDF ページを追加する](/pdf/ja/python-net/add-pages/)
- [Python で PDF ページを移動する](/pdf/ja/python-net/move-pages/)
- [Python で PDF ページを抽出](/pdf/ja/python-net/extract-pages/)
