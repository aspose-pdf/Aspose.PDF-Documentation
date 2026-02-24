---
title: PythonでPDFファイルにリンクを作成する
linktitle: リンク作成
type: docs
weight: 10
url: /ja/python-net/create-links/
description: このセクションでは、Pythonを使用してPDFドキュメントにリンクを作成する方法を説明します。
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDFでリンクを作成する方法
Abstract: Python 用 Aspose.PDF for .NET のリンク作成ガイドは、開発者にPythonを使用してPDFドキュメントにインタラクティブなハイパーリンクを追加する実用的な手順を提供します。外部アプリケーションを起動するリンクや、同一文書内の特定ページへ移動するリンク、他のPDFファイルを開くリンクなど、さまざまなタイプのリンクの作成方法をカバーしています。ドキュメントでは、LinkAnnotation オブジェクトの使用方法、Rectangle でクリック領域を定義する方法、LaunchAction や GoToRemoteAction といったアクションの割り当て方法を解説しています。明確なコード例と段階的なガイダンスにより、このリソースは開発者がPythonアプリケーションでPDFのナビゲーションとインタラクティビティを向上させるのに役立ちます。
---

## PDFドキュメントのリンク

PDF 1.7 仕様 (ISO 32000-1:2008) によれば、**Link annotation** は、アノテーションがアクティブになったときに何が起こるかを定義する複数のアクションをトリガーできます。以下はサポートされている主なアクションです：

1. **GoTo** – 同一文書内の目的地へ移動します。
1. **GoToR** – 別のPDFファイル内の目的地へジャンプします（リモートGoTo）。
1. **URI** – 統一リソース識別子を開きます。通常はウェブリンクです。
1. **Launch** – アプリケーションを起動するかファイルを開きます（プラットフォーム依存で、セキュリティ上制限されることが多い）。
1. **Named** – 次のページへ移動や印刷など、事前定義されたアクションを実行します。
1. **JavaScript** – 埋め込まれたJavaScriptコードを実行します（セキュリティ上の懸念から注意して使用）。
1. **SubmitForm** – フォームデータを指定されたURLへ送信します。
1. **ResetForm** – フォームフィールドをデフォルト値にリセットします。
1. **ImportData** – 外部ファイルからデータを文書にインポートします。

文書にアプリケーションへのリンクを追加することで、文書からアプリケーションへリンクできるようになります。たとえば、チュートリアルの特定の箇所で読者に特定の操作をさせたい場合や、機能豊富な文書を作成したい場合に便利です。

「LaunchAction」を使用してアプリケーションリンクを作成するには：

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Open the input PDF document
    document = ap.Document(path_infile)

    # Select the second page (index 1)
    page = document.pages[1]

    # Create a link annotation with specific dimensions and position
    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))

    # Configure the link's border
    border = ap.annotations.Border(link)
    border.width = 5  # Border width of 5 units
    border.dash = ap.annotations.Dash(1, 1)  # Dashed border style

    # Set link appearance
    link.color = ap.Color.green  # Green color for the link

    # Set the action to launch another PDF file
    # Note: Commented out system command demonstrates potential alternative launch actions
    # link.action = ap.annotations.LaunchAction(document, "start %windir%\explorer.exe")
    link.action = ap.annotations.LaunchAction(document, "sample.pdf")

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified document
    document.save(path_outfile)
```

## PDFファイル内にPDFドキュメントリンクを作成する

### GoToRemoteAction の使用

このコードスニペットは、PythonのPDFライブラリを使用してPDFドキュメントの特定ページにリンクアノテーションを追加する方法を示しています。

1. PDFドキュメントを開く
1. 文書の2ページ目（インデックス1）を選択する
1. リンクアノテーションを作成する：
1. 座標 (10, 580, 120, 600) に配置する
1. 緑色にする
1. 'sample.pdf' の最初のページへリンクする
1. ページにリンクアノテーションを追加する
1. 変更された文書を出力ファイルパスに保存する

「GoToRemoteAction」を使用してPDFドキュメントリンクを作成するには：

```python

