---
title: JavaでPDFに透かしを追加する
linktitle: 透かしを追加する
type: docs
weight: 30
url: /ja/java/add-watermarks/
description: JavaでPDFページにスタイル付きテキスト透かしアーティファクトを追加する。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaで透かしを追加する
Abstract: JavaでPDFページにスタイル付きテキスト透かしアーティファクトを追加する。
---
透かしアーティファクトを使用すると、ページ上に永続的な視覚的マークを配置できますが、メインドキュメントのコンテンツに混ざることはありません。

## 透かしアーティファクトを追加する

ページにカスタム回転、透明度、背景配置を持つ中央揃えのテキスト透かしが表示される場合は、この例を使用してください。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) で元の PDF を開いてください。
1. [WatermarkArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkartifact/) オブジェクトを作成し、テキストのスタイルと配置を設定してください。
1. ページにウォーターマークを追加し、出力ファイルを保存してください。

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

## 関連トピック

- [ウォーターマークの詳細を抽出](/pdf/ja/java/extract-watermarks/)
- [ウォーターマークを削除](/pdf/ja/java/remove-watermarks/)
- [JavaでPDFアーティファクトを扱う](/pdf/ja/java/artifacts/)
