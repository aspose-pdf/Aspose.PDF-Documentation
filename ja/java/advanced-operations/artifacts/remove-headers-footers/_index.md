---
title: JavaでPDFのヘッダーとフッターを削除する
linktitle: ヘッダーとフッターを削除する
type: docs
weight: 110
url: /ja/java/remove-headers-footers/
description: JavaでPDFの最初のページからヘッダーとフッターのアーティファクトを削除する。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaでヘッダーとフッターを削除する
Abstract: JavaでPDFの最初のページからヘッダーとフッターのアーティファクトを削除する。
---
JavaでPDFの最初のページからヘッダーとフッターのアーティファクトを削除する。

## ヘッダーとフッターのアーティファクトを削除する

ページから既存のヘッダーとフッターのアーティファクトを削除する必要がある場合に、このアプローチを使用してください。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) で元の PDF を開いてください。
1. ページ アーティファクト コレクションを逆順に反復処理してください。
1. サブタイプがヘッダーまたはフッターであるページネーション アーティファクトを削除し、ドキュメントを保存してください。

```java
public static void deleteHeaderFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && (artifact.getSubtype() == Artifact.ArtifactSubtype.Header
                    || artifact.getSubtype() == Artifact.ArtifactSubtype.Footer)) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## 関連トピック

- [ヘッダーとフッターを追加](/pdf/ja/java/artifacts-header-footer/)
- [JavaでPDFアーティファクトを扱う](/pdf/ja/java/artifacts/)
