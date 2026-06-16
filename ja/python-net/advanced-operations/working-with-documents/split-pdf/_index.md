---
title: Python で PDF ファイルを分割する方法
linktitle: PDF ファイルの分割
type: docs
weight: 60
url: /ja/python-net/split-pdf-document/
description: Python で PDF ファイルを個々のページ、等しい部分、固定サイズのグループ、カスタムページ範囲、奇数ページまたは偶数ページに分割する方法を学びます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF をページとページ範囲に分割する
Abstract: この記事では、.NET 経由で Python 用 Aspose.PDF を使用して PDF ファイルを分割する方法を説明します。PDF を個々のページ、2 つの等しい部分、固定サイズのページグループ、カスタムページ範囲、名前付きページグループ、固定ファイル名、奇数ページまたは偶数ページファイルに分割する方法について説明します。
---

このページでは、.NET 経由で Aspose.PDF for Python を使用して **Python で PDF ファイルを分割**する方法を説明します。

これらの例は、大きな PDF を、配布、レビュー、または下流処理のために、単一ページのファイル、等しい部分、固定サイズのグループ、カスタムページ範囲、奇数ページセットと偶数ページセットに分割する必要がある場合に使用します。

## PDF を分割するオンライン例

[Aspose.PDF スプリッター](https://products.aspose.app/pdf/splitter) は、PDF 分割機能をテストできるオンライン Web アプリケーションです。

[![アスポーススプリット PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Python で PDF ページを 1 ページの PDF ファイルに分割するには、次の手順に従います。

1. PDFドキュメントのページをループ処理して [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトの [ページコレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) コレクション
1. イテレーションごとに、新しい Document オブジェクトを作成し、個別のオブジェクトを追加します [ページ](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) オブジェクトを空の文書に入れる
1. 次の方法で新しい PDF を保存します。 [保存 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法

## Python でPDFを複数のファイルに分割する方法

次の Python コードスニペットは、PDF ページを個別の PDF ファイルに分割する方法を示しています。

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

## PDF を 2 つの等しい部分に分割する

1. PDF ドキュメントをロードします。
1. ページの総数を決定します。
1. 中間点を計算します。
1. 最初の出力ドキュメントを作成します。
1. 最初の文書から後半ページを削除します。
1. 最初の部分を保存します。
1. 2 番目の出力ドキュメントを作成します。
1. 2 番目の文書から前半ページを削除します。
1. 2 番目の部分を保存します。

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

## NページごとにPDFを複数のファイルに分割

Aspose.PDF for Python を使用して、PDF ドキュメントを一定のページ数に基づいて複数の小さなファイルに分割します。

1. PDF ドキュメントをロードします。
1. ページの総数を決定します。
1. パーツごとにページを定義します。
1. ドキュメントをチャンク単位で反復処理します。
1. 各パーツのページ範囲を計算します。
1. パーツごとに新しいドキュメントを作成します。
1. ページを新しい文書にコピーします。
1. 分割した文書を保存します。
1. すべてのページが処理されるまで繰り返します。

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

## PDF をカスタムページ範囲で分割

Aspose.PDF for Python を使用して、カスタム定義のページ範囲に基づいて PDF ドキュメントを複数のファイルに分割します。

1. PDF ドキュメントをロードします。
1. ページの総数を決定します。
1. (開始ページ、終了ページ) 範囲を表すタプルのリストを作成します。
1. 定義した範囲を繰り返し処理します。
1. スタートページを検証してください。
1. 終了ページを調整してください。
1. 有効範囲を検証してください。
1. 範囲ごとに新しい文書を作成します。
1. ページを新しい文書にコピーします。
1. 分割された各文書を保存します。

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

## PDF を最初のページと残りのページに分割

Aspose.PDF for Python を使用して、PDF ドキュメントの最初のページを残りのページから分離します。

1. PDF ドキュメントをロードします。
1. ページの総数を決定します。
1. 文書が空かどうかを確認してください。
1. 最初のページの文書を作成します。
1. 最初のページを追加します。
1. 最初のページの文書を保存します。
1. 他のページがあるか確認してください。
1. 残りのページの文書を作成します。
1. 残りのページをコピーします。
1. 残りのページの文書を保存します。

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

## PDF を最後のページと前のページに分割

Aspose.PDF for Python を使用して PDF ドキュメントの最後のページを抽出し、それを残りのページから分離します。

1. PDF ドキュメントをロードします。
1. ページの総数を決定します。
1. 文書が空かどうかを確認してください。
1. 最後のページの文書を作成します。
1. 最後のページを追加します。
1. 最後のページの文書を保存します。
1. 単一ページの文書を確認してください。
1. 元の文書から最後のページを削除します。
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

## PDF を 3 つの部分に分割

Python 用 Aspose.PDF を使用して PDF ドキュメントを 3 つの部分に分割します。

1. PDF ドキュメントをロードします。
1. ページの総数を決定します。
1. 文書が空かどうかを確認してください。
1. パーツサイズを計算します。
1. 3 つのパートを繰り返します。
1. 各パーツのページ範囲を指定します。
1. ページ範囲を検証してください。
1. パーツごとに新しいドキュメントを作成します。
1. ページをパーツドキュメントにコピーします。
1. 各パーツを保存します。

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

## カスタム PDF ページスプリッター

Aspose.PDF for Python を使用して、カスタム定義のページグループに基づいて PDF ドキュメントを複数のファイルに分割します。

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

## PDF を安定したファイル名で個々のページに分割

PDF ドキュメントを個々のページに分割し、Aspose.PDF for Python を使用して安定したファイル名で保存します。

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

## PDF を奇数ページと偶数ページに分割

Aspose.PDF for Python を使用して、PDF ドキュメントをそれぞれ奇数ページと偶数ページを含む 2 つのファイルに分割します。

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

## 関連ドキュメントトピック

- [Python で PDF ドキュメントを操作する](/pdf/ja/python-net/working-with-documents/)
- [Python で PDF ファイルをマージする](/pdf/ja/python-net/merge-pdf-documents/)
- [Python で PDF ファイルを最適化する方法](/pdf/ja/python-net/optimize-pdf/)
- [Python で PDF ドキュメントを操作する方法](/pdf/ja/python-net/manipulate-pdf-document/)

