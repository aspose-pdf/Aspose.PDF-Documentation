---
title: 在 Java 中删除 PDF 页眉和页脚
linktitle: 删除页眉和页脚
type: docs
weight: 110
url: /zh/java/remove-headers-footers/
description: 在 Java 中删除 PDF 第一页的页眉和页脚伪影。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中删除页眉和页脚
Abstract: 在 Java 中删除 PDF 第一页的页眉和页脚伪影。
---
在 Java 中删除 PDF 第一页的页眉和页脚伪影。

## 删除页眉和页脚工件

当需要从页面中删除现有的页眉和页脚伪影时，请使用此方法。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 打开源 PDF.
1. 倒序遍历页面工件集合。
1. 删除子类型为页眉或页脚的分页工件，然后保存文档。

```java
public static void deleteHeaderFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && (artifact.getSubtype() == Artifact.ArtifactSubtype.Header
                    || artifact.getSubtype() == Artifact.ArtifactSubtype.Footer)) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## 相关主题

- [添加页眉和页脚](/pdf/zh/java/artifacts-header-footer/)
- [在 Java 中处理 PDF 工件](/pdf/zh/java/artifacts/)
