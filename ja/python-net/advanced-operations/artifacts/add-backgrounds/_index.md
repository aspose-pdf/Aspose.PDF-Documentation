---
title: Python で PDF 背景を追加する方法
linktitle: 背景の追加
type: docs
weight: 20
url: /ja/python-net/add-backgrounds/
description: .NET 経由で Aspose.PDF for Python の BackgroundArtifact クラスを使用して、Python で PDF ページに背景画像を追加する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使って PDF に背景を追加する方法
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントで背景画像を使用する方法について説明します。ここでは、背景画像を個々のページオブジェクトに組み込むことができる `BackgroundArtifact` クラスを利用して、文書に透かしや微妙なデザインを追加できることを強調しています。この記事では、この機能の実装方法を示す実用的なコード例を紹介します。このプロセスには、新しい PDF ドキュメントの作成、ページの追加、「BackgroundArtifact」オブジェクトの作成、背景画像の設定、ページのアーティファクトコレクションへの背景アーティファクトの追加が含まれます。最後に、変更された文書は PDF ファイルとして保存されます。この手法により、PDF 文書の視覚的表示が強化されます。
---

## PDF への背景画像の追加

背景画像を使用して、透かしやその他の微妙なデザインを文書に追加できます。.NET 経由の Aspose.PDF for Python では、各 PDF ドキュメントはページの集まりであり、各ページにはアーティファクトのコレクションが含まれています。は [背景アーティファクト](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/) クラスを使用して、ページオブジェクトに背景画像を追加できます。

この方法は、装飾画像を検索可能な文書テキストに変換せずにメインのPDFコンテンツの背後に配置する必要がある場合に便利です。

次のコードスニペットは、Python で BackgroundArtifact オブジェクトを使用して PDF ページに背景画像を追加する方法を示しています。

1. PDF ドキュメントをロードします。
1. 背景アーティファクトを作成します。
1. 画像ファイルをロードします。
1. アーティファクトをページに添付します。
1. 更新した文書を保存します。

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_image_to_pdf(infile, imagefile, outfile):
    """Add a background image to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## 不透明度のある背景画像を PDF に追加

Aspose.PDF for Python を使用して、半透明の背景イメージを PDF ページに追加します。

不透明度を適用すると、背景画像が部分的に透明になり、元のページコンテンツ（テキスト、画像など）がはっきりと見えるようになります。これは特に以下の場合に役立ちます。

- ウォーターマーク
- ブランディングオーバーレイ
- 微妙なデザインの強化

背景はアーティファクトとして追加され、すべてのページコンテンツの背後に残ります。

1. PDF ドキュメントをロードします。
1. 背景アーティファクトを作成します。
1. 画像ファイルをロードします。
1. 不透明度を設定します。
1. アーティファクトをページに添付します。
1. 更新した文書を保存します。

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_image_with_opacity_to_pdf(infile, imagefile, outfile):
    """Add a background image with opacity to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        artifact.opacity = 0.5
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## PDF への背景色の追加

Aspose.PDF for Python を使用して PDF ページに単色の背景色を適用します。

1. PDF ドキュメントをロードします。
1. 背景アーティファクトを作成します。
1. 背景色を設定します。
1. アーティファクトをページに添付します。
1. 更新した文書を保存します。

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_color_to_pdf(infile, outfile):
    """Add a solid color background to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_color = ap.Color.dark_khaki
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## PDF から背景を削除

Aspose.PDF for Python を使用して PDF ページからバックグラウンドアーティファクトを削除します。
PDF の背景はアーティファクトとして保存されることが多く、この方法では背景要素として分類されたアーティファクトのみを選択的に識別して削除します。

1. PDF ドキュメントをロードします。
1. ページアーティファクトにアクセスします。
1. バックグラウンドアーティファクトをフィルタリングします。
1. 背景要素を集める。
1. 背景のアーティファクトを削除します。
1. 更新した文書を保存します。

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def remove_background(infile, outfile):
    with ap.Document(infile) as document:
        backgrounds = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.BACKGROUND
        ]

        for background in backgrounds:
            document.pages[1].artifacts.delete(background)

        document.save(outfile)
```

## アーティファクトの関連トピック

- [Python で PDF アーティファクトを操作する](/pdf/ja/python-net/artifacts/)
- [Python で PDF にウォーターマークを追加する方法](/pdf/ja/python-net/add-watermarks/)
- [Python でベイツ番号を PDF に追加する方法](/pdf/ja/python-net/add-bates-numbering/)
- [PDF ファイル内のアーティファクトタイプを数える](/pdf/ja/python-net/counting-artifacts/)