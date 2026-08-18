---
title: 使用 Java 将 Bates 编号添加到 PDF
linktitle: 添加贝茨编号
type: docs
weight: 10
url: /java/add-bates-numbering/
description: 了解如何使用 Java 和 Aspose.PDF 在 PDF 文档中添加和删除 Bates 编号。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 通过 Java 添加 Bates 编号
Abstract: 本文介绍如何使用 Aspose.PDF for Java 在 PDF 文档中创建和删除 Bates 编号工件。它包括配置 `BatesNArtifact`、通过 Bates 编号帮助程序或通用分页帮助程序应用它，以及从文档中删除 Bates 编号。
---
贝茨编号工件在法律、档案和文档控制工作流程中非常有用，其中每个页面都需要持久的页面级标识符。

## 使用专用助手添加贝茨编号

当您想要通过专用页面集合帮助程序应用 Bates 编号时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加示例所需的任何额外页面。
1. 创建 [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) 配置。
1. 将 Bates 编号应用于页面集合并保存输出文件。

```java
public static void addBatesNArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 0; i < 2; i++) {
            document.getPages().add();
        }

        BatesNArtifact batesArtifact = createBatesArtifact();
        PageCollectionExtensions.addBatesNumbering(document.getPages(), batesArtifact);
        document.save(outputFile.toString());
    }
}
```

## 通过分页工件添加贝茨编号

此示例通过通用分页 API 传递 Bates 工件来应用 Bates 编号。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加所需的页面。
1. 创建 [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) 并将其添加到分页工件列表中。
1. 将分页工件应用到页面集合并保存文档。

```java
public static void addBatesNArtifactPagination(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 0; i < 2; i++) {
            document.getPages().add();
        }

        BatesNArtifact batesArtifact = createBatesArtifact();
        List<PaginationArtifact> paginationArtifacts = new ArrayList<>();
        paginationArtifacts.add(batesArtifact);
        PageCollectionExtensions.addPagination(document.getPages(), paginationArtifacts);
        document.save(outputFile.toString());
    }
}
```

## 删除贝茨编号

当应从文档中删除现有的 Bates 编号工件时，请使用此方法。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 调用删除 Bates 编号的页面集合助手。
1. 保存清理后的输出文件。

```java
public static void deleteBatesNumbering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageCollectionExtensions.deleteBatesNumbering(document.getPages());
        document.save(outputFile.toString());
    }
}
```
