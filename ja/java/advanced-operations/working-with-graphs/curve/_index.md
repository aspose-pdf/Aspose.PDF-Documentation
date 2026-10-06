---
title: "Java での PDF への曲線シェイプの追加"
linktitle: "曲線の追加"
type: docs
weight: 30
url: /ja/java/add-curve/
description: "Java で PDF ファイルに曲線シェイプを描画および塗りつぶす方法を学習します。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用した PDF ファイルへの曲線シェイプの描画"
Abstract: "この記事では、Aspose.PDF for Java を使用して PDF ドキュメントに曲線シェイプを追加する方法を説明します。座標配列から曲線を作成し、Graph コンテナ内でストロークカラーまたは塗りつぶしカラーを適用する方法をカバーしています。"
---
Aspose.PDF for Java の曲線は、float 型の座標配列を `Curve` コンストラクタに渡すことで定義されます。

## 曲線のアウトラインの追加

1. 新しい PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) として作成してください。
1. ドキュメントに [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を追加してください。
1. [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナを作成し、ページに追加してください。
1. [Curve](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) シェイプを作成し、その制御ポイントを設定してください。
1. [Curve](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) を [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナに追加してください。
1. 例で必要とされるシェイプ プロパティを設定し、[Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) を含めてください。
1. 出力 PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) に保存してください。

```java
public static void addCurve(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Curve curve1 = new Curve(new float[]{10, 10, 50, 60, 70, 10, 100, 120});
        curve1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(curve1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
