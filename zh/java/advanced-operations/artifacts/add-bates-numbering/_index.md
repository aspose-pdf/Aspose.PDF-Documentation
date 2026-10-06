---
title: 在 Java 中为 PDF 添加 Bates 编号
linktitle: 添加 Bates 编号
type: docs
weight: 10
url: /zh/java/add-bates-numbering/
description: 了解如何使用 Java 与 Aspose.PDF 在 PDF 文档中添加和删除 Bates 编号。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 通过 Java 添加 Bates 编号
Abstract: 本文说明了如何使用 Aspose.PDF for Java 在 PDF 文档中创建和删除 Bates 编号伪影。它涵盖了配置 `BatesNArtifact`、通过 Bates 编号帮助器或通用分页帮助器应用它，以及从文档中删除 Bates 编号。
---
Bates 编号伪影在法律、档案和文档控制工作流中非常有用，因为每页都需要持久的页级标识符。

## 使用专用帮助器添加 Bates 编号

当您希望通过专用页面集合帮助器应用 Bates 编号时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加示例所需的任何额外页面。
1. 创建 [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) 配置。
1. 对页面集合应用 Bates 编号并保存输出文件。

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

## 通过分页工件添加 Bates 编号

此示例通过将 Bates 工件传递给通用分页 API 来应用 Bates 编号。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加所需的页面。
1. 创建 [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) 并将其添加到分页工件列表中。
1. 将分页工件应用于页面集合并保存文档。

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

## 删除 Bates 编号

当需要从文档中移除现有的 Bates 编号痕迹时，请使用此方法。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 调用删除 Bates 编号的页面集合助手。
1. 保存已清理的输出文件。

```java
public static void deleteBatesNumbering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageCollectionExtensions.deleteBatesNumbering(document.getPages());
        document.save(outputFile.toString());
    }
}
```
