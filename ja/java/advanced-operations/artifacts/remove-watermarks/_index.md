---
title: JavaでPDFの透かしを削除
linktitle: 透かしを削除
type: docs
weight: 90
url: /ja/java/remove-watermarks/
description: JavaでPDFの最初のページから透かしのアーティファクトを削除します。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaで透かしを削除
Abstract: JavaでPDFの最初のページから透かしのアーティファクトを削除します。
---
JavaでPDFの最初のページから透かしのアーティファクトを削除します。

## 透かしのアーティファクトを削除

この例では、最初のページから、タイプが `Pagination` でサブタイプが `Watermark` のアーティファクトだけを削除します。通常のページテキスト、画像、または注釈として保存されている透かしは、PDF に残ります。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) で元の PDF を開いてください。
1. ページアーティファクトコレクションを逆順に反復処理してください。
1. サブタイプがウォーターマークのページネーションアーティファクトを削除し、ドキュメントを保存してください。

```java
public static void deleteWatermarkArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## 関連トピック

- [透かしを追加](/pdf/ja/java/add-watermarks/)
- [透かしの詳細を抽出](/pdf/ja/java/extract-watermarks/)
- [Java で PDF アーティファクトを操作](/pdf/ja/java/artifacts/)
