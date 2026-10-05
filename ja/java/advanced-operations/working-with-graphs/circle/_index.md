---
title: "Java での PDFに円形シェイプの追加"
linktitle: "円の追加"
type: docs
weight: 20
url: /ja/java/add-circle/
description: JavaでPDFファイルに円形シェイプを描画および塗りつぶす方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaを使用してPDFファイルに円形シェイプを描画する
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントに円形シェイプを追加する方法を示します。円の輪郭の描画、円の色塗り、円形シェイプ内へのテキスト配置について説明します。
---
## 円の輪郭の追加

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. 追加 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ドキュメントへ。
1. 作成 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナを作成し、ページに追加してください。
1. 作成する [Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) シェイプを作成し、ジオメトリを構成してください。
1. 追加する [Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) へ [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナ。
1. 例で必要な形状プロパティを設定し、以下を含みます [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/)。
1. 出力PDFを保存する [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

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
1. 追加 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ドキュメントへ。
1. 作成 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナを作成し、ページに追加してください。
1. 作成する [Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) シェイプを作成し、ジオメトリを構成してください。
1. 追加する [Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) へ [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナ。
1. 例で必要な形状プロパティを設定し、以下を含みます [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) と [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/)。
1. 出力PDFを保存する [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

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
