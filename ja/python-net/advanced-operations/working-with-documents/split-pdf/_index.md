---
title: PythonでPDFファイルを分割
linktitle: PDFファイルを分割
type: docs
weight: 60
url: /ja/python-net/split-pdf-document/
description: PythonでPDFファイルを個々のページ、等しい部分、固定サイズのグループ、カスタムページ範囲、奇数または偶数ページに分割する方法を学びましょう。
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pythonを使用してPDFをページおよびページ範囲に分割する
Abstract: 本記事では、Aspose.PDF for Python via .NET を使用して PDF ファイルを分割する方法を示します。PDF を個別ページに分割する方法、2 等分に分割する方法、固定サイズのページグループに分割する方法、カスタムページ範囲で分割する方法、名前付きページグループ、安定したファイル名、奇数ページまたは偶数ページのファイルに分割する方法について説明します。
---

このページでは、Aspose.PDF for Python via .NET を使用して **Python で PDF ファイルを分割する方法** を示します。

大きな PDF を単一ページのファイル、等分された部分、固定サイズのグループ、カスタムページ範囲、または奇数・偶数ページのセットに分割して、配布、レビュー、または下流処理が必要な場合に、これらの例を使用してください。

## PDF オンライン分割例

[Aspose.PDF スプリッタ](https://products.aspose.app/pdf/splitter) オンラインのウェブアプリケーションで、PDF分割機能をテストできます。

[![Aspose PDF 分割](splitter.png)](https://products.aspose.app/pdf/splitter)

PythonでPDFページを単一ページのPDFファイルに分割するには、次の手順に従ってください：

1. PDFドキュメントのページをループ処理する [ドキュメント](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトの [ページコレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) コレクション
1. 各イテレーションごとに、新しい Document オブジェクトを作成し、個々のものを追加します。 [ページ](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 空のドキュメントにオブジェクト
1. 新しいPDFを保存するには [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッド

## PythonでPDFを複数のファイルに分割

以下のPythonコードスニペットは、PDFページを個別のPDFファイルに分割する方法を示しています。

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents(infile, outdir):
    document = ap.Document(infile)
    for page_num in range(1, len(document.pages) + 1):
        with ap.Document() as new_document:
            new_document.pages.add(document.pages[page_num])
            new_document.save(path.join(outdir, f"Page_{page_num}.pdf"))
```

## PDF を二等分に分割する

1. PDFドキュメントを読み込みます。
1. 総ページ数を決定する。
1. 中点を計算してください。
1. 最初の出力ドキュメントを作成してください。
1. 最初の文書から後半のページを削除します。
1. 最初の部分を保存してください。
1. 2番目の出力ドキュメントを作成してください。
1. 2番目のドキュメントから前半のページを削除します。
1. 2番目の部分を保存してください。

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_into_two_parts(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    mid_point = total_pages // 2

    # First part
    with ap.Document(infile) as first_document:
        first_part_range = range(mid_point + 1, total_pages + 1)
        first_document.pages.delete(first_part_range)
        first_document.save(path.join(outdir, "Part_1.pdf"))

    # Second part
    with ap.Document(infile) as second_document:
        second_part_range = range(1, mid_point + 1)
        second_document.pages.delete(second_part_range)
        second_document.save(path.join(outdir, "Part_2.pdf"))
```

## PDF を N ページごとに複数のファイルに分割する

固定ページ数に基づいて、Aspose.PDF for Python を使用して PDF ドキュメントを複数の小さなファイルに分割します。

1. PDFドキュメントを読み込みます。
1. 総ページ数を決定する。
1. パートごとのページ数を定義する。
1. ドキュメントをチャンクごとに反復処理する。
1. 各パートのページ範囲を計算してください。
1. 各パートごとに新しいドキュメントを作成してください。
1. 新しいドキュメントにページをコピーします。
1. 分割された文書を保存してください。
1. すべてのページが処理されるまで繰り返す。

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_every_n_pages(infile, outdir, pages_per_part=3):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    part_index = 1
    for start_page in range(1, total_pages + 1, pages_per_part):
        end_page = min(start_page + pages_per_part - 1, total_pages)

        with ap.Document() as part_document:
            for page_num in range(start_page, end_page + 1):
                part_document.pages.add(document.pages[page_num])
            part_document.save(
                path.join(outdir, f"Every_{pages_per_part}_Part_{part_index}.pdf")
            )

        part_index += 1
```

## PDFをカスタムページ範囲で分割する

Aspose.PDF for Python を使用して、カスタム定義されたページ範囲に基づき PDF ドキュメントを複数のファイルに分割します。

1. PDFドキュメントを読み込みます。
1. 総ページ数を決定する。
1. （start_page, end_page）範囲を表すタプルのリストを作成する。
1. 定義された範囲を反復処理する。
1. 開始ページを検証してください。
1. 最終ページを調整してください。
1. 有効範囲を検証してください。
1. 各範囲に対して新しいドキュメントを作成します。
1. 新しいドキュメントにページをコピーします。
1. 各分割ドキュメントを保存します。

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_by_page_ranges(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    # Define ranges as (start_page, end_page). Use None to indicate last page.
    ranges = [(1, 3), (4, 6), (7, None)]

    for index, (start_page, end_page) in enumerate(ranges, start=1):
        if start_page > total_pages:
            continue

        effective_end = total_pages if end_page is None else min(end_page, total_pages)
        if start_page > effective_end:
            continue

        with ap.Document() as range_document:
            for page_num in range(start_page, effective_end + 1):
                range_document.pages.add(document.pages[page_num])
            range_document.save(
                path.join(outdir, f"Range_{index}_{start_page}_to_{effective_end}.pdf")
            )
```

## PDF を最初のページと残りのページに分割する

Aspose.PDF for Python を使用して、PDF ドキュメントの最初のページを残りのページから切り離します。

1. PDFドキュメントを読み込みます。
1. 総ページ数を決定する。
1. ドキュメントが空であるかどうかを確認してください。
1. 最初のページのドキュメントを作成してください。
1. 最初のページを追加する。
1. 最初のページのドキュメントを保存してください。
1. 追加のページがあるか確認してください。
1. 残りのページ用にドキュメントを作成してください。
1. 残りのページをコピーする。
1. 残りのページのドキュメントを保存します。

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_first_page_and_rest(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    with ap.Document() as first_page_document:
        first_page_document.pages.add(document.pages[1])
        first_page_document.save(path.join(outdir, "First_Page.pdf"))

    if total_pages == 1:
        return

    with ap.Document() as remaining_pages_document:
        for page_num in range(2, total_pages + 1):
            remaining_pages_document.pages.add(document.pages[page_num])
        remaining_pages_document.save(path.join(outdir, "Remaining_Pages.pdf"))
```

## PDF を最後のページとそれ以前のページに分割する

Aspose.PDF for Python を使用して、PDF ドキュメントの最後のページを抽出し、残りのページから分離します。

1. PDFドキュメントを読み込みます。
1. 総ページ数を決定する。
1. ドキュメントが空であるかどうかを確認してください。
1. 最後のページ用のドキュメントを作成します。
1. 最後のページを追加する。
1. 最後のページのドキュメントを保存します。
1. 単一ページの文書をチェックしてください。
1. 元のドキュメントから最後のページを削除します。
1. 残りのページを保存します。

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_last_page_and_rest(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    with ap.Document() as last_page_document:
        last_page_document.pages.add(document.pages[total_pages])
        last_page_document.save(path.join(outdir, "Last_Page.pdf"))

    if total_pages == 1:
        return

    document.pages.delete(total_pages)  # Remove last page from original document
    document.save(path.join(outdir, "Previous_Pages.pdf"))
```

## PDF を 3 部に分割する

Aspose.PDF for Python を使用して PDF 文書を 3 つの別々の部分に分割します。

1. PDFドキュメントを読み込みます。
1. 総ページ数を決定する。
1. ドキュメントが空であるかどうかを確認してください。
1. パートサイズを計算する。
1. 3つの部分を反復処理する。
1. 各パートのページ範囲を決定します。
1. ページ範囲を検証してください。
1. 各パートごとに新しいドキュメントを作成してください。
1. ページをパート文書にコピーします。
1. 各パートを保存してください。

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_into_three_parts(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    part_size = max(1, (total_pages + 2) // 3)

    for part_index in range(3):
        start_page = part_index * part_size + 1
        end_page = min((part_index + 1) * part_size, total_pages)

        if start_page > total_pages:
            break

        with ap.Document() as part_document:
            for page_num in range(start_page, end_page + 1):
                part_document.pages.add(document.pages[page_num])
            part_document.save(path.join(outdir, f"Three_Parts_{part_index + 1}.pdf"))
```

## カスタム PDF ページ分割ツール

Aspose.PDF for Python を使用して、カスタムで定義されたページグループに基づき、PDF ドキュメントを複数のファイルに分割します。

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_custom_page_groups(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    groups = [
        [1, 2, 5],
        [3, 4, 6, 7],
    ]

    for group_index, group in enumerate(groups, start=1):
        valid_pages = [page_num for page_num in group if 1 <= page_num <= total_pages]
        if not valid_pages:
            continue

        with ap.Document() as group_document:
            for page_num in valid_pages:
                group_document.pages.add(document.pages[page_num])
            group_document.save(path.join(outdir, f"Custom_Group_{group_index}.pdf"))
```

## PDF を個別ページに分割し、安定したファイル名を付ける

Aspose.PDF for Python を使用して、PDF ドキュメントを個々のページに分割し、安定したファイル名で保存します。

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_with_stable_filenames(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    for page_num in range(1, total_pages + 1):
        with ap.Document() as new_document:
            new_document.pages.add(document.pages[page_num])
            new_document.save(path.join(outdir, f"Page_{page_num:03d}.pdf"))
```

## PDFを奇数ページと偶数ページに分割

Aspose.PDF for Python を使用して、PDF ドキュメントを奇数ページと偶数ページそれぞれを含む 2 つの別々のファイルに分割します。

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_odd_even_pages(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    # Odd pages document
    with ap.Document(infile) as document:
        with ap.Document() as odd_document:
            for page_num in range(1, total_pages + 1, 2):
                odd_document.pages.add(document.pages[page_num])
            odd_document.save(path.join(outdir, "Odd_Pages.pdf"))

        with ap.Document() as even_document:
            for page_num in range(2, total_pages + 1, 2):
                even_document.pages.add(document.pages[page_num])
            even_document.save(path.join(outdir, "Even_Pages.pdf"))
```

## 関連文書トピック

- [PythonでPDF文書を扱う](/pdf/ja/python-net/working-with-documents/)
- [PythonでPDFファイルを結合する](/pdf/ja/python-net/merge-pdf-documents/)
- [PythonでPDFファイルを最適化する](/pdf/ja/python-net/optimize-pdf/)
- [PythonでPDFドキュメントを操作する](/pdf/ja/python-net/manipulate-pdf-document/)
