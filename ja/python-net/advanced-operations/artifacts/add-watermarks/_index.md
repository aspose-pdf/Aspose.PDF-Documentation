---
title: Python を使用して PDF に透かしを追加する
linktitle: 透かしの追加
type: docs
weight: 30
url: /ja/python-net/add-watermarks/
description: この記事では、アーティファクトの操作と、Python をプログラムで使用して PDF に透かしを付ける機能について説明します。
lastmod: "2025-11-21"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF に透かしを追加する方法
Abstract: この記事では、.NET 経由の Aspose.PDF for Python を使用して、アーティファクトの管理を通じて PDF ドキュメントに透かしを追加する方法について説明します。アーティファクトを扱うための主要クラスである `Artifact` と `ArtifactCollection` を紹介し、これらへは `Page` クラスの `Artifacts` プロパティを介してアクセスできることを説明します。`Artifact` クラスのプロパティについて詳述し、`contents`、`form`、`image`、`text`、`rectangle`、`rotation`、`opacity` といった属性により、PDF ファイル内のアーティファクトを包括的に操作できることを示します。さらに、実用的な例として、Python を用いて PDF の最初のページにプログラムで透かしを追加する方法を示します。コードスニペットでは、`WatermarkArtifact` の作成と構成、テキスト、配置、回転、透明度の設定を行い、PDF ドキュメントに追加して変更を保存する手順を示しています。
---

## プログラミングサンプル: PDF ファイルに透かしを追加する方法

Aspose.PDF for Python via .NET を使用して、PDF の [`ドキュメント`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) に透かしアーティファクトを追加します。透かしは、ブランド化、セキュリティ、情報提供などの目的でページに適用される視覚的なオーバーレイです。この例では、[`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) の外観を設定し、[`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) と [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/) による位置決め、回転、透明度を構成してから、[`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) に透かしを適用する方法を示しています。

1. 透かしアーティファクトを作成する（[`WatermarkArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/) を参照）。
1. テキストステートを構成する（[`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) を参照）。
1. テキストを透かしにバインドする。
1. [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) と [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/) を使用して位置とスタイルを定義する。
1. ページの [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) コレクションを介して [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) に透かしを付ける（[`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/) を参照）。
1. 更新された [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) を使用して保存する。

```python

import aspose.pdf as ap

def add_watermark(input_pdf, output_pdf):
    # Load the existing PDF document
    document = ap.Document(input_pdf)

    # Create a watermark artifact
    watermark = ap.WatermarkArtifact()

    # Configure text state for the watermark
    text_state = ap.text.TextState()
    text_state.font_size = 72
    text_state.foreground_color = ap.Color.blue
    text_state.font = ap.text.FontRepository.find_font("Courier")

    # Apply text and style to the watermark
    watermark.set_text_and_state("WATERMARK", text_state)

    # Position and style settings
    watermark.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    watermark.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
    watermark.rotation = 45
    watermark.opacity = 0.5
    watermark.is_background = True

    # Add watermark to the first page
    document.pages[1].artifacts.append(watermark)

    # Save the updated PDF
    document.save(output_pdf)
```


