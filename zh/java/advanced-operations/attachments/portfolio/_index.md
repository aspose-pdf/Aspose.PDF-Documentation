---
title: 在 Java 中创建 PDF 作品集
linktitle: 作品集
type: docs
weight: 20
url: /zh/java/portfolio/
description: 了解如何使用 Aspose.PDF 在 Java 中创建和管理 PDF 作品集。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中构建和编辑包含嵌入文件的 PDF 作品集
Abstract: 本文解释了如何使用 Aspose.PDF for Java 创建和管理 PDF 作品集。了解如何在文档上启用集合、向作品集添加多种文件类型，以及如何从现有 PDF 作品集中删除所有集合项。
---
PDF 作品集可以在单个 PDF 容器中捆绑多个文件，同时保持每个文件的原始格式。

## 创建 PDF 作品集

当需要将多个文件打包成 PDF 作品集集合时，请使用此示例。

1. 创建新 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并启用其 [Collection](https://reference.aspose.com/pdf/java/com.aspose.pdf/collection/).
1. 创建 [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) 为每个输入文件创建对象并设置它们的描述。
1. 将文件添加到组合集合中并保存输出文档。

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

## 从 PDF 组合文档中删除文件

当需要清空现有的 PDF 组合文档集合时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
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
