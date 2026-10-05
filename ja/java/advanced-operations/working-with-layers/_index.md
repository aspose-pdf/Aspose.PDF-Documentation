---
title: "Java を使用した PDF レイヤーの操作"
linktitle: "PDF レイヤーの操作"
type: docs
weight: 50
url: /ja/java/working-with-pdf-layers/
description: Java で PDF レイヤーを追加、ロック、抽出、フラット化、マージする方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java で PDF レイヤーを管理する
Abstract: この記事では、Aspose.PDF for Java を使用して、Optional Content Groups とも呼ばれる PDF レイヤーを操作する方法を説明します。ページにレイヤーを追加する方法、既存のレイヤーをロックする方法、レイヤーのコンテンツをファイルやストリームに抽出する方法、レイヤー化されたコンテンツをフラット化する方法、そしてレイヤーを 1 つにマージする方法を学びます。
---
Aspose.PDF for Java は PDF レイヤーを介して公開します `Layer` 各ページの API。オプション コンテンツ グループを作成し、その動作を変更し、必要に応じてコンテンツをエクスポートまたはフラット化できます。

## PDFページへのレイヤーの追加

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. 追加する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ドキュメントに。
1. 必要なものを作成し構成する [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) ページ上のオブジェクト。
1. 出力 PDF を保存する [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

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

## レイヤーをロックする

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ターゲットにアクセスする [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) そしてそれを取得する [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) コレクション。
1. ターゲットをロックする [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/).
1. 更新された PDF を保存する [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

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
