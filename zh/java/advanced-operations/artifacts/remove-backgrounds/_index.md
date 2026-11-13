---
title: 在 Java 中删除 PDF 背景
linktitle: 删除背景
type: docs
weight: 80
url: /zh/java/remove-backgrounds/
description: 在 Java 中删除 PDF 第一页的背景伪影。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中删除背景
Abstract: 在 Java 中删除 PDF 第一页的背景伪影。
---
在 Java 中删除 PDF 第一页的背景工件。

## 删除背景工件

当需要从页面中删除现有的背景工件时，请使用此方法。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 打开源 PDF.
1. 以相反顺序遍历页面工件集合。
1. 删除类型为 pagination 且子类型为 background 的工件，然后保存文档。

```java
public static void removeBackground(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Background) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## 相关主题

- [添加背景](/pdf/zh/java/add-backgrounds/)
- [在 Java 中使用 PDF 工件](/pdf/zh/java/artifacts/)
