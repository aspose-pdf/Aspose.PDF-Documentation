---
title: JavaでPDFアーティファクトをカウントする
linktitle: アーティファクトのカウント
type: docs
weight: 40
url: /ja/java/counting-artifacts/
description: Java と Aspose.PDF を使用して PDF ドキュメントのページネーション アーティファクトを検査およびカウントする方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java を使用した PDF のアーティファクトのカウント
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントのページネーション アーティファクトを検査およびカウントする方法を説明します。ページ アーティファクトを反復処理し、透かし、背景、ヘッダー、フッターのサブタイプをカウントする方法を示します。
---
## ページ上のページネーション アーティファクトをカウントする

ページ上の主要なページングアーティファクトサブタイプのクイックカウントが必要なときにこの例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 読み取る [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) ターゲットからのコレクション [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. ページを反復処理する [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) コレクションを取得し、必要な各ページングサブタイプをカウントしてください。

```java
public static void countPdfArtifacts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int watermarks = 0;
        int backgrounds = 0;
        int headers = 0;
        int footers = 0;

        for (Artifact artifact : document.getPages().get_Item(1).getArtifacts()) {
            if (artifact.getType() == Artifact.ArtifactType.Pagination) {
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                    watermarks++;
                }
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Background) {
                    backgrounds++;
                }
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Header) {
                    headers++;
                }
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Footer) {
                    footers++;
                }
            }
        }

        System.out.println("Watermarks: " + watermarks);
        System.out.println("Backgrounds: " + backgrounds);
        System.out.println("Headers: " + headers);
        System.out.println("Footers: " + footers);
    }
}
```
