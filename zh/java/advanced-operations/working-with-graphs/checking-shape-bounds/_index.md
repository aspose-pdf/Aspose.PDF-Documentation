---
title: 使用 Java 检查 PDF 图形中的形状边界
linktitle: 检查形状边界
type: docs
weight: 70
url: /zh/java/checking-shape-bounds/
description: 了解如何在 Java 中验证 PDF 图形集合中的形状边界。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 验证 PDF 文件中图形形状的边界
Abstract: 本文展示了如何使用 Aspose.PDF for Java 验证图形集合中的形状边界。内容包括启用严格的边界检查、尝试添加超出范围的形状，以及在仍然保存文档的情况下处理由此产生的异常。
---
当需要确保形状适合放入图形容器时，使用 `BoundsCheckMode`。

## 验证图形形状边界

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 将一个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 添加到文档。
1. 创建一个 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 容器并将其添加到页面。
1. 创建 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) 形状并配置其几何属性。
1. 启用严格的边界检查并尝试将形状添加到图形集合中 `BoundsCheckMode`。
1. 如果形状不适合，请处理异常。
1. 保存输出 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

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
