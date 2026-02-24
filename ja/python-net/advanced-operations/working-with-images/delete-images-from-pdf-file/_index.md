---
title: Python を使用して PDF ファイルから画像を削除する
linktitle: 画像を削除
type: docs
weight: 20
url: /ja/python-net/delete-images-from-pdf-file/
description: このセクションでは、Aspose.PDF for Python via .NET を使用して PDF ファイルから画像を削除する方法を説明します。
lastmod: "2025-09-27"
TechArticle: true
AlternativeHeadline: Python を使用して PDF から画像を削除する方法
Abstract: この記事では、プライバシー保護や機密情報への不正アクセス防止、共有や保存を容易にするためのファイルサイズ削減、圧縮やテキスト抽出のためのドキュメント準備など、PDF ファイルから画像を削除するさまざまな理由について説明します。**Aspose.PDF for Python via .NET** をこのタスクを実行するツールとして紹介します。この記事では、Aspose.PDF を使用して PDF ファイルから特定の画像またはすべての画像を削除するためのステップバイステップの手順とコードスニペットを提供します。プロセスは、既存の PDF ドキュメントを開き、画像を個別または一括で削除し、更新されたファイルを保存することを含みます。提供された Python コードは、ドキュメントのリソースにアクセスし、目的のページを変更することで画像を削除する方法を示しています。
---

PDF からすべてまたは特定の画像を削除する理由は多数あります。
場合によっては、PDF ファイルに重要な画像が含まれており、プライバシーを保護したり特定の情報への不正アクセスを防止するために削除する必要があります。

不要または冗長な画像を削除すると、ファイルサイズの削減につながり、PDF の共有や保存が容易になります。
必要に応じて、文書からすべての画像を削除することでページ数を減らすことができます。
また、文書から画像を削除することで、PDF の圧縮やテキスト情報の抽出の準備が整います。

**Aspose.PDF for Python via .NET** がこのタスクを支援します。

## PDF ファイルから画像を削除する

PDF ファイルから画像を削除するには：

1. 既存の PDF ドキュメントを開く。
1. 特定の画像を削除する。
1. 更新された PDF ファイルを保存する。

以下のコードスニペットは、PDF ファイルから画像を削除する方法を示しています。

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    document = ap.Document(path_infile)
    document.pages[1].resources.images.delete(1)
    document.save(path_outfile)
```
