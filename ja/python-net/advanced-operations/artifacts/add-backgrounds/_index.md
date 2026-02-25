---
title: Pythonでアーティファクトとして背景を扱う
linktitle: 背景の追加
type: docs
weight: 20
url: /ja/python-net/add-backgrounds/
description: PythonでPDFファイルに背景画像を追加します。BackgroundArtifact クラスを使用します。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PythonでPDFに背景を追加する方法
Abstract: この記事では、Aspose.PDF for Python via .NET を使用した PDF 文書への背景画像の使用について説明します。`BackgroundArtifact` クラスを利用して、背景画像を個々のページオブジェクトに組み込むことで、透かしや控えめなデザインを文書に追加できることを強調しています。実用的なコード例を提供し、この機能の実装方法を示します。手順は、新しい PDF ドキュメントを作成し、ページを追加し、`BackgroundArtifact` オブジェクトを作成し、背景画像を設定し、ページのアーティファクトコレクションに背景アーティファクトを追加するというものです。最後に、変更された文書を PDF ファイルとして保存します。この手法により、PDF 文書の視覚的プレゼンテーションが向上します。
---

背景画像は、文書に透かしやその他の控えめなデザインを加えるために使用できます。Aspose.PDF for Python via .NET では、各 PDF 文書はページのコレクションで構成され、各ページはアーティファクトのコレクションを含みます。[BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/) クラスを使用して、ページオブジェクトに背景画像を追加できます。

以下のコードスニペットは、Python で BackgroundArtifact オブジェクトを使用して PDF ページに背景画像を追加する方法を示しています。

```python

import aspose.pdf as ap
import io

def add_background_image(input_image_file, output_pdf):
    # Create a new PDF document
    document = ap.Document()

    # Add a blank page to the document
    page = document.pages.add()

    # Create a BackgroundArtifact object
    background = ap.BackgroundArtifact()

    # Load the image as a binary stream
    with open(input_image_file, "rb") as image_stream:
        background.background_image = image_stream

        # Add the background artifact to the page
        page.artifacts.append(background)

    # Save the resulting PDF
    document.save(output_pdf)
```


