---
title: 使用 Java 处理 PDF 图层
linktitle: 处理 PDF 图层
type: docs
weight: 50
url: /zh/java/working-with-pdf-layers/
description: 了解如何在 Java 中添加、锁定、提取、展平和合并 PDF 图层。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 管理 PDF 图层
Abstract: 本文介绍了如何使用 Aspose.PDF for Java 处理 PDF 图层，也称为可选内容组。了解如何向页面添加图层、锁定现有图层、将图层内容提取到文件或流、展平图层内容以及合并图层为一个。
---
Aspose.PDF for Java 通过以下方式公开 PDF 图层 `Layer` 每页的 API。您可以创建可选内容组，修改其行为，并在需要时导出或展平其内容。

## 向 PDF 页面添加图层

1. 创建新 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 添加 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 到文档。
1. 创建并配置所需的 [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) 页面上的对象。
1. 保存输出的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

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

完整示例创建了三个分别包含红色、绿色和蓝色线条内容的独立层。

## 锁定图层

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 访问目标 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 并获取其 [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) 集合。
1. 锁定目标 [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/)。
1. 保存更新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

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
