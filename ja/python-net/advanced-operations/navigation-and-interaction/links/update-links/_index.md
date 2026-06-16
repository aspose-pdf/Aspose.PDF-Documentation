---
title: Python で PDF リンクを更新する方法
linktitle: リンクを更新
type: docs
weight: 20
url: /ja/python-net/update-links/
description: Python で PDF リンクの外観とリンク先を更新する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF のリンクを更新する方法
Abstract: Aspose.PDF for Python via .NET リンクの更新ガイドでは、Python を使用して PDF ドキュメント内のハイパーリンクの動作を変更するプロセスを開発者が順を追って説明しています。特定のページ、外部 Web サイト、または他の PDF ファイルを指すようにリンク先を変更する方法について説明しています。このドキュメントでは、テキストの色を含むリンク注釈の外観を調整する方法についても説明し、各シナリオの実用的なコード例も紹介しています。古い URL を修正する場合でも、ナビゲーションを強化する場合でも、このリソースはリンクをプログラムで管理するための明確で効率的なアプローチを提供します。
---

## リンク注釈のテキスト色を更新

この例は、Aspose.PDF for Python を使用して PDF の最初のページのすべてのリンク注釈を検出し、フォントの色を赤に変更して各リンクの近くのテキストを強調表示する方法を示しています。TextFragmentAbSorber を使用して各リンク四角形の周囲を少し広げて、近くのテキストを検索して変更します。

これは次の用途に使用できます。

- 文書内のリンクを視覚的にマークする
- リンクされたコンテンツを強調することによるアクセシビリティの強化
- レビューまたはエクスポート前の PDF ファイルの前処理

これらのリンク注釈のそれぞれについて、スクリプトは長方形の境界線を取得し、その領域を近くのテキストを含むようにわずかに拡大します。これにより、より広い視覚的識別が可能になります。次に、この拡張された領域に TextFragmentAbSorber を適用して、その領域内にあるテキストフラグメントをすべて抽出します。キャプチャされたこれらの断片は、フォントの色を赤に変更することで修正されます。これにより、周囲のテキストを強調したり確認したりできるようになります。これらの更新をすべて適用すると、変更された文書は出力パスに保存され、強調表示された注釈とそれに関連するテキストは保持されます。

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_text_color(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        ta = ap.text.TextFragmentAbsorber()
        rect = la.rect
        rect.llx -= 2
        rect.lly -= 2
        rect.urx += 2
        rect.ury += 2
        ta.text_search_options = ap.text.TextSearchOptions(rect)
        ta.visit(document.pages[1])
        for textFragment in ta.text_fragments:
            textFragment.text_state.foreground_color = ap.Color.red

    document.save(outfile)
```

## 境界を更新

このスクリプトはドキュメントの最初のページに焦点を当て、すべての注釈を除外してリンクタイプの注釈のみを選択します。これらは通常、ハイパーリンクやナビゲーショントリガーなどのインタラクティブな要素を表します。これらのリンク注釈はそれぞれ LinkAnnotation 型にキャストされ、色プロパティが赤に更新され、他のコンテンツから目立つように視覚的に強調表示されます。すべてのリンク注釈が変更されると、更新された文書は定義済みの出力場所に保存され、新しいスタイルは維持されます。

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_border(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        link_annotation = cast(ap.annotations.LinkAnnotation, la)
        link_annotation.color = ap.Color.red

    document.save(outfile)
```

## Web デスティネーションを更新

パスが設定されると、元のドキュメントが Aspose.PDF ライブラリを使用して読み込まれ、その内容を変更できるようになります。次に、スクリプトは文書の最初のページに焦点を当て、すべての注釈をフィルターで除外し、通常はクリック可能な領域またはハイパーリンクを表すリンクタイプの注釈のみを選択します。タイプミスを防ぎ、安全に処理できるように、各アノテーションは is_assignable でチェックされ、適切な LinkNotation タイプにキャストされます。リンクが GoTouriAction に関連付けられている場合、つまり Web アドレスを指している場合、スクリプトはその URI を更新してユーザーを「」にリダイレクトします。https://www.aspose.com". 最後に、必要な変更がすべて適用された後、変更されたドキュメントは指定された出力パスに保存されます。

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_web_destination(infile, outfile):
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
                action.uri = "https://www.aspose.com"
    document.save(outfile)
```

## 関連リンクトピックス

- [Python で PDF リンクを操作する](/pdf/ja/python-net/links/)
- [Python で PDF リンクを作成](/pdf/ja/python-net/create-links/)
- [Python で PDF リンクを抽出](/pdf/ja/python-net/extract-links/)