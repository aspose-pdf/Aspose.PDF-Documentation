---
title: 使用 Java 处理 PDF 图层
linktitle: 使用 PDF 图层
type: docs
weight: 50
url: /java/working-with-pdf-layers/
description: 了解如何在 Java 中添加、锁定、提取、展平和合并 PDF 图层。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 管理 PDF 图层
Abstract: 本文介绍如何使用 Aspose.PDF for Java 处理 PDF 图层（也称为可选内容组）。了解如何将图层添加到页面、锁定现有图层、将图层内容提取到文件或流、展平分层内容以及将图层合并为一个。
---
Aspose.PDF for Java 通过每个页面上的 `Layer` API 公开 PDF 层。您可以创建可选内容组，修改其行为，并在需要时导出或拼合其内容。

## 将图层添加到 PDF 页面

1. 创建一个新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 将[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 添加到文档中。
1. 在页面上创建并配置所需的[Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/)对象。
1. 保存输出 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

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

完整的示例创建了三个具有红色、绿色和蓝色线条内容的独立图层。

## 锁定图层

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 访问目标[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)并获取其[Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/)集合。
1. 锁定目标[图层](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/)。
1. 保存更新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

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
