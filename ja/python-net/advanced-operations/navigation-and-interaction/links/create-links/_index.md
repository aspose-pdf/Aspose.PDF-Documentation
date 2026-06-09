---
title: Python で PDF リンクを作成
linktitle: リンクを作成
type: docs
weight: 10
url: /ja/python-net/create-links/
description: Python で内部、外部、リモート PDF リンクを作成する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF でリンクを作成する方法
Abstract: リンクの作成に関する Aspose.PDF for Python via .NET ガイドでは、Python を使用して PDF ドキュメントにインタラクティブなハイパーリンクを追加するための実践的な手順を開発者に説明しています。外部アプリケーションを起動したり、同じ文書内の特定のページに移動したり、他の PDF ファイルを開いたりするリンクなど、さまざまな種類のリンクを作成する方法について説明します。このドキュメントでは、LinkAnnotation オブジェクトの使用方法、Rectangle によるクリック可能な領域の定義方法、LaunchAction や GoToRemoteAction などのアクションの割り当て方法について説明しています。このリソースは、わかりやすいコード例とステップバイステップのガイダンスとともに、開発者が Python アプリケーションでの PDF ナビゲーションとインタラクティブ機能を強化するのに役立ちます。
---

## PDF ドキュメント内のリンク

PDF 1.7仕様（ISO 32000-1:2008）によると、**リンクアノテーション**は、アノテーションがアクティブになったときに何が起こるかを定義するいくつかのタイプのアクションをトリガーできます。サポートされている主なアクションは次のとおりです。

1. **GoTo** — 同じ文書内の宛先に移動します。
1. **GoTor** — 別の PDF ファイル内の目的地にジャンプします (リモートアクセス)。
1. **URI** — 統一リソース識別子 (通常は Web リンク) を開きます。
1. **Launch** — アプリケーションを起動するか、ファイルを開きます (プラットフォームによって異なり、セキュリティ上の理由で制限されている場合が多いです)。
1. **名前付き** — 次のページへの移動や文書の印刷など、定義済みのアクションを実行します。
1. **JavaScript** — 埋め込まれた JavaScript コードを実行します (セキュリティ上の懸念から注意して使用してください)。
1. **送信フォーム** — 指定した URL にフォームデータを送信します。
1. **ResetForm** — フォームフィールドをデフォルト値にリセットします。
1. **ImportData ** — 外部ファイルから文書にデータをインポートします。

アプリケーションへのリンクをドキュメントに追加することで、ドキュメントからアプリケーションにリンクできます。これは、たとえばチュートリアルの特定の箇所で読者に特定のアクションを実行させたい場合や、機能豊富なドキュメントを作成する場合に便利です。

「LaunchAction」を使用してアプリケーションリンクを作成するには:

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_launch_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    border = ap.annotations.Border(link)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    link.color = ap.Color.green
    link.action = ap.annotations.LaunchAction(document, "sample.pdf")
    page.annotations.append(link)
    document.save(outfile)
```

## PDF ファイルに PDF ドキュメントリンクを作成

### 「リモートに移動」操作を使用する

このコードスニペットは、Python PDF ライブラリを使用して PDF ドキュメントの特定のページにリンク注釈を追加する方法を示しています。

1. PDF ドキュメントを開く
1. 文書の 2 ページ目を選択 (インデックス 1)
1. リンク注釈の作成:
1. 座標値 (10、580、120、600) で配置されています
1. カラーグリーン
1. 最初のページにある「sample.pdf」へのリンク
1. リンク注釈をページに追加する
1. 変更したドキュメントを出力ファイルパスに保存します

「リモートアクションに移動」を使用して PDF ドキュメントリンクを作成するには:

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_go_to_remote_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    link.color = ap.Color.green
    link.action = ap.annotations.GoToRemoteAction("sample.pdf", 1)
    page.annotations.append(link)
    document.save(outfile)
```

### 「Go To」アクションを使用する

このコードは、Aspose.PDF for Python を使用して PDF ドキュメントの特定のページにリンク注釈を追加する方法を示しています。リンクは緑色の点線の付いた長方形で表示され、ユーザーは同じ PDF 内の別のページに移動できます。「GoToAction」を使用して PDF ドキュメントリンクを作成するには：

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_go_to_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    border = ap.annotations.Border(link)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    link.color = ap.Color.green
    if document.pages.length >= 4:
        link.action = ap.annotations.GoToAction(document.pages[4])
    else:
        link.action = ap.annotations.GoToAction(document.pages[document.pages.length])
    page.annotations.append(link)
    document.save(outfile)
```

### GoTouriアクションの適用

次の例は、Aspose.PDF for Python を使用して PDF ドキュメントにリンクアノテーションを追加する方法を示しています。リンクは最初のページに緑色のクリック可能な領域として表示され、クリックすると、GoTouriAction を使用して Aspose.PDF for Python のドキュメントが Web ブラウザーで開きます。

この機能は、役立つ外部参考資料、ドキュメント、またはサポートリンクをPDF内に直接埋め込むのに便利です。

1. PDF ドキュメントをロードします。AP.Document を使用して既存の PDF ファイルを開きます。
1. 最初のページにアクセスします。document.pages [1] を使用して最初のページにアクセスします (Aspose は 1 から始まるインデックスを使用します)。
1. リンク注釈を作成します。LinkNotation オブジェクトを作成し、ap.Rectangle を使用してクリック可能な四角形領域を指定します。
1. 注釈の外観を設定します。link.color = ap.color.green を使用してアノテーションの色を緑に設定します。
1. URI アクションを割り当てます。GoTouriAction を使用してアノテーションを外部 URL にリンクします。
1. 注釈をページに追加します。設定したリンク注釈を最初のページの注釈コレクションに追加します。
1. 変更した文書を保存します。更新した PDF ドキュメントを指定した出力パスに保存します。

```python
import aspose.pdf as ap
from os import path
import sys
    
def create_link_annotation_go_to_URI_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    link.color = ap.Color.green
    link.action = ap.annotations.GoToURIAction("https://docs.aspose.com/pdf/python")
    page.annotations.append(link)
    document.save(outfile)
```

## 関連リンクトピックス

- [Python で PDF リンクを操作する](/pdf/ja/python-net/links/)
- [Python で PDF からリンクを抽出する方法](/pdf/ja/python-net/extract-links/)
- [Python を使用して PDF 内のリンクを更新する](/pdf/ja/python-net/update-links/)