---
title: Python (.NET 経由)で特定のタイプのアーティファクトをカウントする
linktitle: アーティファクトのカウント
type: docs
weight: 40
url: /ja/python-net/counting-artifacts/
description: この記事では、Aspose.PDF for Python via .NET を使用して PDF ドキュメントのページング アーティファクトを検査する方法を示します。
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用した PDF のアーティファクトのカウント
Abstract: 透かし、背景、ヘッダー、フッターなどのページング アーティファクトは、PDF ドキュメントで構造、ブランディング、識別を提供するために一般的に使用されます。この例では、Aspose.PDF for Python via .NET を使用して、これらのアーティファクトをプログラムで検査しカウントする方法を示します。ページ上のアーティファクトをフィルタリングしサブタイプでグループ化することで、開発者はドキュメントの構成を迅速に分析し、特定の要素の有無を確認できます。提供されたコードは、PDF を開き、最初のページからページング アーティファクトを抽出し、各サブタイプをカウントして結果を出力する方法を示しており、ドキュメントの監査と検証に実用的なアプローチを提供します。
---

## 特定のタイプのアーティファクトのカウント

PDF のページング アーティファクトを検査しカウントするには、[`ドキュメント`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を使用します。ページング アーティファクトは、レイアウトや識別のためにページに適用される透かし、背景、ヘッダー、フッターなどの要素を含みます。[`Artifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) オブジェクトを [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 上でフィルタリングし、サブタイプ（`Artifact.ArtifactSubtype`）でグループ化することで、開発者はドキュメントの構造を迅速に分析し、特定の要素の有無を確認できます。

特定のタイプのアーティファクトの総数（例：透かしの総数）を計算するには、次のコードを使用します。この例では、ページの [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) コレクション（[`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)）を [`Artifact.ArtifactType`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/#properties) でフィルタリングし、サブタイプ（`Artifact.ArtifactSubtype`）をカウントします。

1. PDF ドキュメントを開く（[`ドキュメント`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を参照）。
1. ページの [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) コレクションを使用してページング アーティファクトをフィルタリングする。
1. サブタイプ（`Artifact.ArtifactSubtype`）でアーティファクトをカウントする。
1. 結果を出力する。

```python

import aspose.pdf as ap

def count_pagination_artifacts(path_infile):
    # Open the PDF document
    with ap.Document(path_infile) as document:
        
        # Extract pagination artifacts from the first page
        pagination_artifacts = [
            artifact for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
        ]

        # Count artifacts by subtype
        watermarks = sum(1 for artifact in pagination_artifacts 
                         if artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK)
        backgrounds = sum(1 for artifact in pagination_artifacts 
                          if artifact.subtype == ap.Artifact.ArtifactSubtype.BACKGROUND)
        headers = sum(1 for artifact in pagination_artifacts 
                      if artifact.subtype == ap.Artifact.ArtifactSubtype.HEADER)
        footers = sum(1 for artifact in pagination_artifacts 
                      if artifact.subtype == ap.Artifact.ArtifactSubtype.FOOTER)

        # Display results
        print(f"Watermarks: {watermarks}")
        print(f"Backgrounds: {backgrounds}")
        print(f"Headers: {headers}")
        print(f"Footers: {footers}")
```

