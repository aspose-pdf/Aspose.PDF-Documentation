---
title: Java で PDF グラフのシェイプ バウンダリをチェックする
linktitle: シェイプ バウンダリをチェックする
type: docs
weight: 70
url: /ja/java/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Java で PDF グラフ コレクションのシェイプ バウンダリを検証する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java を使用して PDF ファイル内のグラフ シェイプ バウンダリを検証する
Abstract: この記事では、Aspose.PDF for Java を使用してグラフ コレクションのシェイプ バウンダリを検証する方法を示します。厳格なバウンダリチェックの有効化、範囲外シェイプの追加の試行、そして例外が発生した場合でもドキュメントを保存し続ける方法について説明します。
---
使用 `BoundsCheckMode` シェイプがグラフコンテナ内に収まることを保証する必要があるとき。

## グラフ形状の境界の検証

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. 追加する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ドキュメントに。
1. 作成 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナを作成し、ページに追加してください。
1. 作成する [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) シェイプを作成し、ジオメトリを設定してください。
1. 厳密な境界チェックを有効にし、シェイプをグラフコレクションに追加しようとします `BoundsCheckMode`。
1. シェイプが収まらない場合の例外を処理します。
1. 出力 PDF を保存します [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void checkShapeBounds(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(100.0, 100.0);
        graph.setTop(10);
        graph.setLeft(15);
        graph.setBorder(new BorderInfo(BorderSide.Box, 1, Color.getBlack()));
        page.getParagraphs().add(graph);

        Rectangle rectangle = new Rectangle(-1, 0, 50, 50);
        rectangle.getGraphInfo().setFillColor(Color.getTomato());
        try {
            graph.getShapes().updateBoundsCheckMode(BoundsCheckMode.ThrowExceptionIfDoesNotFit);
            graph.getShapes().addItem(rectangle);
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }

        document.save(outputFile.toString());
    }
}
```
