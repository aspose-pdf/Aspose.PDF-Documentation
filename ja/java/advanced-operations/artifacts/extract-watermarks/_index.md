---
title: JavaでPDFの透かし詳細を抽出する
linktitle: 透かし詳細を抽出する
type: docs
weight: 50
url: /ja/java/extract-watermarks/
description: JavaでPDFの最初のページにある透かしアーティファクトのテキストと境界矩形を読み取ります。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaで透かし詳細を抽出する
Abstract: JavaでPDFの最初のページにある透かしアーティファクトのテキストと境界矩形を読み取ります。
---
JavaでPDFの最初のページにある透かしアーティファクトのテキストと境界矩形を読み取ります。

## PDF から透かしアーティファクトを抽出する

既存の透かしアーティファクトを検査し、そのテキストまたは位置を読み取る必要がある場合に、この例をご使用ください。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) で元の PDF を開いてください。
1. 対象ページのアーティファクト コレクションを反復処理してください。
1. 透かしページ番号のアーティファクトをフィルタリングし、そのテキストと矩形を出力してください。

```java
public static void extractWatermarkFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Artifact artifact : document.getPages().get_Item(1).getArtifacts()) {
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                System.out.println(artifact.getText() + " " + artifact.getRectangle());
            }
        }
    }
}
```

## 関連トピック

- [ウォーターマークを追加](/pdf/ja/java/add-watermarks/)
- [ウォーターマークを削除](/pdf/ja/java/remove-watermarks/)
- [JavaでPDFアーティファクトを操作](/pdf/ja/java/artifacts/)
