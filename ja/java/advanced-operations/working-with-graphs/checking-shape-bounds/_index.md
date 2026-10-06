---
title: "Java での PDF グラフのシェイプ バウンダリのチェック"
linktitle: "シェイプ バウンダリのチェック"
type: docs
weight: 70
url: /ja/java/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Java で PDF グラフ コレクションのシェイプ バウンダリを検証する方法を学びます。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用して PDF ファイル内のグラフ シェイプ バウンダリの検証"
Abstract: "この記事では、Aspose.PDF for Java を使用してグラフ コレクション内のシェイプの境界を検証する方法を示します。厳格な境界チェックの有効化、範囲外のシェイプを追加しようとする試み、および例外が発生してもドキュメントの保存を継続する方法について説明します。"
---
`BoundsCheckMode` を使用すると、シェイプがグラフ コンテナ内に収まることを保証できます。

## グラフ形状の境界の検証

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. ドキュメントに [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を追加してください。
1. [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) コンテナを作成し、ページに追加してください。
1. [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) シェイプを作成し、ジオメトリを設定してください。
1. 厳密な境界チェックを有効にし、`BoundsCheckMode` を使用してシェイプをグラフ コレクションに追加しようとしてください。
1. シェイプが収まらない場合の例外を処理してください。
1. 出力 PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) として保存してください。

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
