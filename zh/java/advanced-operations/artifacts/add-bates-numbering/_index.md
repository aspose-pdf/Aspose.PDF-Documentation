---
title: 在 Java 中向 PDF 添加 Bates 编号
linktitle: 添加 Bates 编号
type: docs
weight: 10
url: /zh/java/add-bates-numbering/
description: 使用专用的 Bates 编号助手或通用分页 API，在 Java 中为 PDF 页面添加顺序的 Bates 标识符。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中添加 Bates 编号
Abstract: 使用专用的 Bates 编号助手或通用分页 API，在 Java 中为 PDF 页面添加顺序的 Bates 标识符。
---
Bates 编号制品在法律、档案和文档控制工作流中非常有用，因为每页都需要持久的页面级标识符。

## 使用专用助手添加 Bates 编号

当您想通过专用页面集合助手应用 Bates 编号时，请使用此示例。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 打开源 PDF 并添加示例所需的任何额外页面。
1. 配置 [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) 对象。
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

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 打开源 PDF 并添加所需的页面。
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

## 相关主题

- [删除 Bates 编号](/pdf/zh/java/remove-bates-numbering/)
- [在 Java 中使用 PDF 工件](/pdf/zh/java/artifacts/)
