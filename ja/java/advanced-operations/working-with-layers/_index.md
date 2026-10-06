---
title: "Java を使用した PDF レイヤーの操作"
linktitle: "PDF レイヤーの操作"
type: docs
weight: 50
url: /ja/java/working-with-pdf-layers/
description: Java で PDF レイヤーを追加、ロック、抽出、フラット化、マージする方法を学びます。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF レイヤーの管理"
Abstract: "この記事では、Aspose.PDF for Java を使用して、オプションコンテンツグループ（Optional Content Groups）とも呼ばれる PDF レイヤーを操作する方法を説明します。ページへのレイヤーの追加、既存レイヤーのロック、レイヤーのコンテンツをファイルやストリームへの抽出、レイヤー化されたコンテンツのフラット化、および複数レイヤーの1つへのマージ方法を学びます。"
---
Aspose.PDF for Java は、各ページの `Layer` API を通じて PDF レイヤーを提供します。オプションコンテンツグループを作成し、その動作を変更したり、必要に応じてコンテンツをエクスポートまたはフラット化したりできます。

## PDF ページへのレイヤーの追加

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. ドキュメントに [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を追加してください。
1. ページ上に必要な [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) オブジェクトを作成し、構成してください。
1. 出力 PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) に保存してください。

```java
public static void addLayers(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Layer layer = new Layer("oc1", "Red Line");
        layer.getContents().add(new SetRGBColorStroke(1, 0, 0));
        layer.getContents().add(new MoveTo(500, 700));
        layer.getContents().add(new LineTo(400, 700));
        layer.getContents().add(new Stroke());
        page.getLayers().add(layer);

        document.save(outputFile.toString());
    }
}
```

完全な例では、赤、緑、青の線コンテンツを持つ3つの個別のレイヤーを作成します。

## レイヤーのロック

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ターゲットの [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) にアクセスし、その [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) コレクションを取得してください。
1. ターゲットの [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) をロックしてください。
1. 更新した PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を保存してください。

```java
public static void lockLayer(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        if (!page.getLayers().isEmpty()) {
            Layer layer = page.getLayers().getFirst();
            layer.lock();
            document.save(outputFile.toString());
        }
    }
}
```
