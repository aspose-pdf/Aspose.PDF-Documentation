---
title: Python を使用して PDF ヘッダーとフッターを管理する
linktitle: PDF ヘッダーとフッターの管理
type: docs
weight: 70
url: /ja/python-net/artifacts-header-footer/
description: Python と Aspose.PDF を使用して PDF ドキュメントのヘッダーとフッターを管理する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF ヘッダーとフッターを追加、カスタマイズ、削除する方法
Abstract: ヘッダーとフッターの管理は、ビジネス、パブリッシング、自動化ワークフローでPDF文書を扱う際の一般的な要件です。この記事では、Aspose.PDF for Python を使用して、フォント、サイズ、色、配置などのカスタムスタイルでプロ並みのヘッダーとフッターを追加する方法を示します。また、PDF ページからヘッダーやフッターなどの既存のページネーションアーティファクトを検出して削除する方法についても説明します。再利用可能な関数とわかりやすい例を使用することで、開発者はこれらの機能を文書処理システムにすばやく統合して、ブランディング、レポート、またはファイルのクリーンアップを行うことができます。
---

## スタイル付きテキストアーティファクトの作成

このユーティリティ関数は、Aspose.PDF for Python を使用して PDF ページ用の再利用可能なテキストアーティファクトを作成する方法を説明します。フォント設定、色、サイズ、配置など、一貫したフォーマットでスタイル付きのヘッダーまたはフッターを生成するように設計されています。この関数はアーティファクトの作成を抽象化して、さまざまなページレベルのテキスト装飾に再利用できます。

1. アーティファクトオブジェクトをインスタンス化します。
1. アーティファクトのテキストコンテンツを設定します。
1. テキストスタイルを適用します。
1. 配置を設定します。
1. 設定済みのアーティファクトを返します。

```python
from os import path
import aspose.pdf as ap
import sys

def _create_text_artifact(artifact_class, text):
    """Create a text artifact (header/footer) with common styling."""
    artifact = artifact_class()
    artifact.text = text
    artifact.text_state.font_size = 14
    artifact.text_state.font = ap.text.FontRepository.find_font("Arial")
    artifact.text_state.foreground_color = ap.Color.navy
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    return artifact

```

## PDF にヘッダーを追加

1. 入力 PDF を開きます。
1. 「サンプルヘッダー」というテキストを含むヘッダーアーティファクトを作成します。
1. 最初のページに追加してください。
1. 更新した PDF を保存します。

```python
from os import path
import aspose.pdf as ap
import sys

def add_header_artifact(infile, outfile):
    """Add a header artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        header = _create_text_artifact(ap.HeaderArtifact, "Sample Header")
        document.pages[1].artifacts.append(header)
        document.save(outfile)
```

## PDF にフッターを追加

1. 入力 PDF を開きます。
1. 「サンプルフッター」というテキストを含むフッターアーティファクトを作成します。
1. 最初のページに追加してください。
1. 出力ファイルを保存します。

```python
from os import path
import aspose.pdf as ap
import sys

def add_footer_artifact(infile, outfile):
    """Add a footer artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        footer = _create_text_artifact(ap.FooterArtifact, "Sample Footer")
        document.pages[1].artifacts.append(footer)
        document.save(outfile)
```

## ヘッダーまたはフッターのアーティファクトを削除

1. PDF を開きます。
1. ページネーションヘッダーまたはフッターとしてマークされたアーティファクトを検索します。
1. 最初のページから削除してください。
1. クリーニングした文書を保存します。

```python
from os import path
import aspose.pdf as ap
import sys

def delete_header_footer_artifact(infile, outfile):
    with ap.Document(infile) as document:
        header_footers = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and (
                artifact.subtype == ap.Artifact.ArtifactSubtype.HEADER
                or artifact.subtype == ap.Artifact.ArtifactSubtype.FOOTER
            )
        ]

        for art in header_footers:
            document.pages[1].artifacts.delete(art)

        document.save(outfile)
```

## アーティファクトの関連トピック

- [Python で PDF アーティファクトを操作する](/pdf/ja/python-net/artifacts/)
- [Python で PDF 背景を追加する方法](/pdf/ja/python-net/add-backgrounds/)
- [Python でベイツ番号を PDF に追加する方法](/pdf/ja/python-net/add-bates-numbering/)
- [PDF ファイル内のアーティファクトタイプを数える](/pdf/ja/python-net/counting-artifacts/)