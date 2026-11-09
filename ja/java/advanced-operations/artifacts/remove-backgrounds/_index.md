---
title: Java で PDF の背景を削除する
linktitle: 背景を削除する
type: docs
weight: 80
url: /ja/java/remove-backgrounds/
description: Java で PDF の最初のページから背景アーティファクトを削除する。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java で背景を削除する
Abstract: Java で PDF の最初のページから背景アーティファクトを削除する。
---
Java で PDF の最初のページから背景アーティファクトを削除する。

## 背景アーティファクトを削除する

ページから既存の背景アーティファクトを削除する必要がある場合に、この方法を使用してください。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) で元の PDF を開いてください。
1. ページアーティファクトコレクションを逆順に反復処理してください。
1. タイプが pagination でサブタイプが background のアーティファクトを削除し、ドキュメントを保存してください。

```java
public static void removeBackground(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Background) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## 関連トピック

- [背景を追加する](/pdf/ja/java/add-backgrounds/)
- [JavaでPDFアーティファクトを扱う](/pdf/ja/java/artifacts/)
