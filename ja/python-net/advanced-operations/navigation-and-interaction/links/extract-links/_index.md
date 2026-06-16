---
title: Python で PDF リンクを抽出
linktitle: リンクを抽出
type: docs
weight: 30
url: /ja/python-net/extract-links/
description: Python で PDF 文書からリンク注釈とハイパーリンクを抽出する方法を学びます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF からリンクを抽出する方法
Abstract: リンクの抽出に関する Aspose.PDF for Python via .NET ガイドでは、Python を使用して PDF ドキュメントからハイパーリンク注釈をプログラム的に取得する方法について説明しています。このドキュメントには実用的なコード例が含まれており、リンク監査、ナビゲーション分析、インタラクティブなドキュメント機能の構築などのタスクにこの機能をどのように使用できるかが強調されています。単一ページの PDF を扱う場合でも、大量のバッチを処理する場合でも、このガイドでは、ハイパーリンクを抽出するための明確で効率的な方法を紹介します。
---

## PDF ファイルからリンクを抽出

この例は、Aspose.PDF for Python を使用して PDF の最初のページのすべてのリンク注釈を繰り返し処理する方法を示しています。注釈をフィルタリングして LinkNotation 型の注釈を識別し、安全にキャストしてから、ページインデックスとページ上の長方形の位置を出力します。

これは、PDF 内の既存のリンク注釈のデバッグ、分析、または自動更新に使用できます。

1. PDF ドキュメントをロードします。AP.Document (パス_infile) を使用してファイルを開きます。
1. 最初のページから注釈にアクセスします。すべてのアノテーションを取得するには document.pages [1] .annotations を使用してください。
1. リンク注釈タイプのみのフィルタ。各アノテーションの annotation_type を確認してください。
1. リンクアノテーションをキャストして処理します。is_assignable () と cast () を使用して、LinkAnnotation プロパティに安全にアクセスできるようにしてください。
1. 注釈の詳細を印刷します。各リンクのページインデックスと四角形 (位置) を出力します。

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def extract_link_annotation(infile):

    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        if is_assignable(la, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, la)
            print(f"Page: {annotation.page_index}, location: {annotation.rect}")
```

## PDF ファイルからハイパーリンクを抽出

このコードは、Aspose.PDF for Python を使用して PDF ドキュメントの最初のページからすべての LinkAnnotation オブジェクトを抽出し、GoTouriAction を含むオブジェクトを識別する方法を示しています。このようなリンクごとに、ページインデックスとターゲット URI が出力されます。

これは次のようなタスクに役立ちます。

- PDF 内の外部リンクの監査
- ドキュメントまたはサポート URL の抽出
- 壊れたハイパーリンクや古いハイパーリンクの検出

1. PDF ドキュメントをロードします。AP.Document を使用してファイルを開きます。
1. 最初のページからすべてのリンク注釈を取得します。アノテーションをフィルタリングして、AnnotationType.Link タイプのアノテーションのみが含まれるようにします。
1. タイプチェックを行い、LinkNotationにキャストします。プロパティにアクセスする前に、各アノテーションが本当に LinkNotation であることを確認してください。
1. リンクのアクションタイプを確認してください。GoTouriAction を使用するリンク (つまり、ウェブ URL へのリンク) をフィルタリングします。
1. URI とページインデックスを抽出して印刷します。.uri を使用して外部リンクを取得し、.page_index を使用してコンテキストを取得します。

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def extract_hyperlinks(infile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        if is_assignable(la, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, la)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                action = cast(ap.annotations.GoToURIAction, annotation.action)
                print(f"Page {annotation.page_index}, URI:{action.uri}")
```

## 関連リンクトピックス

- [Python で PDF リンクを操作する](/pdf/ja/python-net/links/)
- [Python で PDF リンクを作成](/pdf/ja/python-net/create-links/)
- [Python を使用して PDF 内のリンクを更新する](/pdf/ja/python-net/update-links/)