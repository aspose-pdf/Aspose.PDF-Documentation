---
title: PythonでPDFヘッダーとフッターを追加する
linktitle: ヘッダーとフッターを追加する
type: docs
weight: 70
url: /ja/python-net/artifacts-header-footer/
description: PythonでPDFページにスタイルされたヘッダーとフッターのアーティファクトを追加する。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PythonでPDFにヘッダーとフッターを追加する
Abstract: PythonでPDFページにスタイルされたヘッダーとフッターのアーティファクトを追加する。
---

使用する `HeaderArtifact` そして `FooterArtifact` PDFページにランニングテキストを追加します。これらの例は最初のページにアーティファクトを追加します。

## スタイル付きテキストアーティファクトを作成する

追加例を実行する前に、このヘルパー関数を定義してください。この関数は、ヘッダーとフッターに同じフォント、サイズ、色、配置を適用します。

```python
import aspose.pdf as ap

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

## PDF にヘッダーを追加する

ヘルパー関数に `HeaderArtifact` を渡し、返されたアーティファクトをページに追加してください。

```python
import aspose.pdf as ap

def add_header_artifact(infile, outfile):
    """Add a header artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        header = _create_text_artifact(ap.HeaderArtifact, "Sample Header")
        document.pages[1].artifacts.append(header)
        document.save(outfile)
```

## PDF にフッターを追加する

ヘルパー関数に `FooterArtifact` を渡し、返されたアーティファクトをページに追加してください。

```python
import aspose.pdf as ap

def add_footer_artifact(infile, outfile):
    """Add a footer artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        footer = _create_text_artifact(ap.FooterArtifact, "Sample Footer")
        document.pages[1].artifacts.append(footer)
        document.save(outfile)
```

## 関連トピック

- [ヘッダーとフッターを削除する](/pdf/ja/python-net/remove-headers-footers/)
- [PythonでPDFアーティファクトを操作する](/pdf/ja/python-net/artifacts/)
