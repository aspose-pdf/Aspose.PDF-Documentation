---
title: "Java での PDF に透かしの追加"
linktitle: 透かしの追加
type: docs
weight: 30
url: /ja/java/add-watermarks/
description: Aspose.PDF for Java を使用して、PDF ファイル内の透かしアーティファクトを追加、抽出、削除する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java を使用して PDF に透かしを追加する方法
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントにウォーターマーク アーティファクトを追加、検査、削除する方法について説明します。テキストウォーターマークの配置、回転、不透明度、背景設定の作成、ページ上のウォーターマーク アーティファクトの検査、および削除についてカバーしています。
---
ウォーターマーク アーティファクトを使用すると、ページ上に永続的な視覚的マーキングを配置できますが、これらはメインドキュメントのコンテンツに混ざりません。

## PDF からウォーターマーク アーティファクトの抽出

既存のウォーターマーク アーティファクトを検査し、そのテキストまたは位置を読み取る必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 対象ページのアーティファクトコレクションを反復処理してください。
1. 透かしページネーションアーティファクトをフィルタリングし、テキストと矩形を印刷する。

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

## ウォーターマーク アーティファクトの追加

ページにカスタム回転、透過性、背景配置で中央揃えのテキスト透かしを表示する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [WatermarkArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkartifact/) を作成し、そのテキスト状態と配置設定を構成してください。
1. ページに透かしを追加し、出力ファイルを保存してください。

```java
public static void addWatermarkArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextState textState = new TextState();
        textState.setFontSize(72);
        textState.setForegroundColor(Color.getBlueViolet());
        textState.setFontStyle(FontStyles.Bold);
        textState.setFont(FontRepository.findFont("Arial"));

        WatermarkArtifact watermark = new WatermarkArtifact();
        watermark.setTextAndState("WATERMARK", textState);
        watermark.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
        watermark.setArtifactVerticalAlignment(VerticalAlignment.Center);
        watermark.setRotation(60);
        watermark.setOpacity(0.2);
        watermark.setBackground(true);

        document.getPages().get_Item(1).getArtifacts().add(watermark);
        document.save(outputFile.toString());
    }
}
```

## 透かしアーティファクトの削除

ページ上の既存の透かしアーティファクトを削除する必要がある場合は、このアプローチを使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ページのアーティファクトコレクションを逆順に反復してください。
1. サブタイプが透かしであるページネーションアーティファクトを削除し、ドキュメントを保存してください。

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
