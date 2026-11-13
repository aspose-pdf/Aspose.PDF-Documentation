---
title: 在Java中移除PDF的Bates编号
linktitle: 移除Bates编号
type: docs
weight: 100
url: /zh/java/remove-bates-numbering/
description: 在Java中从PDF的所有页面移除Bates编号。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在Java中移除Bates编号
Abstract: 在Java中从PDF的所有页面移除Bates编号。
---
在Java中从PDF的所有页面移除Bates编号。

## 删除Bates编号

当需要从文档中移除已存在的Bates编号痕迹时，请使用此方法。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 打开源 PDF.
1. 调用删除贝茨编号的页面集合助手。
1. 保存已清理的输出文件。

```java
public static void deleteBatesNumbering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageCollectionExtensions.deleteBatesNumbering(document.getPages());
        document.save(outputFile.toString());
    }
}
```

## 相关主题

- [添加 Bates 编号](/pdf/zh/java/add-bates-numbering/)
- [在 Java 中使用 PDF 工件](/pdf/zh/java/artifacts/)
