---
title: Python で PDF にウォーターマークを追加する方法
linktitle: ウォーターマークの追加
type: docs
weight: 30
url: /ja/python-net/add-watermarks/
description: .NET 経由で Aspose.PDF for Python を使用して Python で PDF ファイルにウォーターマークアーティファクトを追加する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pythonを使ってPDFにウォーターマークを追加する方法
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用してアーティファクトを管理して PDF ドキュメントにウォーターマークを追加する方法について説明します。アーティファクトを処理するための主要なクラスである `Artifact` と `ArtifactCollection` を紹介し、`Page` クラスの `Artifacts` プロパティを使用してそれらにアクセスする方法について説明します。この記事では、「コンテンツ」、「フォーム」、「イメージ」、「テキスト」、「長方形」、「回転」、「不透明度」などの属性を含む、「Artifact」クラスのプロパティについて詳しく説明します。これらの属性により、PDFファイル内のアーティファクトを包括的に操作できます。さらに、Python を使用して PDF の最初のページにウォーターマークをプログラムで追加する方法を示す実用的な例も提供されています。このコードスニペットは、PDF ドキュメントに追加して変更を保存する前に、テキスト、配置、回転、不透明度を設定して「WatermarkArtifact」を作成して設定する方法を示しています。
---

PDF へのウォーターマークアーティファクトの追加 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .NET 経由で Python 用 Aspose.PDF を使用する。ウォーターマークは、ブランディング、セキュリティ、または情報提供を目的としてページに適用される視覚的なオーバーレイです。この例は設定方法を示しています。 [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) 外観、位置決め [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) そして [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/)、ウォーターマークを適用する前の回転、透明度 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

## PDF からウォーターマークを抽出

1. PDF ドキュメントをロードします。
1. ページアーティファクトにアクセスします。
1. ウォーターマークアーティファクトをフィルタリングします。
1. ウォーターマークの要素を集めましょう。
1. ウォーターマークプロパティを抽出します。
1. ウォーターマーク情報を出力します。

```python
from os import path
import sys
import aspose.pdf as ap

def extract_watermark_from_pdf(infile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            print(f"{watermark.text} {watermark.rectangle}")
```

## PDF にウォーターマークを追加

Python 用 Aspose.PDF を使用して PDF ドキュメントにテキストウォーターマークを追加します。

1. PDF ドキュメントをロードします。
1. テキストステートを作成します。
1. ウォーターマークアーティファクトを作成します。
1. ウォーターマークのテキストとスタイルを設定します。
1. ポジショニングとローテーションを設定します。
1. 不透明度と背景の動作を設定します。
1. ウォーターマークをページに添付します。
1. 更新した文書を保存します。

```python
from os import path
import sys
import aspose.pdf as ap

def add_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        text_state = ap.text.TextState()
        text_state.font_size = 72
        text_state.foreground_color = ap.Color.blue_violet
        text_state.font_style = ap.text.FontStyles.BOLD
        text_state.font = ap.text.FontRepository.find_font("Arial")

        watermark = ap.WatermarkArtifact()
        watermark.set_text_and_state("WATERMARK", text_state)
        watermark.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
        watermark.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
        watermark.rotation = 60
        watermark.opacity = 0.2
        watermark.is_background = True

        document.pages[1].artifacts.append(watermark)
        document.save(outfile)

```

## PDF ページからウォーターマークアーティファクトを削除 

Aspose.PDF for Python API を使用して、PDF ドキュメントの特定のページからウォーターマークアーティファクトを削除します。このアプローチは、ページアーティファクトとして保存されているウォーターマーク要素（特にページネーションウォーターマークサブタイプとして分類されたもの）を対象とし、それらを繰り返し処理して、更新された文書を保存する前に削除します。

1. PDF ドキュメントをロードします。
1. ページアーティファクトにアクセスします。
1. ウォーターマークアーティファクトをフィルタリングします。
1. ウォーターマークアーティファクトを削除します。
1. 更新した文書を保存します。

```python
from os import path
import sys
import aspose.pdf as ap

def delete_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            document.pages[1].artifacts.delete(watermark)

        document.save(outfile)
```

## アーティファクトの関連トピック

- [Python で PDF アーティファクトを操作する](/pdf/ja/python-net/artifacts/)
- [Python で PDF 背景を追加する方法](/pdf/ja/python-net/add-backgrounds/)
- [Python でベイツ番号を PDF に追加する方法](/pdf/ja/python-net/add-bates-numbering/)
- [PDF ファイル内のアーティファクトタイプを数える](/pdf/ja/python-net/counting-artifacts/)