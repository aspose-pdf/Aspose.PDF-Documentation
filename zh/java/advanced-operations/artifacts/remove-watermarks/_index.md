---
title: 在 Java 中删除 PDF 水印
linktitle: 删除水印
type: docs
weight: 90
url: /zh/java/remove-watermarks/
description: 在 Java 中删除 PDF 首页的水印伪迹。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中删除水印
Abstract: 在 Java 中删除 PDF 首页的水印伪迹。
---
在 Java 中删除 PDF 首页的水印伪迹。

## 删除水印伪迹

此示例仅删除第一页中类型为 `Pagination`、子类型为 `Watermark` 的工件。以普通页面文本、图像或注释形式保存的可见水印仍保留在 PDF 中。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 打开源 PDF.
1. 以相反顺序遍历页面工件集合。
1. 删除子类型为 watermark 的分页工件，然后保存文档。

```java
public static void deleteWatermarkArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## 相关主题

- [添加水印](/pdf/zh/java/add-watermarks/)
- [提取水印详细信息](/pdf/zh/java/extract-watermarks/)
- [在 Java 中使用 PDF 工件](/pdf/zh/java/artifacts/)
