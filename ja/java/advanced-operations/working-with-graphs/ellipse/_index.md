---
title: "Java での PDFに楕円形の追加"
linktitle: "楕円形の追加"
type: docs
weight: 60
url: /ja/java/add-ellipse/
description: JavaでPDFファイルに楕円形を描画、塗りつぶし、ラベル付けする方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaを使用してPDFファイルに楕円形を描画する
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントに楕円形を追加する方法を示します。輪郭付き楕円、塗りつぶし楕円、および楕円形の内部にテキストフラグメントを配置する方法をカバーしています。
---
## 楕円形の輪郭の追加

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. 追加する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ドキュメントへ。
1. 作成する [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナを作成し、ページに追加してください。
1. 作成 [Ellipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) 形状を作成し、そのジオメトリを構成してください。
1. 追加 [Ellipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) へ [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナ。
1. 例で必要なシェイプ プロパティを設定し、以下を含みます [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) と [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/)。
1. 出力 PDF を保存する [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void addEllipse(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Ellipse ellipse1 = new Ellipse(150, 100, 120, 60);
        ellipse1.getGraphInfo().setColor(Color.getGreenYellow());
        ellipse1.setText(new TextFragment("Ellipse"));
        graph.getShapes().addItem(ellipse1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```

完全な例では、同じグラフに 2 つの異なるアウトライン楕円を追加します。

## 塗りつぶし楕円の追加

`createEllipseFilled` 二つの省略記号を埋める `Color.getGreenYellow()` と `Color.getDarkRed()`.

## 楕円の内部にテキストの追加

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. 追加する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ドキュメントへ。
1. [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) を作成し、必要なテキスト書式設定オプションを設定してください。
1. 作成する [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナを作成し、ページに追加してください。
1. 作成 [Ellipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) 形状を作成し、そのジオメトリを構成してください。
1. 追加 [Ellipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) へ [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナ。
1. 出力 PDF を保存する [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void addTextInsideEllipse(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        TextFragment textFragment = new TextFragment("Ellipse");
        textFragment.getTextState().setFont(FontRepository.findFont("Helvetica"));
        textFragment.getTextState().setFontSize(24);

        Ellipse ellipse1 = new Ellipse(100, 100, 120, 180);
        ellipse1.getGraphInfo().setFillColor(Color.getGreenYellow());
        ellipse1.setText(textFragment);
        graph.getShapes().addItem(ellipse1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
