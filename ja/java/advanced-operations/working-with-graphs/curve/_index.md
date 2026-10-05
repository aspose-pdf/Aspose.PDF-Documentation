---
title: "Java での PDFに曲線シェイプの追加"
linktitle: "曲線の追加"
type: docs
weight: 30
url: /ja/java/add-curve/
description: JavaでPDFファイルに曲線シェイプを描画および塗りつぶす方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaを使用してPDFファイルに曲線シェイプを描画する
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントに曲線シェイプを追加する方法を示します。座標配列から曲線を作成し、Graph コンテナ内でストロークカラーまたは塗りつぶしカラーを適用する方法をカバーしています。
---
Aspose.PDF for Java の曲線は、float 座標配列を渡すことで定義されます `Curve`.

## 曲線のアウトラインの追加

1. 新しいPDFを作成 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 追加 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 文書に。
1. 作成する [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナを作成し、ページに追加してください。
1. 作成する [Curve](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) シェイプとその制御ポイントを設定してください。
1. 追加する [Curve](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) へ [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナ。
1. 例で必要とされるシェイプ プロパティを設定し、次を含めます [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/)。
1. 出力 PDF を保存する [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

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
