---
title: PythonでPDFの背景を追加する
linktitle: 背景を追加する
type: docs
weight: 20
url: /ja/python-net/add-backgrounds/
description: PythonでPDFページに画像や単色の背景を追加し、背景画像の不透明度を調整します。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pythonを使用してPDFに背景を追加する
Abstract: PythonでPDFページに画像や単色の背景を追加し、背景画像の不透明度を調整します。
---

使用 `BackgroundArtifact` PDFページのコンテンツの背後に画像または単色を配置するため。これらの例は最初のページを変更します。

## PDF に背景画像を追加する

画像ストリームを `background_image` に設定し、アーティファクトをページに追加してください。

```python
from io import FileIO
import aspose.pdf as ap

def add_background_image_to_pdf(infile, imagefile, outfile, opacity=1.0):
    """Add a background image to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        artifact.opacity = opacity
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## PDF に不透明度を指定した背景画像を追加する

同じ関数に 0～1 の不透明度を渡してください。半透明の画像にするには `0.5` を指定します。

```python
add_background_image_to_pdf("input.pdf", "background.png", "output.pdf", opacity=0.5)
```

## PDF に背景色を追加する

背景を単色にするには、アーティファクトの `background_color` を設定してください。

```python
import aspose.pdf as ap

def add_background_color_to_pdf(infile, outfile):
    """Add a solid color background to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_color = ap.Color.dark_khaki
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## 関連トピック

- [背景を削除](/pdf/ja/python-net/remove-backgrounds/)
- [PythonでPDFアーティファクトを操作する](/pdf/ja/python-net/artifacts/)
