---
title: 用 Java 创建 PDF 包
linktitle: 文件夹
type: docs
weight: 20
url: /java/portfolio/
description: 了解如何使用 Aspose.PDF 在 Java 中创建和管理 PDF 作品集。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 中的嵌入式文件构建和编辑 PDF 包
Abstract: 本文介绍如何使用 Aspose.PDF for Java 创建和管理 PDF 包。了解如何在文档上启用集合、向包中添加多种文件类型以及从现有 PDF 包中删除所有集合项目。
---
PDF 包可以将多个文件捆绑在一个 PDF 容器中，同时保留每个文件的原始格式。

## 创建 PDF 作品集

当您需要将多个文件打包到 PDF 包集合中时，请使用此示例。

1. 创建一个新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并启用其[集合](https://reference.aspose.com/pdf/java/com.aspose.pdf/collection/)。
1. 为每个输入文件创建 [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) 对象并设置其描述。
1. 将文件添加到投资组合集合并保存输出文档。

```java
public static void createPdfPortfolio(Path[] inputFiles, Path outputFile) {
    try (Document document = new Document()) {
        document.setCollection(new Collection());

        FileSpecification excel = new FileSpecification(inputFiles[0].toString());
        FileSpecification word = new FileSpecification(inputFiles[1].toString());
        FileSpecification image = new FileSpecification(inputFiles[2].toString());

        excel.setDescription("Excel File");
        word.setDescription("Word File");
        image.setDescription("Image File");

        document.getCollection().add(excel);
        document.getCollection().add(word);
        document.getCollection().add(image);

        document.save(outputFile.toString());
    }
}
```

## 从 PDF 包中删除文件

当应清除现有 PDF 包集合时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 删除文档集合条目。
1. 保存清理后的输出文档。

```java
public static void removeFilesFromPdfPortfolio(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getCollection().delete();
        document.save(outputFile.toString());
    }
}
```