import aspose.pdf as ap
from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

# Load the input PDF document
document = ap.Document(path_infile)

# Access the first page of the document (Aspose uses 1-based indexing)
page = document.pages[1]

# Create a link annotation in the specified rectangle area on the page
link = ap.annotations.LinkAnnotation(
    page, ap.Rectangle(10, 580, 120, 600, True)  # (left, bottom, right, top, isEmpty)
)

# Set the color of the link annotation to green
link.color = ap.Color.green

# Define a remote action to open "sample.pdf" and navigate to its first page
link.action = ap.annotations.GoToRemoteAction("sample.pdf", 1)

# Add the link annotation to the current page
page.annotations.append(link)

# Save the updated PDF to the specified output path
document.save(path_outfile)
```

### GoToAction の使用

このコードは、Aspose.PDF for Python を使用してPDFドキュメントの特定ページにリンクアノテーションを追加する方法を示します。リンクは緑色の破線枠の矩形として表示され、同一PDF内の別ページへナビゲートできます。「GoToAction」を使用してPDFドキュメントリンクを作成するには：

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Open the PDF document
    document = ap.Document(path_infile)

    # Select the second page (index 1)
    page = document.pages[1]

    # Create a link annotation with specific coordinates
    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))

    # Customize link annotation border
    border = ap.annotations.Border(link)
    border.width = 5  # Border width
    border.dash = ap.annotations.Dash(1, 1)  # Dashed border style

    # Set link color to green
    link.color = ap.Color.green

    # Set link destination
    if document.pages.count >= 4:
        # Link to 4th page if document has 4 or more pages
        link.action = ap.annotations.GoToAction(document.pages[4])
    else:
        # Fallback: link to the last page if less than 4 pages
        link.action = ap.annotations.GoToAction(document.pages[document.pages.count])

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified document
    document.save(path_outfile)
```

### GoToURIAction の適用

次の例は、Aspose.PDF for Python を使用してPDFドキュメントにリンクアノテーションを追加する方法を示します。リンクは1ページ目の緑色のクリック可能領域として表示され、クリックするとGoToURIActionを通じてWebブラウザでAspose.PDF for Python のドキュメントが開きます。

この機能は、役立つ外部参照、ドキュメント、またはサポートリンクをPDF内に直接埋め込む際に便利です。

1. PDFドキュメントをロードする。ap.Document を使用して既存のPDFファイルを開く。
1. 最初のページにアクセスする。document.pages[1] を使用して最初のページにアクセスする（Asposeは1ベースのインデックスを使用）。
1. リンクアノテーションを作成する。LinkAnnotation オブジェクトを作成し、ap.Rectangle を使用してクリック可能な矩形領域を指定する。
1. アノテーションの外観を設定する。link.color = ap.Color.green を使用してアノテーションの色を緑に設定する。
1. URIアクションを割り当てる。GoToURIAction を使用してアノテーションを外部URLにリンクさせる。
1. アノテーションをページに追加する。設定したリンクアノテーションを最初のページのアノテーションコレクションに追加する。
1. 変更されたドキュメントを保存する。更新されたPDFドキュメントを指定された出力パスに保存する。

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Access the first page (Aspose uses 1-based indexing)
    page = document.pages[1]

    # Create a link annotation at the specified rectangle position
    link = ap.annotations.LinkAnnotation(
        page, ap.Rectangle(10, 580, 120, 600, True)  # (left, bottom, right, top, isEmpty)
    )

    # Set the color of the link annotation to green
    link.color = ap.Color.green

    # Define a URI action that navigates to the Aspose.PDF Python documentation
    link.action = ap.annotations.GoToURIAction("https://docs.aspose.com/pdf/python")

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified PDF to the output path
    document.save(path_outfile)
```

