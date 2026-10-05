---
title: "Java での PDF への円形シェイプの追加"
linktitle: "円の追加"
type: docs
weight: 20
url: /ja/java/add-circle/
description: "Java で PDF ファイルに円形シェイプを描画し、塗りつぶす方法を学びます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用して PDF ファイルに円形シェイプの描画"
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントに円形シェイプを追加する方法を示します。円の輪郭の描画、円の色塗り、円形シェイプ内へのテキスト配置について説明します。
---
## 円の輪郭の追加

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. ドキュメントに [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を追加してください。
1. [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナを作成し、ページに追加してください。
1. [Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) シェイプを作成し、ジオメトリを構成してください。
1. [Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) を [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナに追加してください。
1. 例で必要な形状プロパティを設定し、[Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) を含めてください。
1. 出力 PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) として保存してください。

```java
public static void addCircle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Circle circle = new Circle(100, 100, 40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(circle);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```

## テキスト付きの塗りつぶした円の追加

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. ドキュメントに [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を追加してください。
1. [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナを作成し、ページに追加してください。
1. [Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) シェイプを作成し、ジオメトリを構成してください。
1. [Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) を [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナに追加してください。
1. 例で必要な形状プロパティを設定し、[Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) と [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) を含めてください。
1. 出力 PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) として保存してください。

```java
public static void addCircleFilled(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Circle circle = new Circle(100, 100, 40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());
        circle.getGraphInfo().setFillColor(Color.getGreen());
        circle.setText(new TextFragment("Circle"));
        graph.getShapes().addItem(circle);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
