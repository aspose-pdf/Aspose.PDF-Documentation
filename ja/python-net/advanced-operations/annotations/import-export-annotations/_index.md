---
title: Python を使用してアノテーションをインポートおよびエクスポートする
linktitle: 注釈のインポートとエクスポート
type: docs
weight: 80
url: /ja/python-net/import-export-annotations/
description: .NET 経由で Aspose.PDF for Python を使用して、1 つの PDF から注釈をインポートし、新しい PDF ドキュメントにエクスポートする方法について説明します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python でドキュメント間で PDF アノテーションを転送できます。
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用してソース PDF から注釈をコピーし、新しい PDF ドキュメントにエクスポートする方法について説明します。このチュートリアルでは、ソースファイルの読み込み、宛先文書の作成、ページの追加、最初のページからの注釈のコピー、結果の保存など、プロセスを小さなステップに分けて説明します。
---

この記事では、.NET 経由で Aspose.PDF for Python を使用して既存の PDF から注釈をインポートし、新しい PDF ドキュメントにエクスポートする方法を説明します。

この例では、ソースファイルの最初のページから注釈を読み取り、新しい PDF を作成し、空白ページを追加して、各注釈をその新しいページにコピーします。この方法は、コメント、マークアップ、またはレビューノートを別の出力文書に移動する必要がある場合に便利です。

## ソース PDF を読み込む

を作成 `Document` すでに注釈が含まれている入力ファイルのオブジェクト。このオブジェクトにより、ページコレクションと各ページに保存されている注釈にアクセスできます。

```python
source_document = ap.Document(infile)
```

## ターゲット PDF の作成

次に、インポートした注釈を受け取る空の PDF ドキュメントを作成します。この段階では、インポート先の文書にはページが含まれていません。

```python
destination_document = ap.Document()
```

## エクスポートした注釈用のページを追加する

注釈はページに属している必要があるため、何かをコピーする前にコピー先の文書に新しいページを追加してください。

```python
page = destination_document.pages.add()
```

## ソースページから注釈をコピー

ソース PDF の最初のページの注釈コレクションを繰り返し処理し、宛先文書の新しいページに各注釈を追加します。

の 2 番目の引数 `page.annotations.add(annot, True)` 既存のオブジェクト参照だけを再利用するのではなく、注釈を宛先ページにコピーするように Aspose.PDF に指示します。

```python
for annot in source_document.pages[1].annotations:
    page.annotations.add(annot, True)
```

## 出力ドキュメントを保存する

すべての注釈をコピーしたら、コピー先の文書を保存して最終的な PDF ファイルを作成します。

```python
destination_document.save(outfile)
```

## 完全な例

次のコードでは、すべてのステップを 1 つの再利用可能な関数にまとめています。

```python
import sys
import aspose.pdf as ap
from os import path


sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def import_export(infile, outfile):
    """
    Import annotations from one PDF document and export them to a new PDF document.
    """
    source_document = ap.Document(infile)
    destination_document = ap.Document()

    page = destination_document.pages.add()

    for annot in source_document.pages[1].annotations:
        page.annotations.add(annot, True)

    destination_document.save(outfile)
```

## 関連トピック

- [インタラクティブ注釈](/python-net/interactive-annotations/)
- [マークアップ注釈](/python-net/markup-annotations/)
- [メディア注釈](/python-net/media-annotations/)
- [セキュリティ注釈](/python-net/security-annotations/)
- [シェイプ注釈](/python-net/shape-annotations/)
- [テキストベースの注釈](/python-net/text-based-annotations/)
- [ウォーターマーク注釈](/python-net/watermark-annotations/)
